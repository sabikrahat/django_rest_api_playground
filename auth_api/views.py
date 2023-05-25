from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from auth_api.models import User


# Create your views here.
@api_view(['GET', 'POST'])
def check(request):

    response_data = {
        'status': True,
        'message': 'Auth Api Server Connected Successfully...!',
        'data': None
    }

    if request.method == 'GET':
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':

        response_data = {
            'status': True,
            'message': 'Register Function executed without any data...!',
            'data': None
        }

        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            username = request.data['username']
            email = request.data['email']
            password = make_password(request.data['password'])
            phone = request.data['phone']
            address = request.data['address']
            name = request.data['name']

            user = User(username=username, email=email, password=password, phone=phone, address=address, name=name)
        
            if user.isEmailExists():

                response_data = {
                    "success": False,
                    "message": "Email already exists!",
                    "data": None
                }

                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
            
            if user.isUsernameExists():

                response_data = {
                    "success": False,
                    "message": "Username already exists!",
                    "data": None
                }

                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
            
            if user.isPhoneExists():

                response_data = {
                    "success": False,
                    "message": "Phone already exists!",
                    "data": None
                }

                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
            
            user.save()

            response_data = {
                "success": True,
                "message": "User Created Successfully!",
                "data": user.toJson()
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:

            response_data = {
                "success": False,
                "message": "Error: " + str(e),
                "data": None
            }

            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
# sample json to register post api
# {
#     "username": "testuser",
#     "password": "testpassword",
#     "email": "test@gmail.com",
#     "name": "testname",
#     "phone": "1234567890",
#     "address": "testaddress"
# }


@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':

        response_data = {
            'status': True,
            'message': 'Login Function executed without any data...!',
            'data': None
        }

        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            identifier = request.data['identifier']
            password = request.data['password']

            user = None

            if '@' in identifier:
                user = User.objects.filter(email=identifier).first()

            elif identifier.isdigit():
                user = User.objects.filter(phone=identifier).first()

            else:
                user = User.objects.filter(username=identifier).first()
            
            if user is None:

                response_data = {
                    "success": False,
                    "message": "User not found with this indentifier!",
                    "data": None
                }

                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        
            if not check_password(password, user.password):

                response_data = {
                    "success": False,
                    "message": "Password is incorrect!",
                    "data": None
                }
                
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
            
            # Generate tokens for the authenticated user
            refresh = RefreshToken.for_user(user)
            
            response_data = {
                "success": True,
                "message": "Credential matched!",
                "data": user.toJson(),
                "tokens": {
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh)
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)
        
        except Exception as e:

            response_data = {
                "success": False,
                "message": "Error: " + str(e),
                "data": None
            }

            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

# sample json to login post api
# {
#     "identifier": "testuser",
#     "password": "testpassword"
# }


@api_view(['GET', 'POST'])
def refresh(request):
    if request.method == 'GET':

        response_data = {
            'status': True,
            'message': 'Refresh Function executed without any data...!',
            'data': None
        }

        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)

            response_data = {
                "success": True,
                "message": "Refresh Successfully!",
                "data": None,
                "tokens": {
                    "access_token": str(token.access_token),
                    "refresh_token": str(token)
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            response_data = {"success": False, "message": "Error: " + str(e), "data": None}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
# sample json to refresh post api
# {
#    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NDk2MDkyNiwiaWF0IjoxNjg0ODc0NTI2LCJqdGkiOiIxM2E0MDg3MmI4ZGE0MjRlYjQ5N2YzNDgxOTFiODBmMyIsInVzZXJfaWQiOjExfQ.i95a8407qkKiCr-CV8ulsLW8M5_JT3asKJD1lb3nRIQ"
# }


@api_view(['GET', 'POST'])
def logout(request):
    if request.method == 'GET':

        response_data = {
            'status': True,
            'message': 'Logout Function executed without any data...!',
            'data': None
        }

        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            # !TODO: Add token to blacklist
            token.blacklist()

            response_data = {
                "success": True,
                "message": "Session removed. Logout Successfully!",
                "data": None
            }

            return Response(response_data, status=status.HTTP_200_OK)
        
        except Exception as e:

            response_data = {
                "success": False,
                "message": "Error: " + str(e),
                "data": None
            }

            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
# sample json to logout post api
# {
#    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NDk2MDkyNiwiaWF0IjoxNjg0ODc0NTI2LCJqdGkiOiIxM2E0MDg3MmI4ZGE0MjRlYjQ5N2YzNDgxOTFiODBmMyIsInVzZXJfaWQiOjExfQ.i95a8407qkKiCr-CV8ulsLW8M5_JT3asKJD1lb3nRIQ"
# }