from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from base.models import Post

@api_view(['GET'])
def getData(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)