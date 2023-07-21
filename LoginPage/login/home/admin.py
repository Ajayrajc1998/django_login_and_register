from django.contrib import admin
from .models import Faculty,Services,BookService
# Register your models here.
admin.site.register(Faculty)
admin.site.register(Services)
class bookingadmin1(admin.ModelAdmin):
    list_display=('id','b_name','b_phone','b_email','b_service','b_date')
admin.site.register(BookService,bookingadmin1)