from django.urls import path
from Motorcycles.Views import moto_view

urlpatterns = [
    path('motorcycles/', moto_view.MotoGetView.as_view()),
    path('add/motorcycles/', moto_view.MotoPostView.as_view()),
    path('motorcycle/<int:moto_id>/', moto_view.MotoDetailView.as_view()),
]