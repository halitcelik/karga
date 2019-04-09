from django import forms
from django.utils.text import slugify
from .models import Recipe, HopType


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'name',
            'difficulty',
            'original_gravity_plato',
            'final_gravity_plato',
            'original_gravity_sg',
            'final_gravity_sg',
            'abv',
            'image',
            'style',
            'mash_time',
            'boil_time',
            'short_description',
            'ingredients',
            'long_description'
        )



    def save(self):
        instance = super(RecipeForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()

        return instance


    # A nice and clean way of setting labels as placeholders.
    # def __init__(self, *args, **kwargs):
    #     super(RecipeForm, self).__init__(*args, **kwargs)
    #     for key, field in self.fields.items():
    #         if isinstance(field.widget, forms.TextInput) or \
    #             isinstance(field.widget, forms.NumberInput):
    #                 field.widget.attrs.update({'placeholder': field.label + ':'})



class HopTypeForm(forms.ModelForm):
    class Meta:
        model = HopType
        fields = ('hop_type', 'added_at', 'hop_quantity')


    def __init__(self, *args, **kwargs):
        super(HopTypeForm, self).__init__(*args, **kwargs)
        self.fields['added_at'].widget.attrs.update({'placeholder': 'minute'})
