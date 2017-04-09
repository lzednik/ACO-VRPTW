

a=[{'address_components': [{'long_name': '54002', 'short_name': '54002', 'types':['postal_code']}, 
{'long_name': 'Baldwin', 'short_name': 'Baldwin', 'types': ['locality', 'political']}, 
{'long_name': 'St. Croix County', 'short_name': 'St Croix County', 'types': 
    ['administrative_area_level_2', 'political']}, 
    {'long_name': 'Wisconsin', 'short_name': 'WI', 'types': ['administrative_area_level_1', 'political']}, 
    {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}], 
    'place_id': 'ChIJ12fhEkUH-IcReIuyvU9Qqr0', 'types': ['postal_code'], 'geometry': {'location': {'lng': -92.3616203, 'lat': 44.957003}, 
    'bounds': {'northeast': {'lng': -92.298368, 'lat': 45.0934789}, 'southwest': {'lng': -92.43633609999999, 'lat': 44.859305}}, 
    'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lng': -92.298368, 'lat': 45.0934789}, 
        'southwest': {'lng': -92.43633609999999, 'lat': 44.859305}}}, 'formatted_address': 'Baldwin, WI 54002, USA'}]


print(a[0]['geometry']['location']['lat'])
print(a[0]['geometry']['location']['lng'])
