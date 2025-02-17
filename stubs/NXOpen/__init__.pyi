# from NX
# from Session import Session as ses
# Session = ses

from NXOpen.Assemblies import Component


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

# Builder

# CartesianCoordinateSystem

# ClipboardOperationsManager

# Conic

# CoordinateSystem
# CoordinateSystemCollection

# Curve
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
# Direction
# DirectionCollection

# DisplayManager

# DisplayModification
# DisplayPartOption
# DisplayPartOptionMemberType


class DisplayableObject(NXObject):
    # AttributeInformation
    # AttributeType
    # Blank
    # Color
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
    # Highlight
    # IsBlanked
    # IsOccurrence
    # JournalIdentifier
    # Layer
    # LineFont
    # LineWidth
    # Name
    # NameLocation
    # Null
    # ObjectFont
    # ObjectWidth
    # OwningComponent
    # OwningPart
    # Print
    # Prototype
    # RedisplayObject
    # RemoveViewDependency
    # SetAttribute
    # SetBooleanUserAttribute
    # SetName
    # SetNameLocation
    # SetPdmReferenceAttribute
    # SetReferenceAttribute
    # SetTimeAttribute
    # SetTimeUserAttribute
    # SetUserAttribute
    # SetUserAttributeLock
    # Tag
    # Unblank
    # Unhighlight
    pass


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

# Matrix3x3

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
    # AnalysisManager
    # AnalysisResults
    # AnimationCameras
    # Annotations
    # Arcs
    # Assemblies
    # AssemblyManager
    # AssignPermanentName
    # AttributeInformation
    # AttributeType
    # Axes
    # BaseFeatures
    # BlendStopshortBuilder
    # Bodies
    # BookmarkOption
    # CAMDataManager
    # CAMDataPrepManager
    # CAMFeatures
    # CAMSetup
    # CaeViewLayoutManager
    # Cameras
    # CanBeDisplayPart
    # ClipboardOperationsManager
    # Close
    # CloseAfterSave
    # CloseModified
    # CloseWholeTree
    # CollaborativeContentType
    # Colors
    # CompleteStructure
    # Component2dCollection
    # ComponentAssembly
    # ComponentDefinitions
    # ComponentGroups
    # ComputationalTime
    # ConvertPreNX9CompoundWelds
    # ConvertToPMIBuilderManager
    # CoordinateSystems
    # CreateAttributeIterator
    # CreateBoundingObjectBuilder
    # CreateCamSetup
    # CreateDynamicSectionBuilder
    # CreateEffectivityConditionBuilder
    # CreateEmptyBlendSetbackBuilder
    # CreateEmptyBoundaryDefinitionBuilder
    # CreateEmptyExpressionCollectorSet
    # CreateEmptyExpressionSectionSet
    # CreateEmptyRegionPoint
    # CreateEmptySelectionList
    # CreateEmptySpinePlaneBuilder
    # CreateEmptyTransitionCurveBuilder
    # CreateEmptyTwoExpressionsCollectorSet
    # CreateEmptyTwoExpressionsSectionSet
    # CreateExpressionCollectorSet
    # CreateExpressionSectionSet
    # CreateFacetSettingsBuilder
    # CreateGatewayGroupBuilder
    # CreateInspectionSetup
    # CreateKinematicConfigurator
    # CreateObjectList
    # CreatePartFamily
    # CreatePerspectiveOptionsBuilder
    # CreatePointSetAlignmentBuilder
    # CreatePointsFromFileBuilder
    # CreateReferenceSet
    # CreateRegionPoint
    # CreateSelectionList
    # CreateTwoExpressionsCollectorSet
    # CreateTwoExpressionsSectionSet
    # CreateWavelinkRepository
    # CurrentFeature
    # Curves
    # CutViews
    # DBEntityProxies
    # DateAndTimeFormat
    # Datums
    # Decals
    # DeleteAllAttributesByType
    # DeleteAttributeByTypeAndTitle
    # DeleteCamSetup
    # DeleteDisplayFacets
    # DeleteInspectionSetup
    # DeleteReferenceSet
    # DeleteRetainedDraftingObjectsInCurrentLayout
    # DeleteUserAttribute
    # DeleteUserAttributes
    # DesignStudy
    # DiagrammingManager
    # DieSimData
    # Dimensions
    # Directions
    # Displayed
    # DisplayedConstraints
    # DraftPointData
    # Drafting
    # DraftingDrawingSheets
    # DraftingManager
    # DraftingViews
    # DrawingCompare
    # DrawingSheets
    # DynamicSections
    # Ellipses
    # ExpressionGroups
    # Expressions
    # ExternalFileReferenceManager
    # FacePlaneSelectionBuilderData
    # FaceSetData
    # FaceSetOffsets
    # FacetCollectorCollection
    # FacetSelectionRuleFactory
    # FacetedBodies
    # FeatureUpdateStatus
    # Features
    # FieldManager
    # FindObject
    # Fonts
    # FullPath
    # Functions
    # GanttCollection
    # GanttLinkerCollection
    # Gdts
    # GeometryLocationData
    # GetAllReferenceSets
    # GetArrangements
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
    def Display(self)->Part:
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
    def Work(self)->Part:
        pass
    # WorkComponent
    @property
    def WorkComponent(self)->Component:
        pass
    # WorkComponentOption


# PartCleanup

# PartUnits

# Plane
# PlaneCollection

# Point

class Point3d:
    @property
    def X(self)->float:
        pass
    @property
    def Y(self)->float:
        pass
    @property
    def Z(self)->float:
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
    def X(self)->float:
        pass
    @property
    def Y(self)->float:
        pass
    @property
    def Z(self)->float:
        pass

# WCS
# WCSAxis
# WCSAxisMemberType


