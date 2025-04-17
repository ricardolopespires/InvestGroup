
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import RoboLevelSerializer
from rest_framework.views import APIView
from .serializers import RoboSerializer
from .serializers import RiskSerializer
from rest_framework import status
from .models import Robo
from .models import Level
from .models import Risk



class RoboListCreateAPIView(APIView):
    def get(self, request):
        robos = Robo.objects.all()
        serializer = RoboSerializer(robos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoboSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoboDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Robo, pk=pk)

    def get(self, request, pk):
        robo = self.get_object(pk)
        serializer = RoboSerializer(robo)
        return Response(serializer.data)

    def put(self, request, pk):
        robo = self.get_object(pk)
        serializer = RoboSerializer(robo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        robo = self.get_object(pk)
        serializer = RoboSerializer(robo, data=request.data, partial=True)  # <- permite atualizações parciais
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        robo = self.get_object(pk)
        robo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoboLevelAPIView(APIView):
    def get(self, request, pk):
        level = Level.objects.filter(advisor_id=pk)
        serializer = RoboLevelSerializer(level, many=True)
        return Response(serializer.data)
    




class RiskListCreateView(APIView):
    def get(self, request):
        risks = Risk.objects.all()
        serializer = RiskSerializer(risks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class RiskDetailView(APIView):
    permission_classes = [IsAuthenticated]
        

    def get(self, request, pk):
        risk = get_object_or_404(Risk, pk=pk)
        serializer = RiskSerializer(risk)
        return Response(serializer.data)

    def put(self, request, pk):
        risk = get_object_or_404(Risk, pk=pk)
        serializer = RiskSerializer(risk, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk):
        risk = get_object_or_404(Risk, pk=pk)   
        serializer = RiskSerializer(risk, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        risk = get_object_or_404(Risk, pk=pk)
        risk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)