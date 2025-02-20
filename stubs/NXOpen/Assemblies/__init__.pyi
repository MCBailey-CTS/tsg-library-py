from typing import List, Optional, Union
from NXOpen import DisplayableObject, NXObject, Part

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
    def SetLayerOption(self, layer: int) -> None: ...
    @property
    def IsSuppressed(self) -> bool: ...

class ComponentAssembly:
    @property
    def RootComponent(self) -> Optional[Component]:
        pass
