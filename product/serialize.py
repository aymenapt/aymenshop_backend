from rest_framework import serializers
from .models import Category, Product,Comment,Rating,Ads

#make serilize here 

class RatingSerializers(serializers.ModelSerializer) : 
    class Meta :
        model = Rating
        fields=['id','product','user','stars']

class CommentSerialize(serializers.ModelSerializer):
     class Meta:
        model = Comment
        fields = [
            "id",
            "created_by",
            "comments",
            "product"
        ]

class ProductSerialize(serializers.ModelSerializer): 
    comments=CommentSerialize(many=True)
    class Meta :
        model=Product
        fields=['id','name','description','get_absolute_url','get_image','price','comments','num_rating','avg_rating']


class CategorySerializer(serializers.ModelSerializer):
    products =ProductSerialize(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )


class CategoryListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_image",
            "get_absolute_url",
        )


class AdsSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Ads
        fields = (
            "id",
            "get_image",
        )

