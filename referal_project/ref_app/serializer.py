from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length = 255)
    last_name = serializers.CharField(max_length = 255)
    email=serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email'

        ]
    # def validate(self,attrs):
    #     email = attrs.get('email','')
    #     if User.objects.filter(email = email).exists():
    #         raise serializers.ValidationError(
    #             {'email',('email hai re baba!')}
    #         )
    #     return super.validate(attrs)

    def create(self,validated_data):
        print("Data:-----",validated_data)
        return(User.objects.create_user(**validated_data))

