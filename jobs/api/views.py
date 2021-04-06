from rest_framework import generics
# from jobs.api.permissions import IsAdminUserOrReadOnly
from jobs.api.serializers import JobOfferSerializer

from jobs.models import JobOffer

#APIのCRUD操作はDRFで準備してくれてるので継承

class ListView(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all().order_by('-id')
    #作成したSerializerを格納
    serializer_class = JobOfferSerializer
    # permission_classes = [IsAdminUserOrReadOnly]


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    # permission_classes = [IsAdminUserOrReadOnly]
