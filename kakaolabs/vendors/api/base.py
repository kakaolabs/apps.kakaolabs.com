import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.http import HttpResponse

from .authenticate import BaseAuthenticate
from .error import JsonApiError


class HandleRequestMixin(object):
    def _get_argument(self, data, name, is_mandatory, default_value):
        value = data.get(name, default_value)
        if value is None and is_mandatory:
            raise JsonApiError("missing parameter %s" % name)
        return value

    def get_post_argument(self, name, is_mandatory=False, default_value=None):
        return self._get_argument(
            self.request.POST, name, is_mandatory, default_value)

    def get_argument(self, name, is_mandatory=False, default_value=None):
        return self._get_argument(
            self.request.GET, name, is_mandatory, default_value)

    def coerce_post(self, request):
        """ When we make a PUT/PATCH/DELETE request, django wont look at data and
        load it. This function was borrowed from django-piston """
        method = request.method
        if method not in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return

        is_multipart_request = request.META.get(
                'CONTENT_TYPE', '').startswith('multipart/form-data')

        if method == 'POST' and is_multipart_request:
            return

        if hasattr(request, '_post'):
            del request._post
            del request._files

        try:
            request.META['CONTENT_TYPE'] = 'application/x-www-form-urlencoded'
            request.method = 'POST'
            request._load_post_and_files()
            request.method = method
        except AttributeError:
            request.META['CONTENT_TYPE'] = 'application/x-www-form-urlencoded'
            request.META['REQUEST_METHOD'] = 'POST'
            request._load_post_and_files()
            request.META['REQUEST_METHOD'] = method


class BaseController(View, HandleRequestMixin):
    authenticate_class = BaseAuthenticate

    def get_handler(self, method, **kwargs):
        return None

    def log_request(self, prefix):
        full_path = self.request.get_full_path()
        if "login" in full_path:
            return

        if self.request.META['REQUEST_METHOD'] == 'GET':
            print "%s curl -H 'User-Agent: %s' -XGET 'http://%s%s'"  % (
                prefix,
                self.request.META.get('HTTP_USER_AGENT'),
                self.request.get_host(),
                self.request.get_full_path())
        else:
            data = '&'.join("%s=%s" % (k, v) for k, v in self.request.POST.items())
            print "%s curl -H 'User-Agent: %s' -X%s 'http://%s%s' -d'%s'"  % (
                prefix,
                self.request.META.get('HTTP_USER_AGENT'),
                self.request.META['REQUEST_METHOD'],
                self.request.get_host(),
                self.request.get_full_path(),
                data.encode('utf8'))


    def process_request_with_handler(self, handler, *args, **kwargs):
        if not handler:
            data = {"error": "Unsupported method"}
        else:
            try:
                data = handler(*args, **kwargs)
            except JsonApiError, e:
                data = {"error": e.message}
            except Exception, e:
                data = {"error": "Internal error: %s" % e.message}

        if "error" in data:
            self.log_request("RequestErrorWhenHandle %s" % data["error"])
            return HttpResponse(
                json.dumps(data), mimetype="application/json", status=403)
        else:
            return HttpResponse(json.dumps(data), mimetype="application/json")

    def process_request(self, method, *args, **kwargs):
        return None

    def handle_authenticate_failed(self):
        self.log_request("RequestErrorWhenAuthenticate")
        data = {"error": "Authenticate failed"}
        return HttpResponse(
            json.dumps(data), mimetype="application/json", status=403)


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.coerce_post(request)
        self.request = request
        method = request.method.lower()

        try:
            if self.authenticate_class().is_authenticate(request):
                return self.process_request(method, *args, **kwargs)
            else:
                return self.handle_authenticate_failed()
        except JsonApiError, e:
            self.log_request("RequestError %s" % e.message)
            data = {"error": e.message}
            return HttpResponse(
                json.dumps(data), mimetype="application/json", status=403)
        except Exception, e:
            self.log_request("RequestErrorWhenDispatch %s" % e.message)
            data = {"error": "Internal error: %s" % e.message}
            return HttpResponse(
                json.dumps(data), mimetype="application/json", status=403)


class JsonApiController(BaseController):
    def process_request(self, method, *args, **kwargs):
        action = kwargs.pop("action")
        handler = getattr(self, "%s_%s" % (method, action), None)
        return self.process_request_with_handler(handler, *args, **kwargs)


class RestfulApiController(BaseController):
    def process_request(self, method, *args, **kwargs):
        handler = getattr(self, method, None)
        return self.process_request_with_handler(handler, *args, **kwargs)
