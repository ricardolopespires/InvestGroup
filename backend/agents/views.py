from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Asset, RiskProfile, Portfolio, PortfolioAllocation, InvestmentAgent, Transaction, AdvisorRecommendation
from .serializers import (AssetSerializer, RiskProfileSerializer, PortfolioSerializer, 
                         PortfolioAllocationSerializer, InvestmentAgentSerializer, 
                         TransactionSerializer, AdvisorRecommendationSerializer)
from django.shortcuts import get_object_or_404

class AssetListCreateView(APIView):
    def get(self, request):
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetDetailView(APIView):
    def get(self, request, id):
        asset = get_object_or_404(Asset, id=id)
        serializer = AssetSerializer(asset)
        return Response(serializer.data)

    def put(self, request, id):
        asset = get_object_or_404(Asset, id=id)
        serializer = AssetSerializer(asset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        asset = get_object_or_404(Asset, id=id)
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RiskProfileListCreateView(APIView):
    def get(self, request):
        risk_profiles = RiskProfile.objects.all()
        serializer = RiskProfileSerializer(risk_profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RiskProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RiskProfileDetailView(APIView):
    def get(self, request, id):
        risk_profile = get_object_or_404(RiskProfile, id=id)
        serializer = RiskProfileSerializer(risk_profile)
        return Response(serializer.data)

    def put(self, request, id):
        risk_profile = get_object_or_404(RiskProfile, id=id)
        serializer = RiskProfileSerializer(risk_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        risk_profile = get_object_or_404(RiskProfile, id=id)
        risk_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PortfolioListCreateView(APIView):
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

class PortfolioDetailView(APIView):
    def get(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id, user=request.user)
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)

    def put(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id, user=request.user)
        serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id, user=request.user)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PortfolioAllocationListCreateView(APIView):
    def get(self, request):
        allocations = PortfolioAllocation.objects.filter(portfolio__user=request.user)
        serializer = PortfolioAllocationSerializer(allocations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PortfolioAllocationSerializer(data=request.data)
        if serializer.is_valid():
            portfolio = get_object_or_404(Portfolio, id=serializer.validated_data['portfolio'].id, user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PortfolioAllocationDetailView(APIView):
    def get(self, request, id):
        allocation = get_object_or_404(PortfolioAllocation, id=id, portfolio__user=request.user)
        serializer = PortfolioAllocationSerializer(allocation)
        return Response(serializer.data)

    def put(self, request, id):
        allocation = get_object_or_404(PortfolioAllocation, id=id, portfolio__user=request.user)
        serializer = PortfolioAllocationSerializer(allocation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        allocation = get_object_or_404(PortfolioAllocation, id=id, portfolio__user=request.user)
        allocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InvestmentAgentConsultantListView(APIView):
    def get(self, request):
        agents = InvestmentAgent.objects.filter(specialty = 'consultor')
        serializer = InvestmentAgentSerializer(agents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvestmentAgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvestmentAgentDetailView(APIView):
    def get(self, request, id):
        agent = get_object_or_404(InvestmentAgent, id=id)
        serializer = InvestmentAgentSerializer(agent)
        return Response(serializer.data)

    def put(self, request, id):
        agent = get_object_or_404(InvestmentAgent, id=id, user=request.user)
        serializer = InvestmentAgentSerializer(agent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        agent = get_object_or_404(InvestmentAgent, id=id, user=request.user)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class InvestmentAgentManagerListView(APIView):
    def get(self, request):
        agents = InvestmentAgent.objects.filter(specialty = 'gestor')
        serializer = InvestmentAgentSerializer(agents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvestmentAgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InvestmentAgentManagerDetailView(APIView):
    def get(self, request, id):
        agent = get_object_or_404(InvestmentAgent, id=id)
        serializer = InvestmentAgentSerializer(agent)
        return Response(serializer.data)

    def put(self, request, id):
        agent = get_object_or_404(InvestmentAgent, id=id, user=request.user)
        serializer = InvestmentAgentSerializer(agent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        agent = get_object_or_404(InvestmentAgent, id=id, user=request.user)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransactionListCreateView(APIView):
    def get(self, request):
        transactions = Transaction.objects.filter(portfolio__user=request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            portfolio = get_object_or_404(Portfolio, id=serializer.validated_data['portfolio'].id, user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailView(APIView):
    def get(self, request, id):
        transaction = get_object_or_404(Transaction, id=id, portfolio__user=request.user)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, id):
        transaction = get_object_or_404(Transaction, id=id, portfolio__user=request.user)
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        transaction = get_object_or_404(Transaction, id=id, portfolio__user=request.user)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdvisorRecommendationListCreateView(APIView):
    def get(self, request):
        recommendations = AdvisorRecommendation.objects.filter(portfolio__user=request.user)
        serializer = AdvisorRecommendationSerializer(recommendations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvisorRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            portfolio = get_object_or_404(Portfolio, id=serializer.validated_data['portfolio'].id, user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvisorRecommendationDetailView(APIView):
    def get(self, request, id):
        recommendation = get_object_or_404(AdvisorRecommendation, id=id, portfolio__user=request.user)
        serializer = AdvisorRecommendationSerializer(recommendation)
        return Response(serializer.data)

    def put(self, request, id):
        recommendation = get_object_or_404(AdvisorRecommendation, id=id, portfolio__user=request.user)
        serializer = AdvisorRecommendationSerializer(recommendation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recommendation = get_object_or_404(AdvisorRecommendation, id=id, portfolio__user=request.user)
        recommendation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)