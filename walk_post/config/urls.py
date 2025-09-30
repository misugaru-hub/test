
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView 
from django.urls import path,include
from walk.views import (WalkListView,PostCreateView,
                        PostDetailView,PostUpdateView,
                        PostDeleteView)
from django.conf import settings
from django.conf.urls.static import static
from walk.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', WalkListView.as_view(), name="index"),
    path("page/create",PostCreateView.as_view(),name="page-create"),
    path("page/<int:pk>",PostDetailView.as_view(),name="page-detail"),
    path("page/<int:pk>/update",
         PostUpdateView.as_view(), name="page-update"),
    path('page/<int:pk>/delete',
         PostDeleteView.as_view(), name="page-delete"),
    path('index', index, name="map"),
    path('staffroom/', include("staffroom.urls", namespace="staffroom")), 
    path('login', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="logout"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
