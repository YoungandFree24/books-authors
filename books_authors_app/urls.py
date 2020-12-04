from django.urls import path
from . import views

urlpatterns = [
	path('', views.books),
	path('circle',views.creating_book),
	
	# use you only these work
	path('you',views.author),
	path('creating_author',views.creating_author),
    path('thanku',views.thanku),
	path('process', views.process),
	path('details/<int:id_from_route>',views.details)
]