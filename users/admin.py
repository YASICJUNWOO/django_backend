from django.contrib import admin

# admin.ModelAdmin이 아니라 UserAdmin으로 상속
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            # none
            "Profile",
            {
                "fields": ("username", "password", "name", "email", "is_host"),
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
                # "classes": ("wide",),
            },
        ),
        (
            ("Important dates"),
            {
                "fields": ("last_login", "date_joined"),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "name",
        "is_host",
    )
