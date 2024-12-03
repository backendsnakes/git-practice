from dataclasses import dataclass


@dataclass
class Example:
    id: int
    name: str
    description: str

    def __str__(self):
        return f"Example(id={self.id}, name={self.name}, description={self.description})"

    def __repr__(self):
        return str(self)