"""
URL configuration for chatus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentification import views as VI
from Chat import views as V

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', VI.login_page, name='login'),
    path('', VI.home, name='home'),
    path('messagerie_publique', V.chat_echange, name="public_chat"),
    path('signup/', VI.signup_page, name = 'signup'),
    path('logout/', VI.logout_user, name = 'logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)