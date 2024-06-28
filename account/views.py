from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import AccountModelDataGetSerializer, AccountModelRegisterSerializer, AccountModelLoginSerializer
from .models import Account
from django.db.models import Q


# Create your views here.
class GetAllUserData(APIView):
    def get(self, request):
        data = Account.objects.all()
        serializedData = AccountModelDataGetSerializer(data, many=True)
        return Response(serializedData.data)


class RegisterNewUser(APIView):
    def post(self, request):
        serializer = AccountModelRegisterSerializer(data=request.data)

        if (serializer.is_valid()):
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            email = serializer.validated_data['email']
            phone = serializer.validated_data['phone']
            role = serializer.validated_data['role']
            password = serializer.validated_data['password']

            # Create Account object
            new_account = Account(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                role=role
            )

            # Set and hash the password
            new_account.set_password(password)

            # Save the account object
            new_account.save()

            # Serialize the created account object
            serialized_data = AccountModelDataGetSerializer(new_account)

            # Return serialized data as response
            return Response(serialized_data.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    def post(self, request):
        serializer = AccountModelLoginSerializer(data=request.data)

        if (serializer.is_valid()):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                account = Account.objects.get(Q(email=email))

                if(account.check_password(password)):
                    serialized_data = AccountModelLoginSerializer(account)

                    return Response(serialized_data.data)
                else:
                    return Response({'error': 'wrong password'}, status=404)
            except:
                return Response({'error': 'Account not found'}, status=404)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
