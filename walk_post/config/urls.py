
from django.contrib import admin
from django.urls import path
from walk.views import WalkListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', WalkListView.as_view(), name="index"),

]
