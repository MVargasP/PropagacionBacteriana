from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework import status
from bacteria.models import BacterialStrain
from bacteria.api.views import BacterialPopulationView, calculate_population

# Esta es la clase de prueba para la función de cálculo de población de la funcion version 2
#class PopulationCalculationTest(TestCase):
#    def test_calculate_population(self):
#        # Se define el estado inicial de las bacterias (todas adultas)
#        initial_state = [2, 3, 3, 1, 2]
#        days =60 # Se definine el número de días
#        population = calculate_populationv2(initial_state, days)  # Se realiza el cálculo de la población
#        # Aquí se realiza la prueba de aserción para verificar que la población calculada coincide con la esperada
#        self.assertEqual(population,7301991)  

class TestCalculatePopulation(TestCase):
    def setUp(self):
        self.bacteria_strain = BacterialStrain.objects.create(
            maturation_period=1,
            life_expectancy=4,
            reproduction_rate=2
        )
        self.initial_state = [2, 3, 3, 1, 2]

    def test_calculate_population(self):
        # Prueba cuando los días son 8
        result = calculate_population(self.bacteria_strain, self.initial_state, 8)
        self.assertEqual(result, 37)  # El resultado debería ser 37

        # Prueba cuando los días son 60
        result = calculate_population(self.bacteria_strain, self.initial_state, 60)
        self.assertEqual(result, 7301991)  # El resultado debería ser 7301991

    def test_negative_days(self):
        # Prueba cuando los días son negativos, el resultado debería ser igual al número de bacterias iniciales
        result = calculate_population(self.bacteria_strain, self.initial_state, -1)
        self.assertEqual(result, len(self.initial_state))

    def test_no_initial_bacteria(self):
        # Prueba cuando no hay bacterias iniciales, el resultado debería ser 0
        result = calculate_population(self.bacteria_strain, [], 10)
        self.assertEqual(result, 0)