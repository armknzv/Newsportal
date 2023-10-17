from django.db import models
from django.contrib.auth.models import User
from news.models import Category


# Создавайте свои модели здесь.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subscription_date = models.DateField(auto_now_add=True)
