
from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_view,name="adddata"),
    path('delete/<int:id>/',views.delete_view,name="deletedata"),
    path('<int:id>/',views.update_view,name="updateview"),
    path('csv/',views.getfile,name='csv')
]
