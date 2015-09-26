from django.contrib import admin
from models import  Warning,Information,Succes

#admin.site.register(Publisher)
#admin.site.register(Author)

#admin.site.register(Information)
#admin.site.register(Succes)


class WarnAdmin(admin.ModelAdmin):
    # ...
    list_display = ('headLine', 'news_content','publication_date')
    
admin.site.register(Warning,WarnAdmin)

class InfoAdmin(admin.ModelAdmin):
    # ...
    list_display = ('headLine', 'news_content','publication_date')
    
admin.site.register(Information,InfoAdmin)


class SucAdmin(admin.ModelAdmin):
    # ...
    list_display = ('headLine', 'news_content','publication_date')
print Succes
print "==========="
print SucAdmin 
admin.site.register(Succes,SucAdmin)
