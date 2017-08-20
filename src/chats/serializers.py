from rest_framework import serializers


from .models import todoitem

class todoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoitem
        fields = ("id", "text", "done")
