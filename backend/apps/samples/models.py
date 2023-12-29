from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, pre_save


class Characteristic(models.Model):
    name = models.CharField(max_length=128, unique=True)
    expression = models.CharField(max_length=255, null=True, blank=False)


class Sample(models.Model):
    name = models.CharField(max_length=128, unique=True)
    characteristics = models.ManyToManyField(
        Characteristic, through='SampleCharacteristic')


class SampleCharacteristic(models.Model):
    сharacteristic = models.ForeignKey(
        Characteristic, on_delete=models.CASCADE)
    sample = models.ForeignKey(
        Sample, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('сharacteristic', 'sample'),)


# class СharacteristicValue(models.Model):
#   value = models.CharField()
#   sampleCharacteristic =

# class PointSample(models.Model):
#     point = models.OneToOneField(
#         Point, on_delete=models.CASCADE, related_name='point_samples')
#     sample = models.OneToOneField(
#         Sample, on_delete=models.CASCADE, related_name='point_samples')
