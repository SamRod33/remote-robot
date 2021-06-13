from django.urls import path
from django.conf.urls.static import static
from ugv import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('left', views.left, name='left'),
    path('right', views.right, name='right'),
    path('forward', views.forward, name='up'),
    path('backward', views.backward, name='down'),
    path('stop', views.stop, name='stop')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
