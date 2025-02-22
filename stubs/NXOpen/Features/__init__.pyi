from enum import Enum
from typing import Iterable

from NXOpen import Body, Builder, NXObject, SelectNXObjectList

class RemoveParametersBuilder(Builder):
    @property
    def Objects(self) -> SelectNXObjectList:
        pass

class Feature(NXObject):
    @property
    def Suppressed(self) -> bool:
        pass
    @Suppressed.setter
    def Suppressed(self, value: bool) -> None:
        pass
    def MakeCurrentFeature(self) -> None:
        pass

class FeatureCollection(Iterable[Feature]):
    def __iter__(self):  # type: ignore
        pass
    def GetParentFeatureOfBody(self, body: Body) -> Feature:
        pass
    def CreateRemoveParametersBuilder(self) -> RemoveParametersBuilder:
        pass

class BodyFeature(Feature):
    pass

class Block(BodyFeature):
    pass

class Cylinder(BodyFeature): ...

class FeatureBooleanType(Enum):
    Create: int
    EmbossNormalSide: int
    EmbossOppositeNormalSide: int
    Intersect: int
    Subtract: int
    Unite: int

class BooleanFeature(BodyFeature): ...
class ExtractFace(BodyFeature): ...
