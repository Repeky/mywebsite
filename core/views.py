from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'core/index.html')

def handle_uploaded_file(f):
    with open('media/' + str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'core/index.html', {'form': form})
