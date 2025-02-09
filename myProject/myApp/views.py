# myApp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserDetailsForm, OwnerDetailsForm, StaffForm, ServiceForm
from .models import Salon, Service, BookedSlot, ServiceFeedback, OwnerDetails
from django.urls import reverse
from django.template import loader
from geopy.geocoders import Nominatim
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment, UserDetails, Staff, Category
from datetime import datetime, timedelta
from django.db.models import F
from math import radians, sin, cos, sqrt, atan2
from geopy.geocoders import Nominatim
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt

def base_view(request):
    cart_count = request.session.get('cart_count', 0)
    user = request.user
    flash_messages = messages.get_messages(request)

    context = {
        'cart_count': cart_count,
        'user': user,
        'messages': list(flash_messages),
    }
    return render(request, 'myApp/base.html', context)

def register_customer(request):
    if request.method == "POST":
        form = UserDetailsForm(request.POST)
        print("POST data:", request.POST)
        print("Form is valid:", form.is_valid())
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.password = make_password(form.cleaned_data['password'])
            user_details.save()
            return redirect('login_view_customer')  # redirect to home or dashboard
        else:
            messages.error(request, "There were errors in your form. Please check and try again.")
            return render(request, "myApp/register.html", {"form": form})
    else:
        form = UserDetailsForm()
    return render(request, "myApp/register.html", {"form": form})

# User Registration
def register_owner(request):
    if request.method == "POST":
        form = OwnerDetailsForm(request.POST)
        if form.is_valid():
            pasword = form.save(commit=False)
            pasword.password = make_password(form.cleaned_data['password'])
            pasword.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login_view_owner')  # Redirect to login page
        else:
            messages.error(request, "There were errors in your form. Please try again.")
    else:
        form = OwnerDetailsForm()
    return render(request, "myApp/signup.html", {"form": form})

def landing_page(request):
    """Landing page with User and Owner selection buttons."""
    return render(request, 'myApp/landing.html')

@csrf_exempt
def login_view_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f'Username: {username}, Password: {password}')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('home_customer')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'myApp/login_customer.html')

def login_view_owner(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f'Owner Username: {username}, Password: {password}')

        try:
            owner = OwnerDetails.objects.get(username=username)  # Fetch owner by username
            if check_password(password, owner.password):  # Check hashed password
                request.session['owner_id'] = owner.id  # Store owner ID in session
                messages.success(request, 'Successfully logged in as Owner!')
                return redirect('home_owner')  # Redirect to owner's dashboard
            else:
                messages.error(request, 'Invalid username or password')
        except OwnerDetails.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'myApp/login_owner.html')


from geopy.exc import GeocoderTimedOut
import time  # Import time for retry delays

def calculate_distance(lat1, lon1, lat2, lon2):
    """ Haversine formula to calculate the distance between two latitude/longitude points. """
    R = 6371  # Radius of the Earth in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def home_customer(request):
    user_lat = request.GET.get('lat')
    user_lon = request.GET.get('lon')

    if not user_lat or not user_lon:
        return render(request, 'myApp/home_customer.html', {'nearby_salons': []})  # No user location data

    try:
        user_lat, user_lon = float(user_lat), float(user_lon)
    except ValueError:
        return render(request, 'myApp/home_customer.html', {'nearby_salons': []})

    salons = Salon.objects.values('id', 'name', 'rating', 'image_name', 'address', 'latitude', 'longitude')
    print(f"Found {len(salons)} salons.")  # Fetch addresses
    if not salons:
        print(f"No salons found in the database.")

    nearby_salons = []
    for salon in salons:
        print(f"Salon: {salon['name']}, Address: {salon['address']}")
        
        # Use latitude and longitude from the database
        lat = salon['latitude']
        lon = salon['longitude']
        
        if lat is not None and lon is not None:
            distance = calculate_distance(user_lat, user_lon, lat, lon)
            if distance <= 10:  # Show salons within 10 km
                salon['distance'] = round(distance, 2)
                nearby_salons.append(salon)

    nearby_salons = sorted(nearby_salons, key=lambda x: x['distance'])[:3]  # Limit to 3 nearest salons
    services = Service.objects.all()

    return render(request, 'myApp/home_customer.html', {'nearby_salons': nearby_salons, 'services': services})

