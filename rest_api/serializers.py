from rest_api.models import Parking_Lot, User, Booking, Rated
from rest_framework  import serializers
class Parking_Lot_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Parking_Lot
        fields= ('id','name','lat','longt','photo','max_places','open_hour','close_hour','rating','price','info')

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'mat', 'password')

class Booking_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Booking
        #fields = ('id', 'parking_lot', 'mat', 'date_time','penalty')

class Rated_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Rated
        fields = ('id', 'parking_lot', 'mat', 'rating')