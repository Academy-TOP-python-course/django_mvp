from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Article


def home(request):
   # html_content = """
   # <html>
   #     <head>
   #         <title>Мой новостной блог</title>
   #     </head>
   #     <body>
   #         <h1>Добро пожаловать в мой блог!</h1>
   #         <p>Здесь будут новости и статьи.</p>
   #     </body>
   # </html>
   # """
   # return HttpResponse(html_content)
   # news = [
   #    {'title': 'Первая новость', 'content': 'Содержимое первой новости.'},
   #    {'title': 'Вторая новость', 'content': 'Содержимое второй новости.'},
   #    {'title': 'Третья новость', 'content': 'Содержимое третьей новости.'}
   # ]
   # print(news[0]["title"])
   # context = {
   #    'news_list_2': news  # ключ - имя переменной в шаблоне, значение - данные
   # }
   # articles = Article.objects.all()
   # article = Article(
   #    title='Введение в Django ORM 2',
   #    content='Django ORM предоставляет мощный интерфейс для работы с базами данных...',
   #    # author=some_user,
   #    is_published=False
   # )
   # article.save()
   # articles_list = []
   # for article in Article.objects.all():
   #    articles_list.append({
   #       "title": article.title,
   #       "content": article.content
   #    })
   # context = {"news_list": articles_list}
   # published_articles = Article.objects.filter(
   #    is_published=True
   # ).order_by('-published_date')[:10]
   # articles = Article.objects.filter(is_published=True).prefetch_related('tags')
   # articles = Article.objects.raw('SELECT * FROM blog_article WHERE is_published = %s', [True])
   # return render(request, 'blog/home.html', {
   #    'articles': articles
   # })

   # articles = Article.objects.filter(
   #    is_published=True
   # ).select_related(
   #    'author'
   # ).prefetch_related(
   #    'tags'
   # ).order_by('-published_date')[:20]

   articles = Article.objects.published().with_author_and_tags().recent_first()[:20]

   return render(request, 'blog/home.html', {
      'articles': articles
   })


def article_detail(request, article_id):
   article = get_object_or_404(
      Article.objects.published().with_author_and_tags(),
      id=article_id
   )


   # Находим похожие статьи по тегам
   related_articles = Article.objects.published().filter(
      tags__in=article.tags.all()
   ).exclude(
      id=article.id
   ).annotate(
      same_tags=Count('id')
   ).order_by('-same_tags', '-published_date').with_author_and_tags()[:5]

   return render(request, 'blog/article_detail.html', {
      'article': article,
      'related_articles': related_articles
   })
