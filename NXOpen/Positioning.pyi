from typing import Iterable

from NXOpen import DisplayableObject

class DisplayedConstraintCollection(Iterable[DisplayedConstraint]):
    def __iter__(self):  # type: ignore
        pass

class DisplayedConstraint(DisplayableObject):
    def GetConstraint(self) -> None:
        pass
    def GetConstraintPart(self) -> None:
        pass
    def GetContextComponent(self) -> None:
        pass
