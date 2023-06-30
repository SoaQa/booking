from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import ApiUser, Hotel, Room, Booking
from api.serializers import UserSerializer, HotelSerializer, RoomSerializer, BookingSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = UserSerializer

    authentication_classes = []
    permission_classes = []


class HotelModelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(detail=True)
    def rooms(self, request, pk=None):
        hotel = get_object_or_404(Hotel.objects.all(), id=pk)
        free_rooms = hotel.rooms.filter(bookings__isnull=True)
        return Response(
            RoomSerializer(free_rooms, many=True).data
        )


class RoomModelViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingModelViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
