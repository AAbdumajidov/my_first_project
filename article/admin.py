from django.contrib import admin
from .models import Article



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'modified_date', 'is_deleted', 'create_date']
    readonly_fields = ['modified_date', 'create_date']
    fields = ['title', 'image', 'content', 'modified_date', 'create_date']
    list_display_links = ('title', 'id')
    list_per_page = 10
    ordering = ('-id',)
    search_fields = ('title',)
    search_help_text = "'title' orqali qidiriladi "
    list_filter = ('modified_date', 'is_deleted', 'create_date')
    date_hierarchy = 'create_date'


admin.site.register(Article, ArticleAdmin)