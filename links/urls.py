from django.urls import path,include
from rest_framework.routers import DefaultRouter
from links import views

router=DefaultRouter()
router.register('links',views.LinksViewSet)

urlpatterns=[
    path('',include(router.urls))
]