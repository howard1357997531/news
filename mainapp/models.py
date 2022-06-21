from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField  #ckeeditor編輯器用這個才能上傳照片


class Profile(models.Model):    #profile用戶相關數據文件
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    phone= models.CharField(max_length=200,null=True,blank=True)
    email= models.EmailField(max_length=200,null=True,blank=True)
    address= models.CharField(max_length=200,null=True,blank=True)
    picture = models.ImageField(default='user.png',null=True,blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def pictureURL(self):
        try:
            url = self.picture.url
        except:
            url=''
        return url

class Category(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=200,null=True,blank=True)
    content= RichTextUploadingField(null=True,blank=True)
    picture = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(default=True)  #是否顯示
    press = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def pictureURL(self):
        try:
            url = self.picture.url
        except:
            url=''
        return url

class PostComment(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(News,on_delete=models.CASCADE)
    content = models.TextField(null=False,blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author.user)


