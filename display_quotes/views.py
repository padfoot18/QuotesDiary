from django.shortcuts import render, redirect
from django.views.generic import ListView
from manage_quotes.models import Quote


def check(request):
    if 'username' in request.session:
        return redirect('view/all')
    else:
        return redirect('/user/login')


class QuotesList(ListView):
    model = Quote
    context_object_name = 'quote_list'
    template_name = 'home.html'
    paginate_by = 10

    def get_queryset(self):
        self.fk_user = self.request.session['username']
        self.category = self.kwargs['category']
        if self.category == 'all':
            return Quote.objects.filter(fk_usr_id=self.fk_user).order_by('-create_time', '-id')
        else:
            return Quote.objects.filter(fk_usr_id=self.fk_user,
                                        category__iexact=self.category).order_by('-create_time', '-id')


"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'page' in self.request.GET:
            curr = int(self.request.GET['page'])
            if curr > 4:
                context['my_page_range'] = [x for x in range(curr-3, curr+4)]
        return context
"""