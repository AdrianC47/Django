#
from rest_framework import serializers

class LoginSocialSerializer(serializers.Serializer):

    token_id  = models.CharField(required = True)