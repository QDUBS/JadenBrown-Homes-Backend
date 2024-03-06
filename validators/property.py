from rest_framework import serializers

def validate_terms_and_condition(self, value):
        if len(value) < 100:
            raise serializers.ValidationError("Please anter a more descriptive terms and condtions")
        return value