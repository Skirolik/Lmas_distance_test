from math import radians, degrees


def distance_calculation(lat,lon,distance,direction):
    earth_radius = 6371.0

    lat_rad = radians(lat)
    lon_rad = radians(lon)

    distance_in_radians = distance / earth_radius

    if direction == 'north':
        new_lat=degrees(lat_rad+distance_in_radians)
        new_lon=degrees(lon_rad)
    elif direction == 'south':
        new_lat=degrees(lat_rad-distance_in_radians)
        new_lon=degrees(lon_rad)
    elif direction == 'east':
        new_lat=degrees(lat_rad)
        new_lon=degrees(lon_rad+distance_in_radians)
    elif direction == 'west':
        new_lat=degrees(lat_rad)
        new_lon=degrees(lon_rad-distance_in_radians)
    elif direction == 'south_west':
        new_lat=degrees(lat_rad-distance_in_radians)
        new_lon=degrees(lon_rad-distance_in_radians)
    elif direction == 'south_east':
        new_lat=degrees(lat_rad-distance_in_radians)
        new_lon=degrees(lon_rad+distance_in_radians)
    elif direction == 'north_west':
        new_lat=degrees(lat_rad+distance_in_radians)
        new_lon=degrees(lon_rad-distance_in_radians)
    elif direction == 'north_east':
        new_lat=degrees(lat_rad+distance_in_radians)
        new_lon=degrees(lon_rad+distance_in_radians)
    else:
        return ValueError("invalid")

    return new_lat,new_lon

