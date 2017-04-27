from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json, requests

# Create your views here.
def index(request):
    print("Under home page")
    return render(request, 'events/index.html')

def create_events(request):
    if request.method == "POST":
        form = request.POST.dict()
        print("creating events")
        print(request.POST.get("event_name"))
        jsonData = json.dumps(form)
        print(jsonData)
        urlData = "http://35.154.20.226:3000/create_events"
        headers = {'content-type': 'application/json'}
        r = requests.post(urlData, jsonData, headers=headers)
        print(r.status_code)
        event = {
            'EventsName' : request.POST.get("event_name"),
            'department_branch' : request.POST.get("department_branch"),
            'event_information' : request.POST.get("event_information"),
            'event_type' : request.POST.get("event_type"),
            'event_venue' : request.POST.get("event_venue"),
        }
        return render(request, 'events/blank.html')
    return render(request, 'events/forms.html')

def find_events(request):
    print("requesting list of events")
    keyDic = {
        'range' : "0_50"
    }
    jsonData = json.dumps(keyDic)
    urlData = "http://35.154.20.226:3000/find_events"
    headers = {'content-type': 'application/json'}
    r = requests.post(urlData,jsonData, headers=headers)
    print(r.status_code)
    if(r.status_code == 404):
        return HttpResponse("Not Found")
    else:
        recievedJsonData = r.text #string obj
        recievedJsonData_list = json.loads(recievedJsonData)
        # print(type(recD))
        paginator = Paginator(recievedJsonData_list, 2)
        page = request.GET.get('page')
        events = list
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)
        return render(request, 'events/listEvents.html', {'events': events})

def delete_event(request, event_id):
    urlData = "http://35.154.20.226:3000/delete_events"
    headers = {'content-type': 'application/json'}
    keyDic = {
        'id' : event_id
    }
    jsonData = json.dumps(keyDic)
    r = requests.post(urlData, jsonData, headers=headers)
    print(r.status_code)
    return render(request, 'events/blank.html')

def create_placement(request):
    if request.method == "POST":
        form = request.POST.dict()
        print("creating placement details")
        jsonData = json.dumps(form)
        print(jsonData)
        urlData = "http://35.154.20.226:3000/create_placement"
        headers = {'content-type': 'application/json'}
        r = requests.post(urlData, jsonData, headers=headers)
        print(r.status_code)
        event = {
            'EventsName' : request.POST.get("companiesPlacement"),
            'department_branch' : request.POST.get("department_branch"),
            'packagesOffered' : request.POST.get("packagesOffered"),
            'description' : request.POST.get("description"),
            'policy' : request.POST.get("policy"),
        }
        return render(request, 'events/blank.html')
    return render(request, 'events/forms_placement.html')

def find_placement(request):
    print("requesting list of placement")
    keyDic = {
        'range' : "0_50"
    }
    jsonData = json.dumps(keyDic)
    urlData = "http://35.154.20.226:3000/find_placement"
    headers = {'content-type': 'application/json'}
    r = requests.post(urlData,jsonData, headers=headers)
    print(r.status_code)
    if(r.status_code == 404):
        return HttpResponse("Not Found")
    else:
        recievedJsonData = r.text #string obj
        recievedJsonData_list = json.loads(recievedJsonData)
        # print(type(recD))
        paginator = Paginator(recievedJsonData_list, 2)
        page = request.GET.get('page')
        placements = list
        try:
            placements = paginator.page(page)
        except PageNotAnInteger:
            placements = paginator.page(1)
        except EmptyPage:
            placements = paginator.page(paginator.num_pages)
        return render(request, 'events/listPlacements.html', {'placements': placements})

def delete_placement(request, placement_id):
    urlData = "http://35.154.20.226:3000/delete_placement"
    headers = {'content-type': 'application/json'}
    keyDic = {
        'id' : placement_id
    }
    jsonData = json.dumps(keyDic)
    r = requests.post(urlData, jsonData, headers=headers)
    print(r.status_code)
    return render(request, 'events/blank.html')
