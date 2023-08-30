from django.contrib import admin
from blog.models import BlogPost
from blog.models import Document
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    class Meta:
        model = BlogPost
admin.site.register(BlogPost, BlogPostAdmin)

class DocumentAdmin(admin.ModelAdmin):
    class Meta:
        model = Document
admin.site.register(Document, DocumentAdmin)