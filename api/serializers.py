from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from urlShortener.models import ShortURLS


class ShortUrlSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		user = self.context['request'].user
		print('user=> ', user, user.is_anonymous)
		if user.is_anonymous == False:
			validated_data['user'] = user
		# return validated_data
		return ShortURLS.objects.create(**validated_data)

	class Meta:
		model = ShortURLS
		fields = '__all__'
