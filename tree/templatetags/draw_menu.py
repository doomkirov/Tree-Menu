from django import template
from django.db.models.query import QuerySet

from tree.models import TreeMenuModel, TreeMenuItemModel

register = template.Library()


@register.inclusion_tag('tree_menu/tree_menu.html', takes_context=True)
def draw_menu(context: template.Context, menu: str) -> dict:
    """
    Inclusion template tag to draw tree_menu.html

    :param context: context with request params
    :param menu: Menu.title
    :return: dict with data to render tree_menu.html template
    """

    # get all the items with menu__title = menu and their values
    objects = TreeMenuItemModel.objects.filter(menu__title=menu)
    root = [item for item in objects.values().filter(parent=None)]
    if not root:
        return {
            'items': None,
            'menu': menu
        }

    # get selected item slug from context['request'] or get a slug of the first item with no parents
    selected_slug = str(context['request'].GET.get(menu, objects.values().filter(parent=None).first()['slug']))
    selected_item = objects.filter(slug=selected_slug).first()
    selected_item_slug_list = []

    # add all parents of a selected_item to a list
    while selected_item:
        selected_item_slug_list.append(selected_item.slug)
        selected_item = selected_item.parent

    # find all children of selected items and assign them to root[item] dict
    for item in root:
        if item['slug'] in selected_item_slug_list:
            item['child_items'] = get_child_items(objects.values(), item['slug'], selected_item_slug_list)

    return {
        'items': root,
        'menu': menu,
        'selected_slug': selected_slug
    }


def get_child_items(
        values: QuerySet,
        item_slug: str,
        selected_item_slug_list: list[str]
) -> list[dict]:
    """
    Function to find all children of the specified item

    :param values: django.db.models.query.QuerySet object of all items.values()
    :param item_slug: slug of the item which children needed to find
    :param selected_item_slug_list: list of slugs of all items that are selected
    :return: children list of a parent item_slug
    """

    item_list = [item for item in values.filter(parent__slug=item_slug)]
    for item in item_list:
        if item['slug'] in selected_item_slug_list:
            item['child_items'] = get_child_items(values, item['slug'], selected_item_slug_list)
    return item_list
