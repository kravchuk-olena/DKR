import redis
from json import loads
from json import dumps
from database.utils import DataBaseAPI
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
import os


host = os.environ.get("REDIS_HOST")
port = os.environ.get("REDIS_PORT")
db = os.environ.get("REDIS_DB")
redis_cache = redis.Redis(host, port=port, db=db)


class BlogView(APIView):
    def __init__(self):
        super().__init__()
        self.dbAPI = DataBaseAPI()

    def get(self, request: Request):
        id = request.query_params.get('id', None)
        if id is None:
            data = self.dbAPI.record_all()
            return Response(dumps(data), status=200)
        return self.get_detail(id)

    def post(self, request: Request):
        if request.user.is_authenticated:
            data = loads(request.body)
            username = request.user.username
            success = self.dbAPI.record_update(username, data)
            if success:
                redis_cache.delete(data['id'])
                return Response(status=200)
            return Response(status=400)
        return Response(status=400)

    def put(self, request: Request):
        if request.user.is_authenticated:
            data = loads(request.body)
            success = self.dbAPI.record_create(data)
            if success:
                return Response(status=200)
            return Response(status=400)
        return Response(status=400)

    def delete(self, request: Request):
        if request.user.is_authenticated:
            id = request.query_params.get('id', None)
            if not id:
                return Response(status=400)
            username = request.user.username
            self.dbAPI.record_delete(id, username)
            redis_cache.delete(id)
            return Response(status=200)
        return Response(status=400)


    def get_detail(self, id: int):
        cache = redis_cache.get(id)

        if cache:
            return Response(loads(cache), status=200)

        record = self.dbAPI.record_id(id)
        if not record:
            return Response(status=400)

        redis_cache.set(id, dumps(record))
        return Response(dumps(record), status=200)
