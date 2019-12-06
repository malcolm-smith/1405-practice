def reverse(some_string):
    if len(some_string) == 1:
        return some_string
    else:
        return reverse(some_string[1:]) + some_string[0]

print(reverse('hello!'))
