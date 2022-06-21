from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','last_name','first_name','email')
    search_fields =  ('user',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('category','title','date_created')
    search_fields =  ('category','title')

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('author','post','date_created')
    search_fields =  ('author','post')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(PostComment,PostCommentAdmin)