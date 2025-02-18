# myApp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include
from . import views


urlpatterns = [
    path('home/customer/', views.home_customer, name='home_customer'), 
    path('home_owner/', views.home_owner, name='home_owner'),
    path('register_customer/', views.register_customer, name='register_customer'),
    path('register_owner/', views.register_owner, name='register_owner'),
    path('', views.landing_page, name='landing_page'),
    path('login/customer/', views.login_view_customer, name='login_view_customer'),
    path('login/owner/', views.login_view_owner, name='login_view_owner'),
    path('search/', views.search, name='search'),
    path('salons/', views.all_salons, name='all_salons'),
    path('services/', views.all_services, name='all_services'), 
    path('categories/', views.all_categories, name='all_categories'), 
    path('services/', views.service_detail, name='Services'),
    path('categories/<int:category_id>/services/', views.category_services, name='category_services'),
    path('profile_customer/', views.profile_view, name='profile_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'), 
    path('profile_customer/edit_customer/', views.edit_profile, name='edit_profile_customer'), 
    path('select_salon_service/<int:salon_id>/<int:service_id>/', views.select_salon_service, name='select_salon_service'),
    path('book/<int:salon_id>/<int:service_id>/', views.book_appointment, name='book_appointment'),
    path('payment/', views.payment, name='payment'),
    path('user-details/', views.display_user_details, name='user_details'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('logout_customer/', views.logout_view_customer, name='logout_view_customer'),  # Adds the logout URL pattern
    path('book_service/<int:service_id>/', views.book_service, name='book_service'),
    path('salon/<int:salon_id>/', views.salon_details, name='salon_details'),
    path('salons/', views.salon_details, name='Salons'), 
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('services/<str:service_name>/', views.service_detail, name='service_detail'),
    path('feedback/<int:appointment_id>/', views.give_feedback, name='give_feedback'),
    path('get-booked-slots/<int:salon_id>/<int:service_id>/', views.get_booked_slots, name='get_booked_slots'),
    path('signup/', views.register_owner, name='signup'),
    path('logout_owner/', views.logout_view_owner, name='logout_view_owner'),
    #path('service_list/', views.service_list, name='service_list'),
    path('edit_service/<int:pk>/', views.edit_service, name='edit_service'),
    path('delete_service/<int:pk>/', views.delete_service, name='delete_service'),

    path('profile_owner/', views.profile_owner, name='profile_owner'),
    path('edit_profile_owner/', views.edit_profile_owner, name='edit_profile_owner'),

    path('staff_list/', views.staff_list, name='staff_list'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('edit_staff/<int:pk>/', views.edit_staff, name='edit_staff'),
    path('delete_staff/<int:pk>/', views.delete_staff, name='delete_staff'),

    path('notifications/', views.notification_view_owner, name='notifications'),
    path('service_list/', views.service_list, name='service_list'),
    path('service_list/add_category/', views.add_category, name='add_category'),
    path('add_service/', views.add_service, name='add_service'),
    path('add_category/', views.add_category, name='add_category'),
    path('manage_services/', views.manage_services, name='manage_services'),
    #path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)