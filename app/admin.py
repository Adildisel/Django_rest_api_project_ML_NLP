from django.contrib import admin

from .models import ParserComments, ParserVideoId


class ParserVideoIdAdmin(admin.ModelAdmin):
    list_display = (
        'creater', 
        'video_id',
        'name_video',
        # 'date', 
        # 'num_comments',
        )

class ParserCommentsAdmin(admin.ModelAdmin):
    list_display = (
        # 'video', 
        'auth_comment', 
        # 'date_comment', 
        'comment',
        'assessment',
        )


admin.site.register(ParserVideoId, ParserVideoIdAdmin)
admin.site.register(ParserComments, ParserCommentsAdmin)
