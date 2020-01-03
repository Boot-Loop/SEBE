## for function reuse as templates

def debug():
    while True:
        try:
            exec(input('>>> '))
        except: pass

import urllib.parse
import os

from django.shortcuts import render, reverse
from django.http import JsonResponse
from django.http.response import FileResponse

from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

DEFAULT_OBJECT_COUNT = 10

## used in api view detail to get object
def get_object(Model, pk):
    try:
        return Model.objects.get(pk=pk)
    except Model.DoesNotExist:
        raise NotFound(detail="DoesNotExists pk:%s Model:%s"%(pk, Model.__name__ ))

## url/appname/objects/?offset=10&count=12&orderby=name&reverse=true   -- count < 0 -> all objects

def list_response_get(request, Model, Serializer):
    offset  = request.GET.get('offset', 0)
    count   = request.GET.get('count', 10)
    orderby = request.GET.get('orderby', None)
    reverse = request.GET.get('reverse', 'false')

    ## TODO: handle type error maybe an error response
    try:
        offset = max(int(offset), 0)    ## negative indexing not valid
        count  = int(count)
    except:
        offset = 0
        count  = DEFAULT_OBJECT_COUNT

    objects = Model.objects.all()

    ## TODO: handle error maybe an error response
    if orderby :
        try:
            objects = objects.order_by('%s%s'%('-' if reverse == 'true' else '', orderby ))
        except:
            raise NotFound('InvalidOrderBy orderby:%s'%orderby)


    if count >= 0:
        objects = objects[ offset : count+1 ]
    
    serialized = Serializer(objects, many=True)
    return Response(serialized.data)


def list_response_post(request, Serializer):
    serializer = Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db.models.fields.files import File
def detail_response_get(request, pk, Model, Serializer):
    obj = get_object(Model, pk)

    ## download media
    download = request.GET.get('download')
    if download:
        if hasattr(obj, download):
            media = obj.__getattribute__(download)
            if not isinstance(media, File):
                raise NotFound(detail="AttributeNotMedia attr:%s Model:%s"%( download, Model.__name__ ))
            ## TODO: if manually delete the file from media and call the below line : FileNotFoundError raised
            response = FileResponse(media)
            response["Content-Disposition"] = "attachment; filename=" + os.path.split(media.name)[1]
            return response
        else:
            raise NotFound(detail="AttributeNotExists attr:%s Model:%s"%( download, Model.__name__ ))
        
    serialized = Serializer(obj)
    return Response(serialized.data)

def detail_response_post(request, pk, Model, Serializer):
    obj = get_object(Model, pk)
    serializer = Serializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def detail_response_delete(request, pk, Model):
    obj = get_object(Model, pk)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ObjectsResponse:
    def __init__(self, title, list_url_name, object_url_name, Model):
        self.title = title 
        self.list_url_name = list_url_name
        self.object_url_name = object_url_name
        self.Model = Model
    def __call__(self, request):
        if 'HTTP_USER_AGENT' in request.META.keys():
            return render(request, 'objects.html', {
                'title'     : self.title,
                'request'   : request,
                'all_url'   : reverse(self.list_url_name),
                'urls' : [
                    reverse(self.object_url_name, kwargs={'pk':obj.pk} ) for obj in self.Model.objects.all()
                ]
            })
        ctx = { 
            'List' :  reverse(self.list_url_name),
            'Detail' : [
                request.scheme +'://'+ request.META.HTTP_HOST + reverse(self.object_url_name, kwargs={'pk':obj.pk} ) for obj in self.Model.objects.all()
            ]
        }
        return JsonResponse(ctx)    
    pass


def pages_response(request, pages, title):
    if 'HTTP_USER_AGENT' in request.META.keys():
        return render(request, 'pages.html', {
            'request': request,
            'title'  : title,
            'pages'  : pages
        })
    ctx = dict()
    for page in pages: 
        ctx.update( { page.name : request.scheme + '://' + request.META['HTTP_HOST'] + page.url})
    return JsonResponse(ctx)
