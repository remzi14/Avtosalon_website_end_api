from .views import home,aloqa
from rest_framework.routers import SimpleRouter
from django.urls import path

router=SimpleRouter()
# router.register("api/avtolist",AvtoListView,basename='new_mashinalar')
router.register("",home,basename='saxifa')
router.register("alo",aloqa,basename='contact')

urlpatterns=router.urls

