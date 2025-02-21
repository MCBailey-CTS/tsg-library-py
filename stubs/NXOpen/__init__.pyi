"""
NXOpen module mcb
"""

import enum
from typing import Any, Iterable, List, Optional, Self, Sequence, Tuple, Union

import NXOpen
from NXOpen.Annotations import BaseNote
import NXOpen.Assemblies
from NXOpen.Drawings import DrawingSheetCollection
from NXOpen.Features import FeatureCollection
from NXOpen.Layer import LayerManager
from NXOpen.Positioning import DisplayedConstraintCollection
from NXOpen.Assemblies import ComponentAssembly as ComponentAssembly_
from NXOpen.Assemblies import Component as Component_

# ApparentChainingRule
# ApparentChainingRuleSelection
# ApparentChainingRuleSelectionMemberType
# ApparentChainingRuleType
# ApparentChainingRuleTypeMemberType
# Arc
# ArcCollection

# Assemblies
# AssembliesUtils

# Axis
# AxisCollection
# AxisOrientation
# AxisOrientationMemberType
# AxisTypes
# AxisTypesMemberType

# BasePartUnits

# Body
# BodyCollection
# BodyDumbRule

# BodyFeatureRule
# BodyGroupRule
# BodyList

class NXObjectAttributeType(enum.Enum):
    Any:int
    Boolean:int
    Integer:int
    Invalid:int
    Null:int
    Real:int
    Reference:int
    String:int
    Time:int

class Update:
    def DoUpdate(self, mark: int) -> None:...
    def AddObjectsToDeleteList(self, objects: Sequence[TaggedObject]) -> None:...
    def ClearDeleteList(self) -> None:...
    class Option(enum.Enum):
        Later: int
        Now: int

class Builder(TaggedObject):
    def Commit(self) -> Optional[NXObject]:
        pass
    def Destroy(self) -> None:
        pass

class PartCollectionSdpsStatus:
    pass

# ClipboardOperationsManager

class Conic(Curve): ...
class CoordinateSystem(SmartObject): ...

# CoordinateSystemCollection

class SelectNXObjectList(TaggedObject):
    def Add(self, objects: Union[NXObject, List[NXObject]]) -> bool: ...
    @property
    def Size(self) -> int: ...

class Curve(DisplayableObject):
    def GetLength(self) -> float: ...
    def IsReference(self) -> bool: ...

# CurveChainRule
# CurveCollection
# CurveDumbRule
# CurveFeatureChainRule
# CurveFeatureRule
# CurveFeatureTangentRule

# CurveTangentRule

# DatumAxis
# DatumCollection

# DatumPlane

# DexBuilder
# DexManager

class DisplayableObject(NXObject):
    def Blank(self) -> None: ...
    @property
    def Color(self) -> int: ...
    @Color.setter
    def Color(self, color: int) -> None: ...
    def Highlight(self) -> None: ...
    @property
    def IsBlanked(self) -> bool: ...
    @property
    def Layer(self) -> int: ...
    @Layer.setter
    def Layer(self, layer: int) -> None: ...
    def RedisplayObject(self) -> None: ...
    def Unhighlight(self) -> None: ...

class Direction(SmartObject):
    @property
    def Origin(Self) -> Point3d:
        pass
    @property
    def Vector(self) -> Vector3d:
        pass

class DirectionCollection(Iterable[Direction]):
    def __iter__(self): ...  # type: ignore

class Point(SmartObject): ...

class PointCollection(Iterable[Point]):
    def __iter__(self): ...  # type: ignore

class DisplayManager:
    def NewDisplayModification(self) -> DisplayModification:
        pass

class SelectionResponse(enum.Enum):
    Back: int
    Cancel: int
    ObjectSelected: int
    ObjectSelectedByName: int
    Ok: int

class DisplayModification:
    ApplyToAllFaces: bool
    ApplyToOwningParts = False
    NewColor: int
    NewLayer: int
    def Apply(self, nxobjects: List[NXObject]) -> None:
        pass
    def Dispose(self) -> None:
        pass

class SelectionSelectionScope(enum.Enum):
    AnyInAssembly: int
    UseDefault: int
    ValueOf: int
    WorkPart: int
    WorkPartAndOccurrence: int
    WorkPartAndWorkPartOccurrence: int

