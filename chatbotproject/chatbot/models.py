from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ConversationTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)

    def __str__(self):
        return self.topic

class Message(models.Model):
    conversation = models.ForeignKey(ConversationTopic, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # User means message content sender
    message_content = models.TextField()

    def __str__(self):
        return self.message_content