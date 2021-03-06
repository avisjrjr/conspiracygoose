from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

class Conspiracy(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField(max_length=500000)
  author = models.ForeignKey(User, on_delete=CASCADE)
  date = models.DateField(default=now())

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("conspiracy_detail", kwargs={"pk": self.pk})

class Pic(models.Model):
  url = models.CharField(max_length=100)
  conspiracy = models.OneToOneField(Conspiracy, on_delete=CASCADE)

  def __str__(self):
    return f"Pic for conspiracy_id: {self.conspiracy_id} @{self.url}"