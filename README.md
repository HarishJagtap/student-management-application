
# Student management application



## Installation

```bash
    cd inside cloned folder
    virtualenv env -p python3
    source env/bin/activate

    pip install -r requirements.txt

    export SECRET_KEY="some_key"
    python manage.py runserver
```
Now server will be running at http://127.0.0.1:8000/

## Deployment

Application is deployed to heroku
https://student-management-harish.herokuapp.com/

### 1. Admin access
https://student-management-harish.herokuapp.com/admin/
Username: admin
Password: admin123

### 2. URL to fetch student info
https://student-management-harish.herokuapp.com/student/<id>/

### 3. Website to search student
https://student-management-harish.herokuapp.com/website/search/

### 4. Website to create new student
https://student-management-harish.herokuapp.com/website/create/
