from django.shortcuts import render
from .models import Product # 이거 안해줌


# Create your views here.
def index(request):
    # 모든 상품 데이터를 조회해서 goods라는 변수에 담아 주세요.
    goods = Product.objects.all()
    # 내가 쓴 답: goods = dict()
    return render(request, 'goods/index.html', {'goods': goods})
    # 내가 쓴 답: return render(request, 'goods/index.html', context=goods)