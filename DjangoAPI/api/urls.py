from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
app_name = 'api'

urlpatterns = [
    path('fusers/', views.fuser_add, name='creat-user'),
    path('upload/', views.FaceUploadView.as_view(), name='file-upload'),
    path('pswdlogin/', views.pswd_login, name='pswd_login'),
    path('facelogin/', csrf_exempt(views.FaceLoginView.as_view()), name='face-login'),
    path('getinfo/', views.userInfo, name='userinfo'),
    path('updateinfo/', views.updatInfo, name='updateinfo'),
    path('logout/', views.logout, name='logout'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)