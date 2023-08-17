from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from .mi_script_auto import ejecutar_mi_script_auto
from django.http import Http404


class PersonList(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            info = ejecutar_mi_script_auto(data)
            
            eps = info['eps']
            first_name = info['first_name']
            middle_name = info['middle_name']
            last_name = info['last_name']
            second_last_name = info['second_last_name']

            person_instance = Person(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                second_last_name=second_last_name,
                eps=eps,
                document_type=data['document_type'],
                identification_number=data['identification_number']
            )
            
            person_instance.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




class PersonDetail(APIView):
    def get_object(self,  document_type, identification_number):
          
        try:
            return Person.objects.get(document_type=document_type, identification_number=identification_number)

        except Person.DoesNotExist:
            raise Http404

    def get(self, request, document_type, identification_number):
        person = self.get_object(document_type, identification_number)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    # def put(self, request, pk):
    #     person = self.get_object(pk)
    #     serializer = PersonSerializer(person, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     person = self.get_object(pk)
    #     person.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
