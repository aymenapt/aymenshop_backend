from django.db.models import Q
from .models import Comment, Product,Category,User,Rating,Ads
from .serialize import CommentSerialize, ProductSerialize,CategorySerializer,RatingSerializers,CategoryListSerializer,AdsSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView,api_view
from django.http import Http404
from rest_framework import generics,status


# Create your views here.

class ProductList(APIView) :
    def get(self,request):
        product=Product.objects.all()[0:4]
        serializer=ProductSerialize(product,many=True)
        return Response(serializer.data)

class ListOfCategories(generics.ListAPIView) :
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
         

class ProductDetails(APIView):
    def get_object(self,product_slug):
        try :
            return Product.objects.get(slug=product_slug)

        except Product.DoesNotExist :
            raise Http404

    def get(self,request,product_slug,format=None):
        product  =self.get_object(product_slug)     
        serializer=ProductSerialize(product)   
        return Response(serializer.data)

class CategoryList(APIView):
    def get_object(self,category_slug):
        try :
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist :
            raise Http404

    def get(self,request,category_slug,format=None):
        category =self.get_object(category_slug)     
        serializer=CategorySerializer(category)   
        return Response(serializer.data)        

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    serializer = ProductSerialize(products, many=True)
    return Response(serializer.data)

class AddComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialize


class Addrating(generics.CreateAPIView) :
     queryset = Rating.objects.all()
     serializer_class = RatingSerializers
     
class ListOfAds(generics.ListCreateAPIView) :
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer