from django import template
import nepali_datetime

register = template.Library()


@register.filter
def dict_get(dictionary, key):
    """Get value from dictionary using key"""
    if isinstance(dictionary, dict):
        return dictionary.get(key, [])
    return []

@register.filter
def nepali_date(date_string):
    """
    Formats a Nepali date string (e.g., '2082-07-28') to '28 Kartik, 2082'.
    """
    try:
        # Assuming date_string is in 'YYYY-MM-DD' format
        np_date = nepali_datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return np_date.strftime('%d %B, %Y')
    except (ValueError, TypeError):
        return date_string # Return original string if parsing fails

@register.filter
def split_nepali_date(date_string):
    """
    Splits a formatted Nepali date string into its components.
    e.g., '28 Kartik, 2082' -> {'day': '28', 'month': 'Kartik,', 'year': '2082'}
    """
    formatted_date = nepali_date(date_string)
    parts = formatted_date.split(' ')
    if len(parts) == 3:
        return {'day': parts[0], 'month': parts[1].replace(',', ''), 'year': parts[2]}
    return {'day': '', 'month': '', 'year': ''}
