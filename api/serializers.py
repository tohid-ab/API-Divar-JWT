from rest_framework import serializers
from divar.models import *
from django.contrib.auth import get_user_model


class AutherSerializerName(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']


class CenterSerializerName(serializers.ModelSerializer):
    class Meta:
        model = Center()
        fields = ['name']


class ArticleSerializers(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    center = CenterSerializerName()

    class Meta:
        model = Home
        exclude = ('slug', 'category', 'updated')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class CenterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Center
        fields = '__all__'


class TestModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'