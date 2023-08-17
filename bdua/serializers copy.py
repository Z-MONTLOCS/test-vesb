from rest_framework import serializers


from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','document_type','identification_number','first_name', 'middle_name', 'last_name', 'second_last_name', 'eps']

    







       


 