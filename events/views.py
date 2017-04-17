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
        urlData = "https://6d08b7f7.ngrok.io/create_events"
        headers = {'content-type': 'application/json'}
        r = requests.post(urlData, jsonData, headers=headers)
        print(r.status_code)
        event = {
            'EventsName' : request.POST.get("event_name"),
            'department_branch' : request.POST.get("department_branch")
        }
        return render(request, 'events/eSuccessful.html', {'event': form})
    return render(request, 'events/createEvent.html')

def find_events(request):
    print("requesting list of events")
    keyDic = {
        'range' : "0_50"
    }
    jsonData = json.dumps(keyDic)
    urlData = "http://12a7e227.ngrok.io/find_events"
    headers = {'content-type': 'application/json'}
    r = requests.post(urlData,jsonData, headers=headers)
    print(r.status_code)
    if(r.status_code == 404):
        return HttpResponse("Not Found")
    else:
        recievedJsonData = r.text #string obj
        recievedJsonData = json.loads(recievedJsonData)
        # print(type(recD))
        recievedJsonData = {
            'data' : recievedJsonData
        }
        return render(request, 'events/listEvents.html', recievedJsonData)

def delete_events(request):
    print("Deleteing requests")
