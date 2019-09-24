from rest_framework import serializers

from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user model.
    """
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def create(self, validate_data):
        user = User(
            email = validate_data.get('email'),
            first_name = validate_data.get('first_name'),
            last_name = validate_data.get('last_name')
        )
        user.set_password(validate_data.get('password'))
        user.save()
        return user