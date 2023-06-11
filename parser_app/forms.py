from django import forms
from . import models, parser_film, parser_product


class ParserForm(forms.Form):
    MEDIA_CHOISES = (("FILMS_KG", "FILMS_KG"), ("PRODUCT", "PRODUCT"))
    media_type = forms.ChoiceField(choices=MEDIA_CHOISES)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        media_type = self.cleaned_data["media_type"]
        if media_type == "FILMS_KG":
            film_parser = parser_film.parser()
            for i in film_parser:
                models.TvParser.objects.create(**i)
        elif media_type == "PRODUCT":
            product_parser = parser_product.parser()
            for i in product_parser:
                models.PrParser.objects.create(**i)
