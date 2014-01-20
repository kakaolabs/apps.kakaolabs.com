class BaseAuthenticate(object):
    """ Simple authenticate, allow all request """

    def is_authenticate(self, request):
        return True


class UserAuthenticate(BaseAuthenticate):
    """ Allow only logged in user """
    def is_authenticate(self, request):
        return request.user.is_active


class AdminAuthenticate(BaseAuthenticate):
    """ Allow only admin user """
    def is_authenticate(self, request):
        return request.user.is_admin
