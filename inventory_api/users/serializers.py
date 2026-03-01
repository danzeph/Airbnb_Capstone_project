from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """User serializer with password_confirm added for validation"""
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','password_confirm']
        

    def validate(self,data):
            password = data.get("password")
            password_confirm = data.get("password_confirm")

            if password or password_confirm:
                  if password != password_confirm:
                     raise serializers.ValidationError({"password": "Passwords do not match"})
            return data

    def create(self, validated_data):
            validated_data.pop('password_confirm')
            user = User.objects.create_user(**validated_data)
            return user
    

    