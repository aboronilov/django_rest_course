from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from .serializers import WomenSerializer


class WomenModelViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.filter(pk=pk)
        return Response({'cats': [c.name for c in cats]})

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Women.objects.filter(pk=pk)
        return Women.objects.filter(is_published=True)


# class WomenListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenUpdateAPIView(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



