from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# Serializer for user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        # fields = ['conversation','sender', 'message_content']
        fields = ['conversation','sender', 'message_content']

class ConversationTopicSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ConversationTopic
        fields = ['user', 'topic', 'messages']

# class ConversationTopicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConversationTopic
#         # fields = "__all__"
#         exclude = ['id']

# Serializer for Meassage
# class MessageSerializer(serializers.ModelSerializer):
#     conversation = ConversationTopicSerializer(many=True, read_only=True)
#     class Meta:
#         model = Message
#         # fields = "__all__"
#         exclude = ['id']


# chatbot app multiple custome user can pass multiple
# messages on multiple topics but in case superuser send 
# message it can pass into all topics with models  using 
# djangorest generic view
