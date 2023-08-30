import datetime
from django.shortcuts import get_object_or_404, render, redirect

from .forms import DocumentForm
from .models import BlogPost, Document
from django.http import JsonResponse


def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if request.FILES.get('image'):
            uploaded_image = request.FILES['image']
            # Process the uploaded image, save it, and get its URL
            image_url = '../../static/img/'  # Replace this with your image URL logic
            
            # Include the image in the content
            content_with_image = f'<img src="{image_url}" alt="Uploaded Image"><br>{content}'
            content = content_with_image
        BlogPost.objects.create(title=title, content=content)
        return redirect('list_blogs')
    return render(request, 'blog/add_blog.html')

def list_blogs(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/list_blogs.html', {'posts': posts})

def view_blog(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/view_blog.html', {'post': post})

def delete_blog(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    if request.method == 'POST':
        post.delete()
        return redirect('list_blogs')
    return render(request, 'blog/delete_blog.html', {'post': post})

def base_context(request):
    current_year = datetime.datetime.now().year
    return {'current_year': current_year}

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'blog/upload_document.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'blog/documents/document_list.html', {'documents': documents})

# def upload_image(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_image = request.FILES['image']
#         # Process the uploaded image, save it, and get its URL
#         image_url = '../../static/img/'
#         return JsonResponse({'location': image_url})
#     return JsonResponse({'error': 'Image upload failed'})