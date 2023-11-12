from django.core.exceptions import ValidationError

def validate_symbols(value):
    if('0' in value ) or ('#' in value):
        raise ValidationError('"0"과 "#"은 포함될 수 없습니다.',code='symbol-err')