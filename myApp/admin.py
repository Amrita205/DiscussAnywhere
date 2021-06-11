from django.contrib import admin
from myApp.models import topics
from myApp.models import latests
from myApp.models import Profile
from myApp.models import Post
from myApp.models import Answer
admin.site.register(latests)
admin.site.register(topics)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Answer)
# from .models import Image
# admin.site.register(Image)


# Register your models here.
