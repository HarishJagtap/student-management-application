import csv

from student_app.models import Book, School, Student


def fill_books():
    with open("books.csv", newline="") as f:
        csvfile = csv.DictReader(f)
        for row in csvfile:
            book = Book(**row)
            book.save()

def fill_schools():
    with open("schools.csv", newline="") as f:
        csvfile = csv.DictReader(f)
        for row in csvfile:
            school = School(**row)
            school.save()

def fill_students():
    with open("students.csv", newline="") as f:
        csvfile = csv.DictReader(f)
        for row in csvfile:
            student = Student(**row)
            student.save()

def main():
    fill_books()
    fill_schools()
    fill_students()
