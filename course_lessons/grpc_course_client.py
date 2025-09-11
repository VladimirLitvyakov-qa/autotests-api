import grpc

from lesson_course import course_service_pb2, course_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)


response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))

print(f'course_id: "{response.course_id}"')
print(f'title: "{response.title}"')
print(f'description: "{response.description}"')
