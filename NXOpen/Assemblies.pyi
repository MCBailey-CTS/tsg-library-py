
from typing import Sequence, Tuple
from NXOpen import Builder, DisplayableObject, Matrix3x3, NXObjectAttributeType, Part, Point3d, UpdateOption


class Component(DisplayableObject):
    def GetChildren(self) -> Sequence[Component]: ...
    def GetPosition(self) -> Tuple[Point3d, Matrix3x3]: ...
    @property
    def DisplayName(self) -> str: ...
    @property
    def Name(self) -> str: ...
    def SetLayerOption(self, layer: int) -> None: ...
    @property
    def IsSuppressed(self) -> bool: ...
    @property
    def Parent(self) -> Component: ...
    def Suppress(self) -> None: ...
    def Unsuppress(self) -> None: ...
    @property
    def DirectOwner(self) -> ComponentAssembly: ...
    def HasInstanceUserAttribute(
        self, title: str, attribute_type: NXObjectAttributeType, index: int
    ) -> bool: ...
    @property
    def ReferenceSet(self) -> str: ...
    def SetInstanceUserAttribute(
        self, title: str, index: int, value: str, option: UpdateOption
    ) -> None: ...

class ComponentAssembly:
    @property
    def RootComponent(self) -> Component: ...
    def ReplaceReferenceSet(self, cmp: Component, name: str) -> None: ...
    def AddComponent(
        self,
        part_to_add: Part,
        reference_set_name: str,
        component_name: str,
        base_point: Point3d,
        orientation: Matrix3x3,
        layer: int,
    ) -> Component:
        """
        part_to_add	(string) The part that defines the new component
        reference_set_name	(string) The name of the reference set used to represent the new component
        component_name	(string) The name of the new component
        base_point	(NXOpen::Point3d ) Location of the new component
        orientation	(NXOpen::Matrix3x3 ) Orientation matrix for the new component, in column order.
        layer	(int) The layer to place the new component on -1 means use the original layers defined in the component. 0 means use the work layer. 1-256 means use the specified layer.

        """
        pass

class ReplaceComponentBuilder(Builder):
    @property
    def ComponentNameOption(self) -> int: ...
    @ComponentNameOption.setter
    def ComponentNameOption(self, value: int) -> None: ...
