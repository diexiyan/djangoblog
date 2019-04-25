# import datetime
# print(dir(datetime.datetime),)
# print(type(int(datetime.datetime.now().year.__str__()),))
# print(datetime.datetime.now().year.__str__())
from django.core.paginator import *
from collections.abc import Iterator
il = [i for i in range(100)]
# print(isinstance(il, Iterator))
p = Paginator(il, 10)
print(p.count, p.num_pages)
p.page(1).has_previous()