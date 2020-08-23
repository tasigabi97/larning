from typing import List, Union
from pydantic import validate_arguments


@validate_arguments
def concatenate_with_separation(strings: List[str], separator: str) -> str:
    return "".join(s if i == 0 else separator + s for i, s in enumerate(strings))
