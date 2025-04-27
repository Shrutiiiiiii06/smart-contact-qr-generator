# generator/views.py

import uuid
import os
from django.conf import settings
from django.shortcuts import render
import qrcode
from .forms import ContactForm

def generate_qr(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Build the vCard string
            vcard = "BEGIN:VCARD\nVERSION:3.0\n"
            vcard += f"FN:{data['full_name']}\n"
            if data.get('company'):
                vcard += f"ORG:{data['company']}\n"
            if data.get('job_title'):
                vcard += f"TITLE:{data['job_title']}\n"
            vcard += f"TEL:{data['phone']}\n"
            vcard += f"EMAIL:{data['email']}\n"
            if data.get('linkedin'):
                vcard += f"URL;type=LinkedIn:{data['linkedin']}\n"
            if data.get('github'):
                vcard += f"URL;type=GitHub:{data['github']}\n"
            if data.get('instagram'):
                vcard += f"URL;type=Instagram:{data['instagram']}\n"
            if data.get('website'):
                vcard += f"URL;type=Website:{data['website']}\n"
            if data.get('address'):
                vcard += f"ADR:;;{data['address']}\n"
            vcard += "END:VCARD"

            # Generate QR Code
            img = qrcode.make(vcard)

            filename = f"{uuid.uuid4()}.png"
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            img.save(filepath)

            return render(request, 'generator/index.html', {
                'form': ContactForm(),
                'qr_code_url': f"{settings.MEDIA_URL}{filename}",
                'success': True
            })
        else:
            return render(request, 'generator/index.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'generator/index.html', {'form': form})
