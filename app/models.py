from django.db import models

from django.contrib.auth.models import User


class ParserVideoId(models.Model):
    """
    Данные видео и автора запроса
    """
    creater = models.ForeignKey(User, verbose_name='Создатель запроса', on_delete=models.CASCADE)
    # date = models.DateTimeField('Дата создания запроса', auto_now_add=True)

    video_id = models.CharField(verbose_name='Видео id', max_length=125)
    
    # name_channel = models.CharField(verbose_name='Название канала', max_length=255)
    name_video = models.CharField(verbose_name='Название видео', max_length=255)
    # num_comments = models.CharField(verbose_name='Количество комментариев', max_length=255)
    # num_like = models.CharField(verbose_name='Количество лайков', max_length=255)
    # num_dislike = models.CharField(verbose_name='Количество дизлайков', max_length=255)

    def __str__(self):
        return '{}-number:{}'.format(self.creater, self.id)

    class Meta:
        verbose_name = "Данные видео"
        verbose_name_plural = 'Данные видео'




class ParserComments(models.Model):
    """
    Данный коментариев к видео
    """

    video = models.ForeignKey(ParserVideoId, verbose_name='Данные видео', on_delete=models.CASCADE)
    auth_comment = models.CharField(verbose_name='Автор комментария', max_length=255)

    # user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    # date_comment = models.CharField(verbose_name='Дата комментария', max_length=255)
    comment = models.TextField(verbose_name='Текст комментария')
    # num_like_comment = models.CharField(verbose_name='Количество лайков комментария', max_length=255)
    # num_dislike_comment = models.CharField(verbose_name='Количество дизлайков комментария', max_length=255)
    assessment = models.CharField(verbose_name='Оценка коментария', max_length=255)

    class Meta:
        verbose_name = "Данные комментариев"
        verbose_name_plural = 'Данные комментариев'
