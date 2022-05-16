from django.shortcuts import get_object_or_404, render
from django.db.models import Value
from django.db.models.functions import Concat, Trim
from rest_framework.decorators import action, api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from student_app.models import Book, School, Student
from student_app.serializers import StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    """ API to fetch student info from ID, create new student from data.
    
    """

    def retrieve(self, request, pk=None):
        """Fetch student info from ID."""
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def create(self, request):
        """Create new student from data."""
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def StudentSearchWebsite(request):
    """ Provide a website to search student by ID, full name."""
    context = {
        # Status to tell if search is successful or not.
        "student_search_status": [],
        "student_list": [],
    }

    student_id = 0
    full_name = request.GET.get("full_name", "")
    try:
        student_id_get = request.GET.get("student_id", 0)
        if student_id_get:
            student_id = int(student_id_get)
    except:
        context["student_search_status"].append("Student ID is not valid")

    students = Student.objects.all()
    search = False

    # Get all students which match the full name.
    if full_name:
        search = True
        students = students.annotate(full_name=Trim(
            Concat('first_name', Value(' '), 'last_name')))
        students = students.filter(full_name=full_name)

    # Get student which matches the input ID.
    if student_id:
        search = True
        students = students.filter(pk=student_id)

    if search:
        serializer = StudentSerializer(students, many=True)
        for student_data in serializer.data:
            context["student_list"].append(student_data)
        if not serializer.data:
            context["student_search_status"].append("No Students found")
    
    return render(request, "student_search.html", context)


@api_view(['GET', 'POST'])
def StudentCreateWebsite(request):
    """ Provide a website to create new student."""
    context = {
        # Status to tell if new student was created or just webpage was
        # fetched.
        "student_create_status": "",
        # Choices to fill in student creation form.
        "gender_choices": [""],
        "school_choices": [""],
        "books_choices": [],
    }

    # Fill student creation form choices.
    for (gender, display_name) in Student.GENDER_CHOICES:
        context["gender_choices"].append(display_name)
    for school in School.objects.all():
        context["school_choices"].append(school.name)
    for book in Book.objects.all():
        context["books_choices"].append(book.title)

    # Create new student if form data is provided.
    serializer = StudentSerializer(data=request.POST.copy())
    if serializer.is_valid():
        student = serializer.save()
        context["student_create_status"] = "Successfully created student \
            with id {}".format(student.id)

    return render(request, "student_registration.html", context)
