from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from manage_quotes.models import Quote
from manage_users.models import User


class AddQuote(CreateView):
    model = Quote
    fields = ['body', 'person', 'place', 'category', ]
    success_url = '/view/all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['local_css'] = ['css/myforms.css', ]
        return context

    def form_valid(self, form):
        form.instance.fk_usr = User.objects.get(username=self.request.session['username'])
        return super().form_valid(form)


class DeleteQuote(DeleteView):
    model = Quote
    success_url = '/view/all'


class EditQuote(UpdateView):
    model = Quote
    fields = ['body', 'person', 'place', 'category', ]
    success_url = '/view/all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['local_css'] = ['css/myforms.css', ]
        return context
