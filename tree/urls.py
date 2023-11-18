from django.urls import path
from tree.views import TreeMenuView, MenuListView

urlpatterns = [
    path('<str:slug>', TreeMenuView.as_view(), name='choose_menu'),
    path('', MenuListView.as_view(), name='index')
]
