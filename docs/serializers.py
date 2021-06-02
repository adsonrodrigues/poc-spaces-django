from rest_framework import serializers

from docs.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'description', 'document', 'uploaded_at')
