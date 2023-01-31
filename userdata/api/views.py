from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated


# @permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
@api_view()
def userDataFunc(request):

    req_username = request.query_params['username']
    u = User.objects.get(username=req_username)
    u_wrongans = u.userdata.wrongQuestions
    return Response({'wrongAns': u_wrongans})
