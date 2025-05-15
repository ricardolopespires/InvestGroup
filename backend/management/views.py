from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Asset, InvestorProfile, Investidor, InvestmentOperation, RiskAssessment
from .serializers import (
    AssetSerializer,
    InvestorProfileSerializer,
    InvestidorSerializer,
    InvestmentOperationSerializer,
    RiskAssessmentSerializer
)


class AssetListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        assets = Asset.objects.all().select_related()
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Asset.objects.get(pk=pk)
        except Asset.DoesNotExist:
            return None

    def get(self, request, pk):
        asset = self.get_object(pk)
        if asset is None:
            return Response({"error": "Ativo não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AssetSerializer(asset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        asset = self.get_object(pk)
        if asset is None:
            return Response({"error": "Ativo não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AssetSerializer(asset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        asset = self.get_object(pk)
        if asset is None:
            return Response({"error": "Ativo não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvestorProfileListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profiles = InvestorProfile.objects.all().select_related()
        serializer = InvestorProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InvestorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvestorProfileDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return InvestorProfile.objects.get(pk=pk)
        except InvestorProfile.DoesNotExist:
            return None

    def get(self, request, pk):
        profile = self.get_object(pk)
        if profile is None:
            return Response({"error": "Perfil de investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvestorProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        profile = self.get_object(pk)
        if profile is None:
            return Response({"error": "Perfil de investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvestorProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        if profile is None:
            return Response({"error": "Perfil de investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvestidorListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        investidores = Investidor.objects.filter(usuario=request.user).select_related('usuario', 'investor_profile')
        serializer = InvestidorSerializer(investidores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InvestidorSerializer(data={**request.data, 'usuario': request.user.id}, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvestidorDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Investidor.objects.get(pk=pk, usuario=user)
        except Investidor.DoesNotExist:
            return None

    def get(self, request, pk):
        investidor = self.get_object(pk, request.user)
        if investidor is None:
            return Response({"error": "Investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvestidorSerializer(investidor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        investidor = self.get_object(pk, request.user)
        if investidor is None:
            return Response({"error": "Investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvestidorSerializer(investidor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        investidor = self.get_object(pk, request.user)
        if investidor is None:
            return Response({"error": "Investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        investidor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvestmentOperationListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        operations = InvestmentOperation.objects.filter(investidor__usuario=request.user).select_related('asset', 'investidor')
        serializer = InvestmentOperationSerializer(operations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InvestmentOperationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            investidor = serializer.validated_data['investidor']
            if investidor.usuario != request.user:
                return Response({"error": "Você não tem permissão para criar operações para este investidor"}, 
                                status=status.HTTP_403_FORBIDDEN)
            # Validação de exposição máxima
            asset = serializer.validated_data['asset']
            total_value = serializer.validated_data['quantity'] * serializer.validated_data['unit_price']
            profile = investidor.investor_profile
            if profile and total_value > (investidor.investimentos * profile.max_exposure / 100):
                return Response({"error": "Operação excede a exposição máxima permitida pelo perfil"}, 
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvestmentOperationDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return InvestmentOperation.objects.get(pk=pk, investidor__usuario=user)
        except InvestmentOperation.DoesNotExist:
            return None

    def get(self, request, pk):
        operation = self.get_object(pk, request.user)
        if operation is None:
            return Response({"error": "Operação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvestmentOperationSerializer(operation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        operation = self.get_object(pk, request.user)
        if operation is None:
            return Response({"error": "Operação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvestmentOperationSerializer(operation, data=request.data, partial=True)
        if serializer.is_valid():
            investidor = serializer.validated_data.get('investidor', operation.investidor)
            if investidor.usuario != request.user:
                return Response({"error": "Você não tem permissão para editar operações deste investidor"}, 
                                status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        operation = self.get_object(pk, request.user)
        if operation is None:
            return Response({"error": "Operação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RiskAssessmentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        assessments = RiskAssessment.objects.filter(operation__investidor__usuario=request.user).select_related('operation', 'operation__asset', 'operation__investidor')
        serializer = RiskAssessmentSerializer(assessments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RiskAssessmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            operation = serializer.validated_data['operation']
            if operation.investidor.usuario != request.user:
                return Response({"error": "Você não tem permissão para criar avaliações para esta operação"}, 
                                status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiskAssessmentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return RiskAssessment.objects.get(pk=pk, operation__investidor__usuario=user)
        except RiskAssessment.DoesNotExist:
            return None

    def get(self, request, pk):
        assessment = self.get_object(pk, request.user)
        if assessment is None:
            return Response({"error": "Avaliação de risco não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RiskAssessmentSerializer(assessment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        assessment = self.get_object(pk, request.user)
        if assessment is None:
            return Response({"error": "Avaliação de risco não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RiskAssessmentSerializer(assessment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        assessment = self.get_object(pk, request.user)
        if assessment is None:
            return Response({"error": "Avaliação de risco não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)