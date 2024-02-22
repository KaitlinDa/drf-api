from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Drf_api
from .serializers import Drf_api_Serializer
from .permissions import IsOwnerOrReadOnly

class Drf_api_List(ListCreateAPIView):
    queryset = Drf_api.objects.all()

    serializer_class = Drf_api_Serializer

class Drf_api_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Drf_api.objects.all()
    serializer_class = Drf_api_Serializer
    permission_classes = (IsOwnerOrReadOnly,)