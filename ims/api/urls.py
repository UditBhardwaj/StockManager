# from .views import UserList,StockDetail,UserAuthentication
# from django.urls import path,include
# # from .router import router
# from rest_framework.authtoken import views
# # from rest_framework import routers
# #
# # router = routers.DefaultRouter()
# #
# # router.register(r'users', UserList)
# # router.register(r'user', StockDetail,basename='MyModel')
#
#
# app_name = 'stock'
#
# urlpatterns = [
#     # path('<id>/',api_detail_view,name="detail"),
#     path('<id>/update', StockDetail.as_view(), name="detail"),
#     # path('<id>/delete',api_delete_view,name="delete"),
#     path('products/',UserList.as_view(),name="product_list"),
#     # path('auth/',include('authapp.urls')),
#     # app
#     path('auth/',UserAuthentication.as_view(),name="Userauthen"),
#     # path('', include(router.urls)),
#      path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
# ]
# urlpatterns += router.urls

from .views import SalesViewSet,StockViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stocks',StockViewSet,basename='stocks')
router.register(r'sales',SalesViewSet,basename='sales')
urlpatterns = router.urls