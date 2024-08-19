from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    blog = {'title': 'First post', 'content': 'Hey! Welcome to my first post!'}
    return Response(blog)