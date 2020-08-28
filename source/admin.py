from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from source.models import MyUser, Ticket
class CustomUserAdmin(UserAdmin):
        fieldsets = (
        *UserAdmin.fieldsets, 
        (                      
            'Custom Fields',  
            {
                'fields': (                    
                    'bio',              

                ),
            },
        ),
    )
admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(Ticket)
