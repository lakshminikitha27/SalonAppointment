# myApp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserDetailsForm
from .models import Salon, Service, BookedSlot, ServiceFeedback
from django.urls import reverse
from django.template import loader
from geopy.geocoders import Nominatim
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment, UserDetails
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.http import JsonResponse

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

def register(request):
    if request.method == "POST":
        form = UserDetailsForm(request.POST)
        print("POST data:", request.POST)
        print("Form is valid:", form.is_valid())
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.password = make_password(form.cleaned_data['password'])
            user_details.save()
            return redirect('login')  # redirect to home or dashboard
        else:
            messages.error(request, "There were errors in your form. Please check and try again.")
            return render(request, "myApp/register.html", {"form": form})
    else:
        form = UserDetailsForm()
    return render(request, "myApp/register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f'Username: {username}, Password: {password}')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'myApp/login.html')


def home(request):
    # Attempt to load the template manually for debugging
    try:
        template = loader.get_template('home.html')
    except Exception as e:
        print("Error loading template:", e)

    nearby_salons = Salon.objects.all()
    services = Service.objects.all()
    return render(request, 'myApp/home.html', {'nearby_salons': nearby_salons,  'services': services})

def search(request):
    query = request.POST.get('query')
    # Add your search logic here
    # For example, search for products or salons based on the query
    return render(request, 'search_results.html', {'query': query})

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

from django.utils.timezone import datetime, timedelta

from django.utils.timezone import datetime, timedelta

def book_appointment(request, salon_id, service_id):
    salon = get_object_or_404(Salon, id=salon_id)
    service = get_object_or_404(Service, id=service_id)

    # Generate dynamic slots (10:00 AM to 5:00 PM, 30-min intervals)
    start_time = datetime.strptime("10:00", "%H:%M")
    end_time = datetime.strptime("17:00", "%H:%M")
    time_slots = []
    while start_time < end_time:
        time_slots.append(start_time.strftime("%H:%M"))
        start_time += timedelta(minutes=30)

    # Fetch selected date
    selected_date = request.POST.get("appointment-date", datetime.today().date())

    # Fetch booked slots for the selected date, salon, and service
    booked_slots = BookedSlot.objects.filter(
        date=selected_date,
        salon=salon,
        service=service,
    ).values_list("time", flat=True)

    # Mark slots as booked or available
    slots = [{"time": slot, "is_filled": slot in booked_slots} for slot in time_slots]

    if request.method == "POST":
        selected_slot = request.POST.get("selected-slot")
        if selected_slot and selected_date:
            # Check if the slot is already booked
            if selected_slot not in booked_slots:
                # Save the booked slot
                customer_name = request.user.username  # Assuming logged-in user has a `username`
                BookedSlot.objects.create(
                    customer_name=customer_name,
                    salon=salon,
                    service=service,
                    date=selected_date,
                    time=selected_slot,
                )
                # Redirect to payment
                return redirect(
                    f"/payment/?salon={salon.name}&service={service.name}&date={selected_date}&slot={selected_slot}&price={service.price}"
                )
            else:
                # Slot is already booked; display an error message
                return render(
                    request,
                    "myApp/book_appointment.html",
                    {
                        "salon": salon,
                        "service": service,
                        "slots": slots,
                        "error": f"Slot {selected_slot} is already booked. Please choose another slot.",
                    },
                )

    return render(request, "myApp/book_appointment.html", {"salon": salon, "service": service, "slots": slots})

def get_booked_slots(request, salon_id, service_id):
    date = request.GET.get('date')
    if date:
        booked_slots = BookedSlot.objects.filter(
            salon_id=salon_id,
            service_id=service_id,
            date=date
        ).values_list('time', flat=True)
        return JsonResponse({'booked_slots': list(booked_slots)})
    return JsonResponse({'error': 'Invalid date or parameters'}, status=400)

def payment(request):
    if request.method == "POST":
        # Get booking details from the POST request
        salon_name = request.POST.get("salon")
        service_name = request.POST.get("service")
        date = request.POST.get("date")
        slot = request.POST.get("slot")
        price = request.POST.get("price")
        customer_name = request.POST.get("customer_name")
        user_id = request.user.id  # Assuming the user is authenticated

        # Retrieve necessary objects
        try:
            salon = Salon.objects.get(name=salon_name)
            service = Service.objects.get(name=service_name)
            user = UserDetails.objects.get(pk=user_id)  # Replace with your user model if different
        except Salon.DoesNotExist:
            print(f"Salon '{salon_name}' not found")
            return redirect('payment')  # Redirect back to the payment page
        except Service.DoesNotExist:
            print(f"Service '{service_name}' not found")
            return redirect('payment')  # Redirect back to the payment page
        except UserDetails.DoesNotExist:
            print(f"User with ID '{user_id}' not found")
            return redirect('payment')

        # Save to BookedSlot table
        booked_slot = BookedSlot.objects.create(
            time=slot,
            date=date,
            salon=salon,
            service=service,
            customer_name=customer_name
        )

        # Save to Appointment table
        appointment = Appointment.objects.create(
            salon=salon,
            service=service,
            user=user,
            date=date,
            slot=booked_slot  # Reference the created BookedSlot
        )

        print(f"Booking saved: {booked_slot}")
        print(f"Appointment saved: {appointment}")

        # Redirect to a success page
        return redirect("payment_success")  # Replace with your success page route

    # For GET requests, handle parameters and render the payment page
    salon = request.GET.get("salon")
    service_name = request.GET.get("service")
    if not service_name:
        return HttpResponse("Service parameter is missing", status=400)
    date = request.GET.get("date")
    slot = request.GET.get("slot")
    service = get_object_or_404(Service, name=service_name)
    service_price = service.price

    return render(request, "myApp/payment.html", {
        "salon": salon,
        "service": service,
        "date": date,
        "slot": slot,
        "service_price": service_price,
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

def all_salons(request):
    # Fetch all salons, you can use pagination if needed
    salons = Salon.objects.all()

    return render(request, 'myApp/salons.html', {'salons': salons})

def all_services(request):
    services = Service.objects.all()

    return render(request, 'myApp/services_main.html', {'services': services})

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