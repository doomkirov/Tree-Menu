from django.views.generic.base import TemplateView
from tree.models import TreeMenuModel


class MenuListView(TemplateView):
    """
    ViewTemplate to generate index.html where user can choose
    which menu to draw
    """
    template_name = 'tree_menu/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_list'] = [elem for elem in TreeMenuModel.objects.all()]
        return context


class TreeMenuView(TemplateView):
    """
    ViewTemplate for choosen_menu.html to generate a page for
    TreeMenuModel which is specified by slug that user provided
    """
    template_name = 'tree_menu/choosen_menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = TreeMenuModel.objects.filter(slug=self.kwargs.get('slug')).first()
        return context
