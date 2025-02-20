from typing import List, Optional, Sequence, Union
from NXOpen import DisplayableObject, NXObject, Part

class Component(DisplayableObject):
    def GetChildren(self) -> Sequence[Component]:
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
    @property
    def Parent(self) -> Component: ...

class ComponentAssembly:
    @property
    def RootComponent(self) -> Component:
        pass
