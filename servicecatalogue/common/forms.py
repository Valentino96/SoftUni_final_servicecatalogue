from django import forms

from servicecatalogue.common.models import Service, ServiceComment, ServiceLike


class SearchServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('type',)


class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('type', 'description', 'location')


class EditServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('type', 'description', 'location')


class DeleteServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('type', 'description', 'location')

    def save(self, commit=True):
        if commit:
            ServiceLike.objects.filter(service_id=self.instance.id) \
                .delete()
            ServiceComment.objects.filter(service_id=self.instance.id) \
                .delete()
            self.instance.delete()
        return self.instance


class ServiceCommentForm(forms.ModelForm):
    class Meta:
        model = ServiceComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                },
            ),
        }