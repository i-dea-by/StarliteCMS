
from dataclasses import dataclass
from os import PathLike


@dataclass(slots=True)
class Application:
    name: str
    # context_processor: str
    templates_dir: PathLike | None = None


applications_list: list[Application]
