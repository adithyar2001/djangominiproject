from django.contrib import admin
from .models import guesttable,staffprofile,roomtable,bookingtable,feedback
# Register your models here.
admin.site.register(guesttable)
admin.site.register(staffprofile)
admin.site.register(roomtable)
admin.site.register(bookingtable)
admin.site.register(feedback)