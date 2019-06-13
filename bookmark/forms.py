from django import forms

from bookmark.models import BookmarkItem


class BookmarkForm(forms.ModelForm):
    site_name = forms.CharField(
        max_length=50,
        label='사이트 이름',
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2'},
        ),
    )
    site_url = forms.URLField(
        label='URL',
        widget=forms.URLInput(
            attrs={'class': 'form-control mt-2'},
        ),
    )

    class Meta:
        model = BookmarkItem
        fields = ['site_name', 'site_url']
        # TODO: add validator
