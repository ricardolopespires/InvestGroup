# investments/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Portfolio, Investment
from .serializers import PortfolioSerializer, InvestmentSerializer
from django.shortcuts import get_object_or_404

# Views para Portfolio
class PortfolioList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        portfolios = Portfolio.objects.filter(user=request.user)
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PortfolioDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk, user):
        return get_object_or_404(Portfolio, pk=pk, user=user)
    
    def get(self, request, pk):
        portfolio = self.get_object(pk, request.user)
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)
    
    def put(self, request, pk):
        portfolio = self.get_object(pk, request.user)
        serializer = PortfolioSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        portfolio = self.get_object(pk, request.user)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views para Investment
class InvestmentList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        investments = Investment.objects.filter(portfolio__user=request.user)
        serializer = InvestmentSerializer(investments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InvestmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvestmentDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk, user):
        return get_object_or_404(Investment, pk=pk, portfolio__user=user)
    
    def get(self, request, pk):
        investment = self.get_object(pk, request.user)
        serializer = InvestmentSerializer(investment)
        return Response(serializer.data)
    
    def put(self, request, pk):
        investment = self.get_object(pk, request.user)
        serializer = InvestmentSerializer(investment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        investment = self.get_object(pk, request.user)
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

