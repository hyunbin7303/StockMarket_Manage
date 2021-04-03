# sum_integers_args_2.py
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))




# concatenate_2.py
def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
def format_invocation(name='', args=(), kwargs=None, **kw):
    """Given a name, positional arguments, and keyword arguments, format
    a basic Python-style function call.
    >>> print(format_invocation('func', args=(1, 2), kwargs={'c': 3}))
    func(1, 2, c=3)
    >>> print(format_invocation('a_func', args=(1,)))
    a_func(1)
    >>> print(format_invocation('kw_func', kwargs=[('a', 1), ('b', 2)]))
    kw_func(a=1, b=2)
    """
    _repr = kw.pop('repr', bbrepr)
    if kw:
        raise TypeError('unexpected keyword args: %r' % ', '.join(kw.keys()))
    kwargs = kwargs or {}
    a_text = ', '.join([_repr(a) for a in args])
    if isinstance(kwargs, dict):
        kwarg_items = [(k, kwargs[k]) for k in sorted(kwargs)]
    else:
        kwarg_items = kwargs
    kw_text = ', '.join(['%s=%s' % (k, _repr(v)) for k, v in kwarg_items])

    all_args_text = a_text
    if all_args_text and kw_text:
        all_args_text += ', '
    all_args_text += kw_text

    return '%s(%s)' % (name, all_args_text)