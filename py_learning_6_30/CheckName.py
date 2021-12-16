def get_formatted_name(first, last):
    return first.title() + ' ' + last.title()


def get_name():
    first = 'janis'
    last = 'joplin'
    full_name = get_formatted_name(first, last)
    return full_name
