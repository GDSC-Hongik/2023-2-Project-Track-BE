from .models import Post
posts = Post.objects.all()

def validate_post():
  for post in posts:
    if '&' in post.content:
      print(f'{post.id}번 글에 &가 있다.')
      post.content = post.content.replace('&', '')
      post.save()
    
    if post.dt_modified < post.dt_created:
      print(f'{post.id}번 글에 생성일보다 수정일이 앞섭니다.')
      post.save()