from django.shortcuts import render, redirect
from django.views.generic import ListView
from manage_quotes.models import Quote
from django.http import JsonResponse
from django.db.models import Q


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['js_files'] = ['js/search_bar.js']
        return context


def search_results(request):
    search_text = request.GET.get('search_text', None)
    fk_user = request.session.get('username')
    body_res = list(Quote.objects.filter(fk_usr_id=fk_user, body__contains=search_text).values_list('body', flat=True).distinct().order_by('body')[:5])
    person_res = list(Quote.objects.filter(fk_usr_id=fk_user, person__contains=search_text).values_list('person', flat=True).distinct().order_by('person')[:5])
    place_res = list(Quote.objects.filter(fk_usr_id=fk_user, place__contains=search_text).values_list('place', flat=True).distinct().order_by('place')[:5])

    body_res = [x[:40] for x in body_res]
    data = {'quote': body_res,
            'person': person_res,
            'place': place_res}
    return JsonResponse(data)


class SearchResultsView(ListView):
    model = Quote
    context_object_name = 'quote_list'
    template_name = 'home.html'
    paginate_by = 10

    def get_queryset(self):
        self.fk_user = self.request.session['username']
        if self.request.method == 'GET':
            search_text = self.request.GET.get('search-bar')
            return Quote.objects.filter(Q(fk_usr_id=self.fk_user),
                                        Q(body__contains=search_text) | Q(place__contains=search_text) | Q(place__contains=search_text))
        else:
            return Quote.objects.filter(fk_usr_id=self.fk_user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['js_files'] = ['js/search_bar.js']
        return context
