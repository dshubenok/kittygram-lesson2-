from .models import Cat, Owner, Achivement
from rest_framework import serializers

class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'cats']


class AchivementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achivement
        fields = ['name']


class CatSerializer(serializers.ModelSerializer):
    achivements = AchivementSerializer(many=True)
    color = serializers.ChoiceField(choices=['Серый', 'Чёрный', 'Белый', 'Рыжий', 'Смешанный'])

    class Meta:
        model = Cat
        fields = ['name', 'color', 'birth_year', 'achivements', 'owner']
