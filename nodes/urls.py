from django.urls import path,include
from rest_framework.routers import DefaultRouter
from nodes import views

router=DefaultRouter()
router.register('nodes',views.NodesViewSet)
router.register('links',views.LinksViewSet)


urlpatterns=[
    path('',include(router.urls)),
    path('test',views.test,name='test')
]