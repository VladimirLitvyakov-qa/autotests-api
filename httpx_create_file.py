import httpx

from tools.fakers import get_random_email


base_url = "http://localhost:8000"

create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
create_user_response = httpx.post(f"{base_url}/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f"Create user data: {create_user_response_data}")


login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post(f"{base_url}/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"Login data: {login_response_data}")


create_file_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
create_file_response = httpx.post(
    f"{base_url}/api/v1/files",
    data={"filename": "image.png", "directory": "courses"},
    files={"upload_file": open('./testdata/files/image.png', 'rb')},
    headers=create_file_headers
)
create_file_response_data = create_file_response.json()
print(f"Create file data: {create_file_response_data}")
