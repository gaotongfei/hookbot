from rest_framework.views import APIView
from rest_framework.response import Response


class PayloadView(APIView):

	rest_actions = ('post', )

	def post(self, request):
		return Response(request.get_full_path())

