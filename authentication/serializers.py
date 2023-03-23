from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message=("email in use, try another"))]
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'min_length':8,
                'max_length':20,
                'error_messages':{
                    'min_length': 'Password at least 8 digits',
                    'max_length': 'Password up to 20 characters',
                },
            }}
    
    def create(self, validated_data):
        user = User(
            email= validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user) 
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username', 'password')