# Home Page
def home_owner(request):
    username = request.session.get('username')  # Default to 'Guest' if no session data
    return render(request, 'myApp/home_owner.html', {'username': username})

# Service List
@login_required
def manage_services(request):
    if 'username' not in request.session:
        messages.error(request, 'Your session has expired. Please log in again.')
        return redirect('login')

    services = Service.objects.all()
    return render(request, 'myApp/manage_services.html', {
        'services': services,
        'username': request.session.get('username'),
    })

# Add Service
@login_required
@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.created_by = request.user  # Assuming each service has a creator
            service.save()
            messages.success(request, "Service added successfully!")
            
            # Track added services in session
            user_activity = request.session.get('user_activity', [])
            user_activity.append(f"Added service: {service.name} at {str(service.created_at)}")
            request.session['user_activity'] = user_activity

            return redirect('service_list')
        else:
            messages.error(request, "There were errors with the service form. Please try again.")
    
    form = ServiceForm()
    return render(request, 'myApp/add_service.html', {
        'form': form,
        'username': request.session.get('username'),
    })


# Edit Service
@login_required
def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service updated successfully!")
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'myApp/edit_service.html', {'form': form, 'service': service})

# Delete Service
@login_required
def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, "Service deleted successfully!")
        return redirect('service_list')
    return render(request, 'myApp/delete_service.html', {'service': service})

# Service List
@login_required
def service_list(request):
    if 'username' not in request.session:
        messages.error(request, 'Your session has expired. Please log in again.')
        return redirect('login')

    services = Service.objects.all()
    return render(request, 'myApp/service_list.html', {
        'services': services,
        'username': request.session.get('username'),
    })


def search(request):
    query = request.POST.get('query')
    # Add your search logic here
    # For example, search for products or salons based on the query
    return render(request, 'search_results.html', {'query': query})

def select_salon_service(request, salon_id, service_id):
    # Fetch salon and service objects
    salon = Salon.objects.get(id=salon_id)
    service = Service.objects.get(id=service_id)

    # Store in session
    request.session['selected_salon'] = salon.id
    request.session['selected_service'] = service.id
    # Debugging: Print session data
    print("Session Data:", request.session.items())

    return redirect('book_appointment')

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)  # Retrieves the service or returns a 404 error if not found
    salons = service.salons.all().distinct()  # Get salons offering this service

    context = {
        'title': f"Salons Offering {service.name}",
        'salons': salons,
    }
    return render(request, 'myApp/service.html', context)


def profile(request):
    # Logic to handle the profile page
    return render(request, 'myApp/profile.html')


from django.db.utils import IntegrityError

def book_appointment(request, salon_id, service_id):
    salon = get_object_or_404(Salon, id=salon_id)
    service = get_object_or_404(Service, id=service_id)

    if request.method == "POST":
        selected_date = request.POST.get("appointment-date")
        selected_slot = request.POST.get("selected-slot")

        if not selected_date or not selected_slot:
            return render(request, "myApp/book_appointment.html", {
                "salon": salon,
                "service": service,
                "error": "Please select a date and slot.",
            })

        # Save to session for payment process
        request.session["selected_salon"] = salon_id
        request.session["selected_service"] = service_id
        request.session["selected_date"] = selected_date
        request.session["selected_slot"] = selected_slot

        return redirect("payment")  # Redirect to payment

    # Generate all time slots (same as before)
    start_time = datetime.strptime("10:00", "%H:%M")
    end_time = datetime.strptime("17:00", "%H:%M")
    time_slots = []
    
    while start_time < end_time:
        slot_time = start_time.strftime("%H:%M")
        time_slots.append(slot_time)
        start_time += timedelta(minutes=30)

    # Fetch booked slots
    booked_slots = set(BookedSlot.objects.filter(
        date=datetime.today().date(),
        salon_id=salon.id,
        service_id=service.id
    ).values_list("time", flat=True))

    slots = [{"time": slot, "is_filled": slot in booked_slots} for slot in time_slots]

    return render(request, "myApp/book_appointment.html", {
        "salon": salon,
        "service": service,
        "slots": slots,
    })


def get_booked_slots(request, salon_id, service_id):
    selected_date = request.GET.get("date")
    
    # Ensure correct filtering by salon and service
    booked_slots = list(BookedSlot.objects.filter(
        date=selected_date,
        salon_id=salon_id,
        service_id=service_id
    ).values_list("time", flat=True))

    print(f"API Response for Salon {salon_id}, Service {service_id}, Date {selected_date}: {booked_slots}")
    
    return JsonResponse({"booked_slots": booked_slots})

