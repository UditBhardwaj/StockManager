from .views import StockViewSet,SalesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stock', StockViewSet,basename='stocks')
router.register('sales', StockViewSet,basename='stocks')