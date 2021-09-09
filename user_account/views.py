from django.contrib.auth.decorators import login_required
from user_account.models import TemplateClass, Report
from django.http import Http404, JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EditProfileForm
from django.contrib import messages
from .models import TemplateClass
from django.conf import settings
import mimetypes
import subprocess
import datetime
import shutil
import os



@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(instance=request.user, data=request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        profile_form = EditProfileForm(instance=request.user)
    return render(request, 'user_account/profile.html', {'profile_form': profile_form, 'section':'profile'})


@login_required
def templates(request):
    temps = TemplateClass.objects.all()
    return render(request, 'user_account/templates.html', {'temp': temps})

@login_required
def template(request, tmp_id):
    try:
        temp = TemplateClass.objects.get(id=tmp_id)
    except TemplateClass.DoesNotExist:
        raise Http404('Template not found')   
    return render(request, 'user_account/template.html', {'temp': temp})


@login_required
def report(request):
    # generating unique string for the name of the file to be copied
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now = now.replace(":","_")
    # path of the original file
    source = './media/template_folder/main.tex'
    # path of the copied file
    destination = f'./static/compiled/{now}.tex'
    id = request.user.id
    # check if the user exist in the user_account_report table
    rpt = Report.objects.filter(user_id = id).exists()
    if rpt:
        user_template = Report.objects.get(user_id = id)
        user_tmp = user_template.template_file
        path = str(user_tmp)
        handle = open(os.path.join(settings.BASE_DIR, f'{user_tmp}'))
        var = handle.read()
        code = var
        # subprocess.call(['pdflatex', '-output-directory=./static/static/compiled/', path])
        # convert .tex to .pdf by removing .tex and append .pdf
        file_path1 = path[:-1:]
        file_path2 = file_path1[:-1:]
        file_path3 = file_path2[:-1:]
        file_path4 = ''.join((file_path3, 'pdf'))
        if request.is_ajax():
            latex_file = request.POST.get('code')
            with open(path, 'w') as f:
                f.write(latex_file)
                f.close()
            subprocess.call(['pdflatex', '-output-directory=./static/static/compiled/', path])
            file_path4 = ''.join((file_path3, 'pdf'))
            # Implement auto refresh feature  # try adding url and view for compilation
            # make sure you prevent the browser to cache generated PDF file
    else:
        # make copy of the original file
        copy_path = shutil.copy(source, destination)
        # insert user and copy of the original file in the user_account_report table
        Report.objects.create(user_id = id, template_file = copy_path)
        # open the the file you have copied
        handle = open(os.path.join(settings.BASE_DIR, f'{copy_path}'))
        # read the content of the file
        var = handle.read()
        # store file contents in the code variable
        code = var
        # compile and store the PDF file into the output directory
        subprocess.call(["pdflatex", "-output-directory=./static/static/compiled/", copy_path])
        # open the  generated PDF file and display it on template
        file_path1 = copy_path[:-1:]
        file_path2 = file_path1[:-1:]
        file_path3 = file_path2[:-1:]
        file_path4 = ''.join((file_path3, 'pdf'))
    template = 'UDSM CoICT'
    tmp_len = len(template)
    return render(request, 'user_account/coict_template.html', {'template':template, 'tmp_len':tmp_len, 'code':code, 'pdf':file_path4})

@login_required
def user_templates(request):
    id = request.user.id
    rpt = Report.objects.filter(user_id = id).exists()
    if rpt:
        template = 'UDSM CoICT'
        tmp_len = len(template)
    else:
        template = 'No template yet!'
        tmp_len = len(template) 
    return render(request, 'user_account/report.html', {'template': template, 'tmp_len': tmp_len})

@login_required
def report_download(request):
    id = request.user.id
    user_template = Report.objects.get(user_id = id)
    user_tmp = user_template.template_file
    file_path = str(user_tmp)
    path = 'static'
    # joining file paths
    file_joined = os.path.join(path, file_path)
    file_path1 = file_joined[:-1:]
    file_path2 = file_path1[:-1:]
    file_path3 = file_path2[:-1:]
    file_path4 = ''.join((file_path3, 'pdf'))
    file_open = open(file_path4, 'rb')
    mime_type, _ = mimetypes.guess_type(file_path4)
    response = HttpResponse(file_open, content_type=mime_type)
    response['Content-Disposition'] = "attachment; file_path4=%s" % file_path4
    return response