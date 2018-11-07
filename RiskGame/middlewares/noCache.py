from django.views.decorators.cache import never_cache

class NoCachingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #never_cache()
        return self.get_response(request)
