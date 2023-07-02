from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from bacteria.api.serializers import BacterialStrainSerializer
from bacteria.models import BacterialStrain
from bacteria.utilities import calculate_population
from rest_framework import status
class BacterialStrainViewSet(viewsets.ModelViewSet):
    queryset = BacterialStrain.objects.all()
    serializer_class = BacterialStrainSerializer

class BacterialPopulationView(APIView):
    """data de ejemplo para el body {
        "strain_id": 1,
        "days": 60,
        "initial_state": [2, 3, 3, 1, 2]
    }
    """
    def post(self, request, format=None):
        try:
            strain_id = request.data.get('strain_id')
            if strain_id is None:
                return Response({'error': 'Missing strain_id in request body'}, status=status.HTTP_400_BAD_REQUEST)
                
            strain = BacterialStrain.objects.get(id=strain_id)
        except BacterialStrain.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        days = request.data.get('days')
        if days is None:
            return Response({'error': 'Missing days in request body'}, status=status.HTTP_400_BAD_REQUEST)

        initial_state = request.data.get('initial_state')
        if initial_state is None:
            return Response({'error': 'Missing initial_state in request body'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not isinstance(initial_state, list):
            return Response({'error': 'initial_state must be a list'}, status=status.HTTP_400_BAD_REQUEST)

        population = calculate_population(strain,initial_state, days)
        return Response({'population': population})
