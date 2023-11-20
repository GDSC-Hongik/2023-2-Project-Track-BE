from django.core.exceptions import ValidationError

def validate_no_hash(value):
    if '#' in value:
        raise ValidationError('제목과 내용에 "#"이 포함될 수 없습니다.')
    
def validate_no_numbers(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError('감정상태에 숫자는 포함될 수 없습니다.')
        
def validate_score(value):
    if value < 0 or value > 10:
        raise ValidationError('감정 점수는 0~10까지 가능합니다.')