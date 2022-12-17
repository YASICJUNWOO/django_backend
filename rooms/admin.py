from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "created_at",
        "updated_at",
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
