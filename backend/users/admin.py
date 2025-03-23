from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin for the Profile model."""
    list_display = ('user', 'bio', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'bio')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

# Admin for user is already registered
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
#     search_fields = ('username', 'email')
#     list_filter = ('is_staff', 'is_active')
#     readonly_fields = ('date_joined', 'last_login') 