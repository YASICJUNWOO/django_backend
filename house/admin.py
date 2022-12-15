from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):

    list_display = ("name", "price_per_night", "description", "address", "pet_allowed")
    list_filter = ("price_per_night", "pet_allowed")
    # 튜플 원소가 한개라면 뒤에 콤마 붙여주어야함
    # 뒤에 __startwith 붙여주면 시작하는 단어만 찾아줌
