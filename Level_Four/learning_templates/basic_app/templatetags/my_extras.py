from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
	return value.replace(arg,'')

# 下面的是用了register，另外一种就是用decorator, 见第五行的做法
# register.filter('cut',cut)
