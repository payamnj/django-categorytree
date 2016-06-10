from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=250)
    parent = models.ForeignKey('self', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        if self.parent:
            return '%s > %s' % (self.parent.title, self.title)
        else:
            return self.title
        return '%s_%s' % (self._meta.app_label, self._meta.object_name)

    def sub_categories(self):
        childs = type(self).objects.filter(parent=self)
        output = '<ul>'
        for child in childs:
            subchilds = child.sub_categories()
            url = reverse('admin:%s_%s_change' % (
                self._meta.app_label.lower(),
                self._meta.object_name.lower()), args=(child.id,))
            output = '%s<li><a href=\'%s\'>%s</a>%s</li>' % (
                output, url, child.title, subchilds)

        output = '%s</ul>' % output
        return output

    sub_categories.allow_tags = True

    class Meta:
        abstract = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
