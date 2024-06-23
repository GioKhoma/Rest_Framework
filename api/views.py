from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer
from storeapp.models import Product, Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# The two functions api_products and ApiProducts achieve the same functionality of
# handling GET and POST requests for a RESTful API endpoint that deals with Product
# objects. However, they use different approaches provided by Django REST framework.

# In summary, both approaches achieve the same goal, but the class-based view provides a
# more structured and organized way to define views, especially for more complex views that
# require additional methods or functionalities.



# Class-based view (APIView)
class ApiProducts(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ApiProduct(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApiCategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ApiCategory(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        category = get_object_or_404(Category, category_id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function-based view (api_view decorator)

# @api_view(['GET', 'POST'])
# def api_products(request):
#      # Serializing
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     # Deserializing
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # if serializer.is_valid():
#         #     serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def api_product(request, pk):
#     product = get_object_or_404(Product, id=pk)
#
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#
#         # simple version 1
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         # # version 2
#         # if serializer.is_valid():
#         #     serializer.save()
#         # else:
#         #     return Response(serializer.errors)
#
#         return Response(serializer.data)
#
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def api_categories(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_category(request, pk):
#     category = get_object_or_404(Category, category_id=pk)
#
#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'PUT':
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
