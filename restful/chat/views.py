__author__ = 'rrmerugu'

from rest_framework.views import APIView
from rest_framework.response import Response
from restful.chat.models import ChatMessages
from restful.chat.serializers import ChatMessagesSerializer
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework_mongoengine import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from mongoengine.queryset.visitor import Q

import logging

logger = logging.getLogger(__name__)


### utils stars

BUFFER_SIZE = 5

#
# def get_the_buffer_data(message_id):
#     ids = []
#     for id in range(int(message_id) - BUFFER_SIZE, int(message_id) + BUFFER_SIZE + 1):
#         ids.append(id)
#     return ids


#### utils ends


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class ChatList(generics.ListAPIView):
    serializer_class = ChatMessagesSerializer

    def get_queryset(self):
        queryset = ChatMessages.objects.all()
        message = self.request.query_params.get('message', None)
        if message is not None:
            queryset = queryset.filter(message__icontains=message)
        return queryset


class ChatBufferList(generics.ListAPIView):
    serializer_class = ChatMessagesSerializer

    def get_queryset(self):
        queryset = ChatMessages.objects.all()
        message_id = int(self.request.query_params.get('message_id', None))
        queryset = queryset.filter(message_id__gte= message_id - int(BUFFER_SIZE))
        return queryset



# class TalktoMeList(generics.ListAPIView):
#     serializer_class = ChatMessagesSerializer
#
#     def get_queryset(self):
#         queryset = ChatMessages.objects.all()
#         kw = self.request.query_params.get('kw', None)
#         logger.debug(kw)
#
#         if kw is not None:
#             queryset_contains = queryset.filter(message__icontains="%s"%kw)
#             for q in queryset_contains:
#                 logger.debug("%s %s" %(q.message_id , q.message))
#                 queryset2 = queryset.filter(message_id__gte= int(q.message_id),  username = "Chinni")[:5]
#
#                 serializer = ChatMessagesSerializer(queryset2, many=True)
#                 logger.debug(serializer.data)
#         return JSONResponse(serializer.data, status=200)


class TalktoMeList(APIView):
    ''' attend requests by guests '''

    def get(self, request, kw, *args, **kwargs):
        logger.debug(request)
        logger.debug(kw)
        queryset_contains = ChatMessages.objects.filter(message__icontains="%s"%kw)
        messages =  []
        for q in queryset_contains:
            logger.debug("%s %s" %(q.message_id , q.message))
            queryset2 = ChatMessages.objects.filter(message_id__gte= int(q.message_id),  username = "Chinni")[:5]
            serializer = ChatMessagesSerializer(queryset2, many=True)
            logger.debug(serializer.data)
            messages.append(serializer.data)
        logger.debug(messages)
        #serializer = ChatMessagesSerializer(messages, many=True)
        return JSONResponse(messages)



class FindWord(APIView):
    def get(self, request):
        pass
