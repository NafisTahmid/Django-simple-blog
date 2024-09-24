from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home_view, name="index"),
    path('<slug:slug>/', views.single_view, name='single')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
