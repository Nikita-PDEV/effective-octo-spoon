from rest_framework import serializers
from .models import PassUser

class PassUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassUser
        fields = ('email', 'phone_number', 'firstname', 'lastname', 'surname')