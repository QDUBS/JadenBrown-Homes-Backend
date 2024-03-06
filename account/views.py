from rest_framework.request import Request
from rest_framework.views import APIView
from account.models import Account, AccountProfile
from rest_framework.response import Response
from lib.generate_token import decode_token, generate_token
from mixins.crudMixns import ListCreateDestroy
from serializers.account.account import AccountSerializer
from serializers.account.profile import AccountProfileSerializer
from rest_framework import status
from rest_framework_simplejwt.views import  TokenObtainPairView
from django.conf import settings
from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework_simplejwt.tokens import RefreshToken
from lib.format_response import FormatResponse
from datetime import timedelta
from lib.mail import Email
from serializers.public.reset_password import EmailSerializer, ResetPasswordSerializer
from mails.password_reset import reset_password_html
from .tasks import send_reset_password_email



class LoginView(TokenObtainPairView, APIView):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token
    
    def get_token_for_user(self, user):
        refresh = RefreshToken().for_user(user=user)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }
    
    def post(self, request: Request,) -> Response:
        data = request.data
        response = Response()
        email = data.get("email", None)
        password = data.get("password", None)

        user = authenticate(username=email,password=password)
        if user is None:
            return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)
        if user.is_active:
            data = self.get_token_for_user(user)
            response.set_cookie(
                key = settings.SIMPLE_JWT['AUTH_COOKIE'],
                value = data["access"],
                expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request=request)
            response.data = {"Success" : "Login successfully","data":data}
            return response
       
        return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)

class LogOutView(APIView):
    def post(self, request):
        response = Response()
        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE'],
            value = "",
            expires = timedelta(seconds=3),
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        
        response.data = {"Success" : "Logout successfully","data":""}

        return response

class AccountCreateView(APIView):
    serializer_class = AccountSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Account created succesfully"}, status=status.HTTP_201_CREATED)

class AccountActivateView(APIView):
    def post(self, request, token=None):
        if not token:
            return Response({"message":"expected a token"}, status=status.HTTP_400_BAD_REQUEST)
        
        payload = decode_token(token)
        try:
            user = Account.objects.get(**payload)
            user.is_active = True
            user.save()
            return Response({"message":"Account activated successfuly"})
        except Account.DoesNotExist:
            return Response({"message":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exec:
            return Response(str(exec), status=status.HTTP_400_BAD_REQUEST)


class VerifyPasswordEmailView(APIView):
    serializer_class = EmailSerializer
    def post(self, request):
        serialiazer = self.serializer_class(data=request.data)
        serialiazer.is_valid(raise_exception=True)
        email = serialiazer.validated_data.get("email")
        if not email:
            return Response({"Error":"Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            account = Account.objects.get(email=email)
            payload = {"email":account.email, "id":account.id}
            token = generate_token(payload=payload)
            send_reset_password_email.delay(account.email, token)
            return Response({"message":"An email has been sent to your email"})
        except Account.DoesNotExist:
            return Response({"error":"User with email not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exec:
            return Response(str(exec))
       

class ResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer
    def post(self, request, token=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get("password",None)
        if not token:
            return Response({"Error":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({"Error":"insuficient data"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            payload = decode_token(token)
            user = Account.objects.get(**payload)
            user.set_password(password)
            user.save()
            return Response({"message":"password reset succesful"})

        except Account.DoesNotExist:
            return Response({"error":"User with email not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exec:
            return Response(str(exec))
        
        
class AccountProfileView(ListCreateDestroy):
    queryset = AccountProfile.objects.all()
    serializer_class = AccountProfileSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        nickname = serializer.validated_data["nickname"]
        if nickname == "":
            nickname  = serializer.validated_data["first_name"]+serializer.validated_data["last_name"]
            serializer.save(nickname=nickname, user=user)
        else:
            serializer.save(user=user)

        return Response({"message":"profile created success", "data":serializer.data},
            status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        try:
            cookie = request.headers['Cookie']
            profile = AccountProfile.objects.get(user=request.user)
            serializer = self.serializer_class(profile).data
            return Response({"message":"user profile", "data":serializer,}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"message":"Authentication Credentials were not provided"}, status=status.HTTP_401_UNAUTHORIZED)
                 
        except AccountProfile.DoesNotExist:
            return Response({"msg":"Invalid Credentials were provided"}, status=status.HTTP_401_UNAUTHORIZED)