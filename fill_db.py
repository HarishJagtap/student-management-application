import csv

from student_app.models import Book, School, Student


def fill_books():
    with open("books.csv", newline="") as f:
        csvfile = csv.DictReader(f)
        for row in csvfile:
            date_ = row["publication_date"]
            if date_:
                date_ = date_.split("-")
                date_.reverse()
                date_ = "-".join(date_)
                row["publication_date"] = date_
            else:
                row.pop("publication_date")
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
            if row["school"]:
                row["school"] = School.objects.get(name=row["school"])
            else:
                row["school"] = None
            book = None
            if row["books"]:
                book = Book.objects.get(title=row["books"])
            row.pop("books")
            student = Student(**row)
            student.save()
            if book:
                student.books.add(book)

def main():
    fill_books()
    fill_schools()
    fill_students()
