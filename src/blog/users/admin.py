from django.contrib import admin


from .models import User

class UserAdmin(admin.ModelAdmin):

    search_fields = ['email', 'first_name', 'last_name']
    fieldsets = [
        ('info', {'fields' : ('email', 'first_name', 'last_name', 'last_login')}),
        ('permissions', {'fields' : ('is_active', 'is_staff', 'is_superuser', 'user_permissions')})
    ]
    class Meta:
        model = User

admin.site.register(User, UserAdmin)