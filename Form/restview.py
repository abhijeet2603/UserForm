from rest_framework import viewsets

from Form.models import FormInfo
from Form.serializer import FormInfoSerializer


class FormInfoViewSets(viewsets.ModelViewSet):
    queryset = FormInfo.objects.all()
    serializer_class = FormInfoSerializer
