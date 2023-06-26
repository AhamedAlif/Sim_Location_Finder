import phonenumbers
from phonenumbers import geocoder, timezone, carrier
from geopy.geocoders import Nominatim

number = input("Enter the number (with +): ")
phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

geolocator = Nominatim(user_agent="phone_location")

# Retrieve latitude and longitude
location = geolocator.geocode(reg, exactly_one=True)

latitude = None
longitude = None

if location is not None:
    latitude = location.latitude
    longitude = location.longitude

# Reverse geocoding based on latitude and longitude
address = None
if latitude is not None and longitude is not None:
    reverse_location = geolocator.reverse((latitude, longitude), exactly_one=True)
    if reverse_location is not None:
        address = reverse_location.address

print("Phone Number:", number)
print("Time Zones:", list(time))
print("Carrier:", car)
print("Region:", reg)
print("Latitude:", latitude)
print("Longitude:", longitude)
print("Address:", address)

