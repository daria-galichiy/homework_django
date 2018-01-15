from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Actors(models.Model):
    actor_id = models.AutoField(primary_key=True)
    actor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.actor_name

    class Meta:
        verbose_name_plural = "Actors"
        verbose_name = "Actor"


class Filmmakers(models.Model):
    filmmaker_id = models.AutoField(primary_key=True)
    filmmaker_name = models.CharField(max_length=100)

    def __str__(self):
        return self.filmmaker_name

    class Meta:
        verbose_name_plural = "Filmmakers"
        verbose_name = "Filmmaker"


class Film_writers(models.Model):
    film_writer_id = models.AutoField(primary_key=True)
    film_writer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.film_writer_name

    class Meta:
        verbose_name_plural = "Film_writers"
        verbose_name = "Film_writer"


class Producers(models.Model):
    producer_id = models.AutoField(primary_key=True)
    producer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.producer_name

    class Meta:
        verbose_name_plural = "Producers"
        verbose_name = "Producer"


class Cameramen(models.Model):
    cameraman_id = models.AutoField(primary_key=True)
    cameraman_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cameraman_name

    class Meta:
        verbose_name_plural = "Cameramen"
        verbose_name = "Cameraman"


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = "Countries"
        verbose_name = "Country"


class Films(models.Model):
    film_id = models.AutoField(primary_key=True)
    film_name = models.CharField(max_length=100)
    release_date = models.DateField()
    in_the_lead_role = models.ManyToManyField(Actors)
    filmmaker = models.ForeignKey(Filmmakers, on_delete=models.CASCADE)
    film_writer = models.ForeignKey(Film_writers, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producers, on_delete=models.CASCADE)
    cameraman = models.ForeignKey(Cameramen, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    box_office_results = models.IntegerField()

    def __str__(self):
        return self.film_name

    def get_absolute_url(self):
        return reverse('film_url', args=[str(self.id)])

    def get_actors(self):
        return "\n".join([i.actor_name for i in self.in_the_lead_role.all()])
    get_actors.short_description = 'In_the_lead_roles'

    class Meta:
        verbose_name_plural = "Films"
        verbose_name = "Film"


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_film = models.ForeignKey(Films, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_photo = models.ImageField(upload_to='downloaded', default='def.jpg', null=True, blank=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"
