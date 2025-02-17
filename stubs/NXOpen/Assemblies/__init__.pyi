from typing import Optional
from NXOpen import NXObject


class Component:
    # DeleteInstanceUserAttribute
    # DeleteInstanceUserAttributes
    # DirectOwner
    @property
    def DisplayName(self)->str:
        pass
    # FindOccurrence
    # GetChildren
    # GetConstraints
    # GetDegreesOfFreedom
    # GetInstanceUserAttribute
    # GetInstanceUserAttributeAsString
    # GetInstanceUserAttributes
    # GetInstanceUserAttributesAsStrings
    def GetPosition(self)->tuple[Point3d, Matrix3x3]:
        pass
    # HasInstanceUserAttribute
    # IsFixed
    # IsPositioningIsolated
    # IsSuppressed
    # Parent
    # Prototype
    # RedisplayObject
    # ReferenceSet
    # SetInstanceUserAttribute
    # SetName
    # Suppress
    # SuppressingArrangement
    # Unsuppress

# 888-832-4540

class ComponentAssembly(NXObject):
    # AddComponent
    # AddComponents
    # MapComponentsFromSubassembly
    # MoveComponent
    # ReplaceReferenceSet
    # ReplaceReferenceSetInOwners
    @property
    def RootComponent(self)->Optional[Component|None]:
        pass
    # SubstituteComponent
    # SubstitutionMode
    pass