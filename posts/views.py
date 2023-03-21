from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.shortcuts import render
from django.core.mail import send_mail
from datetime import datetime
import csv
from .forms import UploadFileForm
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.


def index(request):
    # if the methode is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print("hello world")
        # If the form is valid
        # enrollment_id = def genEnroll()
        if form.is_valid():
            # Yes, Save
            form.save()
            recipient_list = []    
            for data in Post.objects.all():
                recipient_list.append(data.email)
                mail_id = recipient_list[len(recipient_list)-1]
                std_name = (data.name)
                S_class = (data.Student_class)
                S_section = (data.section)
                r_num = str(data.random_num).zfill(3)

            n_pre = std_name[:3].upper()
            d_pre = datetime.now().strftime('%d%m%y')
            en_id = d_pre + n_pre + r_num
            message = 'Dear'+ ' ' + std_name +"\n\n" +'You got enroll in Dummy School your Enrollment ID is'+'  '+ en_id +' ' +'lets provide us the hard documents for the future references.'+'\n\n'+'Team ' +'\n'+ 'Dummy School '

            admin_msg = 'Dear Admin,' + '\n\n' + 'You got new student'+' ' + std_name + ' ' +'enrolled in class' +' '+ S_class + ' '+', section' + ' '+ S_section + ' '+ 'with enrollment id ' + en_id + '\n\n''Bot Msg.'

            send_mail(
                'Enrollment Details',
                message,
                'aishwaryakp73@gmail.com',
                [mail_id],
                fail_silently= False
            )
            send_mail(
                'Got a new Student ',
                admin_msg,
                'aishwaryakp73@gmail.com',
                ['aishwaryashetty731997@gmail.com'],
                fail_silently= False
            )
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:

            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all students, limit = 20
    students = Post.objects.all().order_by('-created_at')[:20]
    
    # show
    return render(request, 'posts.html',
                  {'students': students})




def upload_file(request):

    # if request.method == 'POST':
        
    #     # try:
    #     #     csv_file = request.FILES['file']
    #     # except MultiValueDictKeyError:

    #     #     decoded_file = csv_file.read().decode('utf-8').splitlines()
    #     #     reader = csv.reader(decoded_file)
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         file = request.FILES['file']
    #         # read the data from the CSV file
    #         data = csv.reader(file)
    #         for row in data:
    #             post = Post(name=row[0], email=row[1], student_class=row[2], section = row[3])
    #             post.save()
    #         return render(request, 'us.html')
    # else:
    #     form = UploadFileForm()
    # return render(request, 'edit.html')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
            for row in csv_data:
                post = Post.objects.get_or_create(
                    name=row[0],
                    email=row[1],
                    student_class=row[2], 
                    section = row[3]
                )
                post.save()
            return render(request, 'us.html')
    return render(request, 'edit.html')

    









