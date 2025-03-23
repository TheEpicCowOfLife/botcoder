from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from knox.models import AuthToken
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the Profile model."""
    
    class Meta:
        model = Profile
        fields = ('bio', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model with Profile data."""
    
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile')


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    
    password = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()
    bio = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'token')

    def create(self, validated_data):
        bio = validated_data.pop('bio', '')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        
        # Update the profile bio
        user.profile.bio = bio
        user.profile.save()
        
        return user

    def get_token(self, obj):
        token = AuthToken.objects.create(obj)[1]
        return token


class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""
    
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            data['user'] = user
            return data
        raise serializers.ValidationError("Incorrect credentials.") 