#Exercise 4.5: Print the values of name , post_code and street_number from the dictionary

place = {
 'name': 'The Anchor',
 'post_code': 'E14 6HY',
 'street_number': '54',
 'location': {
   'longitude': 127,
   'latitude': 63,
   }
 }

print(place['name'])
print(place['post_code'])
print(place['street_number'])

#Extension: Print the values of longitude and latitude from the inner dictionary

print(place['location']['longitude'])
print(place['location']['latitude'])