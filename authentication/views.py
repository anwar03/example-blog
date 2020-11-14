from django.contrib.auth import authenticate, login

from rest_framework import views, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer, BrowsableAPIRenderer
from rest_framework.response import Response

from .serializers import UserLoginSerializer, UserRegistrationSerializer


class UserLoginApiView(views.APIView):
    serializer_class = UserLoginSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = ()

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'serializer': serializer})

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            serializer.error_messages = {"message": "Please enter your correct username or password"}
            return Response({'serializer': serializer})

        if user.is_authenticated:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)


class UserRegistrationApiView(CreateAPIView):
    """User registration api view."""
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'serializer': serializer})

        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
