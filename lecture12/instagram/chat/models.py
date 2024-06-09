from django.db import models

class Message(models.Model):
    content = models.TextField()
    sender_name = models.CharField(max_length=32)
    receiver_name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    sent_on = models.DateTimeField()


