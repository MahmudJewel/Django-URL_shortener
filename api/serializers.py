from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from urlShortener.models import ShortURLS

class ShortUrlSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if IsAuthenticated:
            user = serializers.SerializerMethodField('_user')
            print('user=> ', user)
            # validated_data['user'] = User
        print('datas are=> ', validated_data['long_url'])
        return validated_data
        # return ShortURLS.objects.create(**validated_data)

    class Meta:
        model = ShortURLS
        fields = '__all__' 
    