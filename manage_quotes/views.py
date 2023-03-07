from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from manage_quotes.models import Quote
from django.forms import ModelForm, Textarea, TextInput, Select
from django.conf import settings

User = settings.AUTH_USER_MODEL


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ["body", "person", "place", "category"]
        widgets = {
            "body": Textarea(attrs={"class": "form-control", "rows": "5"}),
            "person": TextInput(attrs={"class": "form-control"}),
            "place": TextInput(attrs={"class": "form-control"}),
            "category": Select(attrs={"class": "form-control"}),
        }


class AddQuote(CreateView):
    model = Quote
    success_url = "/view/all"
    form_class = QuoteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["local_css"] = [
            "css/myforms.css",
        ]
        return context

    def form_valid(self, form):
        form.instance.fk_usr = self.request.user
        return super().form_valid(form)


class DeleteQuote(DeleteView):
    model = Quote
    success_url = "/view/all"


class EditQuote(UpdateView):
    form_class = QuoteForm
    model = Quote
    template_name = "manage_quotes/quote_form.html"
    success_url = "/view/all"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["local_css"] = [
            "css/myforms.css",
        ]
        return context
