from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from faker import Faker

from .forms import GenerateStudentsForm, StudentForm
from .models import Student
from .tasks import generate_random_students


class MainPage(View):
    def get(self, request):
        return render(request, 'students/index.html')


class CreateStudentView(LoginRequiredMixin, CreateView):
    form_class = StudentForm
    template_name = 'students/create_student_form.html'

    def form_valid(self, form):
        Student.objects.create(**form.cleaned_data)
        return redirect('all-students')


class GenerateStudentsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        fake = Faker()
        count = self.request.GET.get('count', '0')
        if count.isnumeric() and 0 < int(count) <= 100:
            students_result = []
            for i in range(1, int(count) + 1):
                students_result.append(Student(first_name=fake.first_name(),
                                               last_name=fake.last_name(),
                                               age=fake.random_int(18, 26)))
            Student.objects.bulk_create(students_result)
            return redirect('all-students')
        elif count == '0':
            return HttpResponse('<h1>Default value is 0</h1>'
                                '<br>Enter positive number from 1 too 100')
        else:
            return HttpResponse('<h3>Enter positive number from 1 too 100</h3>')


class EditStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'students/student_edit_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('all-students')


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('all-students')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class StudentsListView(ListView):
    model = Student
    template_name = 'students/students_list.html'
    paginate_by = 20

    def get_queryset(self):
        filter_params = {}
        student_id = self.request.GET.get('id', '')
        if student_id:
            filter_params['id'] = student_id

        student_first_name = self.request.GET.get('first_name', '')
        if student_first_name:
            filter_params['first_name'] = student_first_name

        student_last_name = self.request.GET.get('last_name', '')
        if student_last_name:
            filter_params['last_name'] = student_last_name

        student_age = self.request.GET.get('age', '')
        if student_age:
            filter_params['age'] = student_age

        queryset = Student.objects.filter(**filter_params)
        return queryset


class GenerateStudentsFormView(LoginRequiredMixin, FormView):
    template_name = 'students/student_generator.html'
    form_class = GenerateStudentsForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        generate_random_students.delay(total)
        messages.success(self.request, 'We are generating random students! Wait a moment and refresh this page.')
        return redirect('all-students')


def handler404(request, exception):
    return render(request, './errors/404_error_handler.html', status=404)


def handler500(request):
    return render(request, './errors/404_error_handler.html', status=500)
