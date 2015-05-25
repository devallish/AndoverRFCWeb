from news.models import NewsArticle
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('news\index.html')


def details(request, news_article_id):
    news_article = NewsArticle.objects.get(id=news_article_id)
    other_news = NewsArticle.objects.all()[:3]
    template = loader.get_template('news/details.html')
    context = Context({'news_article': news_article, 'other_news': other_news})
    return HttpResponse(template.render(context))