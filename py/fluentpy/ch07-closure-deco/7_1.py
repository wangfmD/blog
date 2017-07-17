def deco(func):
    """deco: Docstring for deco.

    """

    def inner():
        print('running inner')

    return inner


@deco
def target():
    """
    :returns: target

    """
    print('running target()')


# target()
print target.__doc__
print deco.__doc__
