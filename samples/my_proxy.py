
def get_password():
    with open("I:\\neotunnel.txt", "rt") as fd:
        content = fd.read()
    lines = content.split()
    the_password = lines[1].strip()
    return the_password


def get_username():
    with open("I:\\neotunnel.txt", "rt") as fd:
        content = fd.read()
    lines = content.split()
    the_username = lines[0].strip()
    return the_username
