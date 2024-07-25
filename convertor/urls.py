from django.urls import path
from . import views

app_name = 'convertor'

urlpatterns = [
    path('image-to-pdf/', views.ImageToPDFApiView.as_view(), name='image_to_pdf'),
]
