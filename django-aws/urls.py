from django.contrib import admin
from django.urls import path
from django_aws import views
from django_aws.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-task', views.create_web_task),
]

admin.site.site_header = "Django AWS Admin Panel"

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
