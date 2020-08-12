from django.db import models


# Create your models here.
class Movie(models.Model):
    class Meta:
        """
        Read :
        https://docs.djangoproject.com/en/3.0/ref/models/options/
        https://docs.djangoproject.com/en/3.0/ref/models/options/#verbose-name
        """

        verbose_name = 'فیلم'  # Normal form
        verbose_name_plural = 'فیلم'  # plural form

    name = models.CharField(max_length=100, verbose_name='نام فیلم')
    # or
    # name = models.CharField('نام فیلم', max_length=100)
    director = models.CharField('تهیه کننده', max_length=50)
    year = models.IntegerField('سال تولید')
    length = models.IntegerField('مدت')
    description = models.TextField('توضیحات')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'

    name = models.CharField('نام سینما', max_length=50)
    city = models.CharField('شهر', max_length=30, default='تهران')
    capacity = models.IntegerField('ظرفیت')
    phone = models.CharField('شماره تماس', max_length=20, null=True)
    address = models.TextField('آدرس')

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    """
    Represents a movie show in a cinema at specific time
    Please read https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    for more details about ForeignKey on_delete parameter

    Also read:
    https://docs.djangoproject.com/en/3.0/topics/db/models/
    https://docs.djangoproject.com/en/3.0/topics/db/models/#relationships
    """

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    """
    In Foreign key properties we should give related model in first parameter
    so we can't give verbose name in first parameter and we should do like this: 
    """
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT, verbose_name='فیلم')
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT, verbose_name='سینما')

    start_time = models.DateTimeField('زمان شروع')
    price = models.IntegerField('قیمت')
    salable_seats = models.IntegerField('صندلی های قابل فروش')
    free_seats = models.IntegerField('صندلی های خالی')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6

    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKETS_SOLD, 'بلیت ها تمام شد'),
        (SALE_CLOSED, 'فروش بلیت بسته شد'),
        (MOVIE_PLAYED, 'فیلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد')
    )

    status = models.IntegerField('', choices=status_choices)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)
