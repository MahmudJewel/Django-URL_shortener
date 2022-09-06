from rest_framework import serializers

from urlShortener.models import ShortURLS

class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURLS
        fields = '__all__' # ['name', 'varsity', 'sid', 'contact'] #or '__all__’