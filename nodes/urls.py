from django.urls import path,include
from rest_framework.routers import DefaultRouter
from nodes import views,ppp

router=DefaultRouter()
router.register('nodes',views.NodesViewSet)
router.register('links',views.LinksViewSet)
router.register('family',views.FamilyViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('test',views.test,name='test'),
    path('test1',views.test1,name='test1'),
    path('test2',views.test2,name='test2'),
    path('test3',ppp.test,name='test3'),
    path('ppp',views.ttt,name='ttt')
]