from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

# 여기 있는 view는 모두 함수형 view이다. 4장에서 클래스형 view를 구현해서 더 간단하게 표현이 가능하다.
def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'posts/post_list.html',context)

def post_detail(request,post_id):
    post = Post.objects.get(id=post_id) # detail 이니까 1개씩 반환받아야함
    context = {'post':post}
    return render(request,'posts/post_detail.html',context)

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST) # form과 data를 바인딩
        if post_form.is_valid():
            new_post = post_form.save() # db에 데이터 저장
            return redirect('post-detail',post_id=new_post.id) # detail.html로 가려면 id필요
    else: # method가 get인 경우
        post_form = PostForm() # form 새로 생성
    return render(request,'posts/post_form.html',{'form':post_form}) # not_valid or get 요청인 경우 실행

def post_update(request,post_id):
    post = Post.objects.get(id=post_id) # 기존에 작성된 post 가져오기
    if request.method == 'POST':
        post_form = PostForm(request.POST,instance=post) # 기존 post 값 넣기
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail',post_id=post.id)
    else: # get 요청인 경우
        post_form = PostForm(instance=post)
    return render(request,'posts/post_form.html',{'form':post_form})

def post_delete(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request,'posts/post_confirm_delete.html',{'post':post})
    
def index(request):
    return redirect('post-list')