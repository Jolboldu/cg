from rest_framework import serializers
from .models import Files


class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = Files
#    fields = ('name', 'name', 'date_time','course')
    fields = '__all__'
