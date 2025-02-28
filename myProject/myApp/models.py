from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class UserDetails(AbstractUser):# Inherit from AbstractUser, not models.Model
    last_login=None
    is_superuser=None
    is_staff=None
    phone = models.CharField(max_length=15)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    city = models.CharField(max_length=100)
    address_line = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True)
    # Fields required for creating superusers (other than username and password)
    REQUIRED_FIELDS = ['email']  # Make sure 'email' is included in the list of required fields

    # Define which field to use for authentication
    USERNAME_FIELD = 'username'  # You can also change this to 'email' if you want email-based authentication
    groups = models.ManyToManyField(Group, related_name="user_details_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="user_details_permissions", blank=True)

    def __str__(self):
        return self.username  # Or you could return something more descriptive, e.g. self.email

class OwnerDetails(AbstractUser):
    last_login=None
    is_superuser=None
    is_staff=None
    salon_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pin_code = models.CharField(max_length=6, blank=True)
    country = models.CharField(max_length=100, blank=True)
    groups = models.ManyToManyField(Group, related_name="salon_details_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="salon_details_permissions", blank=True)

    def _str_(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def _str_(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    duration = models.PositiveIntegerField(default=30,help_text="Duration in minutes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="services", null=True)  # Added category

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)

    def _str_(self):
        return self.name

class Salon(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='salons/', null=True, blank=True)  # Changed from CharField
    rating = models.FloatField(default=0.0)
    services = models.ManyToManyField(Service, related_name='salons')

    def __str__(self):
        return self.name
    
class BookedSlot(models.Model):
    time = models.TimeField()
    date = models.DateField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255, blank=True, null=True)  # Optional: store customer name
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('time', 'date', 'salon')  # Prevent duplicate bookings for the same slot

    def __str__(self):
        return f"{self.salon.name} - {self.date} {self.time}"
    
class Appointment(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)  # Assuming user model is available
    date = models.DateField()
    slot = models.ForeignKey(BookedSlot, on_delete=models.CASCADE, null=True, blank=True) # For example, "10:00 AM"
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Appointment at {self.salon.name} for {self.service.name} on {self.date} at {self.slot}"
    
class ServiceFeedback(models.Model):
    appointment = models.ForeignKey(
        Appointment,  # Replace with the actual Appointment model name
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='service_feedback'
    )
    service = models.ForeignKey(
        Service,  # Replace with the actual Service model name
        on_delete=models.CASCADE,
        related_name='feedback'
    )
    rating = models.IntegerField(null=True, blank=True)  # Ensure this aligns with your rating scale
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def _str_(self):
        return f"Feedback for Service ID {self.service.id} - Rating: {self.rating}"