from . import views
from django.urls import path


urlpatterns = [
    path('', views.PreviewList.as_view(), name='home'),
    path('directory/', views.LocationList.as_view(), name='directory'),
    # path('bookmarks/', views.BookmarkList.as_view(), name='bookmarks'),
    path('<slug:slug>/', views.LocationDetails.as_view(), name='location'),
    path(
        'bookmark/<slug:slug>/', views.LocationBookmark.as_view(),
        name='location_bookmark'
        ),
]