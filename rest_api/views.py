from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_api.helper import distanceInKm
from rest_api.models import Parking_Lot, User, Booking, Rated
from rest_api.serializers import Parking_Lot_Serializer, User_Serializer, Booking_Serializer, Rated_Serializer


#Parking lot Views
@api_view(['GET'])
def parking_distance(request,olat,olongt,km):
    if(request.method=='GET') :
        partkings =Parking_Lot.objects.all().iterator();
        parkings_in_area = []
        x =0;
        for park in partkings:
            x = distanceInKm(lat1=float(olat), lon1=float(olongt), lon2=park.longt, lat2=park.lat)
            print(x)
            if float(km) >= x :
                parkings_in_area.append(park)

    parkingSer=Parking_Lot_Serializer(parkings_in_area, many=True);
    return Response(parkingSer.data)

@api_view(['GET','POST','DELETE','PUT'])
def parking(request):
    #listing
    if(request.method== 'GET') :
        parkings = Parking_Lot.objects.all()
        parkingsSer = Parking_Lot_Serializer(parkings,many=True);
        return Response(parkingsSer.data)
    elif (request.method== 'POST') :
        serializer = Parking_Lot_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)
        return JsonResponse(serializer.errors, safe=True)
    elif (request.method == 'PUT'):
        park =Parking_Lot.objects.get(id=request.data['id'])
        serializer = Parking_Lot_Serializer(park, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)
        return JsonResponse(serializer.errors, safe=True)
    elif (request.method == 'DELETE'):
        park = Parking_Lot.objects.get(id=request.data['id'])
        park.delete()
        return JsonResponse(park, safe=True)


#Users Views
@api_view(['GET'])
def users_pk(request,pk) :
    if (request.method == 'GET'):
        users = get_object_or_404(User,mat=pk)
        userSer = User_Serializer(users);
        return Response(userSer.data)
@api_view(['GET','POST','DELETE','PUT'])
def users(request):
    #listing
    # Login Here -----------------------------------------
    if(request.method== 'GET') :
        users = User.objects.all()
        usersSer = User_Serializer(users,many=True);
        return Response(usersSer.data)
    #Singup --------------------------------------------------------
    elif (request.method== 'POST') :
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)
        return JsonResponse(serializer.errors, safe=True)


#Bookings  Views
@api_view(['GET'])
def bookings_user(request, userid):
    if(request.method== 'GET') :
        bookings = Booking.objects.all().filter(user=userid)
        bookingsSer = Booking_Serializer(bookings,many=True);
        return Response(bookingsSer.data)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def bookings(request):
    # listing
    if (request.method == 'GET'):
        bookings = Booking.objects.all()
        bookingsSer = Booking_Serializer(bookings, many=True);
        return Response(bookingsSer.data)
        # ToBook ------------------------------------
    elif (request.method == 'POST'):
        serializer = Booking_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)
        return JsonResponse(serializer.errors, safe=True)

@api_view(['GET','POST','DELETE','PUT'])
def ratings(request):
    #listing
    #Get Ratings
    if(request.method== 'GET') :
        ratings = Rated.objects.all()
        ratingsSer = Parking_Lot_Serializer(ratings,many=True);
        return Response(ratingsSer.data)

    # To Rate
    elif (request.method== 'POST') :
        serializer = Rated_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)
        return JsonResponse(serializer.errors, safe=True)
