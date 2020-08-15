from django import forms
from .models import Skill, Website, Education, Interest, Badge

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title']

        widgets = {
            'title' : forms.TextInput(attrs={
                'placeholder' : "Enter Skill Name (i.e. Python)"
            })
        }

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ['title']

        widgets = {
            'title' : forms.TextInput(attrs={
                'placeholder' : "Enter Skill Name (i.e. Python)"
            })
        }

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['title']

        widgets = {
            'title' : forms.TextInput(attrs={
                'placeholder' : "Enter Skill Name (i.e. Movies)"
            })
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'yrfrom', 'yrto']

        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : "Enter Skill Name (i.e. Examle University)"
            })
        }
        labels = {
            'yrfrom' : "Year From",
            'yrto' : "Year To",
        }

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['yrfrom'].empty_level = 'Select Year'
        self.fields['yrto'].empty_level = 'Select Year'

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['title', 'bio','facebook', 'twitter', 'linkedin' ,'github', 'instagram', 'cv_link', 'template']

        widgets={
            'title' : forms.TextInput(attrs={
                'placeholder' : "Enter Your Stack Title"
            }),
            'bio' : forms.Textarea(attrs={
                'placeholder' : "Enter Your bio/description here.",
                # 'cols' : 50,
                'rows' : 5,
                'style':'resize:none;'
            }),
            'facebook' : forms.TextInput(attrs={
                'placeholder' : "Enter Facebook Username (i.e. johndoe)"
            }),
            'twitter' : forms.TextInput(attrs={
                'placeholder' : "Enter Twitter Username (i.e. johndoe)"
            }),
            'linkedin' : forms.TextInput(attrs={
                'placeholder' : "Enter LinkedIn Username (i.e. johndoe)"
            }),
            'github' : forms.TextInput(attrs={
                'placeholder' : "Enter Github Username (i.e. johndoe)"
            }),
            'instagram' : forms.TextInput(attrs={
                'placeholder' : "Enter Instagram Username (i.e. johndoe)"
            }),
            'cvv_link' : forms.TextInput(attrs={
                'placeholder' : "Enter your cv file link (i.e. google drive's link)"
            }),
        }

    def __init__(self, *args, **kwargs):
        super(WebsiteForm, self).__init__(*args, **kwargs)
        self.fields['template'].empty_label = "Select Template"