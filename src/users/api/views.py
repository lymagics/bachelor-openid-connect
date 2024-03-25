from oauth2_provider.contrib.rest_framework import OAuth2Authentication, \
    TokenHasReadWriteScope
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.api.schemas import UserOut


@api_view(['GET'])
@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated, TokenHasReadWriteScope])
def user_get(request):
    data = UserOut(request.user).data
    return Response(data)
