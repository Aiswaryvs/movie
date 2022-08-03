from rest_framework import serializers
from movies.models import Movies,Reviews
from django.contrib.auth.models import User



class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields="__all__"


class ReviewSerializer(serializers.ModelSerializer):
    movie=MoviesSerializer(many=False,read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields=["movie","rating","review","review_date","user"]

    def create(self,validated_data):
        user=self.context.get("user")
        movie=self.context.get("movie")
        return Reviews.objects.create(user=user,movie=movie,**validated_data)