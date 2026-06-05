from django.shortcuts import render

from django.http import HttpResponse

def home(request):
   html_content = """
   <html>
       <head>
           <title>Мой новостной блог</title>
       </head>
       <body>
           <h1>Добро пожаловать в мой блог!</h1>
           <p>Здесь будут новости и статьи.</p>
       </body>
   </html>
   """
   return HttpResponse(html_content)
