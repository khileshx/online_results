from django.shortcuts import render
import pdb
from .models import Student, SubjectResult, SemesterResult
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    return render(request, "results/index.html")

def handler404(request, exception, template_name="404.html"):
    response = render_to_reponse(template_name)
    response_status_code = 404
    return reponse

def details(request):
    #import pdb
    #pdb.set_trace()
    roll_no = request.GET.get('roll_no')

    student = Student.objects.get(student_id=str(roll_no))
    results = SubjectResult.objects.filter(student_id=104, semester=2)

    sem_result = SemesterResult.objects.get(student_id=104, semester=2)
    

    var_dict = {"student": student, "results": results, "sem_result": sem_result}
    #import pdb; pdb.set_trace();

    return render(request, "results/details.html", var_dict)
