from django.core.management.base import BaseCommand
from ...models import Topics
from django.utils import timezone
from django.conf import settings
from newsapi import NewsApiClient
import requests
import json
import re


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 最初にモデル内のデータを初期化
        Topics.objects.all().delete()
        c_list = ["kr", "us", "gb", "it", "fr", "jp", "de"]
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        for name in c_list:
            if name == "jp":
                context = newsapi.get_everything(q="コロナ", page_size=100, page=1, sort_by="popularity")
                for i in context["articles"]:
                    try:
                        if i["description"] is not None:
                            Topics.objects.create(title=i["title"], published_date=i["publishedAt"], description=i["description"],
                                                  author=i["author"], image_url=i["urlToImage"], topic_url=i["url"],
                                                  domain_tags=name,sentimental=sentimentals(i["title"]))
                    except json.decoder.JSONDecodeError:
                        pass
                context = newsapi.get_top_headlines(q="コロナ", country=name, page_size=100)
                for i in context["articles"]:
                    try:
                        if i["description"] is not None:
                            Topics.objects.create(title=i["title"], published_date=i["publishedAt"], description=i["description"],
                                                  author=i["author"], image_url=i["urlToImage"], topic_url=i["url"],
                                                  top_news="top", domain_tags=name,sentimental=sentimentals(i["title"]))
                    except json.decoder.JSONDecodeError:
                        pass
            elif name == "kr":
                  context = newsapi.get_everything(q=translate("コロナウイルス", "ja", name), page_size=100, page=1,)
                  for i in context["articles"]:
                      try:
                          if i["description"] is not None:
                             Topics.objects.create(title=translate(i["title"], name, "ja"),
                                                  published_date=i["publishedAt"],
                                                  description=translate(i["description"], name, "ja"),
                                                  author=i["author"],
                                                  image_url=i["urlToImage"], topic_url=i["url"], domain_tags=name,sentimental=sentimentals(i["title"]))
                      except:
                          pass

                  context = newsapi.get_top_headlines(q=translate("コロナウイルス", "ja", name), country=name, page_size=100)
                  for i in context["articles"]:
                      try:
                          if i["description"] is not None:
                             Topics.objects.create(title=translate(i["title"], name, "ja"),
                                                  published_date=i["publishedAt"],
                                                  description=translate(i["description"], name, "ja"),
                                                  author=i["author"], image_url=i["urlToImage"], topic_url=i["url"],
                                                  top_news="top", domain_tags=name,sentimental=sentimentals(i["title"]) )
                      except:
                          pass
            elif name == "gb":
                context = newsapi.get_everything(q=translate("コロナウイルス", "ja", name), page_size=100, page=1, domains="bbc.co.uk",)
                for i in context["articles"]:
                    try:
                        if i["description"] is not None:
                            Topics.objects.create(title=translate(i["title"], name, "ja"),
                                                  published_date=i["publishedAt"],
                                                  description=translate(i["description"], name, "ja"),
                                                  author=i["author"],
                                                  image_url=i["urlToImage"], topic_url=i["url"], domain_tags=name,sentimental=sentimentals(i["title"]))
                    except json.decoder.JSONDecodeError:
                        pass

                context = newsapi.get_top_headlines(q=translate("コロナウイルス", "ja", name), country=name, page_size=100)
                for i in context["articles"]:
                    try:
                        if i["description"] is not None:
                            Topics.objects.create(title=translate(i["title"], name, "ja"),
                                                  published_date=i["publishedAt"],
                                                  description=translate(i["description"], name, "ja"),
                                                  author=i["author"], image_url=i["urlToImage"], topic_url=i["url"],
                                                  top_news="top", domain_tags=name,sentimental=sentimentals(i["title"]) )
                    except json.decoder.JSONDecodeError:
                        pass

            else:
                if name == "us":
                    context = newsapi.get_everything(q=translate("コロナウイルス", "ja", name), page_size=100, page=1,
                                                     language='en')
                else:
                    context = newsapi.get_everything(q=translate("コロナウイルス", "ja", name), page_size=100, page=1,
                                                     language=name)
                for i in context["articles"]:
                    try:
                        if i["description"]or i["title"] is not None:
                            Topics.objects.create(title=translate(i["title"], name, "ja"), published_date=i["publishedAt"],
                                                  description=translate(i["description"], name, "ja"), author=i["author"],
                                                  image_url=i["urlToImage"], topic_url=i["url"], domain_tags=name,sentimental=sentimentals(i["title"]))
                    except:
                        pass
                context = newsapi.get_top_headlines(q=translate("コロナウイルス", "ja", name), country=name, page_size=100)
                for i in context["articles"]:
                    try:
                        if i["description"] or i["title"] is not None:
                            Topics.objects.create(title=translate(i["title"], name, "ja"), published_date=i["publishedAt"],
                                                  description=translate(i["description"], name, "ja"),
                                                  author=i["author"], image_url=i["urlToImage"], topic_url=i["url"],
                                                  top_news="top", domain_tags=name,sentimental=sentimentals(i["title"]) )
                    except:
                        pass

        print('test command')


def translate(sentence, source_country, country_name):
    c_name = country_name
    s_name = source_country
    new_sentence = re.sub(r"&.*?;", "", sentence)
    api = "https://script.google.com/macros/s/AKfycbxy9rc0bI6I4c8UUhFYUeuJT74Vx4pOaSq1BJ75GLKnoevXGnjh/exec?text={sentence}&source={source_name}&target={country_name}"

    if c_name == "kr":
        c_name = "ko"
    elif s_name == "kr":
        s_name = "ko"
    elif c_name == "gb" or c_name == "us":
        c_name = "en"
    elif s_name == "gb" or s_name == "us":
        s_name = "en"
    elif c_name == "be":
        c_name = "nl"
    elif s_name == "be":
        s_name = "nl"
    else:
        c_name = country_name
        s_name = source_country

    url = api.format(sentence=new_sentence, source_name=s_name, country_name=c_name,)
    r = requests.get(url)
    data = json.loads(r.text)
    if data["code"] == 200:
        return data["text"]

def sentimentals(text):
    key = "AIzaSyAKBOrRXBuMCNoujlH--xKWJR4XKe6RYrA"

    # APIのURL
    url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=' + key

    # 基本情報の設定 JAをENにすれば英語のテキストを解析可能
    header = {'Content-Type': 'application/json'}
    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "JA",
            "content": text
        },
        "encodingType": "UTF8"
    }

    # json形式で結果を受け取る。
    response = requests.post(url, headers=header, json=body).json()

    return response["documentSentiment"]["score"]
