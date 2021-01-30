from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rooms import models as rooms_models
from . import models

class RoomInline(admin.TabularInline):
    model = rooms_models.Room

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost", )
    
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