class SelectionSelectionAction(enum.Enum):
    AllAndDisableSpecific: int
    ClearAndEnableSpecific: int
    DisableSpecific: int
    EnableAll: int
    EnableSpecific: int

# DisplayModification
# DisplayPartOption
# DisplayPartOptionMemberType

# DraftingManager
# DxfdwgCreator

# Edge

# Ellipse
# EllipseCollection

# Expression
# ExpressionCollection

# Face

# Hyperbola

# JournalManager

class Line(Curve):
    @property
    def StartPoint(self) -> Point3d: ...
    @property
    def EndPoint(self) -> Point3d: ...

class ListingWindow:
    def Close(self) -> None:
        pass
    def CloseWindow(self) -> None:
        pass
    def Device(self) -> None:
        pass
    def DeviceType(self) -> None:
        pass
    def IsOpen(self) -> None:
        pass
    def Open(self) -> None:
        pass
    def SelectDevice(self) -> None:
        pass
    def WriteFullline(self) -> None:
        pass
    def WriteLine(self, message: str) -> None:
        pass

# ListingWindowDeviceType
# ListingWindowDeviceTypeMemberType
# LoadOptions
# LoadOptionsBookmarkComponents
# LoadOptionsBookmarkComponentsMemberType
# LoadOptionsBookmarkRefsets
# LoadOptionsBookmarkRefsetsMemberType
# LoadOptionsLoadComponents
# LoadOptionsLoadComponentsMemberType
# LoadOptionsLoadMethod
# LoadOptionsLoadMethodMemberType
# LoadOptionsLoadOption
# LoadOptionsLoadOptionMemberType
# LoadOptionsManagedModeLoadMethod
# LoadOptionsManagedModeLoadMethodMemberType
# LoadOptionsParent
# LoadOptionsParentMemberType
# LoadOptionsUpdateSubsetOnLoad
# LoadOptionsUpdateSubsetOnLoadMemberType

# LogFile

class Matrix3x3:
    @property
    def Xx(self)->float: ...
    @Xx.setter
    def Xx(self)->float: ...
    @property
    def Xy(self)->float: ...
    @Xy.setter
    def Xy(self)->float: ...
    @property
    def Xz(self)->float: ...
    @Xz.setter
    def Xz(self)->float: ...
    @property
    def Yx(self)->float: ...
    @Yx.setter
    def Yx(self)->float: ...
    @property
    def Yy(self)->float: ...
    @Yy.setter
    def Yy(self)->float: ...
    @property
    def Yz(self)->float: ...
    @Yz.setter
    def Yz(self)->float: ...
    @property
    def Zx(self)->float: ...
    @Zx.setter
    def Zx(self)->float: ...
    @property
    def Zy(self)->float: ...
    @Zy.setter
    def Zy(self)->float: ...
    @property
    def Zz(self)->float: ...
    @Zz.setter
    def Zz(self)->float: ...



# ModelingView
# ModelingViewCollection

# NXException
class NXMatrix(NXObject): ...

class NXMatrixCollection(Iterable[NXMatrix]):
    def __iter__(self): ...  # type: ignore

