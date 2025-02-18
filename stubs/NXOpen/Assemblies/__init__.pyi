from typing import List
from NXOpen import DisplayableObject

class Component(DisplayableObject):
    def GetChildren(self) -> List[Component]:
        pass
    @property
    def DisplayName(self) -> str:
        """Returns the DisplayName of the component object"""
        pass
    @property
    def Name(self) -> str:
        """Returns the name of the component object"""
        pass
