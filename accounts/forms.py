from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile, HelperProfile
from helpers.choices import DIVISION_CHOICES, DISTRICT_CHOICES, UPAZILA_CHOICES, SERVICE_TYPE_CHOICES, PLACE_TYPE_CHOICES, AVAILABILITY_CHOICES

User = get_user_model()


class SignupForm(forms.Form):
    account_type = forms.ChoiceField(choices=[('user', 'ব্যবহারকারী'), ('helper', 'হেল্পার')], initial='user')
    first_name = forms.CharField(max_length=150, label='নাম')
    last_name = forms.CharField(max_length=150, required=False, label='পদবি')
    email = forms.EmailField(label='ইমেইল')
    phone_number = forms.CharField(max_length=20, label='ফোন নম্বর')
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=8, label='পাসওয়ার্ড')
    password2 = forms.CharField(widget=forms.PasswordInput, label='পাসওয়ার্ড নিশ্চিত করুন')
    terms_accepted = forms.BooleanField(label='শর্তাবলী গ্রহণ')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('এই ইমেইল ইতিমধ্যে ব্যবহৃত হয়েছে।')
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('পাসওয়ার্ড মিলেনি।')
        return cleaned


class LoginForm(forms.Form):
    email = forms.EmailField(label='ইমেইল')
    password = forms.CharField(widget=forms.PasswordInput, label='পাসওয়ার্ড')
    remember = forms.BooleanField(required=False, label='মনে রাখুন')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'division', 'district', 'upazila', 'place_type',
                  'village_city_area', 'house_address', 'landmark', 'latitude', 'longitude',
                  'profile_photo']
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.address = instance.get_full_address()
        if commit:
            instance.save()
        return instance


class HelperProfileForm(forms.ModelForm):
    service_types = forms.MultipleChoiceField(
        choices=SERVICE_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='সেবার ধরন'
    )

    class Meta:
        model = HelperProfile
        fields = ['service_types', 'experience_years', 'hourly_rate', 'monthly_rate',
                  'availability_status', 'bio', 'national_id_number', 'nid_card_image']

    def clean_service_types(self):
        return ','.join(self.cleaned_data.get('service_types', []))

    def save(self, commit=True):
        instance = super().save(commit=False)
        if isinstance(self.cleaned_data.get('service_types'), list):
            instance.service_types = ','.join(self.cleaned_data['service_types'])
        if commit:
            instance.save()
        return instance


class HiringForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='শুরুর তারিখ')
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label='শেষ তারিখ')
    notes = forms.CharField(widget=forms.Textarea, required=False, label='নোট')


class ReviewForm(forms.Form):
    rating = forms.ChoiceField(choices=[(i, f'{i} ★') for i in range(1, 6)], widget=forms.RadioSelect, label='রেটিং')
    comment = forms.CharField(widget=forms.Textarea, label='মন্তব্য')