from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")  # Redirect to login if user is not authenticated
def payment(request):
    if request.method == "POST":
        # Retrieve booking details from session
        salon_id = request.session.get("selected_salon")
        service_id = request.session.get("selected_service")
        selected_date = request.session.get("selected_date")
        selected_slot = request.session.get("selected_slot")
        user_id = request.user.id  # User is authenticated due to @login_required

        if not all([salon_id, service_id, selected_date, selected_slot, user_id]):
            return redirect("book_appointment")  # Redirect if session data is missing

        try:
            # Retrieve necessary objects
            salon = Salon.objects.get(id=salon_id)
            service = Service.objects.get(id=service_id)
            user = UserDetails.objects.get(pk=user_id)  # Use your actual user model

            # **Check if the slot is already booked**
            booked_slot, created = BookedSlot.objects.get_or_create(
                time=selected_slot,
                date=selected_date,
                salon=salon,
                service=service,
                defaults={"customer_name": request.user.username}  # Only set if new
            )

            if not created:
                return render(request, "myApp/payment.html", {
                    "salon": salon.name,
                    "service": service,
                    "date": selected_date,
                    "slot": selected_slot,
                    "service_price": service.price,
                    "error": f"Slot {selected_slot} is already booked. Please choose another slot.",
                })

            # **Save to Appointment table**
            appointment = Appointment.objects.create(
                salon=salon,
                service=service,
                user=user,
                date=selected_date,
                slot=booked_slot  # Reference the created BookedSlot
            )

            print(f"Booking saved: {booked_slot}")
            print(f"Appointment saved: {appointment}")

            # Clear session data after successful booking
            request.session.pop("selected_salon", None)
            request.session.pop("selected_service", None)
            request.session.pop("selected_date", None)
            request.session.pop("selected_slot", None)

            return redirect("payment_success")  # Redirect to success page

        except (Salon.DoesNotExist, Service.DoesNotExist, UserDetails.DoesNotExist):
            return redirect("payment")  # Redirect if any object is missing
        except IntegrityError:
            return render(request, "myApp/payment.html", {
                "salon": salon.name,
                "service": service,
                "date": selected_date,
                "slot": selected_slot,
                "service_price": service.price,
                "error": "Payment failed. Please try again.",
            })

    # **For GET requests, retrieve booking details from session**
    salon_id = request.session.get("selected_salon")
    service_id = request.session.get("selected_service")
    selected_date = request.session.get("selected_date")
    selected_slot = request.session.get("selected_slot")

    if not all([salon_id, service_id, selected_date, selected_slot]):
        return HttpResponse("Session data is missing. Please restart the booking process.", status=400)

    salon = get_object_or_404(Salon, id=salon_id)
    service = get_object_or_404(Service, id=service_id)

    return render(request, "myApp/payment.html", {
        "salon": salon.name,
        "service": service,
        "date": selected_date,
        "slot": selected_slot,
        "service_price": service.price,
    })



def give_feedback(request, appointment_id):
    # Get the appointment instance
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    
    if request.method == "POST":
        # Get data from the form
        rating = request.POST.get("rating")
        comments = request.POST.get("comments")
        
        # Save the feedback
        feedback = ServiceFeedback.objects.create(
            appointment=appointment,
            service=appointment.service,
            rating=rating,
            comments=comments
        )
        messages.success(request, "Thank you for your feedback!")
        return redirect("profile")  # Redirect back to the profile or another page

    # Render the feedback form
    return render(request, "myApp/give_feedback.html", {"appointment": appointment})

def payment_success(request):
    return render(request, 'myApp/success.html')

def display_user_details(request):
    if request.user.is_authenticated:
        user_details = request.user  # Directly fetch the user details

        return render(request, 'myApp/payment.html', {'user_details': user_details})
    else:
        return redirect('login') 

def book_service(request, service_id):
    # Get the service object using the ID from the URL
    service = get_object_or_404(Service, pk=service_id)
    # You can render a booking page or handle booking logic here
    return render(request, 'book_service.html', {'service': service})

