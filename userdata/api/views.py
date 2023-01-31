from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializer import UserDataSerializer
from userdata.models import UserData

# @permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
@api_view()
def userDataFunc(request):

    req_username = request.query_params['username']
    u = User.objects.get(username=req_username)
    u_wrongans = u.userdata.wrongQuestions
    return Response({'wrongAns': u_wrongans})


class UserDataViewSet(viewsets.ModelViewSet):
    serializer_class = UserDataSerializer

    def get_queryset(self):
        userdata = UserData.objects.all()
        return userdata

    def retrieve(self, request, *args, **kwargs):
        param = kwargs
        print(param['pk'])
        userdata = UserData.objects.filter(wrongQuestions=param['pk'])
        serializer = UserDataSerializer(userdata, many=True)
        return Response(serializer.data)