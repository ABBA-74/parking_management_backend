from rest_framework import serializers
from django.contrib.auth.models import User
from user_management.models import CustomUser

class UserProfileSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomUser
        fields = ('phone', 'address', 'postal_code', 'city', 'profile_image_url')
        
    def get_profile_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_image and hasattr(obj.profile_image, 'url'):
            return request.build_absolute_uri(obj.profile_image.url) if request else obj.profile_image.url
        return None

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='customuser')
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'groups', 'profile')
        