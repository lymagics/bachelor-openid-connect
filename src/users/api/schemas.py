from rest_framework import serializers

from users.models import User


class UserOut(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'avatar_url',)
