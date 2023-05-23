from rest_framework import serializers

from Form.models import FormInfo


class FormInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormInfo
        fields = ['Name', 'Dob', 'Email', 'Mobile']
