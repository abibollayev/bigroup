from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Project
from .forms import CallbackRequestForm
from django.contrib import messages


def project_list(request, item_id=None):
    if not item_id:
        return render(request, "projects.html", {"title": "Проекты"})
    if request.method == "POST":
        form = CallbackRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно отправлена!")
    else:
        form = CallbackRequestForm()
    project = Project.objects.filter(id=item_id).values().first()
    tags = project["tags"].split(",") if project["tags"] else []
    return render(
        request,
        "project.html",
        {"title": project["title"], "project": project, "tags": tags, "form": form},
    )


def get_projects(request, item_id=None):
    if item_id is None:
        projects = Project.objects.all().values()
        return JsonResponse(list(projects), safe=False)
    else:
        try:
            project = Project.objects.filter(id=item_id).values().first()
            if project:
                return JsonResponse(project)
            else:
                raise Http404("Item not found")
        except Project.DoesNotExist:
            raise Http404("Item not found")
