from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
