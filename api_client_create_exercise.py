from clients.courses.courses_client import get_courses_client, CreateCoursesRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExercisesRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
file_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'
)
create_file_response = file_client.create_file(create_file_request)
print(f'Create file data: {create_file_response}')

create_course_request = CreateCoursesRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print(f'Create course data: {create_course_response}')

create_exercise_request = CreateExercisesRequestDict(
    title="Exercise 1",
    courseId=create_course_response['course']['id'],
    maxScore=10,
    minScore=2,
    orderIndex=5,
    description="Description Exercise 1",
    estimatedTime="30 minutes"
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print(f'Create exercise data: {create_exercise_response}')
