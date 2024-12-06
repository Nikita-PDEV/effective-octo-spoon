from rest_framework import viewsets
from .models import PassUser
from .serializers import PassUserSerializer

class PassUserViewSet(viewsets.ModelViewSet):
    queryset = PassUser.objects.all()
    serializer_class = PassUserSerializer