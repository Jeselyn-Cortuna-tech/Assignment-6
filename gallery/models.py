from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to='photos/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title