from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/client/customer/")
    zipcode = models.CharField(max_length=100)
    phone_umber = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
