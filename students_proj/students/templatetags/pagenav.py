from django import template
from django.template.loader import get_template

register = template.Library()


@register.inclusion_tag('students/pagination.html')
def pagenav(object_list, is_paginated, paginator):
    return {
        'object_list': object_list,
        'is_paginated': is_paginated,
        'paginator': paginator
    }

# @register.simple_tag
# def pagenav(*args, **kwargs):
#     t = get_template('students/pagination.html')
#     return t.render({
#         'object_list': kwargs['object_list'],
#         'is_paginated': kwargs['is_paginated'],
#         'paginator': kwargs['paginator']
#     })

#
# def pagenav(parser, token):
#     try:
#         tag_name, object_list, is_paginated, paginator = token.split_contents()
#     except ValueError:
#         raise template.TemplateSyntaxError(f'{token.contents.split()[0]} tag requires 3 arguments')
#
#     return PageNavNode(object_list, is_paginated, paginator)
#
#
# class PageNavNode(template.Node):
#
#     def __init__(self, object_list, is_paginated, paginator):
#         self.object_list = template.Variable(object_list)
#         self.is_paginated = template.Variable(is_paginated)
#         self.paginator = template.Variable(paginator)
#
#     def render(self, context):
#         t = template.loader.get_template('students/pagination.html')
#         return t.render(template.Context({
#             'object_list': self.object_list.resolve(context),
#             'is_paginated': self.is_paginated.resolve(context),
#             'paginator': self.paginator.resolve(context)
#         }))
