
from django.conf.urls import url, include
from django.contrib import admin

from chats.views import MessagesView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("chats.urls", namespace="chats")),
    url(r'^messages/api/', MessagesView.as_view()),
]
