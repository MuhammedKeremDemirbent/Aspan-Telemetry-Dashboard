from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Admin listesinde görünecek sütunlar
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)

    # Kullanıcı düzenleme formu
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Kişisel Bilgiler', {'fields': ('first_name', 'last_name', 'phone')}),
        ('İzinler', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Tarihler', {'fields': ('last_login', 'date_joined')}),
    )

    # Yeni kullanıcı oluşturma formu
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
