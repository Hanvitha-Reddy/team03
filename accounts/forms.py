from django.forms import ModelForm
from .models import Book, UserProfile, Submit, AddCourse, CreateCourse, Assignment, Solution, Grade
from django import forms
from django.contrib.auth.models import User
from django.core.validators import EMPTY_VALUES

class BookForm(ModelForm):
    class Meta: 
        model = Book
        help_texts = {
			'extensions': 'Enter comma separated extensions. Example: pdf, docx, txt',
		}
        fields = ['num', 'course', 'Assignment', 'extensions', 'zip_tree_directory']

class SubmissionForm(ModelForm):
    class Meta: 
        model = Submit
        fields = ['num', 'course', 'Submission']

class AssignmentForm(ModelForm):
    class Meta: 
        model = Assignment
        help_texts = {
			'extensions': 'Enter comma separated extensions. Example: pdf, docx, txt',
		}
        fields = ['num', 'course', 'Assignment', 'extensions', 'zip_tree_directory']
	            

class SolutionForm(ModelForm):
    class Meta: 
        model = Solution
        fields = ['num', 'course', 'Submission']

class GradeForm(ModelForm):
    class Meta: 
        model = Grade
        fields = ['Student', 'num', 'marks', 'FeedBack']

class AddCourseForm(ModelForm):
	class Meta:
		model = AddCourse
		fields = ['code']

class CreateCourseForm(ModelForm):
	class Meta:
		model = CreateCourse
		fields = ['course', 'code']

class UserForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		help_texts = {
			'username': 'Enter your College Roll No.',
		}
		fields = ['username', 'email', 'password']

	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError("password does not match")

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['full_name', 'year', 'identity']
