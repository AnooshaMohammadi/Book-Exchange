from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Book, Exchange


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('firstname', 'lastname', 'email', 'phonenumber', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'firstname', 'lastname', 'is_staff')
    search_fields = ('username', 'email', 'firstname', 'lastname')
    ordering = ('username',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'owner')
    search_fields = ('name', 'author', 'owner__username')


class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('thebook', 'borrower', 'lender', 'status', 'date')
    search_fields = ('thebook__name', 'borrower__username', 'lender', 'status')
    list_filter = ('status', 'date')


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Exchange, ExchangeAdmin)
# Register your models here.
