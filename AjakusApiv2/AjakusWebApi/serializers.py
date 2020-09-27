from rest_framework import serializers
from .models import Profile,Content

class Contenterializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    body = serializers.CharField(required=True, allow_blank=False, max_length=100)
    summary = serializers.CharField(required=True, allow_blank=False, max_length=100)
    upload=serializers.FileField(required=False)
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Content.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.upload = validated_data.get('upload', instance.upload)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')
    email=serializers.EmailField(required=True)
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    phone=serializers.IntegerField(required=False)
    address=serializers.CharField(required=False)
    city=serializers.CharField(required=False)
    state=serializers.CharField(required=False)
    country=serializers.CharField(required=False)
    pincode=serializers.IntegerField(required=True)
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        
        """
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance