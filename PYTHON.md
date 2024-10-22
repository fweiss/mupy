# Python notes

## Operator overloading
se operator overloading to provide a concise DSL for the score.

These operators can be overloaded:
> Associativity is left-to-right except as noted.

| operator | type | magic | precedence |
|:---: |--- |--- |---
| ~ | unary | __invert__ | 5 right-to-left
| ** | binary | __pow__ | 4 
| - | unary | __neg__ | 5 right-to-left
| + | unary | __pos__ | 5 right-to-left
| ~ | unary | __invert__ | 5 right-to-left
| * | binary | __mul__ | 6
| / | binary | __truediv__ | 6
| // | binary | __floordiv__ | 6
| % | binary | __mod__ | 6
| + | binary | ``__add__`` | 7
| - | binary | __sub__ | 7
| >> | binary | __rshift__ | 8
| << | binary | __lshift__ | 8
| & | binary | __and__ | 9
| ^ | binary | __xor__ | 10
| \| | binary | __or__ | 11

