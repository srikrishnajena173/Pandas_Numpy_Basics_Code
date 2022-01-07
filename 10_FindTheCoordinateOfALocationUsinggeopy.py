# Here in this doc we will be looking into how to find the geo code of a location
#  (i.e latidute and longitude of a location)

# First install geopy dependencies using the below commands 
# pip3.8 install geopy

import geopy
dir(geopy) # Methods that present in the geopy and NOTE : we always need an internet to work with geopy dependencies

# O/P
# ['AlgoliaPlaces',
#  'ArcGIS',
#  'AzureMaps',
#  'BANFrance',
#  'Baidu',
#  'BaiduV3',
#  'Bing',
#  'DataBC',
#  'GeoNames',
#  'GeocodeEarth',
#  'Geocodio',
#  'Geolake',
#  'GoogleV3',
#  'Here',
#  'HereV7',
#  'IGNFrance',
#  'LiveAddress',
#  'Location',
#  'MapBox',
#  'MapQuest',
#  'MapTiler',
#  'Nominatim',
#  'OpenCage',
#  'OpenMapQuest',
#  'Pelias',
#  'Photon',
#  'PickPoint',
#  'Point',
#  'Timezone',
#  'TomTom',
#  'What3Words',
#  'What3WordsV3',
#  'Yandex',
#  '__builtins__',
#  '__cached__',
#  '__doc__',
#  '__file__',
#  '__loader__',
#  '__name__',
#  '__package__',
#  '__path__',
#  '__spec__',
#  '__version__',
#  '__version_info__',
#  'adapters',
#  'compat',
#  'exc',
#  'format',
#  'geocoders',
#  'get_geocoder_for_service',
#  'get_version',
#  'location',
#  'point',
#  'timezone',
#  'units',
#  'util']

from geopy.geocoders import ArcGIS
nom = ArcGIS()

# Example 1
nom.geocode("21 Rylance Streer, Manchester, United Kingdom")

# O/P :-
# Location(21 Rylance Street, Beswick, Manchester, Lancashire, England, M11 3, (53.47650735408637, -2.2060961749217536, 0.0))

# So here 53.47650735408637 :- Latitude and -2.2060961749217536 :- Longitude

# Example 2
nom.geocode("Chandragiri BDA Flats, Bidare Agraha, Post, Kannamangala, Doddabanahalli, Karnataka, India")

# O/P :-
# Location(Halli, Sagar Sub-District, Shivamogga, Karnataka, (13.976960000000076, 74.78201000000007, 0.0))

n = nom.geocode("Chandragiri BDA Flats, Bidare Agraha, Post, Kannamangala, Doddabanahalli, Karnataka, India")
type(n)

# O/P:
# geopy.location.Location , sp here n is Location type Object 

# Below script is to find the Longitude of a location
n.longitude
# O/P :- 74.78201000000007

# Below script is to find the latitude of a location
n.latitude
# O/P :- 13.976960000000076


# **********************************************************************************************************
# Example of fetching the geocode from the DataFrame 
import pandas
dataF = pandas.read_csv("geolocationplaintext.txt")
dataF

#   ID	Address	City	State	Country	Name
# 0	1	Chandragiri BDA Flat Bidare Agraha Post Kannam...	Bangalore	Karnataka	India	Sri
# 1	2	21 Rlyance Street	Manchester	Manchester	UK	Jena

# Now we are adding a new column called geolocation, where it will reflect the geocode of the 
# location given in the table
dataF["geolocation"] = dataF["Address"]+ ", "+dataF["City"]+ ", " +["State"]+ ", " +["Country"]
dataF

# O/P :
# ID	Address	City	State	Country	Name	geolocation
# 0	1	Chandragiri BDA Flat Bidare Agraha Post Kannam...	Bangalore	Karnataka	India	Sri	Chandragiri BDA Flat Bidare Agraha Post Kannam...
# 1	2	21 Rlyance Street	Manchester	Manchester	UK	Jena	21 Rlyance Street, Manchester, State, Country

# So now we have to add the geocode value in geolocation column , so we dont have to iterate through the each rows and add the 
# geocode value in the geolocation column, so in pandas we have inbuilt method which will update the value is all the rows

dataF["Coordinates"]=dataF["geolocation"].apply(nom.geocode) # So, here apply method will add all the value in the correspoding rows
dataF

# O/P :
#   ID	Address	City	State	Country	Name	geolocation	Coordinates
# 0	1	Chandragiri BDA Flat Bidare Agraha Post Kannam...	Bangalore	Karnataka	India	Sri	Chandragiri BDA Flat Bidare Agraha Post Kannam...	(Chandragiri, Chittoor, Andhra Pradesh, (13.57...
# 1	2	21 Rlyance Street	Manchester	Manchester	UK	Jena	21 Rlyance Street, Manchester, State, Country	(21 Rylance Street, Beswick, Manchester, Lanca...

# So, now get the coordinate value of first index
da1=dataF.Coordinates[0]
print(da1)

# O/P
# Location(Chandragiri, Chittoor, Andhra Pradesh, (13.579120000000046, 79.31314000000003, 0.0))

# to get the latitude value 
da1=dataF.Coordinates[0].latitude
print(da1)

# O/P :- 13.579120000000046

# to get the longitude value
da2=dataF.Coordinates[1].longitude
print(da2)

# O/P :-  -2.2060961749217536

# Now add the latitude and logitude column to the dataFrame and add the corresponding values to the rows
dataF["LatitudeVal"] = dataF["Coordinates"].apply(lambda x: x.latitude)
dataF["LongitudeVal"] = dataF["Coordinates"].apply(lambda y: y.longitude)
dataF

# O/P :

#   ID	Address	City	State	Country	Name	geolocation	Coordinates	LatitudeVal	LongitudeVal
# 0	1	Chandragiri BDA Flat Bidare Agraha Post Kannam...	Bangalore	Karnataka	India	Sri	Chandragiri BDA Flat Bidare Agraha Post Kannam...	(Chandragiri, Chittoor, Andhra Pradesh, (13.57...	13.579120	79.313140
# 1	2	21 Rlyance Street	Manchester	Manchester	UK	Jena	21 Rlyance Street, Manchester, State, Country	

