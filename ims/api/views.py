from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from inventoryapp.models import Stock,Sales
from .serializers import StockSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# class ExampleView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, format=None):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.authapp.User` instance.
#             'authapp': unicode(request.authapp),  # None
#         }
#         return Response(content)


# class UserList(APIView):
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#     @classmethod
#     def get_extra_actions(cls):
#         return []
#
#     def get(self, request):
#
#         model = Stock.objects.all()
#         serializer = StockSerializer(model, many=True)
#         return Response(serializer.data)
# #
#     def post(self, request):
#         serializer = StockSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from articles.models import Article
# from .serializers import ArticleSerializer
from rest_framework import viewsets

class StockViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

class SalesViewSet(viewsets.ModelViewSet):
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()


# @api_view(['GET', ])
# def api_detail_view(request, id):
#
#     try:
#         stock = Stock.objects.get(id=id)
#     except Stock.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = StockSerializer(stock)
#         return Response(serializer.data)
#
#
# @api_view(['PUT','GET'])
# def api_update_view(request, id):
#
#     try:
#         stock = Stock.objects.get(id=id)
#     except Stock.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         serializer = StockSerializer(stock, data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data[SUCCESS] = UPDATE_SUCCESS
#             return Response(data=data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response({'key': 'value'}, status=status.HTTP_200_OK)
#
#
#
# @api_view(['DELETE','GET'])
# def api_delete_view(request, id):
#
#     try:
#         stock = Stock.objects.get(id=id)
#     except Stock.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'DELETE':
#         operation=stock.delete()
#         data = {}
#         if operation:
#             data[SUCCESS] = DELETE_SUCCESS
#             return Response(data=data)
#         # Return this if request method is not POST
#     return Response({'key': 'value'}, status=status.HTTP_200_OK)