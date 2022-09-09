from rest_framework.serializers import ModelSerializer
from .models import *

class NewUserSerializer(ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'

class ResourcesSerializer(ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'