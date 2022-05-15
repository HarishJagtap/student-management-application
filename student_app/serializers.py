from rest_framework import serializers

from student_app.models import Book, School, Student


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    """Student serializer

    Student serializer output is different from serializer input.

    Student serializer output to display data contains:
        full name, 
        email, 
        gender,
        school name,
        school phone, 
        names of all books read by student,
        total no of pages read by student.

    Student serializer input to create new sudent instance contains:
        first name,
        last name,
        email,
        gender (display name),
        school name (school primary key),
        book names (book primary keys),
    """
    
    class Meta:
        model = Student
        fields = "__all__"

    def to_representation(self, instance):
        """Instance data to display data
        
        Student serializer output is different from model fields, so 
        create custom dict with output fields here.
        """
        out = dict()
        out["full_name"] = instance.first_name + " " + instance.last_name
        out["email"] = instance.email
        out["gender"] = instance.get_gender_display()

        out["school_name"] = ""
        out["school_phone"] = ""
        if instance.school:
            out["school_name"] = instance.school.name
            out["school_phone"] = instance.school.phone
        
        out["books"] = []
        out["total_no_of_book_pages_read"] = 0
        for book in instance.books.all():
            out["books"].append(book.title)
            out["total_no_of_book_pages_read"] += book.no_of_pages            
        
        return out

    def to_internal_value(self, data):
        """Display data to instance data
        
        Student serializer input is similar to model fields, except 
        gender, where we accept display name, so convert gender 
        to internal value here.
        """
        gender = dict()
        for choice in Student.GENDER_CHOICES:
            gender[choice[1]] = choice[0]
        data["gender"] = gender.get(data.get("gender", ""), "")

        return super().to_internal_value(data)
