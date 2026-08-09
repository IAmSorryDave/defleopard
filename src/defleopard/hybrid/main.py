import functools
import inspect
from collections.abc import Callable


def hybrid_decorator(func: Callable) -> Callable:
    """Decorate a function so it can behave consistently as hybrid callables.

    The returned wrapper preserves the source signature and returns the
    resolved arguments namespace. When the callable is bound as a method,
    classmethod, or property, instance/class attributes override default
    parameter values when the argument was not explicitly provided.
    """

    signature = inspect.signature(func)
    parameters = signature.parameters

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound = signature.bind_partial(*args, **kwargs)
        explicit_parameters = set(bound.arguments)
        bound.apply_defaults()

        if args:
            subject = args[0]
            for name, parameter in parameters.items():
                if (
                    name not in explicit_parameters
                    and parameter.default is not inspect._empty
                ):
                    if hasattr(subject, name):
                        bound.arguments[name] = getattr(subject, name)

        return bound.arguments.copy()

    return wrapper
