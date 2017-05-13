# Use Whitespace around Keyword Argument Defaults with Type Hints

*From [lupinogle on GitHub](https://github.com/PyCQA/pylint/issues/238#issuecomment-216494517)*

When using type hints AND keyword function arguments AND setting a default, include whitespace around the ` = ` operator.

> When combining an argument annotation with a default value, use spaces around the = sign (but only for those arguments that have both an annotation and a default).

>        Yes:

>    def munge(sep: AnyStr = None): ...
    def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

>        No:

>    def munge(input: AnyStr=None): ...
    def munge(input: AnyStr, limit = 1000): ...

This had always been an open question between me and some coworkers, but we never cared enough to research the answer, and assumed it was the other way around until we updated `pylint`.

On a related note, this also clarified that you should not specify a type when it can be inferred from the default value (i.e. `limit=1000`)
