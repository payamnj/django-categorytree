from django import forms


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        try:
            exclude_ids = [kwargs['instance'].id]
            exclude_ids += self.child_ids(kwargs['instance'])
            qs = self._meta.model.objects.exclude(id__in=exclude_ids)
        except:
            qs = self._meta.model.objects.all()

        self.fields['parent'] = forms.ModelChoiceField(
            queryset=qs,
            required=False)

    def child_ids(self, instance):
        child_id_list = []
        items = type(instance).objects.filter(parent=instance)
        for item in items:
            child_id_list.append(item.id)
            child_id_list += self.child_ids(item)

        return child_id_list

    class Meta:
        exclude = ('active',)


class CategorySuperuserForm(CategoryForm):
    class Meta:
        fields = '__all__'
