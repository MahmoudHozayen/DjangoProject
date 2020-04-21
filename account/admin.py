from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
# Register your models here.


class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('email', 'username',)
	readonly_fields = ('date_joined', 'last_login')


	add_fieldsets = (
	(None, {
	'classes': ('wide',),
	'fields': ('email', 'username',  'password1', 'password2','is_admin', 'is_active',  'is_staff', 'is_superuser'),
	}),
	)
	filter_horizontal = ()
	list_filter = ('is_admin', 'is_active',  'is_staff', 'is_superuser')
	fieldsets = ()

admin.site.register(Account, AccountAdmin)