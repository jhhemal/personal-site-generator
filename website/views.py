from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import WebsiteForm, SkillForm, InterestForm, EducationForm, BadgeForm
from .models import Website, Skill, Interest, Education, Badge
from account.models import User

# Create your views here.
def home(request):
    return render(request, 'website/index.html')

# def site(request):
#     return render(request, 'website/site.html')

class SettingsView(LoginRequiredMixin, UpdateView):
    form_class = WebsiteForm
    model = Website
    context_object_name = 'website'
    template_name = 'website/settings.html'
    success_url = reverse_lazy('settings')

    # def dispatch(self, request, *args, **kwargs):
    #     username = 

    # def get_queryset(self):
    #     site = self.model.objects.filter(user=self.request.user)
    #     return site
    # slug_field = 'website.user.username'
    # slug_url_kwarg = 'website.user.username'

    def get_object(self, queryset=None):
        site = self.model.objects.get(user=self.request.user)
        return site

    # def test_func(self):
    #     obj = self.model.objects.get(user=self.request.user)
    #     if obj:
    #         return True
    #     else:
    #         return False

class SkillListview(ListView):
    model = Skill
    template_name = 'website/skill_list.html'
    context_object_name = 'skills'


    def get_queryset(self):
        skills = self.model.objects.filter(website__user=self.request.user)
        return skills

class SkillCreateView(CreateView):
    form_class = SkillForm
    template_name = 'website/skill_create.html'
    success_url = reverse_lazy('settings')

    def form_valid(self, form):
        form.instance.website = Website.objects.get(user=self.request.user)
        messages.success(self.request, "Skill has been added")
        return super().form_valid(form)

class SkillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'website/skill_update.html'
    success_url = reverse_lazy('skill-list')

    def form_valid(self, form):
        form.instance.website = Website.objects.get(user=self.request.user)
        messages.success(self.request, "Skill has been updated")
        return super().form_valid(form)

    def test_func(self):
        skill = self.get_object()
        if self.request.user == skill.website.user:
            return True
        else:
            return False

class SkillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Skill
    success_url= reverse_lazy('skill-list')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, "Skill has been deleted")
        return super(SkillDeleteView, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        skill = self.get_object()
        if self.request.user == skill.website.user:
            return True
        else:
            return False

class InterestListview(ListView):
    model = Interest
    template_name = 'website/interest_list.html'
    context_object_name = 'interests'


    def get_queryset(self):
        skills = self.model.objects.filter(website__user=self.request.user)
        return skills

class InterestCreateView(CreateView):
    form_class = InterestForm
    template_name = 'website/interest_create.html'
    success_url = reverse_lazy('interest-list')

    def form_valid(self, form):
        form.instance.website = Website.objects.get(user=self.request.user)
        messages.success(self.request, "Interest has been added")
        return super().form_valid(form)

class InterestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Interest
    form_class = InterestForm
    template_name = 'website/interest_update.html'
    success_url = reverse_lazy('interest-list')

    def form_valid(self, form):
        form.instance.website = Website.objects.get(user=self.request.user)
        messages.success(self.request, "Interest has been updated")
        return super().form_valid(form)

    def test_func(self):
        skill = self.get_object()
        if self.request.user == skill.website.user:
            return True
        else:
            return False

class InterestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Skill
    success_url= reverse_lazy('interest-list')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, "Interest has been deleted")
        return super(InterestDeleteView, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        skill = self.get_object()
        if self.request.user == skill.website.user:
            return True
        else:
            return False

class EducationListview(ListView):
    model = Education
    template_name = 'website/education_list.html'
    context_object_name = 'educations'


    def get_queryset(self):
        educations = self.model.objects.filter(website__user=self.request.user)
        return educations

class EducationCreateView(CreateView):
    form_class = EducationForm
    template_name = 'website/education_create.html'
    success_url = reverse_lazy('education-list')

    def form_valid(self, form):
        form.instance.website = Website.objects.get(user=self.request.user)
        messages.success(self.request, "Education has been added")
        return super().form_valid(form)

class EducationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'website/education_update.html'
    success_url = reverse_lazy('education-list')

    def form_valid(self, form):
        form.instance.website = Website.objects.get(user=self.request.user)
        messages.success(self.request, "Education has been updated")
        return super().form_valid(form)

    def test_func(self):
        skill = self.get_object()
        if self.request.user == skill.website.user:
            return True
        else:
            return False

class EducationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Education
    success_url= reverse_lazy('education-list')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, "Education has been deleted")
        return super(EducationDeleteView, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        skill = self.get_object()
        if self.request.user == skill.website.user:
            return True
        else:
            return False

class BadgeListview(ListView):
    model = Badge
    template_name = 'website/badge_list.html'
    context_object_name = 'badges'


    def get_queryset(self):
        badges = self.model.objects.filter(website__user=self.request.user)
        return badges

class BadgeCreateView(CreateView):
    form_class = BadgeForm
    template_name = 'website/badge_create.html'
    success_url = reverse_lazy('badge-list')

    def form_valid(self, form):
        form.instance.website = Website.objects.get(user=self.request.user)
        messages.success(self.request, "Badge has been added")
        return super().form_valid(form)

class BadgeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Badge
    form_class = BadgeForm
    template_name = 'website/badge_update.html'
    success_url = reverse_lazy('badge-list')

    def form_valid(self, form):
        form.instance.website = Website.objects.get(user=self.request.user)
        messages.success(self.request, "Badge has been updated")
        return super().form_valid(form)

    def test_func(self):
        badge = self.get_object()
        if self.request.user == badge.website.user:
            return True
        else:
            return False

class BadgeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Badge
    success_url= reverse_lazy('badge-list')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, "Badge has been deleted")
        return super(BadgeDeleteView, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        badge = self.get_object()
        if self.request.user == badge.website.user:
            return True
        else:
            return False

# def hello(request):
#     return render(request, 'website/hello.py')

class WebsiteView(DetailView):
    model = User
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self):
        user = User.objects.get(username=self.kwargs['username'])
        return user
    
    def get_template_names(self):
        user = User.objects.get(username=self.kwargs['username'])
        if user.website.template == 'default' or user.website.template == None:
            return 'website/template1/index.html'