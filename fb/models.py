from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='',blank=True,null=True)
    email = models.CharField(max_length=100,blank=True)
    d_o_b = models.DateField()
    profile_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(Profile,related_name='post_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/post',blank=True,null=True)
    like = models.ManyToManyField(User,related_name='likes', default='0',blank=True,null=True)
    post_created = models.DateTimeField(auto_now_add=True)

    @property
    def pc(self):
        return Comment.objects.filter(post=self)

    @property
    def cc(self):
        return Comment.objects.filter(post=self).count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=1000)
    comment_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Story(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/story')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.author.user)

