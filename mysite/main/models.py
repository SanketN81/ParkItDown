from django.db import models

# Create your models here.
class Parkingspace(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=80)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150)  # Field name made lowercase.
    landmark = models.CharField(db_column='landmark', max_length=80)
    document = models.CharField(db_column='document', max_length=200)
    image = models.CharField(db_column='Image', max_length=200)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    address = models.TextField(db_column='address')
    slots = models.IntegerField(db_column='Slots')  # Field name made lowercase.
    availslots = models.IntegerField(db_column='AvailSlots')  # Field name made lowercase.
    discription = models.TextField(db_column='Discription')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'parkingspace'

class Login(models.Model):
    lid = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='email', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='password', max_length=50)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'login'

class Bookedspc(models.Model):
    bid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Parkingspace,related_name='lsid',db_column='sid',on_delete=models.CASCADE)  # Field name made lowercase.
    email = models.CharField(db_column='email', max_length=50)  # Field name made lowercase.
    expires = models.DateField(db_column='expires')  # Field name made lowercase.
    mail = models.CharField(db_column='mail', max_length=10)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'bookedspc'