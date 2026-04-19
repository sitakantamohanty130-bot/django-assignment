from django.shortcuts import render

def submit(request):
    return render(request, 'onlinecourse/course_details_bootstrap.html')

def show_exam_result(request):
    return render(request, 'onlinecourse/course_details_bootstrap.html')
