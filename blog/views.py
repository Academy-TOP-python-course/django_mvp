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
   articles = Article.objects.filter(is_published=True)
   return render(request, 'blog/home.html', {
      'articles': articles
   })

