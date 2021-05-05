from django import template
register = template.Library()

"""
 Mapの取得用タグ
"""
@register.filter(name="get_value_by_key")
def get_value_by_key(value, key, default=""):
    if key in value:
        return value[key]
    else:
        return default