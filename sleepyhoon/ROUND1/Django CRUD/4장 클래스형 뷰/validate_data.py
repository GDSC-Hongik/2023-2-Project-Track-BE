from .models import Post

def validate_post(): # 뒤늦게 모든 데이터 유효성 검증하는 방법
    # 1. 모든 데이터 가져오기
    posts = Post.objects.all()
    # 2. 각각의 포스트 데이터를 보면서 &가 있는지 확인하기
    for post in posts:
        if '&' in post.content:
            print(post.id,'번 글에 &가 포함되어 있습니다.')
    # 3. 만약 '&'가 있으면 삭제
            post.content = post.content.replace('&','')
    # 4. 데이터 저장하기
            post.save()
        if post.dt_modified < post.dt_created:
            print(post.id,'번 글의 생성일이 수정일보다 과거입니다.')
            post.save()