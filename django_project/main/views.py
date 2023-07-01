from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
import gridfs
from gridfs import GridFS


def generate(request):
    cluster = MongoClient(
        "mongodb+srv://igorzhilskiy99:N4nWM4JG61M7fmq1@cluster0.01pihmw.mongodb.net/?retryWrites=true&w=majority"
    )
    db = cluster["zenly"]
    fs = GridFS(db)
    collection = db["map"]

    global x
    a = collection.find_one({"name": "nnn"})["id"]
    for grid_out in fs.find({"filename": f"{a}"}):
        data = grid_out.read()
    return HttpResponse(data)

# Create your views here.
