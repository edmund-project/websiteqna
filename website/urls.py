
from django.contrib import admin
from django.urls import path 
from websiteqna.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('signup/', signup, name='signup'),
    path('contact/', contact, name='contact'),
    path('newquestion/', newquestion, name='newquestion'),
    path('question/<int:qid>/<slug:qslug>', viewquestion),
    path('ajax-answer-question', ajaxanswerquestion),
    
] 
    
