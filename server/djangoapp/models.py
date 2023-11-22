from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model 
class CarMake(models.Model):
# - Name and Description
  Name = models.CharField(max_length=100)
  Description = models.TextField()
  
# - __str__ method to print a car make object
  def __str__(self):
    return self.Name




# <HINT> Create a Car Model model
class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
  car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# - Name
  name = models.CharField(max_length=100)
# - Dealer id, used to refer a dealer created in cloudant database
  dealer_id = models.IntegerField()
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
  Choices_Type = [
    ('SEDAN', 'Sedan'),
    ('SUV', 'Suv'),
    ('WAGON', 'Wagon'),
  ]
  car_type = models.CharField(max_length=100, choices=Choices_Type)
# - Year (DateField)
  Year = models.DateField()

# - __str__ method to print a car make object
  def __str__(self):
    return f"{self.car_make} - {self.name}"


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
