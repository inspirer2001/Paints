from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('signup/', views.signup, name='store-signup'),
    path('login/', views.Login, name='store-login'),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('logout/', views.logout, name='store-logout'),
	path('productviews/', views.productview, name='store-productviews'),
]