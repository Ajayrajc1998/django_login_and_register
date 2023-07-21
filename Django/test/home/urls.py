from django.urls import path,include  
from .views import index,about,doctors,contact
urlpatterns = [
    path('', index,name='sample'),
    path('admin/', admin.site.urls),
    path('about', about),
    path('doctors', doctors),
    path('contact', contact),        
]
