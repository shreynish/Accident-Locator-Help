# Importing required libraries.
from googleplaces import GooglePlaces
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Use your own Google API key for making api request calls.
# Remember to enable Places API service.
API_KEY = ''

# Initialising the GooglePlaces constructor.
google_places = GooglePlaces(API_KEY)

# Call the function nearby search with the parameters as longitude, latitude, radius
# And type of place which needs to be searched of.
nearby_result = google_places.nearby_search(
			        lat_lng ={'lat': , 'lng': },	#Enter the latitude and longitude.
			        types =[types.TYPE_HOSPITAL])	#TYPE_POLICE for Police Station.

for place in nearby_result.places:
    print (place.name)		                                                #You will get the Place(hospital) Name.
    print("Latitude =", place.geo_location['lat'])					        #Latitude of place.
    print("Longitude =", place.geo_location['lng'])					        #Longitude of place.
    place.get_details()											          	#You will get the place details in depth.
    print("Phone no. =", help_number = place.international_phone_number)	#Phone number of that place.
    print()
    break

Send message to the hospital using twilio services.
message = client.messages.create(
							body ='Need Help!!!',
                            from_='',				#Enter your twilio number
                            to = help_number
                          )

# Message unique ID is generated.
print(message.sid)