from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializer import ReviewSerializer


class RoomListSerializer(ModelSerializer):

    rating = SerializerMethodField()
    is_owner = SerializerMethodField()

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
        )

    def get_rating(self, rooms):
        return rooms.rating()

    def get_is_owner(self, room):
        request = self.context.get("request")
        if request:
            return room.owner == request.user
        return False


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    is_owner = SerializerMethodField()
    reviews = ReviewSerializer(
        many=True,
        read_only=True,
    )

    rating = SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

    def get_rating(self, rooms):
        return rooms.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user
