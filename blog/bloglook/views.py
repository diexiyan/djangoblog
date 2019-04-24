from django.shortcuts import render,reverse
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
import datetime


def index(request, tid=None, type=None):
    """首页"""
    # 所有文章
    arilist = Article.objects.all()
    if type !="":
        # print('***************************************************')
        if type == '1':
            # print('...................根据分类...........................')
            arilist = Article.objects.all().filter(atype_id=int(tid))
        elif type == '2':
            # print('...................根据标签...........................')
            arilist = Article.objects.all().filter(atag_id=int(tid))
        elif type == '3':
            nowyear = datetime.datetime.now().year
            stra = nowyear.__str__()
            inta = int(stra)
            # nowyear.
            # print('...................根据时间............................')
            arilist = Article.objects.all().filter(atime__year=inta).filter(atime__month=int(tid))
    # print('文章信息列表------------------->', arilist)
    # 最新文章
    # lastestlist = arilist.order_by('-atime').all()
    lastestlist = Article.objects.all().order_by('-atime').all()
    # 归档
    time = datetime.datetime.now()
    # print('最新文章列表------------------->', lastestlist)
    # 分类
    typelist = ArticleType.objects.all()
    # print('归类列表------------------->', typelist)
    # 标签云
    taglist = Tag.objects.all()
    # print('标签列表------------------->', taglist)
    return render(request, 'bloglook/index.html',
                  {'arilist': arilist,'typelist': typelist,
                   'taglist': taglist,'lastestlist': lastestlist,
                   'time': time,
                   })


def show(request, aid):
    """
    展示文章
    :param request:
    :param aid: 文章id
    :return:
    """
    # 所有文章
    arilist = Article.objects.all()
    # 最新文章
    # 归档
    time = datetime.datetime.now()
    # lastestlist = arilist.order_by('-atime').all()
    lastestlist = Article.objects.all().order_by('-atime').all()
    # 分类
    typelist = ArticleType.objects.all()
    # 标签云
    taglist = Tag.objects.all()
    ariinfo = Article.objects.get(pk=int(aid))

    # 阅读数加1
    ariinfo.acou += 1
    ariinfo.save()
    # 文章内容
    conlist = ariinfo.articlecontent_set.all()
    # 一级标题
    firsttag = []
    for c in conlist:
        # 判断是否为标题
        if c.ctag.id == 1:
            firsttag.append(c.ctxt)
    # 评论
    comlist = ariinfo.comment_set.all()
    return render(request, 'bloglook/single.html',
                  {'ariinfo': ariinfo, 'conlist': conlist, 'firsttag': firsttag,
                   'comlist': comlist, 'time': time,
                   'arilist': arilist, 'typelist': typelist,
                   'taglist': taglist, 'lastestlist': lastestlist,
                   })


def type(request, typeid):
    """
    根据分类查询所有文章
    :param request:
    :param typeid: 分类标识
    :return:
    """
    return HttpResponseRedirect('/blog/'+typeid+'/1')


def tag(request, tagid):
    return HttpResponseRedirect('/blog/'+tagid+'/1')


def pubcom(request, aid):
    com = Comment()
    com.cari = Article.objects.get(pk=int(aid))
    com.cpeo = request.POST['name']
    com.cemail = request.POST['email']
    com.curl = request.POST['url']
    com.ctext = request.POST['comment']
    com.save()
    return HttpResponseRedirect(reverse('bloglook:show', args=[aid, ]))


def time(request, month):
    """
    根据时间分类
    :param request:
    :param month: 当年月份
    :return:
    """
    return HttpResponseRedirect('/blog/'+month+'/3')
