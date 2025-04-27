from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=100)
    phone = forms.CharField(label="Phone Number", max_length=20)
    email = forms.EmailField(label="Email Address")
    linkedin = forms.URLField(label="LinkedIn Profile", required=False)
    github = forms.URLField(label="GitHub Profile", required=False)
    instagram = forms.URLField(label="Instagram Profile", required=False)
    website = forms.URLField(label="Personal Website", required=False)
    company = forms.CharField(label="Company Name", required=False)
    job_title = forms.CharField(label="Job Title", required=False)
    address = forms.CharField(label="Address", required=False)
