
from enum import Enum
from typing import Iterable, Sequence

from NXOpen import Body, Builder, Edge, Face, NXObject, SelectNXObjectList


class RemoveParametersBuilder(Builder):
    @property
    def Objects(self) -> SelectNXObjectList:
        pass

class Feature(NXObject):
    # ('BooleanType', <class 'NXOpen.Features.FeatureBooleanType'>)
    # ('DiagnosticType', <class 'NXOpen.Features.FeatureDiagnosticType'>)
    # ('__new__', <built-in method __new__ of type object at 0x00007FFFCDD80650>)
    # ('GetExpressions', <method 'GetExpressions' of 'NXOpen.Features.Feature' objects>)
    # ('GetBodies', <method 'GetBodies' of 'NXOpen.Features.Feature' objects>)
    # ('GetFaces', <method 'GetFaces' of 'NXOpen.Features.Feature' objects>)
    # ('GetEdges', <method 'GetEdges' of 'NXOpen.Features.Feature' objects>)
    # ('GetParents', <method 'GetParents' of 'NXOpen.Features.Feature' objects>)
    # ('GetChildren', <method 'GetChildren' of 'NXOpen.Features.Feature' objects>)
    # ('GetAllChildren', <method 'GetAllChildren' of 'NXOpen.Features.Feature' objects>)
    # ('Highlight', <method 'Highlight' of 'NXOpen.Features.Feature' objects>)
    # ('Unhighlight', <method 'Unhighlight' of 'NXOpen.Features.Feature' objects>)
    # ('MakeCurrentFeature', <method 'MakeCurrentFeature' of 'NXOpen.Features.Feature' objects>)
    # ('ShowBody', <method 'ShowBody' of 'NXOpen.Features.Feature' objects>)
    # ('ShowParents', <method 'ShowParents' of 'NXOpen.Features.Feature' objects>)
    # ('HideBody', <method 'HideBody' of 'NXOpen.Features.Feature' objects>)
    # ('HideParents', <method 'HideParents' of 'NXOpen.Features.Feature' objects>)
    # ('Suppress', <method 'Suppress' of 'NXOpen.Features.Feature' objects>)
    # ('Unsuppress', <method 'Unsuppress' of 'NXOpen.Features.Feature' objects>)
    # ('GetEntities', <method 'GetEntities' of 'NXOpen.Features.Feature' objects>)
    # ('GetFeatureErrorMessages', <method 'GetFeatureErrorMessages' of 'NXOpen.Features.Feature' objects>)
    # ('GetFeatureInformationalMessages', <method 'GetFeatureInformationalMessages' of 'NXOpen.Features.Feature' objects>)
    # ('DeleteInformationalAlerts', <method 'DeleteInformationalAlerts' of 'NXOpen.Features.Feature' objects>)
    # ('DeleteWarningAlerts', <method 'DeleteWarningAlerts' of 'NXOpen.Features.Feature' objects>)
    # ('GetFeatureWarningMessages', <method 'GetFeatureWarningMessages' of 'NXOpen.Features.Feature' objects>)
    # ('GetFeatureClueMessages', <method 'GetFeatureClueMessages' of 'NXOpen.Features.Feature' objects>)
    # ('DeleteClueAlerts', <method 'DeleteClueAlerts' of 'NXOpen.Features.Feature' objects>)
    # ('GetFeatureClueHintMessages', <method 'GetFeatureClueHintMessages' of 'NXOpen.Features.Feature' objects>)
    # ('GetFeatureHintMessages', <method 'GetFeatureHintMessages' of 'NXOpen.Features.Feature' objects>)
    # ('DeleteHintAlerts', <method 'DeleteHintAlerts' of 'NXOpen.Features.Feature' objects>)
    # ('MakeSketchInternal', <method 'MakeSketchInternal' of 'NXOpen.Features.Feature' objects>)
    # ('MakeSketchExternal', <method 'MakeSketchExternal' of 'NXOpen.Features.Feature' objects>)
    # ('RemoveForEdit', <method 'RemoveForEdit' of 'NXOpen.Features.Feature' objects>)
    # ('RemoveParameters', <method 'RemoveParameters' of 'NXOpen.Features.Feature' objects>)
    # ('ShowDimensions', <method 'ShowDimensions' of 'NXOpen.Features.Feature' objects>)
    # ('GetFeatureName', <method 'GetFeatureName' of 'NXOpen.Features.Feature' objects>)
    # ('GetSections', <method 'GetSections' of 'NXOpen.Features.Feature' objects>)
    # ('SetGroupActive', <method 'SetGroupActive' of 'NXOpen.Features.Feature' objects>)
    # ('LogDiagnostic', <method 'LogDiagnostic' of 'NXOpen.Features.Feature' objects>)
    # ('ChangeBooleanType', <method 'ChangeBooleanType' of 'NXOpen.Features.Feature' objects>)
    # ('GetFeatureColor', <method 'GetFeatureColor' of 'NXOpen.Features.Feature' objects>)
    # ('BreakWaveLink', <method 'BreakWaveLink' of 'NXOpen.Features.Feature' objects>)
    # ('LoadParentPart', <method 'LoadParentPart' of 'NXOpen.Features.Feature' objects>)
    # ('IsBrowsableFeature', <method 'IsBrowsableFeature' of 'NXOpen.Features.Feature' objects>)
    # ('AlgorithmVersion', <attribute 'AlgorithmVersion' of 'NXOpen.Features.Feature' objects>)
    # ('ContainerFeature', <attribute 'ContainerFeature' of 'NXOpen.Features.Feature' objects>)
    # ('FeatureType', <attribute 'FeatureType' of 'NXOpen.Features.Feature' objects>)
    # ('IsContainedFeature', <attribute 'IsContainedFeature' of 'NXOpen.Features.Feature' objects>)
    # ('IsInternal', <attribute 'IsInternal' of 'NXOpen.Features.Feature' objects>)
    # ('Location', <attribute 'Location' of 'NXOpen.Features.Feature' objects>)
    # ('Suppressed', <attribute 'Suppressed' of 'NXOpen.Features.Feature' objects>)
    # ('Timestamp', <attribute 'Timestamp' of 'NXOpen.Features.Feature' objects>)
    @property
    def FeatureType(self) -> str: ...
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
    def GetBodies(self) -> Sequence[Body]: ...
    def GetEdges(self) -> Sequence[Edge]: ...
    def GetFaces(self) -> Sequence[Face]: ...

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
