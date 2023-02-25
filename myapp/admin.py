from django.contrib import admin

from myapp import models

# Register your models here.
admin.site.register(models.Locatario)
admin.site.register(models.RegistrarLocacao)

##admin.site.register(models.Imovel)
##admin.site.register(models.ImagemImovel)


class ImagemImovelInlineAdmin(admin.TabularInline):
    model = models.ImagemImovel
    extra = 0

class ImovelAdmin(admin.ModelAdmin):
    inlines = [ImagemImovelInlineAdmin]
    

admin.site.register(models.Imovel, ImovelAdmin)