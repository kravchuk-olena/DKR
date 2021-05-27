from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserAPI:
    @staticmethod
    def register(data):
        username = data['username']
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password1']
        user = User()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.set_password(password)
        user.save()

    @staticmethod
    def auth(data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return None
        return user
