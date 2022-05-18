from rest_framework import serializers
from django.contrib.auth.models import User
class UserInlineSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    class Meta:
        model= User
        fields=['username']