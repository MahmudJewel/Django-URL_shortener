from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from urlShortener.models import ShortURLS

class ShortUrlSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if IsAuthenticated:
            user = self.context['request'].user
            print('user=> ', user)
            validated_data['user'] = user
        # print('datas are=> ', validated_data['long_url'])
        # return validated_data
        return ShortURLS.objects.create(**validated_data)

    class Meta:
        model = ShortURLS
        fields = '__all__' 
    