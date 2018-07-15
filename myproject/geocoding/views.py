from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
from .forms import DocumentForm
from .models import Document
import os
import xlrd, xlwt
from xlutils.copy import copy
import requests
from django.conf import settings
# Create your views here.

def home(request):
    files = Document.objects.all()
    return render(request, 'home.html', {'files': files})

def upload_files(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            newdoc = Document(title = request.POST['title'], docfile = request.FILES['docfile'])
            newdoc.save()
            rb = xlrd.open_workbook(os.path.join(settings.MEDIA_ROOT, newdoc.docfile.name))
            r_sheet = rb.sheet_by_index(0)
            address = [",".join([r_sheet.cell_value(r,c) for c in range(r_sheet.ncols)])for r in range (r_sheet.nrows)]
            api_key = "**********************************"
            wb = copy(rb)
            print('rows', r_sheet.nrows)
            for i in range(r_sheet.nrows):    
                api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address[i], api_key))
                api_response_dict = api_response.json()
                print(api_response_dict['status'])

                if api_response_dict['status'] == 'OK':
                    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
                    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
                    w_sheet = wb.get_sheet(0)
                    print(i)
                    w_sheet.write(i,3,latitude)
                    w_sheet.write(i,4,longitude)
                    wb.save(os.path.join(settings.MEDIA_ROOT, newdoc.docfile.name))
                    print('Latitude:', latitude)
                    print('Longitude:', longitude)
            return redirect('home')
    else:
        form = DocumentForm()
    # files = Document.objects.all()
    return render(request, 'upload.html', {'form': form})

def download_files(request, pk):
    newdoc = Document.objects.get(pk = pk)
    file_path = os.path.join(settings.MEDIA_ROOT, newdoc.docfile.name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename=%s.xls' % newdoc.docfile.name
            return response
    raise Http404
