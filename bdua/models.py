from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    document_type_choices = [
        ('AS', 'Adulto sin identificación'),
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cedula de Extranjería'),
        ('CD', 'Carnet diplomático'),
        ('CN', 'Certificado Nacido Vivo'),
        ('MS', 'Menor sin Identificación'),
        ('NU', 'No. Único de Id. Personal'),
        ('PA', 'Pasaporte'),
        ('PE', 'Per Especial Permanencia'),
        ('PT', 'Permiso por Protección Temporal'),
        ('RC', 'Registro Civil'),
        ('SC', 'Salvo Conducto'),
        ('TI', 'Tarjeta de Identidad'),
    ]

    gender_choices = [
        ('F', 'F'),
        ('M', 'M'),
    ]

    affiliation_state_choices = [
        ('activo', 'activo'),
        ('retirado', 'retirado'),
    ]

    membership_type_choices = [
        ('cotizante', 'cotizante'),
    ]

    document_type = models.CharField(max_length=2, choices=document_type_choices, null=True)
    identification_number = models.PositiveIntegerField(unique=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_choices, null=True)
    birthdate = models.DateField(null=True)
    eps = models.CharField(max_length=255, null=True)

    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    second_last_name = models.CharField(max_length=255, null=True)

    phone_number = models.CharField(max_length=255, unique=True, null=True)
    city = models.CharField(max_length=255, null=True)
    
    affiliation_state = models.CharField(max_length=10, choices=affiliation_state_choices, null=True)
    membership_type = models.CharField(max_length=10, choices=membership_type_choices, null=True)
    
    eps_user = models.CharField(max_length=255, null=True)
    password_eps = models.CharField(max_length=255, null=True)
    
    email = models.EmailField(unique=True, null=True)
