from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class CreateCourse(models.Model):
	username = models.CharField(max_length=500,default="")
	course = models.CharField(max_length = 5, unique=True, default = "")
	code = models.CharField(max_length = 6, unique=True, default="XXXXXX")
	def _str_(self):
		return self.code

class AddCourse(models.Model):
	username = models.CharField(max_length=500,default="")
	code = models.CharField(max_length = 6,default="")
	def _str_(self):
		return self.code

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	YEAR_IN_COLLEGE_CHOICES = (
		(1, '1st Year'),
		(2, '2nd Year'),
		(3, '3rd Year'),
		(4, '4th Year'),
	)
	IDENTITY_CHOICE=(
		('teacher','teacher'),
		('student', 'student'),
	)
	courses=models.CharField(max_length=500,default="")
	#courses=models.CharField(choices = Course.COURSE_CHOICE, max_length=100,default="")
	identity=models.CharField(choices=IDENTITY_CHOICE,max_length=100,default="student")
	full_name = models.CharField(max_length = 100)
	year = models.PositiveIntegerField(choices=YEAR_IN_COLLEGE_CHOICES, default=1)
	roll_no = models.CharField(max_length = 8, unique=True)
	#created = models.DateField(editable=False, null=True)

	def _str_(self):
		return self.roll_no

	def save(self):
		if not self.id:
			self.roll_no = self.user.username
			self.created = datetime.date.today()
		super(UserProfile, self).save()

class Book(models.Model):
	Course_choice = (
		('CS251', 'CS251'),
		('CS215', 'CS215'),
		('CS293', 'CS293'),
	)
	username = models.CharField(max_length=500,default="")
	num = models.PositiveIntegerField(default=1)
	course = models.CharField(max_length=5, choices=Course_choice, default='')
	#deadline = models.DateField(default=datetime.now)
	Assignment = models.FileField(upload_to="assignment/", null=True, blank=True)
	extensions = models.CharField(max_length=500,default="")
	zip_tree_directory = models.FileField(upload_to="File_format/", null=True, blank=True)

class Submit(models.Model):
	Course_choice = (
		('CS251', 'CS251'),
		('CS215', 'CS215'),
		('CS293', 'CS293'),
	)
	username = models.CharField(max_length=500,default="")
	num = models.PositiveIntegerField(default=1)
	course = models.CharField(max_length=5, choices=Course_choice, default='')
	Submission = models.FileField(upload_to="submission/", null=True, blank=True)
	def __str__(self):
		return self.num
	
class Assignment(models.Model):
	username = models.CharField(max_length=500,default="")
	num = models.PositiveIntegerField(default=1)
	course = models.CharField(max_length=5, default='')
	Assignment = models.FileField(upload_to="assignment/", null=True, blank=True)
	extensions = models.CharField(max_length=500,default="")
	zip_tree_directory = models.FileField(upload_to="File_format/", null=True, blank=True)

class Solution(models.Model):
	username = models.CharField(max_length=500,default="")
	num = models.PositiveIntegerField(default=1)
	course = models.CharField(max_length=5, default='')
	Submission = models.FileField(upload_to="submission/", null=True, blank=True)

class Grade(models.Model):
	username_t = models.CharField(max_length=500,default="")
	Student = models.CharField(max_length=500,default="")
	num = models.PositiveIntegerField(default=1)
	course = models.CharField(max_length=5, default='')
	marks = models.PositiveIntegerField(default=0)
	FeedBack = models.CharField(max_length=500,default="")