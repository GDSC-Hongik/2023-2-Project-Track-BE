#from django.shortcuts import render,redirect,get_object_or_404
#from django.core.paginator import Paginator
from django.views.generic import (
    CreateView,ListView,DetailView, UpdateView,DeleteView,RedirectView
)
from django.urls import reverse
from django.views import View
from .models import Post
from .form import PostForm
# Create your views here.

#함수형 view
#def index(request):
#    return redirect('post-list')

#제네릭
class IndexRedirectView(RedirectView):
    pattern_name='post-list'


#def post_lists(request):
#    posts=Post.objects.all()
#    paginator=Paginator(posts,6)
#    curr_page_number=request.GET.get('page')
#    if curr_page_number is None:
#        curr_page_number=1
#    page=paginator.page(curr_page_number)
#    return render(request,'posts/post_list.html',{'page':page})



class PostListView(ListView):
    model=Post
    #template_name='posts/post_list.html'
    #context_object_name='posts'
    ordering=['-dt_create']
    paginate_by=6
    #page_kwarg='page'
    
    

#def post_detail(request,post_id):
#    post=get_object_or_404(Post,id=post_id)
#    
#    context={"post":post}
#    return render(request,'posts/post_detail.html',context)

class PostDetailView(DetailView):
    model=Post
    #template_name='posts/post_detail.html'
    #pk_url_kwarg='post_id'
    #context_object_name='post'


#함수형 view
#def post_create(request):
#    if request.method=='POST':
#        post_form=PostForm(request.POST)
#        #유효성 검증
#        if post_form.is_valid(): 
#            #save를 호출하면 데이터 베이스에 데이터 저장됨
#            new_post=post_form.save()
#            return redirect('post-detail',post_id=new_post.id)
#        
#    else:
#        #서버에서는 데이터를 입력할 폼을 돌려주어야 함
#        post_form=PostForm()
#    
#    return render(request,'posts/post_form.html',{'form':post_form})



#def post_update(request,post_id):
#    post=get_object_or_404(Post,id=post_id)
#    if request.method=='POST':
#        post_form=PostForm(request.POST,instance=post)
#        if post_form.is_valid():
#            post_form.save()
#            return redirect('post-detial',post_id=post.id)
#        else:
#            post_form=PostForm(instance=post)
#    post_form=PostForm(instance=post)
#    return render(request,'posts/post_form.html',{'form':post_form})

class PostUpdateView(UpdateView):
    model=Post
    form_class=PostForm
    #template_name='posts/post_form.html'
    #pk_url_kwarg='pk'
    
    def get_success_url(self):
        return reverse('post-detail',kwargs={'pk':self.object.id})

#class PostCreateView(View):
#    def get(self,request):
#        post_form=PostForm()
#        return render(request,'posts/post_form.html',{'form':post_form})
#    
#    def post(self,request):
#        post_form=PostForm(request.POST)
#        if post_form.is_valid():
#            new_post=post_form.save()
#            return redirect('post-detial',post_id=new_post.id)
#       return render(request,'posts/post_form.html',{'form':post
# -form})
        
        
#제네릭 뷰
class PostCreateView(CreateView):
    model=Post
    form_class=PostForm
    # template_name='posts/post_form.html'
    
    def get_success_url(self):
        return reverse('post-detail',kwargs={'pk':self.object.id})


#def post_delete(request,post_id):
#    post=get_object_or_404(Post,id=post_id)
#    if request.method=="POST":
#        post.delete()
#        return redirect('post-list')
#    else:
#        return render(request,'posts/post_confirm_delete.html',{'post':post})
    


class PostDeleteView(DeleteView):
    model=Post
    #template_name='posts/post_confirm_delete.html'
    #pk_url_kwarg='pk'
    #context_object_name='post'
    
    
    def get_success_url(self):
        return reverse('post-list')
    