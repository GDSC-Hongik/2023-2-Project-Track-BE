from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from coplate.views import CustomPasswordChangeView
urlpatterns = [  # url pattern을 확인할 때는 맨위에서부터 차례로 확인함
    # admin
    path('admin/', admin.site.urls),
    # coplate
    path('', include('coplate.urls')),
    # allauth
    path('email-confirmation-done/',
         TemplateView.as_view(template_name='coplate/email_confirmation_done.html'),
         name='account_email_confirmation_done',
    ),
    path('password/change/',CustomPasswordChangeView.as_view(),\
        name = 'account_password_change'),
    path('', include('allauth.urls')),
]
