from django.contrib import admin
from .models import Project, CallbackRequest


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "copy",
        "type",
        "tags",
        "address",
        "desc",
        "main_img",
        "youtube_url",
        "panorama_img",
        "title_content",
        "desc_content",
        "price",
        "apartment_count",
        "created_at",
        "updated_at",
    )
    search_fields = ("title",)

admin.site.register(CallbackRequest)