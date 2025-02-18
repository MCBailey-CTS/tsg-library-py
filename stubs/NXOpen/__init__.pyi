"""
NXOpen module mcb
"""
from typing import Any, List, Optional

from NXOpen.Assemblies import Component
import NXOpen

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

class Builder(TaggedObject):
    def Commit(self) -> Optional[NXObject]:
        pass
    def Destroy(self) -> None:
        pass

# CartesianCoordinateSystem

# ClipboardOperationsManager

# Conic

# CoordinateSystem
# CoordinateSystemCollection

class Curve(DisplayableObject):
    pass

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
    # Blank
    # Color
    # Highlight
    # IsBlanked
    # Layer
    @property
    def Name(self) -> str:
        """Returns the name of the object"""
        pass
    # RedisplayObject
    # Unhighlight
    pass

class Direction(SmartObject):
    @property
    def Origin(Self) -> Point3d:
        pass
    @property
    def Vector(self) -> Vector3d:
        pass

# DirectionCollection

# DisplayManager

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
    pass

# ModelingView
# ModelingViewCollection

# NXException
# NXMatrix
# NXMatrixCollection

class NXObject(TaggedObject):
    # AttributeInformation
    # AttributeType
    # ComputationalTime
    # CreateAttributeIterator
    # DateAndTimeFormat
    # DeleteAllAttributesByType
    # DeleteAttributeByTypeAndTitle
    # DeleteUserAttribute
    # DeleteUserAttributes
    # FindObject
    # GetAttributeTitlesByType
    # GetBooleanUserAttribute
    # GetComputationalTimeUserAttribute
    # GetIntegerAttribute
    # GetIntegerUserAttribute
    # GetNextUserAttribute
    # GetPdmReferenceAttributeValue
    # GetRealAttribute
    # GetRealUserAttribute
    # GetReferenceAttribute
    # GetStringAttribute
    # GetStringUserAttribute
    # GetTimeAttribute
    # GetTimeUserAttribute
    # GetUserAttribute
    # GetUserAttributeAsString
    # GetUserAttributeCount
    # GetUserAttributeLock
    # GetUserAttributeSize
    # GetUserAttributeSourceObjects
    # GetUserAttributes
    # GetUserAttributesAsStrings
    # HasUserAttribute
    # IsOccurrence
    # JournalIdentifier
    # Name
    # Null
    # OwningComponent
    # OwningPart
    # Print
    # Prototype
    # SetAttribute
    # SetBooleanUserAttribute
    # SetName
    # SetPdmReferenceAttribute
    # SetReferenceAttribute
    # SetTimeAttribute
    # SetTimeUserAttribute
    # SetUserAttribute
    # SetUserAttributeLock
    # Tag
    pass

# Parabola

class Part:
    # Annotations
    # Arcs
    # Axes
    # Bodies
    # CanBeDisplayPart
    # Close
    # CloseAfterSave
    # CloseModified
    # CloseWholeTree
    # ComponentAssembly
    # CoordinateSystems
    # CurrentFeature
    # Curves
    # Datums
    # Dimensions
    # Directions
    # Displayed
    # DisplayedConstraints
    # DrawingSheets
    # Ellipses
    # Expressions
    @property
    def Features(self) -> List[NXOpen.Features.Feature]:
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
    # Layers
    # LayoutDrawingSheets
    # Layouts
    # Leaf
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
    # SetDisplay
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
    # Work
    @property
    def Work(self) -> Part:
        pass
    # WorkComponent
    @property
    def WorkComponent(self) -> Component:
        """"""
        pass
    # WorkComponentOption

# PartCleanup

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

class SmartObject(DisplayableObject):
    pass

class Session(TaggedObject):
    @property
    def ListingWindow(self) -> ListingWindow:
        pass
    @staticmethod
    def GetSession() -> "Session":
        pass
    @property
    def Parts(self) -> PartCollection:
        pass

# Spline

class TaggedObject:
    Null: "TaggedObject"

    @property
    def Tag(self) -> int:
        pass

# TaggedObjectList
# TaggedObjectManager

# TransientObject
# UI

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
    @property
    def X(self) -> float:
        pass
    @property
    def Y(self) -> float:
        pass
    @property
    def Z(self) -> float:
        pass

# WCS
# WCSAxis
# WCSAxisMemberType
