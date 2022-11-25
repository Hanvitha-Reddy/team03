from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from .forms import BookForm, SubmissionForm, UserForm, UserProfileForm, AddCourseForm, CreateCourseForm
from .forms import SolutionForm, AssignmentForm, GradeForm
from .models import Submit, Book, UserProfile, AddCourse, CreateCourse, Assignment, Solution, Grade
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import csv, os, filecmp
from zipfile import ZipFile
from django.core.exceptions import ObjectDoesNotExist


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
#Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return redirect('accounts:login')
	else:
		user_profile = UserProfile.objects.get(user = request.user)
		if user_profile.identity == 'teacher':
			return redirect('accounts:home_t')
		return redirect('accounts:home')

def assigns_251(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity == 'teacher':
		Submissions = Submit.objects.filter(course = 251)
		return render(request, 'accounts/assign.html',{
            'Submissions': Submissions
        })
	else:
		logout(request)
		return HttpResponseRedirect('/accounts/')

def assigns_215(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity == 'teacher':
		Submissions = Submit.objects.filter(course = 215)
		return render(request, 'accounts/assign.html',{
            'Submissions': Submissions
        })
	else:
		logout(request)
		return HttpResponseRedirect('/accounts/')

def assigns_293(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity == 'teacher':
		Submissions = Submit.objects.filter(course = 293)
		return render(request, 'accounts/assign.html',{
            'Submissions': Submissions
        })
	else:
		logout(request)
		return HttpResponseRedirect('/accounts/')

def upload_book(request):
    user_profile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST' and user_profile.identity == 'student':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid:
            question = Book.objects.get(num = request.POST['num'], course = request.POST['course'])
            list = str(question.extensions).split(',')
            f = request.FILES['Submission']
            if f.name.split('.')[1] in list:
                if f.name.split('.') == 'zip':
                    with ZipFile(f, 'r') as zip:
                        zip.extractall()
                        print(zip.namelist(), file=open('output.txt', 'a'))
                    file = question.zip_tree_directory
                    if filecmp.cmp('output.txt', 'media/' + str(file)):
                        form.instance.username = user_profile.user.username
                        form.save()
                        os.remove('output.txt')
                        return redirect('/accounts/home/')
                    else:
                        os.remove('output.txt')
                        form = SubmissionForm()
                        return render(request, 'accounts/upload_book.html', {
                            'form': form,
					        'error_message': 'Invalid Tree Directory'
                        })
                else:
                    form.instance.username = user_profile.user.username
                    form.save()
                    return redirect('/accounts/home/')
            else:
                form = SubmissionForm()
                return render(request, 'accounts/upload_book.html', {
                    'form': form,
					'error_message': 'Invalid file format'
                })
    if user_profile.identity != 'student':
        logout(request)
        return HttpResponseRedirect('/accounts/')
    else:
        form = SubmissionForm()
    return render(request, 'accounts/upload_book.html', {
        'form': form
    })

def new_upload(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if request.method == 'POST' and user_profile.identity == 'student':
		form = SolutionForm(request.POST, request.FILES)
		if form.is_valid:
			form.instance.username = user_profile.user.username
			courses = AddCourse.objects.filter(username = user_profile.user.username)
			for course in courses:
				total = CreateCourse.objects.filter(code = course.code)
				for name in total:
					if name.course == request.POST['course']:
						question = Assignment.objects.get(num = request.POST['num'],course = request.POST['course'])
						list = str(question.extensions).split(',')
						f = request.FILES['Submission']
						if f.name.split('.')[1] in list:
							if f.name.split('.')[1] != 'zip':
								form.save()
								return redirect('/accounts/home/')
							else:
								with ZipFile(f, 'r') as zip:
									zip.extractall()
									print(zip.namelist(), file=open('output.txt', 'a'))
								file = question.zip_tree_directory
								if filecmp.cmp('output.txt', 'media/' + str(file)):
									form.instance.username = user_profile.user.username
									form.save()
									os.remove('output.txt')
									return redirect('/accounts/home/')
								else:
									os.remove('output.txt')
									form = SubmissionForm()
									return render(request, 'accounts/Submit.html',{
										'form': form,
										'error_message': 'Invalid Tree Directory',
									})
						else:
							form = SolutionForm
							return render(request, 'accounts/Submit.html', {
								'form': form,
								'error_message': 'Invalid file format'
							})
	if user_profile.identity != 'student':
		logout(request)
		return HttpResponseRedirect('/accounts/')
	else:
		form = SolutionForm()
	return render(request, 'accounts/Submit.html', {
        'form': form
    })

def new_upload_t(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if request.method == 'POST' and user_profile.identity == 'teacher':
		form = AssignmentForm(request.POST, request.FILES)
		if form.is_valid:
			form.instance.username = user_profile.user.username
			courses = CreateCourse.objects.filter(username = user_profile.user.username)
			for course in courses:
				if course.course == request.POST['course']:
					form.save()
					return redirect('/accounts/home_t/')
	if user_profile.identity != 'teacher':
		logout(request)
		return HttpResponseRedirect('/accounts/')
	else:
		form = AssignmentForm()
	return render(request, 'accounts/Assignment.html', {
        'form': form
    })

def upload_book_t(request):
    user_profile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST' and user_profile.identity == 'teacher':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid:
            form.instance.username = user_profile.user.username
            form.save()
            return redirect('/accounts/home_t/')
    if user_profile.identity != 'teacher':
        logout(request)
        return HttpResponseRedirect('/accounts/')
    else:
        form = BookForm()
    return render(request, 'accounts/upload_book_t.html', {
        'form': form
    })


def register(request):
	if request.user.is_authenticated:
		return render(request, 'accounts/home.html', {'error_message': "You are already registered!!"})
	else:	
		user_form = UserForm(request.POST or None)
		profile_form = UserProfileForm(request.POST or None)
		if request.method == 'POST':
			if user_form.is_valid() and profile_form.is_valid():
				user = user_form.save(commit=False)
				username = user_form.cleaned_data['username']
				password = user_form.cleaned_data['password']
				user.set_password(user.password)
				user.save()
				profile = profile_form.save(commit=False)
				profile.user = user
				profile.save()
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						login(request, user)
						return redirect('accounts:login')
		context = {
			"pform": profile_form,
			"uform": user_form,
		}
		return render(request, 'accounts/register.html', context)

def home(request):
	if not request.user.is_authenticated:
		return redirect('accounts:login')
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity != 'student':
		logout(request)
		return render(request, 'accounts/login.html')
	else:
		course_form = AddCourseForm(request.POST or None)
		create_courses = CreateCourse.objects.all()
		add_courses = AddCourse.objects.all()
		if request.method == "POST":
			if course_form.is_valid():
				course_form.instance.username = user_profile.user.username
				course_form.save()
				return redirect('accounts:home')
			return render(request, 'accounts/home.html', {'error_message': 'Unmatched Content'})
		context = {
			"form": course_form,
			"create_courses": create_courses,
			"add_courses": add_courses,
		}
		return render(request, 'accounts/home.html', context)	

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		identity = request.POST['identity']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				try:
					user_profile = UserProfile.objects.get(user=user,identity=identity)
				except ObjectDoesNotExist:
					logout(request)
					return render(request, 'accounts/login.html')
				if user_profile is not None:
					if identity=='student':
						return redirect('accounts:home')
					else:
						return redirect('accounts:home_t')
		else:
			return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})
	logout(request)
	return render(request, 'accounts/login.html')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/accounts/')

def home_t(request):
	if not request.user.is_authenticated:
		return render(request, 'accounts/login.html')
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity != 'teacher':
		logout(request)
		return render(request, 'accounts/login.html')
	else:
		courses = CreateCourse.objects.filter(username = user_profile.user.username)
		return render(request, 'accounts/home_t.html', {
			'courses': courses
		})

def course_251(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity == 'teacher':
		logout(request)
		return render(request, 'accounts/login.html')
	Assignments = Book.objects.filter(course = 'CS251')
	return render(request, 'accounts/course.html',{
            'Assignments': Assignments
    })

def course_293(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity == 'teacher':
		logout(request)
		return render(request, 'accounts/login.html')
	Assignments = Book.objects.filter(course = 'CS293')
	return render(request, 'accounts/course.html',{
            'Assignments': Assignments
    })

def course_215(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity == 'teacher':
		logout(request)
		return render(request, 'accounts/login.html')
	Assignments = Book.objects.filter(course = 'CS215')
	return render(request, 'accounts/course.html',{
            'Assignments': Assignments
    })

def profile(request):
	if not request.user.is_authenticated:
		return redirect('accounts:login')
	user_profile = UserProfile.objects.get(user=request.user)
	return render(request, 'accounts/profile.html', {
		    'profile':user_profile})

def course(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if request.method == 'POST' and user_profile.identity == 'teacher':
		form = CreateCourseForm(request.POST, request.FILES)
		if form.is_valid:
			form.instance.username = user_profile.user.username
			form.save()
			return redirect('/accounts/home_t/')
		return redirect('accounts:course')
	else:
		if user_profile.identity != 'teacher':
			logout(request)
			return HttpResponseRedirect('/accounts/')
		form = CreateCourseForm()
		courses = CreateCourse.objects.filter(username = user_profile.user.username)
		return render(request, 'accounts/create_course.html', {
        'form': form,
		'courses': courses,
    })

def assignments(request):
	user_profile = UserProfile.objects.get(user = request.user)
	Assignments = Book.objects.all()
	Submissions = Submit.objects.all()
	NewAssignments = Assignment.objects.all()
	NewSubmissions = Solution.objects.all()
	if user_profile.identity == 'student':
		Grades = Grade.objects.filter(Student = user_profile.user.username)
		context = {
			"Assignments": Assignments,
			"Submissions": Submissions,
			"NewAssignments": NewAssignments,
			"NewSubmissions": NewSubmissions,
			"Grades": Grades,
		}
		return render(request, 'accounts/assignments_s.html', context)
	elif user_profile.identity == 'teacher':
		context = {
			"Assignments": Assignments,
			"Submissions": Submissions,
			"NewAssignments": NewAssignments,
			"NewSubmissions": NewSubmissions,
		}
		return render(request, 'accounts/assignments.html', context)
	else:
		logout(request)
		return HttpResponseRedirect('/accounts/')

def submissions(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity != 'teacher':
		logout(request)
		return HttpResponseRedirect('/accounts')
	Assignments = Assignment.objects.filter(username = user_profile.user.username)
	Solutions = Solution.objects.all()
	context = {
		'Assignments': Assignments,
		'Solutions': Solutions,
	}
	return render(request, 'accounts/submissions.html', context)

def courseview(request):
	user_profile = UserProfile.objects.get(user = request.user)
	Assignments = []
	Submissions = []
	NewAssignments = Assignment.objects.all()
	NewSubmissions = Solution.objects.all()
	if user_profile.identity == 'student':
		Grades = Grade.objects.filter(Student = user_profile.user.username)
		context = {
			"Assignments": Assignments,
			"Submissions": Submissions,
			"NewAssignments": NewAssignments,
			"NewSubmissions": NewSubmissions,
			"Grades": Grades,
		}
		return render(request, 'accounts/assignments_s.html', context)
	else:
		logout(request)
		return HttpResponseRedirect('/accounts/')

def view(request):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity != 'student':
		logout(request)
		return HttpResponseRedirect('/accounts/')
	courses = AddCourse.objects.filter(username = user_profile.user.username)
	Assignments = Assignment.objects.all()
	total = CreateCourse.objects.all()
	context = {
		'courses': courses,
		'Assignments': Assignments,
		'total': total,
	}
	return render(request, 'accounts/view.html', context)
def vsc(request):
	user_profile = UserProfile.objects.get(user = request.user)
	filename = user_profile.user.username + '.csv'
	if user_profile.identity == 'teacher':
		response = HttpResponse('')
		response['Content-Disposition'] = 'attachment; filename = {}'.format(filename)
		writer = csv.writer(response)
		writer.writerow(['Student', 'Qsn.NO', 'Course', 'Marks', 'FeedBack'])
		if Grade.objects.filter(username_t = user_profile.user.username) != []:
			grade = Grade.objects.filter(username_t = user_profile.user.username)
			var1 = True
		if var1:
			for grades in grade:
				writer.writerow([grades.Student, grades.num, grades.course, grades.marks, grades.FeedBack])
		return response

def grade(request, course):
	user_profile = UserProfile.objects.get(user = request.user)
	if user_profile.identity != 'teacher':
		logout(request)
		return HttpResponseRedirect('/accounts/')
	if request.method == "POST":
		grade_form = GradeForm(request.POST or None)
		if grade_form.is_valid():
			grade_form.instance.course = course
			grade_form.instance.username_t = user_profile.user.username
			grade_form.save()
			return redirect('accounts:home_t')
	form = GradeForm()
	return render(request, 'accounts/grade.html',{
			'form': form
		})
