## for function reuse as templates

import urllib.parse
import os

from django.urls import path
from django.shortcuts import render, reverse
from django.http import JsonResponse
from django.http.response import FileResponse

from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework import serializers

from .sebedecor import login_required

DEFAULT_OBJECT_COUNT = 10

from . import Page


## TODO: move this
def getPageUrlName(Model):
    return '%s-%s'%( Model._meta.app_label, Model._meta.verbose_name_plural )

def getListUrlName(Model):
    return '%s-%s-list'%( Model._meta.app_label, Model._meta.verbose_name_plural )

def getDetailUrlName(Model):
    return '%s-%s'%( Model._meta.app_label, Model._meta.verbose_name)

class AppHomeResponse:

    def __init__(self, model_registry):
        self.model_registry = model_registry

    @login_required
    def __call__(self, request):
        pages = []
        for Model in self.model_registry:
            pages.append( Page(Model._meta.verbose_name_plural, reverse(getPageUrlName(Model))) )
        return pages_response(request, pages, Model._meta.app_label.capitalize())



## returns the url patterns for the models to be registered
def register_models(model_registry_list):
    urlpatterns = []
    for Model in model_registry_list:
        model_name_s    = Model._meta.verbose_name
        model_name_p    = Model._meta.verbose_name_plural 

        ## default url patterns
        model_page      = '%s/'%model_name_p
        page_url_name   = getPageUrlName(Model)

        model_list      = '%s/list'%model_name_p
        list_url_name   = getListUrlName(Model)

        model_detail      = '%s/<int:pk>'%model_name_s
        detail_url_name = getDetailUrlName(Model)
        
        urlpatterns += [
            path(model_page ,  ObjectsResponse(Model),   name=page_url_name),
            path(model_list,   make_list_view_class(Model).as_view(),   name=list_url_name),
            path(model_detail, make_detail_view_class(Model).as_view(), name=detail_url_name),
        ]
    return urlpatterns



def make_serializer_class(Model):
    class Serializer(serializers.ModelSerializer):
        class Meta:
            model  = Model
            fields = list( map( lambda field : field.name, Model._meta.fields ) )
    return Serializer

def make_list_view_class(Model):
    class ListView(APIView):
        
        @login_required
        def get(self, request):
            return list_response_get(request, Model, make_serializer_class(Model))
        
        @login_required
        def post(self, request, format=None):
            return list_response_post(request, make_serializer_class(Model))
    ListView.__name__ = Model.__name__
    return ListView

def make_detail_view_class(Model):
    class DetailView(UpdateAPIView):
        queryset = Model.objects.all()
        serializer_class = make_serializer_class(Model)

        @login_required
        def get(self, request, pk):
            return detail_response_get(request, pk, Model, self.serializer_class)

        @login_required
        def put(self, request, pk, format=None):
            return detail_response_put(request, pk, Model, self.serializer_class)

        @login_required
        def delete(self, request, pk, format=None):
            return detail_response_delete(request, pk, self.serializer_class)
    DetailView.__name__ = Model.__name__
    return DetailView



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

def detail_response_put(request, pk, Model, Serializer):
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

## TODO: title -> Model.__name__
## get other default urls from settings : get_list_ulr(Model), get_object_url(Model)
class ObjectsResponse:
    def __init__(self, Model):
        self.title = Model.__name__ 
        self.list_url_name = getListUrlName(Model)
        self.detail_url_name = getDetailUrlName(Model)
        self.Model = Model
    
    @login_required
    def __call__(self, request):
        if 'HTTP_USER_AGENT' in request.META.keys():
            return render(request, 'objects.html', {
                'title'     : self.title,
                'request'   : request,
                'all_url'   : reverse(self.list_url_name),
                'urls' : [
                    reverse(self.detail_url_name, kwargs={'pk':obj.pk} ) for obj in self.Model.objects.all()
                ]
            })
        ctx = { 
            'List' :  reverse(self.list_url_name),
            'Detail' : [
                request.scheme +'://'+ request.META.HTTP_HOST + reverse(self.detail_url_name, kwargs={'pk':obj.pk} ) for obj in self.Model.objects.all()
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
