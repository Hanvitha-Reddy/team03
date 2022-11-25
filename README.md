# team03
Repository for the course project done as part of CS-251 (Software Systems Lab) course at IIT Bombay in Autumn 2022.
A Course Management System similar to Moodle created by Subhash,Praneeth,Hanvitha .We used Django Framework for the backend and HTML library for the frontend.

##Key Features:

### Authentication
We have used django-rest-auth for authentication and tokenization of users. To use the Course management page first of all each user should register their account with name, username, year of study, email id and identity whether he/she is a teacher or a student and then login with username,password and correct identity whether teacher or student(this is done to avoid confusion when a teaching assistant (teacher) who can also be a student for other courses) which then takes to the respective home pages 

### Courses and Assignments
We divided the courses to core courses and additional courses(like minors) .Core courses are accessible to all the students and teachers whereas minor courses i.e additional courses can be created by teachers specifying codes to register for the course while creating .Students can use theese code (which should be communicated using other forms) to enroll the course 
Teachers can upload assignments  in the all the core courses and additional courses created by them and can specify the submission file type for students
Students can dowload the 
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
