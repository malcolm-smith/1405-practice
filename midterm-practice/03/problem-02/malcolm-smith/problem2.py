def removehtml(html):
    flag = False
    out = ''
    for i in html:
        if i == '<': flag = True
        elif i == '>': flag = False
        elif not flag:
            out = out + i
    return out

print(removehtml('<html><head><title>Page Title<title><head><html>'))
print(removehtml('<a href=”p1”>Link 1</a><a href=”p2”>Link 2</a>'))
print(removehtml('<p>Click <a href=”here.html”>here</a></p>'))
