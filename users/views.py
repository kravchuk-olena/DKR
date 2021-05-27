from json import loads
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import LoginSerialier
from .serializer import RegSerializer
from .utils import UserAPI
from django.contrib.auth import login, logout

class UserView(APIView):
    def __init__(self):
        super().__init__()
        self.userAPI = UserAPI
        self.reg_serializer = RegSerializer
        self.login_serializer = LoginSerialier
    #for register
    def post(self, request: HttpRequest):
        user_data = loads(request.body)
        user_serializer = self.reg_serializer(data=user_data)
        if user_serializer.is_valid():
            try:
                self.userAPI.register(user_serializer.data)
            except:
                return Response(status=400)
        else:
            return Response(status=400)

    #for login
    def put(self, request: HttpRequest):
        user_data = loads(request.body)
        user_serializer = self.login_serializer(data=user_data)
        if user_serializer.is_valid():
            user = self.userAPI.auth(user_serializer.data)
            if user is None:
                return Response(status=400)
            login(request, user)
            return Response(status=200)
        else:
            return Response(status=400)

    def delete(self, request):
        logout(request)
        return Response(status=200)