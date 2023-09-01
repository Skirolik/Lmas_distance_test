import requests
from distance_calculation import distance_calculation
from get_weather_data import get_weather_data




user_latitude = 9.925730045317891
user_longitude= 78.10013479091396
distance= 22



north_lat, north_lon = distance_calculation(user_latitude, user_longitude, distance, 'north')
south_lat, south_lon = distance_calculation(user_latitude, user_longitude, distance, 'south')
east_lat, east_lon = distance_calculation(user_latitude, user_longitude, distance, 'east')
west_lat, west_lon = distance_calculation(user_latitude, user_longitude, distance, 'west')
south_east_lat, south_east_lon = distance_calculation(user_latitude, user_longitude, distance, 'south_east')
south_west_lat, south_west_lon = distance_calculation(user_latitude, user_longitude, distance, 'south_west')

north_east_lat, north_east_lon = distance_calculation(user_latitude, user_longitude, distance, 'north_east')
north_west_lat, north_west_lon = distance_calculation(user_latitude, user_longitude, distance, 'north_west')



# print('northlat:',north_lat)
# print('northlon:',north_lon)
# print('southlat:',south_lat)
# print('south_lon:',south_lon)
# print('east_lat:',east_lat)
# print('east_lon:',east_lon)
# print('west_lat:',west_lat)
# print('west_lon:',west_lon)
# print('south_east_lat:',south_east_lat)
# print('south_east_lon:',south_east_lon)
# print('south_west_lat:',south_west_lat)
# print('south_west_lon:',south_west_lon)
#
#
# print('north_east_lat:',north_east_lat)
# print('north_east_lon:',north_east_lon)
# print('north_west_lat:',north_west_lat)
# print('north_west_lon:',north_west_lon)








user_weather = get_weather_data(user_latitude, user_longitude)
north_weather = get_weather_data(north_lat, north_lon)
south_weather = get_weather_data(south_lat, south_lon)
east_weather = get_weather_data(east_lat, east_lon)
west_weather = get_weather_data(west_lat, west_lon)
south_east_weather = get_weather_data(south_east_lat, south_east_lon)
south_west_weather = get_weather_data(south_west_lat, south_west_lon)
north_east_weather = get_weather_data(north_east_lat, north_east_lon)
north_west_weather = get_weather_data(north_west_lat, north_west_lon)

#
#
print(user_weather)
#
print('north',north_weather)
print('south',south_weather)
print('east',east_weather)
print('west',west_weather)
print('south_east',south_east_weather)
print('south_west',south_west_weather)
print('north_east',north_east_weather)
print('north_east',north_west_weather)
