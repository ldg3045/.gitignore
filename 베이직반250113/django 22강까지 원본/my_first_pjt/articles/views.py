from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST



# Create your views here.
def index(request):
    return render(request, "articles/index.html")

def articles(request):
    articles = Article.objects.all().order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all().order_by("-pk")
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "articles/article_detail.html", context)


# 새 글을 생성하고 상세 페이지로 이동
@login_required
def create(request):
    if request.method == "POST":  # 데이터 전송 방식이 POST 일 때
        form = ArticleForm(request.POST, request.FILES) # form에 request.POST에 있는 데이터 채움, request.FILES에 있는 파일 추가
        if form.is_valid():  # form 형식에 맞으면
            article = form.save() # 저장하고 해당 객체 반환
            return redirect('articles:article_detail', article.pk) # 상세 페이지로 이동
    else:                    # 데이터 전송 방식이 POST가 아닐 때
        form = ArticleForm() # 비어있는 form 생성

    context = {"form": form}
    return render(request, "articles/create.html", context) 
    

# 글 수정(업데이트)
@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article) # 강의와 별개로 request.FILES 사진 수정 변경 추가
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/update.html", context)


# 글 삭제
@require_POST # POST 방식으로만 접근 가능
def delete(request, pk):
    if request.user.is_authenticated:   
        article = get_object_or_404(Article, pk=pk)
        article.delete() # 삭제
    return redirect("articles:articles") # 삭제 후 목록으로 이동

@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect("articles:article_detail", article.pk)



    
def data_throw(request):
    return render(request, "articles/data-throw.html")


def data_catch(request):
    data = request.GET.get("message")
    context = {
        "data": data
    }
    return render(request, "articles/data_catch.html", context)


