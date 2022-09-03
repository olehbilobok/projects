from django.db import models


class Owners(models.Model):

    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Cities(models.Model):

    id                      = models.IntegerField(primary_key=True)
    city_name               = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name


class Appartments(models.Model):

    id                              = models.IntegerField(primary_key=True)
    operation_type                  = models.IntegerField()
    city                            = models.ForeignKey(Cities, on_delete=models.CASCADE, to_field='id')
    district_name                   = models.CharField(max_length=255, null=True)
    street_name                     = models.CharField(max_length=255, null=True)
    square_meters                   = models.FloatField(null=True)
    rooms_count                     = models.IntegerField(null=True)
    floor                           = models.IntegerField(null=True)
    total_price                     = models.IntegerField(null=True)
    created_at                      = models.DateTimeField()
    user                            = models.ForeignKey(Owners, on_delete=models.CASCADE, to_field='id')
    photo                           = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.city

