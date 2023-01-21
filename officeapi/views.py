from rest_framework.decorators import api_view
from rest_framework.response import Response
from .data.characters import characters
from .data.seasons import seasons
from .data.bestepisodes import bestepisodes


@api_view(['GET'])
def get_characters(request):
    return Response(characters)


@api_view(['GET'])
def get_character(request, _id):
    for char in characters:
        if char['_id'] == _id:
            return Response(char)


@api_view(['GET'])
def get_seasons(request):
    return Response(seasons)


@api_view(['GET'])
def get_season(request, s_id):
    for season in seasons:
        if season['s_id'] == s_id:
            return Response(season)


@api_view(['GET'])
def get_bestepisodes(request):
    return Response(bestepisodes)
