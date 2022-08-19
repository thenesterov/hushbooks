### How to develop?
1. `git clone https://github.com/thenesterov/hushbooks`
2. `python3 -m venv venv`
3. `. venv/bin/python3` (linux and macos) or `venv\Scripts\activate.bat` (windows)
4. `pip3 install -r requirements.txt`
5. `python3 manage.py migrate`
6. `python3 manage.py runserver`