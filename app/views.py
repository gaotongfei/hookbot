from rest_framework.response import Response
from matcha.views import APIView

from app.utils import is_default_branch


class PayloadView(APIView):
    rest_actions = ('post', )

    def post(self, request):
        data = self.data(request)
        if is_default_branch(data):
            print('u')
        return Response(data)
