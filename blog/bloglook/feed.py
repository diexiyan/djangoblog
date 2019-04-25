from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import Article


class AriFeed(Feed):
    title = '文章'
    link = '/'
    # description = '摘要'

    def items(self):
        print('-------------------------', '’文章')
        return Article.objects.all()

    def item_title(self, item):
        print('-------------------------', '’atitle')

        return item.atitle

    def item_link(self, item):
        print('-------------------------', '’item_link')

        return reverse('bloglook:show', args=(item.id,))

    # def item_description(self, item):
    #     print('-------------------------', '’item_description')
    #     print('2222222222222222222222', item.articlecontent_set.all())
    #
    #     return item.articlecontent_set.all()[0].ctxt
