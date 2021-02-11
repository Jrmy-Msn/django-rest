import logging
from datetime import date
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo

logger = logging.getLogger(__name__)

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'name', 'description', 'limit_date', 'checked', 'user')
        depth = 1

    def validate_limit_date(self, value):
        if value < date.today():
            raise serializers.ValidationError('Date can not be in the past')
        return value