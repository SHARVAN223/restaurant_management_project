from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',Menucategories,name='categories'),
    
]