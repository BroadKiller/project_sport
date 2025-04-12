
from django.urls.conf import path, include
from django.contrib import admin


urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('sport.urls')),

]
