from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

LIFESTYLE = (
    ('T', 'Terrestrial'),
    ('O', 'Oviparous'),
    ('A', 'Arboreal'),
    ('C', 'Congregatory'),
    ('N', 'Nomadic')
)

OPTION = (
    (0, 'No'),
    (1, 'Yes')
)

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id}) 


class Photo(models.Model):
    url = models.CharField(max_length=200)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for finch_id: {self.finch_id} @{self.url}"


class Lifestyle(models.Model):
  migrates = models.BooleanField(choices=OPTION, blank=False)
  lifestyle = models.CharField(
    max_length=20,
	 choices=LIFESTYLE,
	 default=LIFESTYLE[0][0]
  )
 
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_lifestyle_display()} and {self.migrates}"
