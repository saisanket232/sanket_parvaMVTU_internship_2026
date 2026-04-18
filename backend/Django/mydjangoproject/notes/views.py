from django.shortcuts import render, redirect
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'list.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('list')

    return render(request, 'form.html')


def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('list')