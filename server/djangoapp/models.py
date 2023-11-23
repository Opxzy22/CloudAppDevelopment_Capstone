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
class CarDealer:

    def __init__(self, id, city, state, st, address, zip, lat, long, full_name, short_name):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
        # dealer state
        self.state = state

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

  def __init__(self, id, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year):
    # dealer id
    self.id = id
    # dealer name
    self.name = name
    # dealership
    self.dealership = dealership
    # review
    self.review = review
    # purchase
    self.purchase = purchase
    # purchase date
    self.purchase_date = purchase_date
    # car make
    self.car_make = car_make
    # car model
    self.car_model = car_model
    # car year
    self.car_year = car_year
