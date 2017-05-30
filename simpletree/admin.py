from django.contrib import admin
from .forms import NodeForm, NodeSuperuserForm

class NodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_nodes', 'active']

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = NodeSuperuserForm
        else:
            kwargs['form'] = NodeForm

        return super(NodeAdmin, self).get_form(request, obj, **kwargs)

    def get_queryset(self, request):
        queryset = super(NodeAdmin, self).get_queryset(request)

        if request.path_info == '/admin/%s/%s/' % (
                self.model._meta.app_label.lower(),
                self.model._meta.object_name.lower()):

            queryset = queryset.filter(parent__isnull=True)

        return queryset

    class Meta:
        abstract = True
