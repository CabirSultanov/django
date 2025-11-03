from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .forms import ArticleForm
from .models import Article

def index(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'habr_app/index.html', {'articles': articles})

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)


    liked_articles = request.session.get('liked_articles', [])
    disliked_articles = request.session.get('disliked_articles', [])
    
    user_like_status = None
    if article_id in liked_articles:
        user_like_status = 'like'
    elif article_id in disliked_articles:
        user_like_status = 'dislike'
    
    return render(request, 'habr_app/detail.html', {
        'article': article,
        'user_like_status': user_like_status
    })

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('habr_app:index')
    else:
        form = ArticleForm()
    return render(request, 'habr_app/create.html', {'form': form})

@login_required
def like_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_id)
        
        liked_articles = request.session.get('liked_articles', [])
        disliked_articles = request.session.get('disliked_articles', [])
        
        if article_id in liked_articles:
            article.likes -= 1
            article.save()
            liked_articles.remove(article_id)
            request.session['liked_articles'] = liked_articles
            action = 'removed'
        elif article_id in disliked_articles:

            article.dislikes -= 1
            article.likes += 1
            article.save()
            disliked_articles.remove(article_id)
            liked_articles.append(article_id)
            request.session['disliked_articles'] = disliked_articles
            request.session['liked_articles'] = liked_articles
            action = 'changed_to_like'
        else:
 
            article.likes += 1
            article.save()
            liked_articles.append(article_id)
            request.session['liked_articles'] = liked_articles
            action = 'added'
        
        return JsonResponse({
            'success': True,
            'likes': article.likes,
            'dislikes': article.dislikes,
            'action': action
        })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@login_required
def dislike_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_id)
        

        liked_articles = request.session.get('liked_articles', [])
        disliked_articles = request.session.get('disliked_articles', [])
        
        if article_id in disliked_articles:
  
            article.dislikes -= 1
            article.save()
            disliked_articles.remove(article_id)
            request.session['disliked_articles'] = disliked_articles
            action = 'removed'
        elif article_id in liked_articles:

            article.likes -= 1
            article.dislikes += 1
            article.save()
            liked_articles.remove(article_id)
            disliked_articles.append(article_id)
            request.session['liked_articles'] = liked_articles
            request.session['disliked_articles'] = disliked_articles
            action = 'changed_to_dislike'
        else:

            article.dislikes += 1
            article.save()
            disliked_articles.append(article_id)
            request.session['disliked_articles'] = disliked_articles
            action = 'added'
        
        return JsonResponse({
            'success': True,
            'likes': article.likes,
            'dislikes': article.dislikes,
            'action': action
        })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



