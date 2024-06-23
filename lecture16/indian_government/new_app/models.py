from django.db import models
from myapp.models import Indian

class Device(models.Model):
    model_no = models.CharField(max_length=30)
    company = models.CharField(max_length=40)
    indian = models.ForeignKey(to="myapp.Indian", on_delete=models.CASCADE, null=True, related_name="abc")