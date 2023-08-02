from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Blog
from drf_dynamic_fields import DynamicFieldsMixin


class BlogSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_auther(self, obj):
        return obj.auther.username

    auther = serializers.SerializerMethodField('get_auther')

    class Meta:
        model = Blog
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
