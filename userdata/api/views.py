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
# get
    def retrieve(self, request, *args, **kwargs):
        param = kwargs
        print(param['pk'])
        # split list of kwargs separated by -
        # params_list = param['pk'].split('-')
        userdata = UserData.objects.filter(wrongQuestions=param['pk'])
        # filter object by 2 vars
        # userdata2 = UserData.objects.filter(wrongQuestions=params_list[0], rightQuestions=params_list[1])

        serializer = UserDataSerializer(userdata, many=True)
        return Response(serializer.data)
# post
#    def create(self, request, *args, **kwargs):
#        data = request.data
#
#        new_userdata = UserData.objects.create(user=data["id"], answeredQuestions=["total"], rightQuestions=["right"], wrongQuestions=["wrong"])
#
#        new_userdata.save()
#
#        serializer = UserDataSerializer(new_userdata)
#
#        return Response(serializer.data)

#delete

#   def destroy(self, request, *args, **kwargs):
#   loggedIn_user = request.user
#   if(loggedIn_user == "admin")
#       data = self.getData()
#       data.delete()
#       return Response({"message": "data has been deleted"})
#   else
#       return Response({"message": "not allowed"})
