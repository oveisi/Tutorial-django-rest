from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions, mixins, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


# @permission_classes((permissions.AllowAny,))
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @permission_classes((permissions.AllowAny,))
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
