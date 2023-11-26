# 여기에 코드를 작성하세요
from django.core.exceptions import ValidationError

def validate_no_hash(value):
    if '#' in value:
        raise ValidationError('error message')
        
def validate_no_numbers(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError('error message')
            
def validate_score():
    if not (0 <= value and value <= 10):
        raise ValidationError('error message')