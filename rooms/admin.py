from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "owner",
        "created_at",
    )
    list_filter = (
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    def total_amenities(self, room):
        return room.amenities.count()


@admin.register(Amenity)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    # 읽기 전용
    readonly_fields = (
        "created_at",
        "updated_at",
    )
