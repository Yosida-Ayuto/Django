from xml.etree.ElementTree import Comment
from django.contrib import admin

# Register your models here.

# from .models import CustomUser

# admin.site.register(CustomUser)

from .models import bulletim_board

admin.site.register(bulletim_board)

from .models import Comment_Model
admin.site.register(Comment_Model)