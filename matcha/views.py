from rest_framework.views import APIView as View
from matcha.exceptions import NotAllowedMethod


class APIView(View):
    def data(self, request):
        allowed_methods = ['GET', 'POST']
        if request.method not in allowed_methods:
            return NotAllowedMethod('Only `GET` and `POST` method is allowed')
        if request.method == 'GET':
            data = request.GET
        else:
            data= request.data
            try:
                data = data.dict()
            except AttributeError:
                pass

        return data
