# utils.py (hoặc helpers.py)
def format_currency(value):
    value = float(value)
    value = value / 1000
    formatted_value = "{:,.3f}".format(value)
    return formatted_value + " VND"
