from django import forms


class PlayerSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["q"].widget.input_type = "search"
        # These fields are added for dropdown functionality with Bootstrap5
        self.fields["q"].widget.attrs.update({"data-bs-toggle": "dropdown"})
        self.fields["q"].widget.attrs.update({"placeholder": "Player Search"})
        self.fields["q"].widget.attrs.update({"autocomplete": "off"})
        self.fields["q"].widget.attrs.update({"class": "menudd"})
