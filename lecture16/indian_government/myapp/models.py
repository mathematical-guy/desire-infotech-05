from django.db import models

class Indian(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class AadharDetail(models.Model):
    aadhar_no = models.CharField(unique=True, max_length=16)
    aadhar_address = models.TextField()
    aadhar_expiry_date = models.DateField()
    # indian_id = models.IntegerField(unique=True)
    indian = models.OneToOneField(to=Indian, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.aadhar_no


    
