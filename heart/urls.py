from django.urls import path,include
from rest_framework.routers import DefaultRouter
from heart import views

router=DefaultRouter()
router.register('heart',views.HeartViewSet)

urlpatterns=[
    path('',include(router.urls))
]