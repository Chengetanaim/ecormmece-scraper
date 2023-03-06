from django.urls import path
from . import views
from .views import SearchResultsView


app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path('store/', views.store, name='store'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('website/<int:website_id>/', views.website, name='website'),
    path('about-us/', views.about_us, name='about_us'),
    path('search-results/', SearchResultsView.as_view(), name='search_results'),
    path('create/', views.image_create, name='create'),
    path('mybookmarks/', views.mybookmarks, name='mybookmarks'),
    path('mybookmark/<int:bookmark_id>/', views.mybookmark, name='mybookmark'),
    path('like/', views.image_like, name='like'),
    path('mobile-search/', views.mobile_search, name='mobile_search')
]