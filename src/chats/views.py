from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import todoitemSerializer
from .models import todoitem

# Create your views here.
def post_home(request):
    return render(request,"index.html", {})


class MessagesView(APIView):
    def get(self, request):
        todos = todoitem.objects.all()
        todosSerializer = todoitemSerializer(todos, many=True)
        return Response(todosSerializer.data)
