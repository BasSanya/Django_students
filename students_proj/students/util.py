from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(objects, size, request, context, var_name="object_list"):
    """Paginate objects provided by view.

    This function takes:
    * list of elements;
    * number of objects per page;
    * request object to get url parameters from;
    * context to set new variables into;
    * var_name - variable name for list of objects.
    It returns updated context object.
    """
    paginator = Paginator(objects, size)

    page = request.GET.get('page', '1')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['start_index'] = object_list.start_index()
    context['paginator'] = paginator

    return context


def get_groups(request):
    from .models import Groups

    cur_group = get_current_group(request)

    groups = []
    for group in Groups.objects.all().order_by('title'):
        groups.append({
            'id': group.id,
            'title': group.title,
            'leader': group.leader and f'{group.leader.first_name} {group.leader.last_name}' or None,
            'selected': cur_group and cur_group.id == group.id or False
        })
    return groups

def get_current_group(request):
    pk = request.COOKIES.get('current_group')

    if pk:
        from .models import Groups
        try:
            group = Groups.objects.get(pk=int(pk))
        except Groups.DoesNotExist:
            return None
        else:
            return group
    else:
        return None
