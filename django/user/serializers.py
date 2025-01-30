from rest_framework import serializers
from order.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(required=True)
    email = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'created_at', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
