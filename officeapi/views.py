from django.http import JsonResponse
from .models import Character
from .serializers import CharacterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .characters import characters


@api_view(['GET'])
def get_characters(request):
    # characters = Character.objects.all()
    # serializer = CharacterSerializer(characters, many=True)
    return Response(characters)
