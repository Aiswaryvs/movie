from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from movies.serializers import MoviesSerializer,ReviewSerializer
from movies.models import Movies,Reviews
from rest_framework import permissions
from rest_framework.decorators import action

# Create your views here.
class MovieModelViewsetView(viewsets.ModelViewSet):
    serializer_class=MoviesSerializer
    queryset = Movies.objects.all()
    model = Movies
    permission_classes =[permissions.IsAuthenticated]

    @action(detail=True, methods=["get"])
    def get_reviews(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       movie=Movies.objects.get(id=id)
       qs=Reviews.objects.filter(movie=movie)
       serializer=ReviewSerializer(qs,many=True)
       return Response(data=serializer.data)

    @action(detail=True, methods=["post"])
    def add_reviews(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie=Movies.objects.get(id=id)
        user=request.user
        serializer=ReviewSerializer(data=request.data,context={"user":user,"movie":movie})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)