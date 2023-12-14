import ast
from operator import itemgetter

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import *
from ..models import *

@api_view(["GET"])
def get_requests(request):
    requests = Requests.objects.all()
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_request_by_id(request, request_id):
    if not Requests.objects.filter(pk=request_id).exists():
        return Response(f"Заявки с таким id не существует!")

    req = Requests.objects.get(pk=request_id)
    serializer = RequestSerializer(req, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def update_request(request, request_id):
    if not Requests.objects.filter(pk=request_id).exists():
        return Response(f"Заявки с таким id не существует!")

    req = Requests.objects.get(pk=request_id)
    serializer = RequestSerializer(req, data=request.data, many=False, partial=True)

    if serializer.is_valid():
        serializer.save()

    req.req_status = 1
    req.save()

    return Response(serializer.data)

@api_view(["PUT"])
def update_request_user(request, request_id):
    if not Requests.objects.filter(pk=request_id).exists():
        return Response(f"Заявки с таким id не существует!")

    request_status = request.data["req_status"]

    if request_status not in [1, 5]:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    req = Requests.objects.get(pk=request_id)
    req_status = req.req_status

    if req_status == 5:
        return Response("Статус изменить нельзя")

    req.req_status = request_status
    req.save()

    serializer = RequestSerializer(req, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def update_request_admin(request, request_id):
    if not Requests.objects.filter(pk=request_id).exists():
        return Response(f"Заявки с таким id не существует!")

    request_status = request.data["req_status"]

    if request_status in [1, 5]:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    req = Requests.objects.get(pk=request_id)

    req_status = req.req_status

    if req_status in [3, 4, 5]:
        return Response("Статус изменить нельзя")

    req.req_status = request_status
    req.save()

    serializer = RequestSerializer(req, many=False)
    return Response(serializer.data)

@api_view(["DELETE"])
def delete_request(request, request_id):
    if not Requests.objects.filter(pk=request_id).exists():
        return Response(f"Заявки с таким id не существует!")

    req = Requests.objects.get(pk=request_id)
    req.req_status = 5
    req.save()

    requests = Requests.objects.all()
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
def delete_expertise_from_request(request, request_id, expertise_id):
    if not Requests.objects.filter(pk=request_id).exists():
        return Response(f"Заявки с таким id не существует")

    if not Expertises.objects.filter(pk=expertise_id).exists():
        return Response(f"Экспертизы с таким id не существует")

    req = Requests.objects.get(pk=request_id)
    req.expertises.remove(Expertises.objects.get(pk=expertise_id))
    req.save()

    serializer = ExpertiseSerializer(req.expertises, many=True)
    return Response(serializer.data)