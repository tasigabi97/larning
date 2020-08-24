from typing import List, Union, Iterable, Tuple,Sequence
from pydantic import validate_arguments


@validate_arguments
def concatenate_with_separation(strings: Sequence[str], separator: str) -> str:
    return "".join(s if i == 0 else separator + s for i, s in enumerate(strings))
