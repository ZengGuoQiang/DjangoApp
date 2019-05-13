from django.contrib import admin
from server.models import Person,Link

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'time']

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'txt']

admin.site.register(Person, PersonAdmin)
admin.site.register(Link,LinkAdmin)