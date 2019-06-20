from django.db import models
from movie import models as movie_models
from theater import models as theater_models
from django.contrib.auth.models import User


class Booking(models.Model):
    PAYMENT_TYPES = (
        (0, "unpaid"),
        (1, "card"),
        (2, "mobile"),
        (3, "ssl"),
        (4, "other"),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    payment_type = models.PositiveSmallIntegerField(
        choices=PAYMENT_TYPES, default=0
    )
    purchase_datetime = models.DateTimeField(auto_now=True)


class Ticket(models.Model):
    ticketId = models.CharField(max_length=10)
    movie = models.ForeignKey(
        movie_models.Movie, null=True, on_delete=models.SET_NULL
    )
    hall = models.ForeignKey(
        theater_models.Hall, null=True, on_delete=models.SET_NULL
    )
    show_time = models.ForeignKey(
        theater_models.ShowTime, null=True, on_delete=models.SET_NULL
    )
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    show_date = models.DateField()
    seat_number = models.CharField(max_length=10)