def get_lat_lon(address):
    geolocator = Nominatim(user_agent="your_app_name")
    try:
        location = geolocator.geocode(address)
        if location:
            print(f"Geocoding successful: {address} -> Latitude: {location.latitude}, Longitude: {location.longitude}")
            return location.latitude, location.longitude
        else:
            print(f"Geocoding failed for address: {address}")
            return None, None
    except Exception as e:
        print(f"Error during geocoding: {e}")
        return None, None

from geopy.distance import geodesic

def get_nearby_salons(request):
    user_lat = request.GET.get("lat")
    user_lon = request.GET.get("lon")

    if not user_lat or not user_lon:
        return JsonResponse({"error": "Invalid location"}, status=400)

    user_location = (float(user_lat), float(user_lon))
    nearby_salons = []

    for salon in Salon.objects.all():
        if salon.latitude and salon.longitude:
            salon_location = (salon.latitude, salon.longitude)
            distance = geodesic(user_location, salon_location).km  # Calculate distance
            nearby_salons.append({
                "name": salon.name,
                "address": salon.address,
                "distance": round(distance, 2),
                "image_url": salon.image.url if salon.image else "",
                "rating": salon.rating if hasattr(salon, "rating") else 0,
                "id": salon.id
            })

    # Sort salons by distance in ascending order and take the top 3
    nearby_salons = sorted(nearby_salons, key=lambda x: x["distance"])[:3]

    return JsonResponse({"salons": nearby_salons})

def salon_details(request, salon_id):
    # Use prefetch_related with the correct related name
    salon = get_object_or_404(Salon.objects.prefetch_related('services'), id=salon_id)

    # If latitude and longitude are not already set, use geocoding
    if not salon.latitude or not salon.longitude:
        latitude, longitude = get_lat_lon(salon.address)
        if latitude and longitude:  # Ensure that we have valid lat/lon
            salon.latitude = latitude
            salon.longitude = longitude
            salon.save()
        else:
            print(f"Failed to fetch coordinates for salon: {salon.name}")

    services = salon.services.all()  # Access related services using the related name 'salon_services'
    return render(request, 'myApp/salon_details.html', {'salon': salon, 'services': services})

# Staff List
@login_required
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'myApp/staff_list.html', {'staff_members': staff_members, 'username': request.session.get('username'),})

# Add Staff
@login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff added successfully!")
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'myApp/add_staff.html', {'form': form})

# Edit Staff
@login_required
def edit_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff details updated successfully!")
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'myApp/add_staff.html', {'form': form})

# Delete Staff
@login_required
def delete_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    staff.delete()
    messages.success(request, "Staff member deleted successfully!")
    return redirect('staff_list')

def notification_view_owner(request):
    """
    View to display all appointments in the notification.html page.
    """
    # Fetch all appointments from the database
    appointments = Appointment.objects.all()
    return render(request, 'myApp/notifications.html', {'appointments': appointments})

def add_category(request):
    categories = Category.objects.all()
    return render(request, 'myApp/add_category.html', {'categories': categories})


def all_salons(request):
    # Fetch all salons, you can use pagination if needed
    salons = Salon.objects.all()

    return render(request, 'myApp/salons.html', {'salons': salons})

def all_services(request):
    services = Service.objects.all()

    return render(request, 'myApp/services_main.html', {'services': services})


# User Profile
@login_required
def profile_owner(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(UserDetails, id=user_id)
    return render(request, 'myApp/profile.html', {'user': user, 'username': request.session.get('username'),})


# Edit Profile
@login_required
def edit_profile_owner(request):
    user = request.user  # Get the currently logged-in user
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = UserDetailsForm(instance=user)
    return render(request, 'myApp/edit_profile.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).select_related('salon')  # Retrieve appointments with salon info
    return render(request, 'myApp/profile.html', {
        'user': user,
        'appointments': appointments,
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Retrieve the currently logged-in user's instance
        user = request.user

        # Update fields in the UserDetails model
        user.first_name = request.POST.get('username', user.first_name)
        user.email = request.POST.get('email', user.email)
        user.phone = request.POST.get('phone', user.phone)
        user.save()

        # Redirect to the profile page after saving
        return redirect('profile')

    # Handle the GET request or render an edit profile form if needed
    return render(request, 'myApp/edit_profile.html', {'user': request.user})

# User Logout
def logout_view(request):
    # Clear the session data
    request.session.flush()
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('login')