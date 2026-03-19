from django.contrib import admin

from .models import User,Transaction,Bet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','password','email')

    # def password(self,obj):
    #     return obj.password[12::]
    #
    # password.short_description = 'password'

admin.site.register(Transaction)
admin.site.register(Bet)

