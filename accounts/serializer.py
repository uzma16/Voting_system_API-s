from rest_framework import serializers 
from .models import CustomUser
 
 
class CustomUserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CustomUser
        fields = ('id','name','mobile_no','email','password','is_valid')
                  