# coding: utf-8
from django.shortcuts import get_object_or_404, render,render_to_response,redirect
from vkrm.models import State,Age, GreatPersonality, GreatEvent, GreatDiscovery, Article, Wonder
from django.views import generic
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import ArticleForm
from django.contrib.auth.models import User

from vkrm.permission_resolver import get_object_permissions_for_user


class States(generic.ListView):
    template_name = 'states.html'
    context_object_name = 'states_list'

    def get_queryset(self):
        states = list(State.objects.order_by('state_birth_year'))
        for state in states:
            state.permissions = get_object_permissions_for_user(self.request.user, state)
        return [state for state in states if state.permissions.get('read')]


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'age_list'

    def get_queryset(self):
        return Age.objects.order_by('age_year')


class Personalities(generic.ListView):
    template_name = 'personalities.html'
    context_object_name = 'pers_list'

    def get_queryset(self):
        return GreatPersonality.objects.order_by('pers_name')


class Events(generic.ListView):
    template_name = 'events.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        return GreatEvent.objects.order_by('event_year')


class Discoveries(generic.ListView):
    template_name = 'discoveries.html'
    context_object_name = 'disc_list'

    def get_queryset(self):
        return GreatDiscovery.objects.order_by('discovery_year')


class Articles(generic.ListView):
    template_name = 'articles.html'
    context_object_name = 'articles_list'

    def get_queryset(self):
        return Article.objects.order_by('-article_date')


class DetailState(generic.DetailView):
    model = State
    template_name = 'detail_state.html'


class DetailAge(generic.DetailView):
    model = Age
    template_name = 'detail_age.html'


class DetailPersonality(generic.DetailView):
    model = GreatPersonality
    template_name = 'detail_personality.html'


class DetailEvent(generic.DetailView):
    model = GreatEvent
    template_name = 'detail_event.html'


class DetailDiscovery(generic.DetailView):
    model = GreatDiscovery
    template_name = 'detail_discovery.html'


class DetailArticle(generic.DetailView):
    model = Article
    template_name = 'detail_article.html'


def WorkView(request):
    return render(request, 'main.html')


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response("login.html", args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)


def addArticle(request):
    args = {}
    args.update(csrf(request))
    args['form'] = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(data=request.POST)
        if int(form.data['author']) != request.user.id:
            form.errors['author'] = (u'Пользователь не тот',)
        if form.is_valid():
            form.save()
            return redirect('/articles/')
        else:
            args['form'] = form
    return render(request, 'addArticle.html', args)


def editArticle(request, pk):
    args = {}
    args.update(csrf(request))
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
        else:
            args['form'] = form
        return redirect('/editArticle/{}/'.format(pk))
    else:
        args['form'] = ArticleForm(instance=article)
        return render(request, 'editArticle.html', args)


def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('/articles/')

class Wonders(generic.ListView):
    template_name = 'wonders.html'
    context_object_name = 'wonder_list'

    def get_queryset(self):
        return Wonder.objects.order_by('wonder_year')


class DetailWonder(generic.DetailView):
    model = Wonder
    template_name = 'detail_wonder.html'
