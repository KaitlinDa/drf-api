from django.urls import path
from .views import Drf_api_List, Drf_api_Detail

urlpatterns = [
  path("", Drf_api_List.as_view(), name="drf_api_list"),
  path("<int:pk>/", Drf_api_Detail.as_view(), name="drf_api_detail"),
]