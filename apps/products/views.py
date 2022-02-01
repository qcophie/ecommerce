from django.db.models import Q
from django.http import Http404
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class LatestProductsList(APIView):
	permission_classes = (AllowAny,)
	
	def get(self, request):
		products = Product.objects.all()[0:4]
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)


class ProductDetail(APIView):
	permission_classes = (AllowAny,)
	
	def get_object(self, category_id, product_id):
		try:
			return Product.objects.filter(category__id=category_id).get(id=product_id)
		except Product.DoesNotExist:
			raise Http404
	
	def get(self, request, category_id, product_id):
		product = self.get_object(category_id, product_id)
		serializer = ProductSerializer(product)
		return Response(serializer.data)


class CategoryDetail(APIView):
	permission_classes = (AllowAny,)
	
	def get_object(self, category_id):
		try:
			return Category.objects.get(id=category_id)
		except Category.DoesNotExist:
			raise Http404
	
	def get(self, request, category_id):
		category = self.get_object(category_id)
		serializer = CategorySerializer(category)
		return Response(serializer.data)


@api_view(['POST'])
def search(request):
	query = request.data.get('query', '')
	
	if query:
		products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)
	else:
		return Response({"products": []})
