"""mathapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from landing_page import views as landing_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chapters/', include(('chapters.urls', 'chapters'), namespace='chapters')),
    path('quizzes/', include(('quizzes.urls', 'quizzes'), namespace='quizzes')),
    path('_nested_admin/', include('nested_admin.urls')),
    path('', landing_views.testing, name='home_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
