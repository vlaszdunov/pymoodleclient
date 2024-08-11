from dataclasses import dataclass as __dataclass, asdict


@__dataclass
class ResponseObject:
    pass

    def todict(self) -> dict:
        return asdict(self)
