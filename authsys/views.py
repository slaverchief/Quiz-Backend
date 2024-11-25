from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from QuizAPI.decorators import handle_exceptions
from QuizAPI.exceptions import HandledException
from QuizAPI.permissions import *
from .serializers import *

class UserView(APIView):

    @handle_exceptions
    def get(self, request):
        user = UserSerializer(instance=request.user)
        return Response(user.data)

    @handle_exceptions
    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response(status=200)

