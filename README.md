# team03
Repository for the course project done as part of CS-251 (Software Systems Lab) course at IIT Bombay in Autumn 2022.
A Course Management System similar to Moodle created by Subhash,Praneeth,Hanvitha .We used Django Framework for the backend and HTML library for the frontend.

##Key Features:

###Authentication
To use the Course management page first of all each user should register account with name,username,mail id and identity whether he/she is a teacher or a student 
First things first, you’re providing a service. Users need to sign up and then log in. Any data relevant to a user must be accessed in authenticated sessions only.


Once a user is in, they can create a course and add other users, either as teachers or students. To start with, this can be done utilizing an access code (course code) (which can be shared through means that don’t involve your tool), or, bonus, if you’re feeling ambitious, you can allow the course creator to invite teachers/students themselves, via email invitation.


Now that a course is set up, it is clear that teachers and students will have different levels of access to the course. This distinction between student and teacher could vary from course to course. (Assigning TA roles to students to grade/ make announcements)


We have used django-rest-auth for authentication and tokenization of users. To use all the features of our server, each user has to signup and login first.

Courses, Assignments and Teaching Assistants
The teacher can create courses, assignments within courses and assign teaching assistants with editable privileges. Deadlines and weightage can be set for assignments. The teacher can see which assignments are left for grading. Students can submit files into the assignment as long as deadline is pending, and download their submitted file any time.

Announcements, Emails and Messaging
The teacher (and possibly TAs) can make announcements (automated email to all enrolled in course) within all courses. Messaging between any 2 users is allowed (unless disabled for students by teacher).

Grading and Analysis
Once the deadline is crossed, the teacher can either download all submissions and submit feedback (as a CSV) or opt for auto-grading and provide evaluate.sh and out.txt (following some restrictions) to grade the python files of the students. Grades will then be assigned to the students, and the teacher can view course statistics (average histogram) as well as individual assignment grades (marks histogram). Each student may also see their marks for the course or each assignment.

CLI
All students can signup or login into the server using appropriate commands and credentials. Once they log in, they can view their grades for each course, access new course and submit files for an assignment.

Basic Commands
Run the commands from the project directory (containing manage.py)

For back-end:
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
For front-end:
npm i
npm start
For cli (requires back-end running):
python3 cli.py
Overview of framework and libraries
We have implemented a Django Rest API with the back-end using Django with a Django-REST framework. The frontend uses JavaScript along with React library combined with Redux. The CLI uses Prompt Toolkit and Requests module. The complete list of frameworks and libraries for backend can be found in requirements.txt, and for the frontend can be found in package.json.

Reference for boilerplate
YouTube
