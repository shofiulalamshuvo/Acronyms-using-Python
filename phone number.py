import phonenumbers
#add a new python file named test.py to import your phone number
from test import number

#find out your country
from phonenumbers import geocoder
cH_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(cH_number, "en"))

#find out your service provider company name
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

