import httpx


base_url = "http://localhost:8000"

login_payload = {
  "email": "flapsya@ya.ru",
  "password": "test"
}
login_response = httpx.post(f"{base_url}/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(f"Login response: {login_response_data}")
print(f"Status code: {login_response.status_code}")


bearer_token = f"Bearer {login_response_data['token']['accessToken']}"
headers = {
    "Authorization": bearer_token,
}

users_me_response = httpx.get(f"{base_url}/api/v1/users/me", headers=headers)
users_me_data = users_me_response.json()

print(f"Users me response: {users_me_data}")
print(f"Status code: {users_me_response.status_code}")
