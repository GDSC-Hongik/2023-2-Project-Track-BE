from django.core.exceptions import ValidationError

def validate_symbols(value):
    if ('@'in value) or ('#'in value):
        raise ValidationError('"@"와 "#"는 사용 불가입니다.',code='symbol-err')
    