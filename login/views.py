from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint' : '/users/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of users',
        },
        {
            'Endpoint' : '/users/add',
            'method' : 'GET',
            'body' : None,
            'description' : 'adding users',
        },
        {
            'Endpoint' : '/resources',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of resources',
        },
        {
            'Endpoint' : '/resources/add',
            'method' : 'GET',
            'body' : None,
            'description' : 'adding resources',
        },
    ]

    return Response(routes)


@api_view(['GET'])
def get_users(request):
    users = NewUser.objects.all()
    serializer = NewUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_resources(request, speciality, level):
    resources = Resources.objects.filter(speciality=speciality, level=level)
    serializer = ResourcesSerializer(resources, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    data = request.data

    user = NewUser.objects.create(
        email = data['email'],
        user_name = data['user_name'],
        first_name = data['first_name'],
        last_name = data['last_name'],
        is_student = data['is_student'],
        university = data['university'],
        level = data['level'],
        company = data['company'],

        is_residence = data['is_residence'],
        residence = data['residence'],
        is_staff = data['is_staff'],
        is_active = data['is_active'],
        profile_image = data['profile_image'],
        student_card = data['student_card'],
    )

    serializer = NewUserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addResources(request):
    data = request.data

    user = Resources.objects.create(
        user_publish = data['user_publish'],
        speciality = data['speciality'],
        level = data['level'],
        link = data['link'],
        description = data['description']
    )

    serializer = NewUserSerializer(user, many=False)
    return Response(serializer.data)