### How to develop?
1. `git clone https://github.com/thenesterov/hushbooks`
2. `python3 -m venv venv`
3. `. venv/bin/python3` (linux and macos) or `venv\Scripts\activate.bat` (windows)
4. `pip3 install -r requirements.txt`
5. `python3 manage.py makemigrations`
6. `python3 manage.py migrate`
7. `python3 manage.py runserver`

### How to registration?
Send http post request to `http://127.0.0.1:8000/api/v1/auth/users/` with body form-data:
1. username
2. password
3. email

### How to auth?
Send http post request to `http://127.0.0.1:8000/auth/token/login`. It will be return a token

### How to logout?
Send http post request to `http://127.0.0.1:8000/auth/token/logout` with header `Authorization` that will be equal the `Token ` + token. E.g. `Token bcedbf639a444d987759d63b8661dc42795005bb`

It works with Djoser (docs: https://djoser.readthedocs.io/en/latest/base_endpoints.html)