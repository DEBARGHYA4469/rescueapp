from googleplaces import GooglePlaces, types, lang
from pprint import pprint

google_places = GooglePlaces("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

coords = str(26.190)+" "+str(91.690)
query_result = google_places.nearby_search(
        location=coords,
        radius=20000, types=[types.TYPE_HOSPITAL,types.TYPE_BANK])

#if query_result.has_attributions:
a=2
try:
	a= query_result.places
except:
	print "eerrr"

print a
