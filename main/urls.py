from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_lifestyle/', views.add_lifestyle, name='add_lifestyle'),
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
    path('finches/<int:finch_id>/add_photo/', views.add_photo, name='add_photo'),
    path('finches/<int:finch_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    path('accounts/signup/', views.signup, name='signup'),
]
