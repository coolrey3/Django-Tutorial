import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBOo4mw12YfwuQChyCFPIX49bYPn60_QoI')

# Geocoding an address
geocode_result = gmaps.geocode('9191 fontainebleau blvd #14, miami, FL 33172')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
# print(geocode_result)
# print(reverse_geocode_result)
#
# # for steps in directions_result:
# #
# print(directions_result)

sample = gmaps.find_place('mobile repair techs', 'textquery')

print( sample)