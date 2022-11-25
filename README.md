# team03
Repository for the course project done as part of CS-251 (Software Systems Lab) course at IIT Bombay in Autumn 2022.
A Course Management System similar to Moodle created by Subhash, Praneeth, Hanvitha.
We used Django Framework for the backend and HTML,Bootstrap library for the frontend.

## Ruuning Commands:
Open directory CS251 and then run commands <br>
python3 manage.py makemigrations <br>
python3 manage.py migrate <br>
python3 manage.py migrate --run-syncdb <br>
python3 manage.py runserver <br>

## To view documentation:
Cs251/docs/build/html/index.html

## Key Features:

### Authentication
We have used django-rest-auth for authentication and tokenization of users. To use the Course management page first of all each user should register their account with name, username, password, year of study, email id and identity whether he/she is a teacher or a student and then login with username,password and correct identity whether teacher or student(this is done to avoid confusion when a teaching assistant (teacher) who can also be a student for other courses) which then takes to the respective home pages .Home page contains profile option where they can see their details

### Courses and Assignments
We divided the courses to core courses and additional courses(like minors) .Core courses are accessible to all the students and teachers whereas minor courses i.e additional courses can be created by teachers by entering course name and specifying the code(6 letter) for students to enroll course .Students can use theese code (which should be communicated using other forms) to enroll the course 
Teachers can upload assignments  in the all the core courses and additional courses created by them and can specify the submission file type for students
Students can dowload the assignments posted, submit solutions and view feedback 

#### Create and enroll for courses:
For teacher to create a course he should click on create course option in the navigation bar and enter the course name and course code(6 letter) ( He can also see the courses created )
For a student to enroll a course he/she should enter the course code in the enroll course option on the home page

#### Create assignments and upload solutions:
For teacher to post assignment in core courses he can use the option Create Assignment in navigation bar and enter the assignment number(which should be unique for each assignment) select the course and extensions type for student submissions. 
And to create for additional courses he can use the option Create Assignment-2 in navigation bar and follow the same process.
For student to view assignment and submit solutions they should click on Assignments in the navigation bar and there they can see and download the assignments and have a submit option beside each assignment where they should enter assignment number and course name and upload files of specific types else they will get a message "invalid file type"


### Grading and Feedback
When teacher clicked on the course cards he can see the all submissions made by students with Assignments numbers and have an option to downloads files and give feedback
When clicked on the feedback option It asks for student name,Assignment number and they can give marks and any comments to students 
All students can signup or login into the server using appropriate commands and credentials. Once they log in, they can view their marks and feedback if any in beside their submissions in the respective course cards, if the feedback column is empty that means submission is not yet graded

### Checking file format
When teacher is creating an assignment there they can see an option to upload a text file (to specify the Tree Directory for zip files) and when students tries to upload  a file with different file network it shows an error "invalid Tree Directory" and for files of different type there is no need to upload a file to check

### Overview of framework and libraries
We have implemented with the back-end using Django with a Django-REST framework. And for the front end we used HTML,Bootstrap.


