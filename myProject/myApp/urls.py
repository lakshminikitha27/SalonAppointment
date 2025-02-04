# myApp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('search/', views.search, name='search'),
    path('salons/', views.all_salons, name='all_salons'),
    path('services/', views.all_services, name='all_services'), 
    path('services/', views.service_detail, name='Services'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'), 
    path('select_salon_service/<int:salon_id>/<int:service_id>/', views.select_salon_service, name='select_salon_service'),
    path('book/<int:salon_id>/<int:service_id>/', views.book_appointment, name='book_appointment'),
    path('payment/', views.payment, name='payment'),
    path('user-details/', views.display_user_details, name='user_details'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('logout/', LogoutView.as_view(next_page='home/'), name='logout'),  # Adds the logout URL pattern
    path('book_service/<int:service_id>/', views.book_service, name='book_service'),
    path('salon/<int:salon_id>/', views.salon_details, name='salon_details'),
    path('salons/', views.salon_details, name='Salons'), 
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('services/<str:service_name>/', views.service_detail, name='service_detail'),
    path('feedback/<int:appointment_id>/', views.give_feedback, name='give_feedback'),
    path('get-booked-slots/<int:salon_id>/<int:service_id>/', views.get_booked_slots, name='get_booked_slots'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)