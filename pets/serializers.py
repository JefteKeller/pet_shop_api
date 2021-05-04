from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    scientific_name = serializers.CharField(max_length=255)


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    characteristic = serializers.CharField(max_length=255)


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=255)

    group = GroupSerializer()
    characteristic_set = CharacteristicSerializer(many=True)
