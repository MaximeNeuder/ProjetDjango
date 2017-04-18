from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def validate_image(fieldfile_obj):
    if fieldfile_obj:
        filesize = fieldfile_obj.file.size
        megabyte_limit = int(15)
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max : %s Mo" % str(megabyte_limit))


def avatar_filename(instance, filename):
    fname, dot, extension = filename.rpartition('.')
    slug = instance.slug
    path = 'gallery/'
    return '%s%s.%s' % (path, slug, extension)

class Item(models.Model) :

    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )

    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )

    place_occupe = models.IntegerField(
        verbose_name="Place requise",
        null=False
    )

    inventaire = models.ForeignKey(
        "Inventaire",
        null=True
    )

    class Meta:
        app_label = "inv"

    def __str__(self):
        return str(self.name)

class Inventaire(models.Model) :
    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )

    place_max = models.IntegerField(
        verbose_name="Place max",
        null=False
    )

    proprietaire = models.OneToOneField(
        "Member",
        null=True
    )

    class Meta:
        app_label = "inv"

    def __str__(self):
        return str(self.name)

class Member(models.Model):
    user = models.OneToOneField(
        User,
        related_name="member"
    )
    avatar = models.ImageField(
        verbose_name="Avatar membre",
        upload_to=avatar_filename,
        validators=[validate_image],
        null=True,
        blank=True
    )

    class Meta:
        app_label = "inv"

    def __str__(self):
        return str(self.user)