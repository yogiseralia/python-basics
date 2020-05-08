def banner(message, border = '-'):
    """default args must be after normal arguments,else syntax error occurs
       and

    >>> banner(border ="*","hello")
      File "<stdin>", line 1
    SyntaxError: positional argument follows keyword argument

    >>> banner(border ="*",message="dsjfldskf")
    *********
    dsjfldskf
    *********

    """
    line = border * len(message)
    print(line)
    print(message)
    print(line)