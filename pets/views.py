from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from pets.models import Animal, Group, Characteristic
from pets.serializers import AnimalSerializer


class AnimalView(APIView):
    def get(self, request, animal_id=None):

        if animal_id:
            found_animal = get_object_or_404(Animal, id=animal_id)
            serializer = AnimalSerializer(found_animal)

            return Response(serializer.data, status=status.HTTP_200_OK)

        animal_list = Animal.objects.all()
        animal_list = AnimalSerializer(animal_list, many=True)

        return Response(animal_list.data, status=status.HTTP_200_OK)

    def post(self, request):
        input_serializer = AnimalSerializer(data=request.data)

        if not input_serializer.is_valid():
            return Response(input_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        data: dict = input_serializer.data
        group: dict = data.pop('group')
        characteristic_set: list = data.pop('characteristic_set')

        try:
            found_group = Group.objects.get(name=group.get('name'))
        except ObjectDoesNotExist:
            found_group = Group.objects.create(**group)

        animal = Animal.objects.create(**data, group=found_group)

        for char in characteristic_set:
            try:
                found_char = Characteristic.objects.get(
                    characteristic=char.get('characteristic'))
            except ObjectDoesNotExist:
                found_char = Characteristic.objects.create(**char)

            animal.characteristic_set.add(found_char)

        output_serializer = AnimalSerializer(animal)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, animal_id):
        found_animal = get_object_or_404(Animal, id=animal_id)
        found_animal.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
