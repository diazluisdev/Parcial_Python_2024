from django.urls import path,include

from rest_framework import routers

from apirest import views

router=routers.DefaultRouter()
router.register(r'persona',views.PersonaViewSet)

urlpatterns = [
    
    path('',include(router.urls))
    
    
]