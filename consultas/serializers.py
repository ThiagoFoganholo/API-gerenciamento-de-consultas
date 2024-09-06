from rest_framework import serializers
from .models import Profissional, Consulta

class ProfissionalSerializer(serializers.ModelSerializer):
    def validate_contato(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("O contato deve conter apenas números.")
        return value

    class Meta:
        model = Profissional
        fields = ['id', 
                  'nome_completo', 
                  'nome_social', 
                  'profissao', 
                  'endereco', 
                  'contato'
                ]

    
class ConsultaSerializer(serializers.ModelSerializer):
    profissional = ProfissionalSerializer(read_only=True)

    class Meta:
        model = Consulta
        fields =[ 'id', 
                  'data_consulta', 
                  'profissional'
                ]
        

        