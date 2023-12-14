import ast
from operator import itemgetter

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import *
from ..models import *

@api_view(["GET"])
def get_expertises(request):
    expertises = Expertises.objects.all()
    serializer = ExpertiseSerializer(expertises, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_expertise_by_id(request, expertise_id):
    if not Expertises.objects.filter(pk=expertise_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    expertise = Expertises.objects.get(pk=expertise_id)
    serializer = ExpertiseSerializer(expertise, many=False)

    return Response(serializer.data)

@api_view(["POST"])
def create_expertise(request):
    Expertises.objects.create()

    expertises = Expertises.objects.all()
    serializer = ExpertiseSerializer(expertises, many=True)
    return Response(serializer.data)

@api_view(["PUT"])
def update_expertise(request, expertise_id):
    if not Expertises.objects.filter(pk=expertise_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    expertise = Expertises.objects.get(pk=expertise_id)
    serializer = ExpertiseSerializer(expertise, data=request.data, many=False, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["DELETE"])
def delete_expertise(request, expertise_id):
    if not Expertises.objects.filter(pk=expertise_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    expertise = Expertises.objects.get(pk=expertise_id)
    expertise.expertise_status = 2
    expertise.save()

    expertises = Expertises.objects.filter(expertise_status=1)
    serializer = ExpertiseSerializer(expertises, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def add_expertise_to_request(request, expertise_id):
    if not Expertises.objects.filter(pk=expertise_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    expertise = Expertises.objects.get(pk=expertise_id)

    req = Requests.objects.filter(req_status=1).last()

    if req is None:
        req = Requests.objects.create()

    req.expertises.add(expertise)
    req.save()

    serializer = ExpertiseSerializer(req.expertises, many=True)
    return Response(serializer.data)
