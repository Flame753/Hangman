def get_percentage(number, r=None):
    percent = round(number * 100, r)
    string = "{}%".format(percent)
    return string
