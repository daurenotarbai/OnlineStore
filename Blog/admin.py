from django.contrib import admin
from Blog.models import Blog, BlogTags, CommentBlog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.fields]

    
admin.site.register(Blog,BlogAdmin)


class BlogTagsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BlogTags._meta.fields]

admin.site.register(BlogTags,BlogTagsAdmin)

class CommentBlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CommentBlog._meta.fields]

    
admin.site.register(CommentBlog,CommentBlogAdmin)


admin.site.site_title = "QazStore admin"
admin.site.site_header = "QazStore admin"



# EXAMPLES #######################################################################################


# class MovieAdminForm(forms.ModelForm):
#     """Форма с виджетом ckeditor"""
#     description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Movie
#         fields = '__all__'


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     """Категории"""
#     list_display = ("id", "name", "url")
#     list_display_links = ("name",)


# class ReviewInline(admin.TabularInline):
#     """Отзывы на странице фильма"""
#     model = Reviews
#     extra = 1
#     readonly_fields = ("name", "email")


# class MovieShotsInline(admin.TabularInline):
#     model = MovieShots
#     extra = 1
#     readonly_fields = ("get_image",)

#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

#     get_image.short_description = "Изображение"


# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     """Фильмы"""
#     list_display = ("title", "category", "url", "draft")
#     list_filter = ("category", "year")
#     search_fields = ("title", "category__name")
#     inlines = [MovieShotsInline, ReviewInline]
#     save_on_top = True
#     save_as = True
#     list_editable = ("draft",)
#     actions = ["publish", "unpublish"]
#     form = MovieAdminForm
#     readonly_fields = ("get_image",)
#     fieldsets = (
#         ("Actors", {
#             "classes": ("collapse",),
#             "fields": (("actors", "directors", "genres", "category"),)
#         }),
#         (None, {
#             "fields": (("budget", "fees_in_usa", "fess_in_world"),)
#         }),
#         ("Options", {
#             "fields": (("url", "draft"),)
#         }),
#     )

#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

#     def unpublish(self, request, queryset):
#         """Снять с публикации"""
#         row_update = queryset.update(draft=True)
#         if row_update == 1:
#             message_bit = "1 запись была обновлена"
#         else:
#             message_bit = f"{row_update} записей были обновлены"
#         self.message_user(request, f"{message_bit}")

#     def publish(self, request, queryset):
#         """Опубликовать"""
#         row_update = queryset.update(draft=False)
#         if row_update == 1:
#             message_bit = "1 запись была обновлена"
#         else:
#             message_bit = f"{row_update} записей были обновлены"
#         self.message_user(request, f"{message_bit}")

#     publish.short_description = "Опубликовать"
#     publish.allowed_permissions = ('change', )

#     unpublish.short_description = "Снять с публикации"
#     unpublish.allowed_permissions = ('change',)

#     get_image.short_description = "Постер"





# @admin.register(Actor)
# class ActorAdmin(admin.ModelAdmin):
#     """Актеры"""
#     list_display = ("name", "age", "get_image")
#     readonly_fields = ("get_image",)

#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

#     get_image.short_description = "Изображение"



# @admin.register(MovieShots)
# class MovieShotsAdmin(admin.ModelAdmin):
#     """Кадры из фильма"""
#     list_display = ("title", "movie", "get_image")
#     readonly_fields = ("get_image",)

#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

#     get_image.short_description = "Изображение"