class NXObject(TaggedObject):
    # AttributeInformation
    # AttributeType
    def DeleteUserAttribute(self, title: str, index: int) -> None: ...
    # DeleteUserAttributes
    def GetStringUserAttribute(self, title: str, index: int) -> None: ...
    # GetUserAttributeAsString
    # GetUserAttributes
    # GetUserAttributesAsStrings
    def HasUserAttribute(self, title: str, type_:NXObject.AttributeType, index: int) -> bool: ...
    @property
    def IsOccurrence(self) -> bool: ...
    @property
    def JournalIdentifier(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def OwningComponent(self) -> Component_: ...
    @property
    def OwningPart(self) -> Part: ...
    def Print(self) -> None: ...
    @property
    def Prototype(self) -> NXObject: ...
    def SetName(self, name: str) -> None: ...
    def SetUserAttribute(
        self, title: str, index: int, value: str, option: Update.Option
    ) -> None: ...

# Parabola

class Body(DisplayableObject):
    pass

class CartesianCoordinateSystem(CoordinateSystem): ...

class CylindricalCoordinateSystem(CoordinateSystem):
    pass

class SphericalCoordinateSystem(CoordinateSystem):
    pass

class DatumCollection(List[DisplayableObject]):
    def CreateFixedDatumAxis(self) -> None:
        pass
    def CreateFixedDatumPlane(self) -> None:
        pass
    def FindObject(self) -> None:
        pass
    def __iter__(self):  # type: ignore
        pass

# class TaggedObjectCollection(Iterable):
#     def __iter__(self):
#         pass

class CurveCollection(Iterable[Curve]):
    def __iter__(self):  # type: ignore
        pass

class BodyCollection(Iterable[Body]):
    def __iter__(self):  # type: ignore
        pass

class CoordinateSystemCollection(Iterable[CoordinateSystem]):
    def __iter__(self):  # type: ignore
        pass

class NoteCollection(Iterable[BaseNote]):
    def __iter__(self):  # type: ignore
        pass

class ExpressionCollection(Iterable[Expression]):
    def __iter__(self):  # type: ignore
        pass

class Expression(NXObject):
    pass

class Part(NXObject):
    # Annotations
    #
    # @property
    # def Arcs(self) -> NXOpen.ArcCollection:
    #     pass
    # @property
    # def Axes(self) -> NXOpen.AxesCollection:
    #     pass
    @property
    def Curves(self) -> CurveCollection: ...
    @property
    def Datums(self) -> DatumCollection: ...
    @property
    def Bodies(self) -> BodyCollection: ...
    @property
    def Points(self) -> BodyCollection: ...
    @property
    def Notes(self) -> NoteCollection: ...
    @property
    def CoordinateSystems(self) -> CoordinateSystemCollection: ...
    @property
    def Expressions(self) -> ExpressionCollection: ...
    # @property
    # def CoordinateSystems(self) -> NXOpen.BodyCollection:
    #     pass
    # @property
    # def Notes(self) -> NXOpen.BodyCollection:
    #     pass
    # @property
    # def DisplayedConstraints(self) -> NXOpen.Positioning.DisplayedConstraint:
    #     pass
    # @property
    # def DrawingSheets(self) -> NXOpen.BodyCollection:
    #     pass
    # CanBeDisplayPart
    # Close
    # CloseAfterSave
    # CloseModified
    # CloseWholeTree
    @property
    def ComponentAssembly(self) -> ComponentAssembly_:
        pass
    # CoordinateSystems
    # CurrentFeature
    # Curves
    # Datums
    # Dimensions
    # Directions
    # Displayed
    @property
    def DisplayedConstraints(self) -> DisplayedConstraintCollection:
        pass
    @property
    def DrawingSheets(self) -> DrawingSheetCollection:
        pass
    # Ellipses
    # Expressions
    @property
    def Features(self) -> FeatureCollection:
        pass
    # FullPath
    # GetAttributeTitlesByType
    # GetBooleanUserAttribute
    # GetCollaborativeContentType
    # GetComputationalTimeUserAttribute
    # GetFamilyInstance
    # GetHistoryInformation
    # GetIncompleteStatus
    # GetIntegerAttribute
    # GetIntegerUserAttribute
    # GetInterpartChildren
    # GetInterpartParents
    # GetMakeUniqueName
    # GetMinimallyLoadedParts
    # GetNextUserAttribute
    # GetPartFamilyManager
    # GetPdmReferenceAttributeValue
    # GetPreviewImage
    # GetRealAttribute
    # GetRealUserAttribute
    # GetReferenceAttribute
    # GetStringAttribute
    # GetStringUserAttribute
    # GetTimeAttribute
    # GetTimeUserAttribute
    # GetTransientStatus
    # GetUpdateStatusReport
    # GetUserAttribute
    # GetUserAttributeAsString
    # GetUserAttributeCount
    # GetUserAttributeLock
    # GetUserAttributeSize
    # GetUserAttributeSourceObjects
    # GetUserAttributes
    # GetUserAttributesAsStrings
    # Grids
    # HasAnyMinimallyLoadedChildren
    # HasReuseTemplate
    # HasUserAttribute
    # HasWriteAccess
    # HistoryEventInformation
    # Hyperbolas
    # ImageCaptureManager
    # Images
    # ImagesData
    # ImportManager
    # IncompleteStatus
    # InfiniteLines
    # InspectionSetup
    # IsBookletPart
    # IsDesignReviewPart
    # IsFullyLoaded
    # IsModified
    # IsOccurrence
    # IsReadOnly
    # JournalIdentifier
    # KinematicConfigurator
    # Labels
    # LayerCategories
    @property
    def Layers(self) -> LayerManager: ...
    # LayoutDrawingSheets
    # Layouts
    @property
    def Leaf(self) -> str:
        pass
    # Lights
    # Lines
    # LoadFeatureDataForSelection
    # LoadFully
    # LoadThisPartFully
    # LoadThisPartPartially
    # LocalDefinitionFolders
    # LocalUntrimManager
    # MakeAllFeaturesInactive
    # MakeNoPartModuleActive
    # Markers
    # Markups
    # MaterialManager
    # MeasureManager
    # MechatronicsManager
    # ModelingViews
    # MotionManager
    # NXMatrices
    # Name
    # NewPartFamilyMemberData
    # NewPartFamilyMemberValues
    # NewPartFamilyTemplateManager
    # Notes
    # Null
    # Offsets
    # OmnicadManager
    # OnestepUnforms
    # Optimization
    # OwningComponent
    # OwningPart
    # PDMPart
    # PackagingCollection
    # Parabolas
    # ParameterLibraryManager
    # ParameterTables
    # PartFamilyAttrType
    # PartFamilyAttributeData
    # PartLoadState
    # PartPreview
    # PartPreviewMode
    # PartUnits
    # PenetrationManager
    # PersistentResults
    # PhysicsManager
    # Planes
    # PlasManager
    # PlotManager
    # PmiManager
    # PmiSettingsManager
    # PointClouds
    # Points
    # Polylines
    # Preferences
    # Print
    # ProductInterface
    # PropertiesManager
    # Prototype
    # ProxyObjectCollection
    # ProxyOverrideObjectCollection
    # RegenerateDisplayFacets
    # ReinstateTransience
    # Relations
    # Relinkers
    # RemoveMissingParentsFromEdgeBlend
    # RemoveTransience
    # Reopen
    # ReopenAs
    # RequirementChecks
    # Requirements
    # ResetTimestampToLatestFeature
    # ReusableParts
    # ReverseBlankAll
    # RouteManager
    # RuleManager
    # SHEDObjs
    # Save
    # SaveAs
    # SaveBookmark
    # SaveComponents
    # SaveDisplayFacets
    # SaveOptions
    # ScCollectors
    # ScRuleFactory
    # Scalars
    # Sections
    # SegmentManager
    # SelPref
    # SetAttribute
    # SetBooleanUserAttribute
    # SetMakeUniqueName
    # SetName
    # SetPdmReferenceAttribute
    # SetReferenceAttribute
    # SetTimeAttribute
    # SetTimeUserAttribute
    # SetUserAttribute
    # SetUserAttributeLock
    # SettingsManager
    # ShipDimensions
    # SketchEvaluators
    # Sketches
    # SmartDiagrammingManager
    # SpinePointData
    # Splines
    # SubdivisionBodies
    # Tag
    # ToolingManager
    # Tracelines
    # TransientStatus
    # TrueStudioObjs
    # UVMappingCollection
    # Undisplay
    # UniqueIdentifier
    # UnitCollection
    # Units
    # UserDefinedObjectManager
    # UserDefinedTemplates
    # Validations
    # ViewAlignments
    # ViewPreferences
    # Views
    # WCS
    # Xforms
    pass

class PartCollection:
    # AddPartClosedHandler
    # AddPartCreatedHandler
    # AddPartModifiedHandler
    # AddPartOpenedHandler
    # AddPartRenamedHandler
    # AddPartSavedAsHandler
    # AddPartSavedHandler
    # AddWorkPartChangedHandler
    # AllowMultipleDisplayedParts
    # BaseDisplay
    # BaseWork
    # CloseAll
    # ClosePasswordSafe
    # CreateCloudDMNewPartBuilder
    # CreateGenericFileNewBuilder
    # CreateLinkedMirrorPartBuilder
    @property
    def Display(self) -> Part:
        pass
    # EnsurePartsLoadedFully
    # EnsurePartsLoadedPartially
    # FileNew
    # FindObject
    # ForceSaveAll
    # GetDisplayedParts
    # GetMirrorCsysOptionOfMirrorPart
    # GetMirrorPartType
    # GetMirrorPlaneDataOfMirrorPart
    # GetPartLoadStateOfFileName
    # GetSourcePartNameOfMirrorPart
    # ImportToolDesignPackage
    # IsExactMirroredPart
    # IsMirroredPart
    # LoadOptions
    # MultipleDisplayedPartStatus

    # NewBase
    # NewBaseDisplay
    # NewDisplay
    # NewPartCloseResponses
    # Open
    # OpenActiveDisplay
    # OpenBase
    # OpenBaseDisplay
    # OpenDisplay
    # OpenPasswordSafe
    # OpenSeedPartBlankTemplate
    # PDMPartManager
    # RefreshPartNavigator
    # RefsetOption
    # RemovePartClosedHandler
    # RemovePartCreatedHandler
    # RemovePartModifiedHandler
    # RemovePartOpenedHandler
    # RemovePartRenamedHandler
    # RemovePartSavedAsHandler
    # RemovePartSavedHandler
    # RemovePassword
    # RemoveWorkPartChangedHandler
    # ReopenAll
    # SaveAll
    # SaveOptions
    # SdpsStatus
    # SetActiveDisplay
    # SetAllowMultipleDisplayedParts
    def SetDisplay(self, part: Part, false0: bool, false1: bool) -> None:
        pass
    # SetMirrorPartType
    # SetNonmasterSeedPartData
    # SetOpenPassword
    # SetPassword
    # SetProtectionOn
    # SetSeedPartTemplateData
    # SetWork
    # SetWorkComponent
    # SetWorkComponentOverride
    # ShapeSearchManager
    # SolveAllPostponedConstraints
    @property
    def Work(self) -> Part:
        pass
    # WorkComponent
    @property
    def WorkComponent(self) -> NXOpen.Assemblies.Component:
        """"""
        pass
    # WorkComponentOption

# PartCleanup
class PartCleanupCleanupParts(enum.Enum):
    All: int
    Components: int
    Work: int

class PartCleanupResetComponentDisplayAction(enum.Enum):
    No: int
    RemoveAllChanges: int
    RemoveRedundantChanges: int

class PartCleanupDeleteGroups(enum.Enum):
    All: int
    NotSet: int
    Unnamed: int

# PartUnits

# Plane
# PlaneCollection

# Point

class Point3d:
    @property
    def X(self) -> float:
        pass
    @property
    def Y(self) -> float:
        pass
    @property
    def Z(self) -> float:
        pass

# PointCollection

# ReferenceSet

# RemoteUtilities

# ScCollector
# ScCollectorAllowTypes
# ScCollectorAllowTypesMemberType
# ScCollectorCollection

# ScRuleFactory
# ScalarCollection

# Section

# Sense
# SenseMemberType

class Selection:
    class MaskTriple:
        def __init__(self, type_: float, sub_type: float, solid_type: float) -> None:
            pass
    def SelectTaggedObjects(
        self,
        message: str,
        title: str,
        scope: SelectionSelectionScope,
        action: SelectionSelectionAction,
        include_features: bool,
        keep_highlighted: bool,
        mas_array: List[MaskTriple],
    ) -> Tuple[SelectionResponse, List[TaggedObject]]:
        pass

# message	(string) Cue line message to display
# title	(string) Dialog title
# scope	(NXOpen::Selection::SelectionScope ) Selection scope
# action	(NXOpen::Selection::SelectionAction ) Indicates how the mask array will modify the selection filter
# include_features	(bool) Whether to allow the selection of features
# keep_highlighted	(bool) Whether to keep the selection highlighted after it has been selected
# mask_array	(NXOpen::Selection::MaskTriple ) Modifies the list of object types that can be selected. How it modifies the list of object types is determined by the SelectionAction parameter.

class SmartObject(DisplayableObject):
    pass

class Session(TaggedObject):
    class SetUndoMarkVisibility:
        Visible: Session.SetUndoMarkVisibility
    @property
    def ListingWindow(self) -> ListingWindow:
        pass
    @staticmethod
    def GetSession() -> NXOpen.Session:
        pass
    @property
    def Parts(self) -> PartCollection:
        pass
    @property
    def UpdateManager(self) -> Update:
        pass
    def SetUndoMark(
        self, visibility: NXOpen.Session.SetUndoMarkVisibility, name: str
    ) -> int:
        pass
    @property
    def DisplayManager(self) -> NXOpen.DisplayManager:
        pass
    def NewPartCleanup(self) -> PartCleanup:
        pass

# Spline

class PartCleanup:
    @property
    def PartsToCleanup(self) -> PartCleanupCleanupParts:
        pass
    @PartsToCleanup.setter
    def PartsToCleanup(self, value: PartCleanupCleanupParts) -> None:
        pass
    @property
    def CleanupAssemblyConstraints(self) -> bool:
        pass
    @CleanupAssemblyConstraints.setter
    def CleanupAssemblyConstraints(self, value: bool) -> None:
        pass
    @property
    def CleanupCAMObjects(self) -> bool:
        pass
    @CleanupCAMObjects.setter
    def CleanupCAMObjects(self, value: bool) -> None:
        pass
    @property
    def CleanupDraftingObjects(self) -> bool:
        pass
    @CleanupDraftingObjects.setter
    def CleanupDraftingObjects(self, value: bool) -> None:
        pass
    @property
    def CleanupFeatureData(self) -> bool:
        pass
    @CleanupFeatureData.setter
    def CleanupFeatureData(self, value: bool) -> None:
        pass
    @property
    def CleanupMatingData(self) -> bool:
        pass
    @CleanupMatingData.setter
    def CleanupMatingData(self, value: bool) -> None:
        pass
    @property
    def CleanupMotionData(self) -> bool:
        pass
    @CleanupMotionData.setter
    def CleanupMotionData(self, value: bool) -> None:
        pass
    @property
    def CleanupPartFamilyData(self) -> bool:
        pass
    @CleanupPartFamilyData.setter
    def CleanupPartFamilyData(self, value: bool) -> None:
        pass
    @property
    def CleanupRoutingData(self) -> bool:
        pass
    @CleanupRoutingData.setter
    def CleanupRoutingData(self, value: bool) -> None:
        pass
    @property
    def DeleteBrokenInterpartLinks(self) -> bool:
        pass
    @DeleteBrokenInterpartLinks.setter
    def DeleteBrokenInterpartLinks(self, value: bool) -> None:
        pass
    @property
    def DeleteDuplicateLights(self) -> bool:
        pass
    @DeleteDuplicateLights.setter
    def DeleteDuplicateLights(self, value: bool) -> None:
        pass
    @property
    def DeleteInvalidAttributes(self) -> bool:
        pass
    @DeleteInvalidAttributes.setter
    def DeleteInvalidAttributes(self, value: bool) -> None:
        pass
    @property
    def DeleteMaterials(self) -> bool:
        pass
    @DeleteMaterials.setter
    def DeleteMaterials(self, value: bool) -> None:
        pass
    @property
    def DeleteSpreadSheetData(self) -> bool:
        pass
    @DeleteSpreadSheetData.setter
    def DeleteSpreadSheetData(self, value: bool) -> None:
        pass
    @property
    def DeleteUnusedExpressions(self) -> bool:
        pass
    @DeleteUnusedExpressions.setter
    def DeleteUnusedExpressions(self, value: bool) -> None:
        pass
    @property
    def DeleteUnusedExtractReferences(self) -> bool:
        pass
    @DeleteUnusedExtractReferences.setter
    def DeleteUnusedExtractReferences(self, value: bool) -> None:
        pass
    @property
    def DeleteUnusedFonts(self) -> bool:
        pass
    @DeleteUnusedFonts.setter
    def DeleteUnusedFonts(self, value: bool) -> None:
        pass
    @property
    def DeleteUnusedObjects(self) -> bool:
        pass
    @DeleteUnusedObjects.setter
    def DeleteUnusedObjects(self, value: bool) -> None:
        pass
    @property
    def DeleteUnusedUnits(self) -> bool:
        pass
    @DeleteUnusedUnits.setter
    def DeleteUnusedUnits(self, value: bool) -> None:
        pass
    @property
    def DeleteVisualEditorData(self) -> bool:
        pass
    @DeleteVisualEditorData.setter
    def DeleteVisualEditorData(self, value: bool) -> None:
        pass
    @property
    def FixOffplaneSketchCurves(self) -> bool:
        pass
    @FixOffplaneSketchCurves.setter
    def FixOffplaneSketchCurves(self, value: bool) -> None:
        pass
    @property
    def GroupsToDelete(self) -> PartCleanupDeleteGroups:
        pass
    @GroupsToDelete.setter
    def GroupsToDelete(self, value: PartCleanupDeleteGroups) -> None:
        pass
    @property
    def ResetComponentDisplay(self) -> PartCleanupResetComponentDisplayAction:
        pass
    @ResetComponentDisplay.setter
    def ResetComponentDisplay(
        self, value: PartCleanupResetComponentDisplayAction
    ) -> None:
        pass
    #     part_cleanup.GroupsToDelete = NXOpen.PartCleanup.DeleteGroups.All
    # part_cleanup.ResetComponentDisplay = (
    #     NXOpen.PartCleanup.ResetComponentDisplayAction.RemoveAllChanges
    # )

    @property
    def TurnOffHighlighting(self) -> bool:
        pass
    @TurnOffHighlighting.setter
    def TurnOffHighlighting(self, value: bool) -> None:
        pass
    def DoCleanup(self) -> None:
        pass

class TaggedObject:
    Null: TaggedObject

    @property
    def Tag(self) -> int:
        pass

# TaggedObjectList
# TaggedObjectManager
class TaggedObjectManager:
    @staticmethod
    def GetTaggedObject(tag: int) -> TaggedObject:
        pass

# TransientObject
class UI:
    # AddUtilityFunctionVisibilityHandler
    # AskLockStatus
    # CanOpenPart
    # CreateCustomPopupMenuHandler
    # CreateDialog
    # CreateImageExportBuilder
    @staticmethod
    def GetUI() -> UI:
        pass
    # JournalPause
    # LockAccess
    # MenuBarManager
    # MovieManager
    # NXMessageBox
    # Null
    # ObjectPreferences
    # RemoveUtilityFunctionVisibilityHandler
    @property
    def SelectionManager(self) -> Selection:
        pass
    # Status
    # Styler
    # Tag
    # UnlockAccess
    # UserInterfacePreferences
    # ViewUIManager
    # VisualizationLinePreferences
    # VisualizationShadingPreferences
    # VisualizationVisualPreferences
    pass

# Unit
# UnitCollection
# UnitCollectionUnitDefaults
# UnitCollectionUnitDefaultsMemberType
# Update
# UpdateFailureOption
# UpdateFailureOptionMemberType
# UpdateOption
# UpdateOptionMemberType

class Vector3d:
    def __init__(self, x: float, y: float, z: float) -> None: ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...

# WCS
class WCS:
    @property
    def CoordinateSystem(self)->CartesianCoordinateSystem:
        """
        Getter for property: (NXOpen::CartesianCoordinateSystem ) CoordinateSystem. More...
        """
        pass
 
    def 	Origin (self):
        """Getter for property: (NXOpen::Point3d ) Origin. More..."""
        pass
    
    def 	Origin (self, origin):
        """Setter for property: (NXOpen::Point3d ) Origin. More..."""
        pass
    
    def 	Rotate (self, rotation_axis, angle):
        """Rotates the WCS about the specified axis. More..."""
        pass
    
    def 	Save (self):
        """Saves the WCS. More..."""
        pass
    
    def 	SetCoordinateSystem (self, new_cs):
        """Changes the coordinate system of the WCS to a new coordinate system. More..."""
        pass
    
    def 	SetCoordinateSystemCartesianAtCsys (self, new_cs):
        """Creates a WCS at a new coordinate system. More..."""
        pass
    
    def 	SetOriginAndMatrix (self, origin, matrix):
        """Sets the origin and orientation matrix of the WCS. More..."""
        pass
    
    def 	Visibility (self):
        """Getter for property: (bool) Visibility. More..."""
        pass
    
    def 	Visibility (self, is_visible):
        """Setter for property: (bool) Visibility. More..."""
        pass
# WCSAxis
# WCSAxisMemberType
