from rest_framework import serializers
from .models import BlogRecord
class BlogRecordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = BlogRecord
        fields = '__all__'