from django.db import models
from django.contrib.auth import get_user_model

class Todo(models.Model):
    user_model = get_user_model()
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 800)
    limit_date = models.DateField(blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
    checked = models.BooleanField(default = False)
    user = models.ForeignKey(user_model, on_delete = models.CASCADE)