import math

def rad2deg(rad):
  return (rad * 180.0 / math.pi)
def deg2rad(deg):
    return (deg*180.0/math.pi)
def distanceInKm(lat1 , lon1,lat2 ,lon2 ):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    R = 6371.0;

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance;
