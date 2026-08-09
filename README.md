# defleopard

Tools for Hybrid Programming.

## Features

- `defleopard.hybrid.hybrid_decorator`: decorate a callable so it works as a plain function, instance method, class method, static method, or property.
- When used on bound methods and properties, instance/class attributes override default argument values if the argument is not explicitly provided.

## Usage

```python
from defleopard.hybrid import hybrid_decorator

@hybrid_decorator
def example(*args, x=1, y='hello', **kwargs):
    return locals().copy()
```

The decorated callable can be attached to classes and properties while preserving hybrid behavior.