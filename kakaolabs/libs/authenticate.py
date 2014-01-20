import hashlib

from kakaolabs.core.models import Member
from kakaolabs.vendors.api.authenticate import BaseAuthenticate

class SignatureAuthenticate(BaseAuthenticate):
    """ Authenticate base on API signature """

    def is_authenticate(self, request):
        # get api_secret
        api_key = request.GET.get('api_key')
        member = Member.objects.get(api_key=api_key)
        api_secret = member.api_secret

        # get data from request
        data = { k:v for k, v in request.POST.items() }
        data.update({ k:v for k, v in request.GET.items() })

        # remove api_sig from data
        api_sig = data.pop("api_sig", None)
        if not api_sig:
            return False

        # generate signature
        sorted_keys = sorted(data.keys())
        message = "%s%s%s" % (request.path,
                "".join("%s=%s" % (k, data[k]) for k in sorted_keys), api_secret)
        sha = hashlib.sha1()
        sha.update(message.encode('utf8'))
        expected_signature = sha.hexdigest()

        if (api_sig == expected_signature):
            request.user = member

        return api_sig == expected_signature
