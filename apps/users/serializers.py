from rest_framework import serializers
from .models import EUser


# User Serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = EUser
		fields = ('id', 'auth_token', 'email', 'first_name', 'last_name', 'phone_number', 'address')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = EUser
		fields = ('email', 'first_name', 'last_name', 'phone_number', 'address', 'password')
		extra_kwargs = {
			'password': {'write_only': True},
			'first_name': {'required': True},
			'last_name': {'required': True},
			'phone_number': {'required': True},
			'address': {'required': True}
		}
	
	def create(self, validated_data):
		user = EUser.objects.create(**validated_data)
		user.permission = "2"
		user.set_password(validated_data['password'])
		user.save()
		return user
