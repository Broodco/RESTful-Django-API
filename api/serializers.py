from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    package_name = serializers.ReadOnlyField()
    package_version_code = serializers.ReadOnlyField()
    class Meta:
        ordering = ['-id']
        model = Application
        fields = ("id","application","package_name","package_version_code")

