# serializers.py

from rest_framework import serializers

from .models import Hero, StudentDetail

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class StudentDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentDetail
        fields = ('id', 'firstname', 'lastname', 'grade', 'mailid', 'contactnumber', 'adharnumber', 'address', 'vaccinationstatus')

