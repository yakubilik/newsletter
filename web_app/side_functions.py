from .models import News, create_database
import requests
import json
from sqlalchemy import func
from .models import create_database



def fresh_news():
    res = requests.get("https://newsapi.org/v2/everything?q=Apple&from=2022-12-17&sortBy=popularity&apiKey=3dd4e4368f9b48178d50ba760d38be19")
    articles = res.content.decode("utf-8")
    articles = json.loads(articles)
    articles = articles.get("articles")
    session = create_database()
    news = News.session.query(News).all()
    if len(news)>1:
        id = News.session.query(func.max(News.id)).scalar()+1
    else:
        id = 1
    obj_list =[]
    for item in articles:
        id += 1
        title =item.get("title")
        content = item.get("content")
        image= item.get("urlToImage")
        obj = News(id ,title ,content ,image)
        obj_list.append(obj)

    session.add_all(obj_list)
    session.commit()
