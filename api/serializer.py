from .models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Profile
        fields = [ 'id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'image', 'docfile']