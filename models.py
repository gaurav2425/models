from django.db import models
import datetime
from django.utils.timezone import utc
from django.utils import timezone
from datetime import datetime
import time
# Create your models here.
Day = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)

Month = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)


class Trending(models.Model):

    name = models.CharField(max_length=70, default='trending')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/trending/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/trending/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/trending/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Hot(models.Model):

    name = models.CharField(max_length=70, default='hot')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/hot/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/hot/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/hot/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class New(models.Model):

    name = models.CharField(max_length=70, default='new')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/new/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/new/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/new/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Amazon(models.Model):

    name = models.CharField(max_length=70, default='amazon')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/amazon/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/amazon/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/amazon/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Google(models.Model):

    name = models.CharField(max_length=70, default='google')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/google/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/google/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/google/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Microsoft(models.Model):

    name = models.CharField(max_length=70, default='microsoft')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/microsoft/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/microsoft/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/microsoft/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Tesla(models.Model):

    name = models.CharField(max_length=70, default='tesla')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/tesla/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/tesla/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/tesla/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Apple(models.Model):

    name = models.CharField(max_length=70, default='apple')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/apple/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/apple/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/apple/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Facebook(models.Model):

    name = models.CharField(max_length=70, default='facebook')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/facebook/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/facebook/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/facebook/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Privacy(models.Model):

    name = models.CharField(max_length=70, default='privacy')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/privacy/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/privacy/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/privacy/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Cybersecurity(models.Model):

    name = models.CharField(max_length=70, default='cybersecurity')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/cybersecurity/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/cybersecurity/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/cybersecurity/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Netflix(models.Model):

    name = models.CharField(max_length=70, default='netflix')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/netflix/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/netflix/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/netflix/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Sports(models.Model):

    name = models.CharField(max_length=70, default='sports')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/sports/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/sports/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/sports/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Television(models.Model):

    name = models.CharField(max_length=70, default='television')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/television/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/television/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/television/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Films(models.Model):

    name = models.CharField(max_length=70, default='films')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/films/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/films/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/films/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Gaming(models.Model):

    name = models.CharField(max_length=70, default='gaming')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/gaming/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/gaming/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/gaming/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Phones(models.Model):

    name = models.CharField(max_length=70, default='phones')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/phones/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/phones/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/phones/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Laptops(models.Model):

    name = models.CharField(max_length=70, default='laptops')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/laptops/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/laptops/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/laptops/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Cameras(models.Model):

    name = models.CharField(max_length=70, default='cameras')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/cameras/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/cameras/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/cameras/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Headphones(models.Model):

    name = models.CharField(max_length=70, default='headphones')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/headphones/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/headphones/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/headphones/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Speakers(models.Model):

    name = models.CharField(max_length=70, default='speakers')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/speakers/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/speakers/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/speakers/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Youtube(models.Model):

    name = models.CharField(max_length=70, default='youtube')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/youtube/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/youtube/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/youtube/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Instagram(models.Model):

    name = models.CharField(max_length=70, default='instagram')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/instagram/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/instagram/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/instagram/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Linkedin(models.Model):

    name = models.CharField(max_length=70, default='linkedin')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/linkedin/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/linkedin/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/linkedin/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Twitter(models.Model):

    name = models.CharField(max_length=70, default='twitter')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/twitter/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/twitter/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/twitter/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Nasa(models.Model):

    name = models.CharField(max_length=70, default='nasa')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/nasa/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/nasa/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/nasa/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Spacex(models.Model):

    name = models.CharField(max_length=70, default='spacex')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/spacex/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/spacex/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/spacex/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Health(models.Model):

    name = models.CharField(max_length=70, default='health')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/health/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/health/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/health/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Energy(models.Model):

    name = models.CharField(max_length=70, default='energy')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/energy/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/energy/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/energy/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Environment(models.Model):

    name = models.CharField(max_length=70, default='environment')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/environment/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/environment/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/environment/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class More(models.Model):

    name = models.CharField(max_length=70, default='more')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/more/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/more/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/more/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Archives(models.Model):

    name = models.CharField(max_length=70, default='archives')
    title = models.CharField(max_length=150, default='', blank=True)
    subtitle = models.CharField(max_length=70, default="", blank=True)
    caption = models.CharField(max_length=70, default="", blank=True)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/archives/thumbnail')

    image1 = models.ImageField(
        null=True, blank=True, upload_to='images/archives/image1')
    image1credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para1h = models.CharField(max_length=50, default='', blank=True)
    para1 = models.CharField(max_length=1000, default='', blank=True)

    para2h = models.CharField(max_length=50, default='', blank=True)
    para2 = models.CharField(max_length=1000, default='', blank=True)

    quote1 = models.CharField(max_length=200, default='', blank=True)

    para3h = models.CharField(max_length=50, default='', blank=True)
    para3 = models.CharField(max_length=1000, default='', blank=True)

    youtubevideo = models.CharField(
        default='', max_length=300, blank=True)
    youtubevideocredit = models.CharField(
        max_length=100, default='Youtube:', blank=True)

    para4h = models.CharField(max_length=50, default='', blank=True)
    para4 = models.CharField(max_length=1000, default='', blank=True)

    para5h = models.CharField(max_length=50, default='', blank=True)
    para5 = models.CharField(max_length=1000, default='', blank=True)

    image2 = models.ImageField(null=True, blank=True,
                               upload_to='images/archives/image2')
    image2credit = models.CharField(
        max_length=100, default='Image:', blank=True)

    para6h = models.CharField(max_length=50, default='', blank=True)
    para6 = models.CharField(max_length=1000, default='', blank=True)

    para7h = models.CharField(max_length=50, default='', blank=True)
    para7 = models.CharField(max_length=1000, default='', blank=True)

    tweetid = models.CharField(max_length=30, default='', blank=True)

    para8h = models.CharField(max_length=50, default='', blank=True)
    para8 = models.CharField(max_length=1000, default='', blank=True)

    para9h = models.CharField(max_length=50, default='', blank=True)
    para9 = models.CharField(max_length=1000, default='', blank=True)

    videosrc = models.CharField(
        default='', max_length=300, blank=True)

    para10h = models.CharField(max_length=50, default='', blank=True)
    para10 = models.CharField(max_length=1000, default='', blank=True)

    quote2 = models.CharField(max_length=200, default='', blank=True)

    para11h = models.CharField(max_length=50, default='', blank=True)
    para11 = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    fullname = models.CharField(max_length=70, default='')
    email = models.CharField(max_length=70, default='')
    message = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.email
