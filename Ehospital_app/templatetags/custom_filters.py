# custom_filters.py

from django import template

register = template.Library()

@register.filter
def mask_account_number(account_number):
    # Convert account_number to string if it's an integer
    account_number = str(account_number)

    # Check if the account number is at least 6 characters long
    if len(account_number) >= 6:
        return account_number[0] + '*' * (len(account_number) - 5) + account_number[-4:]
    else:
        # If the account number is too short to mask, return it unchanged
        return account_number
@register.filter
def mask_phone_number(phone_number):
    # Convert phone_number to string if it's an integer
    phone_number = str(phone_number)

    # Check if the phone_number is at least 6 characters long
    if len(phone_number) >= 6:
        if phone_number[0]=='0':
            return phone_number[:4] + '*' * (len(phone_number) - 6) + phone_number[-2:]
        else:
            return phone_number[:7] + '*' * (len(phone_number) - 9) + phone_number[-2:]
    else:
        # If the phone_number is too short to mask, return it unchanged
        return phone_number

from django import template

register = template.Library()

@register.filter
def split_into_columns(value, num_columns):
    """
    Split a list into `num_columns` columns.
    """
    length = len(value)
    return [value[i::num_columns] for i in range(num_columns)]
