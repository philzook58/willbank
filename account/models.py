
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
	#username = models.CharField(max_length=30)
	#password = models.CharField(max_length=30)
	#name = models.CharField(max_length=30)
	user = models.ForeignKey(User,null=True)#,default=User(username='philzook58'))
	balance = models.DecimalField(max_digits=6, decimal_places=2)


	def __str__(self):
		if self.user:
			return self.user.username
		else:
			return "No User"


class Transaction(models.Model):
	account = models.ForeignKey('Account')
	amount = models.DecimalField(max_digits=6, decimal_places=2)

class UserProfile(models.Model):
	user = models.OneToOneField(User,null=True)
	message = models.TextField()
	picture = models.ImageField(upload_to='profile_images',blank=True)

	
