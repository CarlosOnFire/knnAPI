from django.shortcuts import render
from rest_framework import generics
from .serializers import KnnListSerializer
from .models import KnnList

class CreateView(generics.ListCreateAPIView):
    """ This clas defines the create behavior of our rest api. """
    queryset = KnnList.objects.all()
    serializer_class = KnnListSerializer

    def perform_create(self, serializer):
        """ Save the post data when creating a new knnlist.  """
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ This class handles the http GET, PUT and DELETE requests. """
    queryset = KnnList.objects.all()
    serializer_class = KnnListSerializer
