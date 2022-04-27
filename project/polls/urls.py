from django.urls import path

from .views import *
from .views import EmailAttachementView


urlpatterns = (
    path('', index, name="index"),
    path('registration/', registration, name='register'),
    # path('send/', send_message),
    path('sends/', EmailAttachementView.as_view(), name='emailattachment'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
)
