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
from django.contrib.auth import views as auth_views
from landing_page import views as landing_views
from users import views as users_views
from quizzes import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chapters/', include(('chapters.urls', 'chapters'), namespace='chapters')),
    path('exercises/', include(('exercises.urls', 'exercises'), namespace='exercises')),
    path('notes/', include(('notes.urls', 'notes'), namespace='notes')),
    path('quizzes/', include(('quizzes.urls', 'quizzes'), namespace='quizzes')),
    path('_nested_admin/', include('nested_admin.urls')),
    path('', landing_views.landing_page, name='home_page'),
    path('credits/', landing_views.credits, name='credits'),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('quiz/result', quiz_views.quiz_result, name='quiz-result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
