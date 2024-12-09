
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from QuizAPI.decorators import handle_exceptions
from .serializers import *

class UserView(APIView):
    authentication_classes = []

    @handle_exceptions
    def get(self, request):
        user = UserSerializer(instance=request.user)
        return Response(user.data)


    @handle_exceptions
    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user_obj = user.save()
        token_data = RefreshToken.for_user(user_obj)
        refresh, access = str(token_data), str(token_data.access_token)
        return Response(status=200, data={"refresh": refresh, "access": access})

