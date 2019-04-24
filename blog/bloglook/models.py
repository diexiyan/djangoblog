from django.db import models
from django.forms import ModelForm

# Create your models here.
class ArticleTag(models.Model):
    """文章的具体内容"""
    # id 自增长
    tatype = models.CharField(max_length=20, default='标题')

    def __str__(self):
        return self.tatype


class ArticleType(models.Model):
    """分类"""
    tname = models.CharField(max_length=20, default='python')
    # tnum 后台管理生成文章，无法使文章数加一

    def __str__(self):
        return self.tname


class Tag(models.Model):
    """标签"""
    tname = models.CharField(max_length=20, default='python')

    def __str__(self):
        return self.tname


class Article(models.Model):
    """文章信息"""
    awri = models.CharField(max_length=20, default='bh')
    # 设置修改时间为发表时间
    atime = models.DateTimeField(auto_now_add=True)
    # 分类
    atype = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
    # 标签
    atag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # 阅读次数
    acou = models.IntegerField(default='0')
    # 题目
    atitle = models.CharField(max_length=50)

    def __str__(self):
        return self.atitle


class ArticleContent(models.Model):
    """文章内容"""
    # 内容
    ctxt = models.TextField()
    # 标签
    ctag = models.ForeignKey(ArticleTag, on_delete=models.CASCADE)
    # 绑定文章
    cari = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.ctxt


class Comment(models.Model):
    """评论"""
    cpeo = models.CharField(max_length=20, default='yiyi')
    ctime = models.DateTimeField(auto_now=True)
    # 评论内容
    ctext = models.CharField(max_length=500)
    # 绑定文章
    cari = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 邮箱
    # cemail = models.EmailField()
    cemail = models.CharField(max_length=20, default='3020498522@qq.com', null=True, blank=True)
    # 网址
    # curl = models.URLField()
    curl = models.CharField(max_length=20, default='127.0.0.1...', null=True, blank=True)

    def __str__(self):
        return self.ctext











