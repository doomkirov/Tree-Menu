from django.contrib import admin
from tree.models import TreeMenuModel, TreeMenuItemModel


@admin.register(TreeMenuModel)
class TreeMenuModelAdmin(admin.ModelAdmin):
    """
    TreeMenuModel configurator
    """
    list_display = ('pk', 'title', 'slug')
    search_fields = ('title',)


@admin.register(TreeMenuItemModel)
class TreeMenuItemModelAdmin(admin.ModelAdmin):
    """
    Configurator for items in Tree (TreeMenuItemModel)
    """
    list_display = ('pk', 'title', 'menu', 'slug', 'parent')
    search_fields = ('pk', 'title', 'slug')
    ordering = ('menu', 'pk')
