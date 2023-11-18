from typing import Union

from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class TreeMenuModel(models.Model):
    """
    Model class for all of menus that can contain multiple MenuItems
    """

    title = models.CharField(max_length=30, verbose_name='Menu title')
    slug = models.SlugField(max_length=30, verbose_name='Menu slug', blank=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TreeMenuModel, self).save(*args, **kwargs)


def get_default_menu() -> Union[TreeMenuModel, None]:
    """
    Returns first TreeMenuModel to be a default value.
    If there is no TreeMenuModel objects - return will be None
    """
    return TreeMenuModel.objects.filter(id=1).first()


class TreeMenuItemModel(models.Model):
    """
    Model class for all MenuItems that are linked to TreeMenu
    """

    title = models.CharField(max_length=30, verbose_name='Item title')
    slug = models.SlugField(max_length=30,verbose_name='Item slug', blank=True)
    menu = models.ForeignKey(
        TreeMenuModel, on_delete=models.CASCADE, blank=True,
        related_name='items', default=get_default_menu
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True,
        related_name='children', null=True
    )

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TreeMenuItemModel, self).save(*args, **kwargs)

