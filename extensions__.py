from typing import List, Optional, Sequence, Tuple, Union
import NXOpen
from NXOpen import (
    WCS,
    Body,
    Curve,
    Expression,
    Line,
    Matrix3x3,
    NXObject,
    Part,
    Point,
    Point3d,
    SmartObject,
    TaggedObject,
    Update,
    Vector3d,
)
from NXOpen.Assemblies import Component
from NXOpen.Drawings import DrawingSheet
from NXOpen.Features import Block, Cylinder, Feature
from NXOpen.UF import UFSession as UFSession_


def session() -> NXOpen.Session:
    return NXOpen.Session.GetSession()


def wcs() -> WCS:
    return display_part().WCS


def ufsession() -> UFSession_:
    return NXOpen.UF.UFSession.GetUFSession()


def select_components() -> List[Component]:
    selected_objects = NXOpen.UI.GetUI().SelectionManager.SelectTaggedObjects(
        "Select components",
        "Select components",
        NXOpen.SelectionSelectionScope.AnyInAssembly,
        NXOpen.SelectionSelectionAction.ClearAndEnableSpecific,
        False,
        False,
        [NXOpen.Selection.MaskTriple(63, 0, 0)],
    )
    return cast_components(selected_objects[1])


def display_part() -> NXOpen.Part:
    return session().Parts.Display


def work_part() -> NXOpen.Part:
    return session().Parts.Work


def work_component() -> Component:
    return session().Parts.WorkComponent


def cast_tagged_object(tag: int) -> TaggedObject:
    return NXOpen.TaggedObjectManager.GetTaggedObject(tag)


def cast_component(obj: Union[TaggedObject, int]) -> Component:
    if isinstance(obj, int):
        tagged_object = cast_tagged_object(obj)
        return cast_component(tagged_object)
    assert isinstance(obj, Component), f"Could not cast type {obj} to Component"
    return obj


def cast_components(tagged_objects: List[TaggedObject]) -> List[Component]:
    components: List[Component] = []
    for obj in tagged_objects:
        components.append(cast_component(obj))
    return components


def cycle_by_name(name: str) -> List[TaggedObject]:
    objects: List[TaggedObject] = []
    tag = 0
    while True:
        tag = UFSession_.GetUFSession().Obj.CycleByName(name, tag)
        if tag == 0:
            break
        objects.append(cast_tagged_object(tag))
    return objects


def component_ancestors(component: Component) -> List[Component]:
    ancestors: List[Component] = []
    ancestor = component.Parent
    while ancestor is not None:
        ancestors.append(ancestor)
        ancestor = ancestor.Parent
    return ancestors



def set_display_part(part:Part)->None:
    session().Parts.SetDisplay(part,False,False)

def part_get_modeling_view(part:Part,name:str):
    for view in list(part.ModelingViews):
        if view.Name == name:
            return view
    return None

# public enum SdpsStatus
# {
#     //
#     // Summary:
#     //     The work part was set successfully. This code indicates success: all other codes
#     //     indicate failure
#     Ok,
#     //
#     // Summary:
#     //     The modelling application is not active
#     OutsideModelling,
#     //
#     // Summary:
#     //     A drawing is currently displayed
#     DrawingDisplayed,
#     //
#     // Summary:
#     //     The Part List module is active
#     InPartsList,
#     //
#     // Summary:
#     //     The Tolerancing module is active
#     Gdt,
#     //
#     // Summary:
#     //     The work part and displayed part have different units
#     UnitsMismatch
# # }


def print_(obj: object) -> None:
    listing_window = session().ListingWindow
    listing_window.Open()
    listing_window.WriteLine(str(obj))


# get all objects like {point, lines, bodies} and so on
def all_objects(part: NXOpen.Part) -> List[NXOpen.NXObject]:
    raise Exception()


#    #region BasePart

#         public enum CurveOrientations
#         {
#             /// <summary>Along the tangent vector of the curve at the point</summary>
#             Tangent,

#             /// <summary>Along the normal vector of the curve at the point</summary>
#             Normal,

#             /// <summary>Along the binormal vector of the curve at the point</summary>
#             Binormal
#         }

#         //public static NXOpen.Assemblies.Component __AddComponent(
#         //   this NXOpen.BasePart basePart,
#         //   NXOpen.BasePart partToAdd,
#         //   string referenceSet = "Entire Part",
#         //   string componentName = null,
#         //   NXOpen.Point3d? origin = null,
#         //   NXOpen.Matrix3x3? orientation = null,
#         //   int layer = 1)
#         //{
#         //    basePart.__AssertIsWorkPart();
#         //    NXOpen.Point3d __origin = origin ?? new NXOpen.Point3d(0d, 0d, 0d);
#         //    NXOpen.Matrix3x3 __orientation = orientation ?? new NXOpen.Matrix3x3
#         //    {
#         //        Xx = 1,
#         //        Xy = 0,
#         //        Xz = 0,
#         //        Yx = 0,
#         //        Yy = 1,
#         //        Yz = 0,
#         //        Zx = 0,
#         //        Zy = 0,
#         //        Zz = 1,
#         //    };

#         //    string __name = componentName ?? basePart.Leaf;
#         //    return basePart.ComponentAssembly.AddComponent(partToAdd, referenceSet, __name, __origin, __orientation, layer, out _);
#         //}

#         public static void __NXOpenBasePart(BasePart basePart)


def part_create_cylinder(
    part: Part,
    axis_point: Point3d,
    axis_vector: Vector3d,
    height: float,
    diameter: float,
) -> Cylinder:
    """
    <summary>
        Creates a cylinder feature, given base point, direction, height and diameter<br />
        expressions
    </summary>
    <param name="basePart">THe part to place the Cyclinder in</param>
    <param name="axisPoint">The point at base of cylinder</param>
    <param name="axisVector">The cylinder axis vector (length doesn't matter)</param>
    <param name="height">The cylinder height</param>
    <param name="diameter">The cylinder diameter</param>
    <returns>An NX.Cylinder feature</returns>
    """
    # assert part_is_work_part(part)
    # builder = part.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    # try:
    #     builder.Type = CylinderBuilder.Types.AxisDiameterAndHeight
    #     builder.BooleanOption.Type = BooleanOperation.BooleanType.Create
    #     builder.Diameter.RightHandSide = str(diameter)
    #     builder.Height.RightHandSide = height.ToString()
    #     direction = part.Directions.CreateDirection(
    #     point_3d_origin,
    #     axis_vector,
    #     SmartObject.UpdateOption.WithinModeling
    #     )
    #     builder.Axis.Direction = direction
    #     builder.Axis.Point = part.Points.CreatePoint(axis_point)
    #     return cast_cylinder(builder.Commit())
    # finally:
    #     builder.Destroy()
    raise NotImplementedError()


#         public static SetWorkPartContextQuietly __UsingSetWorkPartQuietly(this BasePart basePart)
#         {
#             return new SetWorkPartContextQuietly(basePart);
#         }


def part_sequence_drawing_sheets(part: Part) -> Sequence[DrawingSheet]:
    return List(part.DrawingSheets)


def part_try_drawing_sheet(
    part: Part, name: str
) -> Tuple[bool, Optional[DrawingSheet]]:
    for sheet in part_sequence_drawing_sheets(part):
        if sheet.Name == name:
            return (True, sheet)
    return (False, None)




def part_has_drawing_sheet(part: Part, name: str) -> bool:
    for sheet in list(part.DrawingSheets):
        if sheet == name:
            return True
    return False


def part_get_expression_or_none(part: Part, name: str) -> Optional[Expression]:
    for expression in list(part.Expressions):
        if expression.Name == name:
            return expression
    return None


def part_get_expression(part: Part, name: str) -> Expression:
    expression = part_get_expression_or_none(part, name)
    assert expression is not None
    return expression


#         //public static bool _HasModelingView(this NXOpen.BasePart part, string modelingViewName)
#         //{
#         //    return part._FindModelingViewOrNull(modelingViewName) != null;
#         //}

#         public static ModelingView __FindModelingViewOrNull(
#             this BasePart part,
#             string modelingViewName
#         )
#         {
#             return part.ModelingViews
#                 .ToArray()
#                 .SingleOrDefault(view => view.Name == modelingViewName);
#         }


def part_get_modeling_view(part:Part, name:str)->ModelingView:
    #         public static ModelingView __FindModelingView(this BasePart part, string modelingViewName)
    #         {
    #             return part.__FindModelingViewOrNull(modelingViewName)
    #                 ?? throw new Exception(
    #                     $"Could not find modeling view in part \"{part.Leaf}\" with name \"{modelingViewName}\"."
    #                 );
    #         }
    raise NotImplementedError()


def part_descendant_parts(part: Part) -> Sequence[Part]:
    # return nxPart.ComponentAssembly.RootComponent?
    # .__Descendants(true, true)
    # .Distinct(new EqualityDisplayName())
    # .Select(c => c.Prototype)
    # .OfType<BasePart>()
    # .ToArray()
    # ?? new[] { nxPart };
    raise NotImplementedError()


#         public static bool __IsCasting(this BasePart part)
#         {
#             if (!part.__IsPartDetail())
#                 return false;

#             string[] materials = Ucf.StaticRead(
#                     Ucf.ConceptControlFile,
#                     ":CASTING_MATERIALS:",
#                     ":END_CASTING_MATERIALS:",
#                     StringComparison.OrdinalIgnoreCase
#                 )
#                 .ToArray();
#             const string material = "MATERIAL";

#             if (!Regex.IsMatch(part.Leaf, RegexDetail))
#                 return false;

#             if (!part.HasUserAttribute(material, NXObject.AttributeType.String, -1))
#                 return false;

#             string materialValue = part.GetUserAttributeAsString(
#                 material,
#                 NXObject.AttributeType.String,
#                 -1
#             );

#             return materialValue != null && materials.Any(s => materialValue.Contains(s));
#         }

#         /// <summary>Constructs a fillet arc from three points</summary>
#         /// <param name="p0">First point</param>
#         /// <param name="pa">Apex point</param>
#         /// <param name="p1">Last point</param>
#         /// <param name="radius">Radius</param>
#         /// <returns>An NXOpen.Arc representing the fillet</returns>
#         /// <remarks>
#         ///     <para>
#         ///         The fillet will be tangent to the lines p0-pa and pa-p1.
#         ///         Its angular span will we be less than 180 degrees.
#         ///     </para>
#         /// </remarks>
#         internal static Arc __CreateArcFillet(
#             this BasePart basePart,
#             Point3d p0,
#             Point3d pa,
#             Point3d p1,
#             double radius
#         )
#         {
#             Geom.Curve.Arc arc = Geom.Curve.Arc.Fillet(p0, pa, p1, radius);
#             return basePart.__CreateArc(
#                 arc.Center,
#                 arc.AxisX,
#                 arc.AxisY,
#                 arc.Radius,
#                 arc.StartAngle,
#                 arc.EndAngle
#             );
#         }


def part_is_work_part(part: Part) -> bool:
    return part.Tag == work_part().Tag


def part_crt_boolean_feature(
    part: Part,
    target: Body,
    tools: Sequence[Body],
    boolean_type,  #:  Feature.BooleanType
):  # -> BooleanFeature:
    #         /// <summary>
    #         ///     Creates a <see cref="BooleanFeature" />
    #         /// </summary>
    #         /// <param name="target">Target body</param>
    #         /// <param name="toolBodies">Array of tool bodies</param>
    #         /// <param name="booleanType">Type of boolean operation (unions, subtract, etc.)</param>
    #         /// <returns>NX.Boolean feature formed by operation</returns>
    #         {
    assert part_is_work_part(part)
    builder = part.Features.CreateBooleanBuilder(Feature.Null)

    try:
        builder.Operation = boolean_type
        builder.Target = target
        for body in tools:
            builder.Tools.Add(body)
        return builder.Commit()
    finally:
        builder.Destroy()


def is_display_part(part: Part) -> bool:
    return part.Tag == display_part().Tag


#         [Obsolete(nameof(NotImplementedException))]
#         public static TaggedObject[] __CycleObjsInPart1(this BasePart basePart, string name)
#         {
#             //basePart._AssertIsWorkPart();
#             //NXOpen.Tag _tag = NXOpen.Tag.Null;
#             //var list = new List<NXOpen.TaggedObject>();

#             //while (true)
#             //{
#             //    ufsession_.Obj.CycleObjsInPart1(name, ref _tag);

#             //    if (_tag == NXOpen.Tag.Null)
#             //        break;

#             //    list.Add(session_.GetObjectManager().GetTaggedObject(_tag));
#             //}

#             //return list.ToArray();
#             throw new NotImplementedException();
#         }

#         public static void __Reopen(
#             this BasePart basePart,
#             ReopenScope scope = ReopenScope.PartAndSubassemblies,
#             ReopenMode mode = ReopenMode.ReopenAll
#         )
#         {
#             ufsession_.Part.Reopen(basePart.Tag, (int)scope, (int)mode, out _);
#         }


def part_is_modified(part:Part)->bool:
#         public static bool __IsModified(this BasePart basePart)
#         {
#             return ufsession_.Part.IsModified(basePart.Tag);
#         }
    raise NotImplementedError()


#         public static DatumCsys __AbsoluteDatumCsys(this BasePart basePart)
#         {
#             return basePart.Features.OfType<DatumCsys>().First();
#         }
def part_create_text_feature(
    part: Part,
    note: str,
    origin: Point3d,
    orientation: Matrix3x3,
    length: float,
    height: float,
    script,  #:TextBuilder.ScriptOptions
):  # ->TextFeature:
    #         {
    #             TextBuilder textBuilder = part.Features.CreateTextBuilder(null);

    #             using (new Destroyer(textBuilder))
    #             {
    #                 textBuilder.PlanarFrame.AnchorLocation = RectangularFrameBuilder
    #                     .AnchorLocationType
    #                     .MiddleCenter;
    #                 textBuilder.PlanarFrame.WScale = 100.0;
    #                 textBuilder.PlanarFrame.Length.RightHandSide = $"{length}";
    #                 textBuilder.PlanarFrame.Height.RightHandSide = $"{height}";
    #                 textBuilder.PlanarFrame.WScale = 75d;
    #                 textBuilder.SelectFont(font, script);
    #                 textBuilder.TextString = note;
    #                 Point point2 = part.Points.CreatePoint(origin);
    #                 CartesianCoordinateSystem csys = part.CoordinateSystems.CreateCoordinateSystem(
    #                     origin,
    #                     orientation,
    #                     true
    #                 );
    #                 textBuilder.PlanarFrame.CoordinateSystem = csys;
    #                 textBuilder.PlanarFrame.UpdateOnCoordinateSystem();
    #                 ModelingView workView = session_.Parts.Work.ModelingViews.WorkView;
    #                 textBuilder.PlanarFrame.AnchorLocator.SetValue(point2, workView, origin);
    #                 return (Text)textBuilder.Commit();
    #             }
    #         }
    pass


#         public static void __SetWcsToAbsolute(this BasePart part)
#         {
#             part.WCS.SetOriginAndMatrix(_Point3dOrigin, _Matrix3x3Identity);
#         }

#         public static void __Save(
#             this BasePart part,
#             bool saveChildComponents = false,
#             bool closeAfterSave = false
#         )
#         {
#             part.Save(
#                 saveChildComponents ? BasePart.SaveComponents.True : BasePart.SaveComponents.False,
#                 closeAfterSave ? BasePart.CloseAfterSave.True : BasePart.CloseAfterSave.False
#             );
#         }


# def part_cre_category(part)
#         /// <summary>Creates a layer category with a given name</summary>
#         /// <param name="name">Name of layer category</param>
#         /// <param name="description">Description of layer category</param>
#         /// <param name="layers">Layers to be placed into the category</param>
#         /// <returns>An NX.Category object</returns>
#         /// <exception cref="ArgumentException"></exception>
#         internal static Category __CreateCategory(
#             this BasePart basePart,
#             string name,
#             string description,
#             params int[] layers
#         )
#         {
#             basePart.__AssertIsWorkPart();

#             try
#             {
#                 return __work_part_.LayerCategories.CreateCategory(name, description, layers);
#             }
#             catch (NXException ex)
#             {
#                 if (ex.ErrorCode == 3515007)
#                 {
#                     string message = "A category with the given name already exists.";
#                     ArgumentException ex2 = new ArgumentException(message, ex);
#                     throw ex2;
#                 }

#                 throw new ArgumentException("unknown error", ex);
#             }
#         }

#         /// <summary>
#         ///     Creates a Snap.NX.Chamfer feature
#         /// </summary>
#         /// <param name="edge">Edge used to chamfer</param>
#         /// <param name="distance">Offset distance</param>
#         /// <param name="offsetFaces">
#         ///     The offsetting method used to determine the size of the chamfer If true, the<br />
#         ///     edges of the chamfer face will be constructed by offsetting the faces adjacent<br />
#         ///     to the selected edge If false, the edges of the chamfer face will be constructed<br />
#         ///     by offsetting the selected edge along the adjacent faces
#         /// </param>
#         /// <returns>An NX.Chamfer object</returns>
#         internal static Chamfer __CreateChamfer(
#             this BasePart basePart,
#             Edge edge,
#             double distance,
#             bool offsetFaces
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             ChamferBuilder chamferBuilder = part.Features.CreateChamferBuilder(null);

#             using (session_.__UsingBuilderDestroyer(chamferBuilder))
#             {
#                 chamferBuilder.Option = ChamferBuilder.ChamferOption.SymmetricOffsets;

#                 chamferBuilder.Method = offsetFaces
#                     ? ChamferBuilder.OffsetMethod.FacesAndTrim
#                     : ChamferBuilder.OffsetMethod.EdgesAlongFaces;

#                 chamferBuilder.FirstOffset = distance.ToString();
#                 chamferBuilder.SecondOffset = distance.ToString();
#                 chamferBuilder.Tolerance = DistanceTolerance;
#                 ScCollector scCollector = part.ScCollectors.CreateCollector();
#                 EdgeTangentRule edgeTangentRule = part.__CreateRuleEdgeTangent(edge);
#                 SelectionIntentRule[] rules = new SelectionIntentRule[1] { edgeTangentRule };
#                 scCollector.ReplaceRules(rules, false);
#                 chamferBuilder.SmartCollector = scCollector;
#                 Feature feature = chamferBuilder.CommitFeature();
#                 return (Chamfer)feature;
#             }
#         }

#         /// <summary>
#         ///     Creates a chamfer object
#         /// </summary>
#         /// <param name="edge">Edge used to chamfer</param>
#         /// <param name="distance1">Offset distance1</param>
#         /// <param name="distance2">Offset distance2</param>
#         /// <param name="offsetFaces">
#         ///     The offsetting method used to determine the size of the chamfer If true, the<br />
#         ///     edges of the chamfer face will be constructed by offsetting the faces adjacent<br />
#         ///     to the selected edge If false, the edges of the chamfer face will be constructed<br />
#         ///     by offsetting the selected edge along the adjacent faces
#         /// </param>
#         /// <returns>An NX.Chamfer object</returns>
#         internal static Chamfer __CreateChamfer(
#             this BasePart basePart,
#             Edge edge,
#             double distance1,
#             double distance2,
#             bool offsetFaces
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             ChamferBuilder chamferBuilder = part.Features.CreateChamferBuilder(null);

#             using (session_.__UsingBuilderDestroyer(chamferBuilder))
#             {
#                 chamferBuilder.Option = ChamferBuilder.ChamferOption.TwoOffsets;
#                 chamferBuilder.Method = offsetFaces
#                     ? ChamferBuilder.OffsetMethod.FacesAndTrim
#                     : ChamferBuilder.OffsetMethod.EdgesAlongFaces;
#                 chamferBuilder.FirstOffset = distance1.ToString();
#                 chamferBuilder.SecondOffset = distance2.ToString();
#                 chamferBuilder.Tolerance = DistanceTolerance;
#                 ScCollector scCollector = part.ScCollectors.CreateCollector();
#                 EdgeTangentRule edgeTangentRule = part.ScRuleFactory.CreateRuleEdgeTangent(
#                     edge,
#                     null,
#                     false,
#                     AngleTolerance,
#                     false,
#                     false
#                 );
#                 SelectionIntentRule[] rules = new SelectionIntentRule[1] { edgeTangentRule };
#                 scCollector.ReplaceRules(rules, false);
#                 chamferBuilder.SmartCollector = scCollector;
#                 Feature feature = chamferBuilder.CommitFeature();
#                 return (Chamfer)feature;
#             }
#         }

#         /// <summary>Creates a chamfer object</summary>
#         /// <param name="edge">Edge used to chamfer</param>
#         /// <param name="distance">Offset distance</param>
#         /// <param name="angle">Offset angle</param>
#         /// <returns>An NX.Chamfer object</returns>
#         internal static Chamfer __CreateChamfer(
#             this BasePart basePart,
#             Edge edge,
#             double distance,
#             double angle
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             ChamferBuilder chamferBuilder = part.Features.CreateChamferBuilder(null);

#             using (session_.__UsingBuilderDestroyer(chamferBuilder))
#             {
#                 chamferBuilder.Option = ChamferBuilder.ChamferOption.OffsetAndAngle;
#                 chamferBuilder.FirstOffset = distance.ToString();
#                 chamferBuilder.Angle = angle.ToString();
#                 chamferBuilder.Tolerance = DistanceTolerance;
#                 ScCollector scCollector = part.ScCollectors.CreateCollector();
#                 EdgeTangentRule edgeTangentRule = part.ScRuleFactory.CreateRuleEdgeTangent(
#                     edge,
#                     null,
#                     true,
#                     AngleTolerance,
#                     false,
#                     false
#                 );
#                 SelectionIntentRule[] rules = new SelectionIntentRule[1] { edgeTangentRule };
#                 scCollector.ReplaceRules(rules, false);
#                 chamferBuilder.SmartCollector = scCollector;
#                 chamferBuilder.AllInstances = false;
#                 Feature feature = chamferBuilder.CommitFeature();
#                 return (Chamfer)feature;
#             }
#         }

#         /// <summary>Creates a datum axis object</summary>
#         /// <param name="icurve">Icurve is an edge or a curve</param>
#         /// <param name="arcLengthPercent">Percent arcLength, in range 0 to 100</param>
#         /// <param name="curveOrientation">The curve orientation used by axis</param>
#         /// <returns>An NX.DatumAxis object</returns>
#         internal static DatumAxisFeature __CreateDatumAxis(
#             this BasePart basePart,
#             ICurve icurve,
#             double arcLengthPercent,
#             CurveOrientations curveOrientation
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             DatumAxisBuilder datumAxisBuilder = __work_part_.Features.CreateDatumAxisBuilder(null);

#             using (session_.__UsingBuilderDestroyer(datumAxisBuilder))
#             {
#                 datumAxisBuilder.Type = DatumAxisBuilder.Types.OnCurveVector;
#                 datumAxisBuilder.ArcLength.IsPercentUsed = true;
#                 datumAxisBuilder.ArcLength.Expression.RightHandSide = arcLengthPercent.ToString();
#                 datumAxisBuilder.CurveOrientation =
#                     (DatumAxisBuilder.CurveOrientations)curveOrientation;
#                 datumAxisBuilder.IsAssociative = true;
#                 datumAxisBuilder.IsAxisReversed = false;
#                 datumAxisBuilder.Curve.Value = icurve;
#                 datumAxisBuilder.ArcLength.Path.Value = (TaggedObject)icurve;
#                 datumAxisBuilder.ArcLength.Update(OnPathDimensionBuilder.UpdateReason.Path);
#                 return (DatumAxisFeature)datumAxisBuilder.Commit();
#             }
#         }

#         /// <summary>Creates an edge blend object</summary>
#         /// <param name="edges">Edge array used to blend</param>
#         /// <param name="radius">Radius of a regular blend</param>
#         /// <returns>An NX.EdgeBlend object</returns>
#         internal static EdgeBlend __CreateEdgeBlend(
#             this BasePart basePart,
#             double radius,
#             Edge[] edges
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             EdgeBlendBuilder edgeBlendBuilder = part.Features.CreateEdgeBlendBuilder(null);

#             using (session_.__UsingBuilderDestroyer(edgeBlendBuilder))
#             {
#                 _ = edgeBlendBuilder.LimitsListData;
#                 ScCollector scCollector = part.ScCollectors.CreateCollector();
#                 Edge[] array = new Edge[edges.Length];

#                 for (int i = 0; i < array.Length; i++)
#                     array[i] = edges[i];

#                 EdgeMultipleSeedTangentRule edgeMultipleSeedTangentRule =
#                     part.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(
#                         array,
#                         AngleTolerance,
#                         true
#                     );

#                 SelectionIntentRule[] rules = new SelectionIntentRule[1]
#                 {
#                     edgeMultipleSeedTangentRule
#                 };
#                 scCollector.ReplaceRules(rules, false);
#                 edgeBlendBuilder.Tolerance = DistanceTolerance;
#                 edgeBlendBuilder.AllInstancesOption = false;
#                 edgeBlendBuilder.RemoveSelfIntersection = true;
#                 edgeBlendBuilder.ConvexConcaveY = false;
#                 edgeBlendBuilder.RollOverSmoothEdge = true;
#                 edgeBlendBuilder.RollOntoEdge = true;
#                 edgeBlendBuilder.MoveSharpEdge = true;
#                 edgeBlendBuilder.TrimmingOption = false;
#                 edgeBlendBuilder.OverlapOption = EdgeBlendBuilder.Overlap.AnyConvexityRollOver;
#                 edgeBlendBuilder.BlendOrder = EdgeBlendBuilder.OrderOfBlending.ConvexFirst;
#                 edgeBlendBuilder.SetbackOption = EdgeBlendBuilder.Setback.SeparateFromCorner;
#                 edgeBlendBuilder.AddChainset(scCollector, radius.ToString());
#                 Feature feature = edgeBlendBuilder.CommitFeature();
#                 return (EdgeBlend)feature;
#             }
#         }

#         /// <summary>Creates an extract object</summary>
#         /// <param name="faces">The face array which will be extracted</param>
#         /// <returns>An NX.ExtractFace feature</returns>
#         internal static ExtractFace __CreateExtractFace(this BasePart basePart, Face[] faces)
#         {
#             basePart.__AssertIsDisplayPart();
#             Part part = __work_part_;
#             ExtractFaceBuilder builder = part.Features.CreateExtractFaceBuilder(null);

#             using (session_.__UsingBuilderDestroyer(builder))
#             {
#                 builder.FaceOption = ExtractFaceBuilder.FaceOptionType.FaceChain;
#                 Face[] array = new Face[faces.Length];

#                 for (int i = 0; i < faces.Length; i++)
#                     array[i] = faces[i];

#                 FaceDumbRule faceDumbRule = part.ScRuleFactory.CreateRuleFaceDumb(array);
#                 SelectionIntentRule[] rules = new SelectionIntentRule[1] { faceDumbRule };
#                 builder.FaceChain.ReplaceRules(rules, false);
#                 ExtractFace extract = (ExtractFace)builder.CommitFeature();
#                 return extract;
#             }
#         }

#         public static Extrude __CreateExtrude(
#             this BasePart part,
#             Curve[] curves,
#             Vector3d direction,
#             double start,
#             double end
#         )
#         {
#             part.__AssertIsWorkPart();
#             ExtrudeBuilder builder = part.Features.CreateExtrudeBuilder(null);

#             using (session_.__UsingBuilderDestroyer(builder))
#             {
#                 SelectionIntentRule[] rules = { part.ScRuleFactory.CreateRuleCurveDumb(curves) };
#                 builder.Section = __display_part_.Sections.CreateSection();
#                 builder.Section.AddToSection(
#                     rules,
#                     null,
#                     null,
#                     null,
#                     _Point3dOrigin,
#                     Section.Mode.Create,
#                     false
#                 );
#                 builder.Limits.StartExtend.Value.Value = start;
#                 builder.Limits.EndExtend.Value.Value = end;

#                 builder.Direction = part.Directions.CreateDirection(
#                     curves[0].__StartPoint(),
#                     direction,
#                     SmartObject.UpdateOption.WithinModeling
#                 );

#                 return (Extrude)builder.Commit();
#             }
#         }

#         public static CartesianCoordinateSystem __CreateCsys(
#             this BasePart part,
#             Point3d origin,
#             Matrix3x3 orientation,
#             bool makeTemporary = true
#         )
#         {
#             // Creates and NXMatrix with the orientation of the {orientation}.
#             NXMatrix matrix = part.__OwningPart().NXMatrices.Create(orientation);
#             // The tag to hold the csys.
#             Tag csysId;

#             if (makeTemporary)
#                 ufsession_.Csys.CreateTempCsys(origin.__ToArray(), matrix.Tag, out csysId);
#             else
#                 ufsession_.Csys.CreateCsys(origin.__ToArray(), matrix.Tag, out csysId);

#             return (CartesianCoordinateSystem)NXObjectManager.Get(csysId);
#         }

#         public static CartesianCoordinateSystem __CreateCsys(
#             this BasePart part,
#             bool makeTemporary = true
#         )
#         {
#             return part.__CreateCsys(_Point3dOrigin, _Matrix3x3Identity, makeTemporary);
#         }

#         internal static OffsetCurve __CreateOffsetLine(
#             this BasePart basePart,
#             ICurve icurve,
#             Point point,
#             string height,
#             string angle,
#             bool reverseDirection
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             OffsetCurveBuilder offsetCurveBuilder = part.Features.CreateOffsetCurveBuilder(null);

#             using (session_.__UsingBuilderDestroyer(offsetCurveBuilder))
#             {
#                 offsetCurveBuilder.Type = OffsetCurveBuilder.Types.Draft;
#                 offsetCurveBuilder.InputCurvesOptions.InputCurveOption = CurveOptions
#                     .InputCurve
#                     .Retain;
#                 offsetCurveBuilder.CurveFitData.Tolerance = DistanceTolerance;
#                 offsetCurveBuilder.PointOnOffsetPlane = point;
#                 offsetCurveBuilder.DraftHeight.RightHandSide = height;
#                 offsetCurveBuilder.DraftAngle.RightHandSide = angle;
#                 offsetCurveBuilder.ReverseDirection = reverseDirection;
#                 Section section = offsetCurveBuilder.CurvesToOffset;
#                 section.__AddICurve(icurve);
#                 Feature feature = offsetCurveBuilder.CommitFeature();
#                 offsetCurveBuilder.CurvesToOffset.CleanMappingData();
#                 return feature as OffsetCurve;
#             }
#         }

#         private static void __VarBlend(
#             this BasePart part,
#             Edge edge,
#             double[] arclengthPercents,
#             double[] radii
#         )
#         {
#             part.__AssertIsWorkPart();
#             EdgeBlendBuilder edgeBlendBuilder = part.Features.CreateEdgeBlendBuilder(null);

#             using (session_.__UsingBuilderDestroyer(edgeBlendBuilder))
#             {
#                 ScCollector scCollector = part.ScCollectors.CreateCollector();
#                 Edge[] edges = new Edge[1] { edge };
#                 EdgeDumbRule edgeDumbRule = part.ScRuleFactory.CreateRuleEdgeDumb(edges);
#                 SelectionIntentRule[] rules = new SelectionIntentRule[1] { edgeDumbRule };
#                 scCollector.ReplaceRules(rules, false);
#                 edgeBlendBuilder.AddChainset(scCollector, "5");
#                 string parameter = arclengthPercents[0].ToString();
#                 string parameter2 = arclengthPercents[1].ToString();
#                 string radius = radii[0].ToString();
#                 string radius2 = radii[1].ToString();
#                 Point smartPoint = null;
#                 edgeBlendBuilder.AddVariablePointData(
#                     edge,
#                     parameter,
#                     radius,
#                     "3.333",
#                     "0.6",
#                     smartPoint,
#                     false,
#                     false
#                 );
#                 edgeBlendBuilder.AddVariablePointData(
#                     edge,
#                     parameter2,
#                     radius2,
#                     "3.333",
#                     "0.6",
#                     smartPoint,
#                     false,
#                     false
#                 );
#                 edgeBlendBuilder.Tolerance = DistanceTolerance;
#                 edgeBlendBuilder.AllInstancesOption = false;
#                 edgeBlendBuilder.RemoveSelfIntersection = true;
#                 edgeBlendBuilder.PatchComplexGeometryAreas = true;
#                 edgeBlendBuilder.LimitFailingAreas = true;
#                 edgeBlendBuilder.ConvexConcaveY = false;
#                 edgeBlendBuilder.RollOverSmoothEdge = true;
#                 edgeBlendBuilder.RollOntoEdge = true;
#                 edgeBlendBuilder.MoveSharpEdge = true;
#                 edgeBlendBuilder.TrimmingOption = false;
#                 edgeBlendBuilder.OverlapOption = EdgeBlendBuilder.Overlap.AnyConvexityRollOver;
#                 edgeBlendBuilder.BlendOrder = EdgeBlendBuilder.OrderOfBlending.ConvexFirst;
#                 edgeBlendBuilder.SetbackOption = EdgeBlendBuilder.Setback.SeparateFromCorner;
#                 edgeBlendBuilder.CommitFeature();
#             }
#         }

#         public static Component __RootComponentOrNull(this BasePart nxPart)
#         {
#             return nxPart.ComponentAssembly?.RootComponent;
#         }

#         public static Component __RootComponent(this BasePart nxPart)
#         {
#             return nxPart.__RootComponentOrNull() ?? throw new ArgumentException();
#         }

#         public static void __Save(this BasePart part)
#         {
#             part.__Save(BasePart.SaveComponents.True);
#         }

#         public static void __Save(this BasePart part, BasePart.SaveComponents saveComponents)
#         {
#             part.Save(saveComponents, BasePart.CloseAfterSave.False);
#         }


def part_is_see_3d_data(part: Part) -> bool:
    # value = part_attribute

    #         public static bool __IsSee3DData(this BasePart part)
    #         {
    #             Regex regex = new Regex("SEE(-|_| )3D(-|_| )DATA");

    #             if (!part.HasUserAttribute("DESCRIPTION", NXObject.AttributeType.String, -1))
    #                 return false;

    #             string descriptionValue = part.GetUserAttributeAsString(
    #                 "DESCRIPTION",
    #                 NXObject.AttributeType.String,
    #                 -1
    #             );
    #             return descriptionValue != null && regex.IsMatch(descriptionValue.ToUpper());
    #         }
    pass


#         /// <summary>Creates a tube feature, given spine and inner/outer diameters</summary>
#         /// <param name="spine">The centerline (spine) of the tube</param>
#         /// <param name="outerDiameter">Outer diameter</param>
#         /// <param name="innerDiameter">Inner diameter</param>
#         /// <param name="createBsurface">If true, creates a single b-surface for the inner and outer faces of the tube</param>
#         /// <returns>An NX.Tube object</returns>
#         internal static Tube __CreateTube(
#             this BasePart basePart,
#             Curve spine,
#             double outerDiameter,
#             double innerDiameter,
#             bool createBsurface
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             TubeBuilder tubeBuilder = part.Features.CreateTubeBuilder(null);

#             using (session_.__UsingBuilderDestroyer(tubeBuilder))
#             {
#                 tubeBuilder.Tolerance = DistanceTolerance;
#                 tubeBuilder.OuterDiameter.RightHandSide = outerDiameter.ToString();
#                 tubeBuilder.InnerDiameter.RightHandSide = innerDiameter.ToString();
#                 tubeBuilder.OutputOption = TubeBuilder.Output.MultipleSegments;

#                 if (createBsurface)
#                     tubeBuilder.OutputOption = TubeBuilder.Output.SingleSegment;

#                 Section section = tubeBuilder.PathSection;
#                 section.__AddICurve(spine);
#                 tubeBuilder.BooleanOption.Type = BooleanOperation.BooleanType.Create;
#                 Tube tube = (Tube)tubeBuilder.CommitFeature();
#                 return tube;
#             }
#         }


#         public static void __Close(
#             this BasePart part,
#             bool closeWholeTree = false,
#             bool closeModified = false
#         )
#         {
#             BasePart.CloseWholeTree closeWholeTree_ = closeWholeTree
#                 ? BasePart.CloseWholeTree.True
#                 : BasePart.CloseWholeTree.False;

#             BasePart.CloseModified closeModified_ = closeModified
#                 ? BasePart.CloseModified.CloseModified
#                 : BasePart.CloseModified.DontCloseModified;

#             part.Close(closeWholeTree_, closeModified_, null);
#         }

#         ///// <summary>Constructs a NXOpen.Arc from center, rotation matrix, radius, angles</summary>
#         ///// <param name="center">Center point (in absolute coordinates)</param>
#         ///// <param name="matrix">Orientation</param>
#         ///// <param name="radius">Radius</param>
#         ///// <param name="angle1">Start angle (in degrees)</param>
#         ///// <param name="angle2">End angle (in degrees)</param>
#         ///// <returns>A <see cref="NXOpen.Arc">NXOpen.Arc</see> object</returns>
#         //public static NXOpen.Arc Arc(
#         //    this NXOpen.BasePart part,
#         //    NXOpen.Point3d center,
#         //    NXOpen.Matrix3x3 matrix,
#         //    double radius,
#         //    double angle1,
#         //    double angle2)
#         //{
#         //    NXOpen.Vector3d axisX = matrix._AxisX();
#         //    NXOpen.Vector3d axisY = matrix._AxisY();
#         //    return part.__CreateArc(center, axisX, axisY, radius, angle1, angle2);
#         //}


#         public static DatumAxis __CreateFixedDatumAxis(
#             this BasePart part,
#             Point3d start,
#             Point3d end
#         )
#         {
#             return part.Datums.CreateFixedDatumAxis(start, end);
#         }

#         public static ScCollector __CreateScCollector(
#             this BasePart part,
#             params SelectionIntentRule[] intentRules
#         )
#         {
#             if (intentRules.Length == 0)
#                 throw new ArgumentException(
#                     $"Cannot create {nameof(ScCollector)} from 0 {nameof(intentRules)}.",
#                     nameof(intentRules)
#                 );

#             ScCollector collector = part.ScCollectors.CreateCollector();
#             collector.ReplaceRules(intentRules, false);
#             return collector;
#         }

#         public static Section __CreateSection(
#             this BasePart part,
#             SelectionIntentRule[] intentRules,
#             NXObject seed,
#             NXObject startConnector = null,
#             NXObject endConnector = null,
#             Point3d helpPoint = default,
#             Section.Mode mode = Section.Mode.Create
#         )
#         {
#             if (intentRules.Length == 0)
#                 throw new ArgumentException(
#                     $"Cannot create {nameof(Section)} from 0 {nameof(intentRules)}.",
#                     nameof(intentRules)
#                 );

#             Section section = part.Sections.CreateSection();
#             section.AddToSection(intentRules, seed, startConnector, endConnector, helpPoint, mode);
#             return section;
#         }

#         public static DatumAxis __CreateFixedDatumAxis(
#             this BasePart part,
#             Point3d origin,
#             Vector3d vector
#         )
#         {
#             return part.Datums.CreateFixedDatumAxis(origin, origin.__Add(vector));
#         }

#         /// <summary>
#         ///     Created an offset face object
#         /// </summary>
#         /// <param name="faces">Offset faces</param>
#         /// <param name="distance">Offset distace</param>
#         /// <param name="direction">Offset direction</param>
#         /// <returns>An NX.OffsetFace object</returns>
#         internal static OffsetFace __CreateOffsetFace(
#             this BasePart basePart,
#             Face[] faces,
#             double distance,
#             bool direction
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             OffsetFaceBuilder offsetFaceBuilder = part.Features.CreateOffsetFaceBuilder(null);

#             using (session_.__UsingBuilderDestroyer(offsetFaceBuilder))
#             {
#                 offsetFaceBuilder.Distance.RightHandSide = distance.ToString();
#                 SelectionIntentRule[] array = new SelectionIntentRule[faces.Length];

#                 for (int i = 0; i < faces.Length; i++)
#                 {
#                     Face[] boundaryFaces = new Face[0];
#                     array[i] = part.ScRuleFactory.CreateRuleFaceTangent(faces[i], boundaryFaces);
#                 }

#                 offsetFaceBuilder.FaceCollector.ReplaceRules(array, false);
#                 offsetFaceBuilder.Direction = direction;
#                 OffsetFace offsetFace = (OffsetFace)offsetFaceBuilder.Commit();
#                 return offsetFace;
#             }
#         }

#         /// <summary>Creates a line tangent to two curves</summary>
#         /// <param name="icurve1">The first curve or edge</param>
#         /// <param name="helpPoint1">A point near the desired tangency point on the first curve</param>
#         /// <param name="icurve2">The second curve or edge</param>
#         /// <param name="helpPoint2">A point near the desired tangency point on the second curve</param>
#         /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#         /// <remarks>
#         ///     <para>
#         ///         The line will start and end at the tangency points on the two curves.
#         ///     </para>
#         ///     <para>
#         ///         The help points do not have to lie on the curves, just somewhere near the desired tangency points.
#         ///     </para>
#         ///     <para>
#         ///         If the two given curves are not coplanar, then the second curve is projected to the plane of the first curve,
#         ///         and a tangent line is constructed between the first curve and the projected one.
#         ///     </para>
#         /// </remarks>
#         [Obsolete(nameof(NotImplementedException))]
#         public static Line __CreateLineTangent(
#             this BasePart basePart,
#             ICurve icurve1,
#             Point3d helpPoint1,
#             ICurve icurve2,
#             Point3d helpPoint2
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             icurve1.__IsLinearCurve();
#             icurve1.__IsPlanar();
#             icurve2.__IsLinearCurve();
#             icurve2.__IsPlanar();
#             double value = icurve1.__Parameter(icurve1.__StartPoint());
#             Surface.Plane plane = new Surface.Plane(
#                 icurve1.__StartPoint(),
#                 icurve1.__Binormal(value)
#             );
#             helpPoint1 = helpPoint1.__Project(plane);
#             helpPoint2 = helpPoint2.__Project(plane);
#             Part workPart = __work_part_;
#             AssociativeLine associativeLine = null;
#             AssociativeLineBuilder associativeLineBuilder =
#                 workPart.BaseFeatures.CreateAssociativeLineBuilder(associativeLine);

#             using (session_.__UsingBuilderDestroyer(associativeLineBuilder))
#             {
#                 associativeLineBuilder.StartPointOptions = AssociativeLineBuilder
#                     .StartOption
#                     .Tangent;
#                 associativeLineBuilder.StartTangent.SetValue(icurve1, null, helpPoint1);
#                 associativeLineBuilder.EndPointOptions = AssociativeLineBuilder.EndOption.Tangent;
#                 associativeLineBuilder.EndTangent.SetValue(icurve2, null, helpPoint2);
#                 associativeLineBuilder.Associative = false;
#                 associativeLineBuilder.Commit();
#                 NXObject nXObject = associativeLineBuilder.GetCommittedObjects()[0];
#                 return (Line)nXObject;
#             }
#         }

#         /// <summary>Creates a line at a given angle, tangent to a given curve</summary>
#         /// <param name="icurve">A curve or edge lying in a plane parallel to the XY-plane</param>
#         /// <param name="angle">An angle measured relative to the X-axis</param>
#         /// <param name="helpPoint">A point near the desired tangency point</param>
#         /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#         /// <remarks>
#         ///     <para>
#         ///         The line created has "infinite" length; specifically, its length is
#         ///         limited by the bounding box of the model.
#         ///     </para>
#         /// </remarks>
#         /// <exception cref="T:System.ArgumentException">
#         ///     The input curve is a line, is non-planar, or does not lie in a plane
#         ///     parallel to the XY-plane
#         /// </exception>
#         [Obsolete(nameof(NotImplementedException))]
#         public static Line __CreateLineTangent(
#             this BasePart basePart,
#             ICurve icurve,
#             double angle,
#             Point3d helpPoint
#         )
#         {
#             //basePart.__AssertIsWorkPart();
#             //icurve.__IsLinearCurve();
#             //icurve.__IsPlanar();
#             //NXOpen.Session.UndoMarkId markId = SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Snap_TangentLineAngle999");
#             //NXOpen.Part workPart = __work_part_;
#             //NXOpen.Features.AssociativeLine associativeLine = null;
#             //NXOpen.Features.AssociativeLineBuilder associativeLineBuilder = workPart.BaseFeatures.CreateAssociativeLineBuilder(associativeLine);

#             //using (session_.using_builder_destroyer(associativeLineBuilder))
#             //{
#             //    associativeLineBuilder.StartPointOptions = NXOpen.Features.AssociativeLineBuilder.StartOption.Tangent;
#             //    associativeLineBuilder.StartTangent.SetValue(icurve, null, helpPoint);
#             //    associativeLineBuilder.EndPointOptions = NXOpen.Features.AssociativeLineBuilder.EndOption.AtAngle;
#             //    associativeLineBuilder.EndAtAngle.Value = DatumAxis(_Point3dOrigin, _Point3dOrigin._Add(_Vector3dX())).DatumAxis;
#             //    associativeLineBuilder.EndAngle.RightHandSide = angle.ToString();
#             //    associativeLineBuilder.Associative = false;
#             //    associativeLineBuilder.Commit();
#             //    NXOpen.Line obj = (NXOpen.Line)associativeLineBuilder.GetCommittedObjects()[0];
#             //    NXOpen.Point3d position = obj.StartPoint;
#             //    NXOpen.Point3d position2 = obj.EndPoint;
#             //    NXOpen.Point3d[] array = Compute.ClipRay(new Geom.Curve.Ray(position, position2._Subtract(position)));
#             //    UndoToMark(markId, "Snap_TangentLineAngle999");
#             //    DeleteUndoMark(markId, "Snap_TangentLineAngle999");
#             //    return Line(array[0], array[1]);
#             //}

#             throw new NotImplementedException();
#         }

#         /// <summary>Creates an offset curve feature from given curves, direction, distance</summary>
#         /// <param name="curves">Array of curves to be offset</param>
#         /// <param name="distance">Offset distance</param>
#         /// <param name="reverseDirection">
#         ///     If true, reverse direction of offset. The default direction is the normal of<br />
#         ///     the array of curves.
#         /// </param>
#         /// <remarks>
#         ///     The resulting NX.OffsetCurve object may consist of many curves. Use the Curves<br />
#         ///     property of this object to get the curves themselves.<br /><br />
#         ///     This function doesn't accept a single line as input. Please us the function OffsetLine<br />
#         ///     if you want to offset a single line.
#         /// </remarks>
#         /// <returns>A Snap.NX.OffsetCurve object</returns>
#         [Obsolete(
#             "Deprecated in NX8.5, please use Snap.Create.OffsetCurve(double, double, NXOpen.Point3d, NXOpen.Vector3d, params NX.ICurve[]) instead."
#         )]
#         internal static OffsetCurve __CreateOffsetCurve(
#             this BasePart basePart,
#             ICurve[] curves,
#             double distance,
#             bool reverseDirection
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             OffsetCurveBuilder offsetCurveBuilder = part.Features.CreateOffsetCurveBuilder(null);

#             using (session_.__UsingBuilderDestroyer(offsetCurveBuilder))
#             {
#                 offsetCurveBuilder.Type = OffsetCurveBuilder.Types.Distance;
#                 offsetCurveBuilder.InputCurvesOptions.InputCurveOption = CurveOptions
#                     .InputCurve
#                     .Retain;
#                 offsetCurveBuilder.CurveFitData.Tolerance = DistanceTolerance;
#                 offsetCurveBuilder.TrimMethod = OffsetCurveBuilder.TrimOption.ExtendTangents;
#                 offsetCurveBuilder.CurvesToOffset.DistanceTolerance = DistanceTolerance;
#                 offsetCurveBuilder.CurvesToOffset.AngleTolerance = AngleTolerance;
#                 offsetCurveBuilder.CurvesToOffset.ChainingTolerance = ChainingTolerance;
#                 offsetCurveBuilder.CurvesToOffset.SetAllowedEntityTypes(
#                     Section.AllowTypes.OnlyCurves
#                 );
#                 offsetCurveBuilder.CurvesToOffset.AllowSelfIntersection(true);
#                 offsetCurveBuilder.OffsetDistance.RightHandSide = distance.ToString();
#                 offsetCurveBuilder.ReverseDirection = reverseDirection;
#                 Section section = offsetCurveBuilder.CurvesToOffset;

#                 for (int i = 0; i < curves.Length; i++)
#                     section.__AddICurve(curves);

#                 Feature feature = offsetCurveBuilder.CommitFeature();
#                 return feature as OffsetCurve;
#             }
#         }

#         /// <summary>Creates an offset curve feature from given curves, direction, distance</summary>
#         /// <param name="icurves">Array of curves to be offset</param>
#         /// <param name="height">Draft height</param>
#         /// <param name="angle">Draft angle</param>
#         /// <param name="reverseDirection">
#         ///     If true, reverse direction of offset.<br />
#         ///     The default direction is close to the normal of the array of curves.
#         /// </param>
#         /// <remarks>
#         ///     The resulting NX.OffsetCurve object may consist of many curves. Use the Curves<br />
#         ///     property of this object to get the curves themselves.<br /><br />
#         ///     This function doesn't accept a single line as input. Please us the function OffsetLine<br />
#         ///     if you want to offset a single line.
#         /// </remarks>
#         /// <returns>A Snap.NX.OffsetCurve object</returns>
#         internal static OffsetCurve __CreateOffsetCurve(
#             this BasePart basePart,
#             ICurve[] icurves,
#             double height,
#             double angle,
#             bool reverseDirection
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             OffsetCurveBuilder offsetCurveBuilder = part.Features.CreateOffsetCurveBuilder(null);

#             using (session_.__UsingBuilderDestroyer(offsetCurveBuilder))
#             {
#                 offsetCurveBuilder.Type = OffsetCurveBuilder.Types.Draft;
#                 offsetCurveBuilder.InputCurvesOptions.InputCurveOption = CurveOptions
#                     .InputCurve
#                     .Retain;
#                 offsetCurveBuilder.CurveFitData.Tolerance = DistanceTolerance;
#                 offsetCurveBuilder.DraftHeight.RightHandSide = height.ToString();
#                 offsetCurveBuilder.DraftAngle.RightHandSide = angle.ToString();
#                 offsetCurveBuilder.ReverseDirection = reverseDirection;
#                 Section section = offsetCurveBuilder.CurvesToOffset;

#                 for (int i = 0; i < icurves.Length; i++)
#                     section.__AddICurve(icurves);

#                 Feature feature = offsetCurveBuilder.CommitFeature();
#                 offsetCurveBuilder.CurvesToOffset.CleanMappingData();
#                 return feature as OffsetCurve;
#             }
#         }

#         /// <summary>
#         ///     Creates an offset curve feature from given curves, direction, distance
#         /// </summary>
#         /// <remarks>
#         ///     This function doesn't accept an array consisting of a single line as input.
#         ///     The resulting NX.OffsetCurve object may consist of many curves. Use the Curves
#         ///     property of this object to get the curves themselves.
#         ///     Offsets of lines and arcs will again be lines and arcs, respectively. Offsets
#         ///     of splines and ellipses will be splines that approximate the exact offsets to
#         ///     with DistanceTolerance.
#         /// </remarks>
#         /// <param name="curves">Array of base curves to be offset</param>
#         /// <param name="distance">Offset distance</param>
#         /// <param name="helpPoint">A help point on the base curves</param>
#         /// <param name="helpVector">The offset direction (roughly) at the help point</param>
#         /// <returns>A Snap.NX.OffsetCurve object</returns>
#         internal static OffsetCurve __CreateOffsetCurve(
#             this BasePart basePart,
#             ICurve[] curves,
#             double distance,
#             Point3d helpPoint,
#             Vector3d helpVector
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             OffsetCurveBuilder offsetCurveBuilder = part.Features.CreateOffsetCurveBuilder(null);

#             using (session_.__UsingBuilderDestroyer(offsetCurveBuilder))
#             {
#                 offsetCurveBuilder.Type = OffsetCurveBuilder.Types.Distance;
#                 offsetCurveBuilder.InputCurvesOptions.InputCurveOption = CurveOptions
#                     .InputCurve
#                     .Retain;
#                 offsetCurveBuilder.CurveFitData.Tolerance = DistanceTolerance;
#                 offsetCurveBuilder.CurveFitData.AngleTolerance = AngleTolerance;
#                 offsetCurveBuilder.CurvesToOffset.SetAllowedEntityTypes(
#                     Section.AllowTypes.OnlyCurves
#                 );
#                 offsetCurveBuilder.CurvesToOffset.AllowSelfIntersection(true);
#                 offsetCurveBuilder.OffsetDistance.RightHandSide = distance.ToString();
#                 Section section = offsetCurveBuilder.CurvesToOffset;
#                 section.__AddICurve(curves);
# #pragma warning disable CS0618 // Type or member is obsolete
#                 offsetCurveBuilder.ReverseDirection = __IsReverseDirection(
#                     offsetCurveBuilder,
#                     curves,
#                     helpPoint,
#                     helpVector
#                 );
# #pragma warning restore CS0618 // Type or member is obsolete
#                 Feature feature = offsetCurveBuilder.CommitFeature();
#                 return feature as OffsetCurve;
#             }
#         }

#         [Obsolete(nameof(NotImplementedException))]
#         public static bool __IsReverseDirection(
#             OffsetCurveBuilder builder,
#             ICurve[] icurves,
#             Point3d pos,
#             Vector3d helpVector
#         )
#         {
#             //int num = -1;
#             //double num2 = -1.0;

#             //for (int i = 0; i < icurves.Length; i++)
#             //{
#             //    double num3 = -1.0;
#             //    num3 = Compute.Distance(pos, (NXObject)icurves[i]);

#             //    if (num3 > num2)
#             //    {
#             //        num2 = num3;
#             //        num = i;
#             //    }
#             //}

#             //builder.ComputeOffsetDirection(seedPoint: (icurves[num] is NXOpen.Edge)
#             //    ? Compute.ClosestPoints(pos, (NXOpen.Curve)icurves[num]).Point2
#             //    : Compute.ClosestPoints(pos, (Edge)icurves[num]).Point2, seedEntity: icurves[num], offsetDirection: out Vector3d offsetDirection, startPoint: out Point3d _);

#             //return helpVector._Multiply(offsetDirection) < 0.0;
#             throw new NotImplementedException();
#         }

#         /// <summary>
#         ///     Creates an offset curve feature from given curves, direction, distance
#         /// </summary>
#         /// <remarks>
#         ///     The resulting NX.OffsetCurve object may consist of many curves. Use the Curves<br />
#         ///     property of this object to get the curves themselves.<br /><br />
#         ///     Offsets of lines and arcs will again be lines and arcs, respectively. Offsets
#         ///     of splines and ellipses will be splines that approximate the exact offsets to
#         ///     with DistanceTolerance.<br /><br />
#         ///     This function doesn't accept an array consisting of a single line as input.
#         ///     <remarks />
#         ///     <param name="curves">Array of curves to be offset</param>
#         ///     <param name="height">Draft height</param>
#         ///     <param name="angle">Draft angle</param>
#         ///     <param name="helpPoint">A help point on the base curves</param>
#         ///     <param name="helpVector">The offset direction (roughly) at the help point</param>
#         ///     <returns>A Snap.NX.OffsetCurve object</returns>
#         internal static OffsetCurve __CreateOffsetCurve(
#             this BasePart basePart,
#             ICurve[] curves,
#             double height,
#             double angle,
#             Point3d helpPoint,
#             Vector3d helpVector
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             OffsetCurveBuilder offsetCurveBuilder = part.Features.CreateOffsetCurveBuilder(null);

#             using (session_.__UsingBuilderDestroyer(offsetCurveBuilder))
#             {
#                 offsetCurveBuilder.Type = OffsetCurveBuilder.Types.Draft;
#                 offsetCurveBuilder.InputCurvesOptions.InputCurveOption = CurveOptions
#                     .InputCurve
#                     .Retain;
#                 offsetCurveBuilder.CurveFitData.Tolerance = DistanceTolerance;
#                 offsetCurveBuilder.DraftHeight.RightHandSide = height.ToString();
#                 offsetCurveBuilder.DraftAngle.RightHandSide = angle.ToString();
#                 Section section = offsetCurveBuilder.CurvesToOffset;
#                 section.__AddICurve(curves);
# #pragma warning disable CS0618 // Type or member is obsolete
#                 offsetCurveBuilder.ReverseDirection = __IsReverseDirection(
#                     offsetCurveBuilder,
#                     curves,
#                     helpPoint,
#                     helpVector
#                 );
# #pragma warning restore CS0618 // Type or member is obsolete
#                 Feature feature = offsetCurveBuilder.CommitFeature();
#                 offsetCurveBuilder.CurvesToOffset.CleanMappingData();
#                 return feature as OffsetCurve;
#             }
#         }

#         /// <summary>
#         ///     Creates an offset curve feature from given curve, direction, distance
#         /// </summary>
#         /// <param name="basePart"></param>
#         /// <param name="icurve">Array of curves to be offset</param>
#         /// <param name="point">Point on offset plane</param>
#         /// <param name="distance">Offset Distance</param>
#         /// <param name="reverseDirection">
#         ///     If true, reverse direction of offset. The default direction is the normal of<br />
#         ///     the array of curves.
#         /// </param>
#         /// <remarks>
#         ///     The resulting NX.OffsetCurve object may consist of many curves. Use the Curves<br />
#         ///     property of this object to get the curves themselves.<br /><br />
#         ///     This function only accept a single line as input. Please us the function Offset<br />
#         ///     if you want to offset a non-linear curve.
#         /// </remarks>
#         /// <returns>A Snap.NX.OffsetCurve object</returns>
#         internal static OffsetCurve __CreateOffsetLine(
#             this BasePart basePart,
#             ICurve icurve,
#             Point point,
#             string distance,
#             bool reverseDirection
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Part part = __work_part_;
#             OffsetCurveBuilder offsetCurveBuilder = part.Features.CreateOffsetCurveBuilder(null);

#             using (session_.__UsingBuilderDestroyer(offsetCurveBuilder))
#             {
#                 offsetCurveBuilder.Type = OffsetCurveBuilder.Types.Distance;
#                 offsetCurveBuilder.InputCurvesOptions.InputCurveOption = CurveOptions
#                     .InputCurve
#                     .Retain;
#                 offsetCurveBuilder.CurveFitData.Tolerance = DistanceTolerance;
#                 offsetCurveBuilder.OffsetDistance.RightHandSide = distance;
#                 offsetCurveBuilder.ReverseDirection = reverseDirection;
#                 offsetCurveBuilder.PointOnOffsetPlane = point;
#                 Section section = offsetCurveBuilder.CurvesToOffset;
#                 section.__AddICurve(icurve);
#                 Feature feature = offsetCurveBuilder.CommitFeature();
#                 offsetCurveBuilder.CurvesToOffset.CleanMappingData();
#                 return feature as OffsetCurve;
#             }
#         }

#         /// <summary>Creates a fillets with two given curves</summary>
#         /// <param name="curve1">First curve for the fillet</param>
#         /// <param name="curve2">Second curve for the fillet</param>
#         /// <param name="radius">Radius of the fillet</param>
#         /// <param name="center">Approximate fillet center expressed as absolute coordinates</param>
#         /// <param name="doTrim">If true, indicates that the input curves should get trimmed by the fillet</param>
#         /// <returns>An NX.Arc object</returns>
#         internal static Arc __CreateArcFillet(
#             this BasePart basePart,
#             Curve curve1,
#             Curve curve2,
#             double radius,
#             Point3d center,
#             bool doTrim
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             Tag[] curveObjs = new Tag[2] { curve1.Tag, curve2.Tag };
#             double[] array = center.__ToArray();
#             int[] array2 = new int[3];
#             int[] arcOpts = new int[3];
#             if (doTrim)
#             {
#                 array2[0] = 1;
#                 array2[1] = 1;
#             }
#             else
#             {
#                 array2[0] = 0;
#                 array2[1] = 0;
#             }

#             ufsession_.Curve.CreateFillet(
#                 0,
#                 curveObjs,
#                 array,
#                 radius,
#                 array2,
#                 arcOpts,
#                 out Tag filletObj
#             );
#             return (Arc)session_.__GetTaggedObject(filletObj);
#         }

#         public static void __AssertIsWorkPart(this BasePart basePart)
#         {
#             if (__work_part_.Tag != basePart.Tag)
#                 throw new AssertWorkPartException(basePart);
#         }

#         /// <summary>Creates a Snap.NX.TrimBody feature</summary>
#         /// <param name="targetBody">The target body will be trimmed</param>
#         /// <param name="toolBody">The sheet body used to trim target body</param>
#         /// <param name="direction">The default direction is the normal of the sheet body.</param>
#         /// <returns>A Snap.NX.TrimBody feature</returns>
#         internal static TrimBody2 __CreateTrimBody(
#             this BasePart basePart,
#             Body targetBody,
#             Body toolBody,
#             bool direction
#         )
#         {
#             Part part = __work_part_;
#             TrimBody2Builder trimBody2Builder = part.Features.CreateTrimBody2Builder(null);

#             using (session_.__UsingBuilderDestroyer(trimBody2Builder))
#             {
#                 trimBody2Builder.Tolerance = DistanceTolerance;
#                 trimBody2Builder.BooleanTool.ExtrudeRevolveTool.ToolSection.DistanceTolerance =
#                     DistanceTolerance;
#                 trimBody2Builder.BooleanTool.ExtrudeRevolveTool.ToolSection.ChainingTolerance =
#                     ChainingTolerance;
#                 ScCollector scCollector = part.ScCollectors.CreateCollector();
#                 Body[] bodies = new Body[1] { targetBody };
#                 BodyDumbRule bodyDumbRule = part.ScRuleFactory.CreateRuleBodyDumb(bodies);
#                 SelectionIntentRule[] rules = new SelectionIntentRule[1] { bodyDumbRule };
#                 scCollector.ReplaceRules(rules, false);
#                 trimBody2Builder.TargetBodyCollector = scCollector;
#                 SelectionIntentRule[] rules2 = new SelectionIntentRule[1]
#                 {
#                     part.ScRuleFactory.CreateRuleFaceBody(toolBody)
#                 };
#                 trimBody2Builder.BooleanTool.FacePlaneTool.ToolFaces.FaceCollector.ReplaceRules(
#                     rules2,
#                     false
#                 );
#                 trimBody2Builder.BooleanTool.ReverseDirection = direction;
#                 return (TrimBody2)trimBody2Builder.Commit();
#             }
#         }

#         /// <summary>Creates a Snap.NX.TrimBody feature</summary>
#         /// <param name="targetBody">The target body will be trimmed</param>
#         /// <param name="toolDatumPlane">The datum plane used to trim target body</param>
#         /// <param name="direction">Trim direction. The default direction is the normal of the datum plane.</param>
#         /// <returns>A Snap.NX.TrimBody feature</returns>
#         internal static TrimBody2 __CreateTrimBody(
#             this BasePart basePart,
#             Body targetBody,
#             DatumPlane toolDatumPlane,
#             bool direction
#         )
#         {
#             Part part = __work_part_;
#             TrimBody2Builder trimBody2Builder = part.Features.CreateTrimBody2Builder(null);

#             using (session_.__UsingBuilderDestroyer(trimBody2Builder))
#             {
#                 trimBody2Builder.Tolerance = DistanceTolerance;
#                 trimBody2Builder.BooleanTool.ExtrudeRevolveTool.ToolSection.DistanceTolerance =
#                     DistanceTolerance;
#                 trimBody2Builder.BooleanTool.ExtrudeRevolveTool.ToolSection.ChainingTolerance =
#                     ChainingTolerance;
#                 ScCollector scCollector = part.ScCollectors.CreateCollector();
#                 Body[] bodies = new Body[1] { targetBody };
#                 BodyDumbRule bodyDumbRule = part.ScRuleFactory.CreateRuleBodyDumb(bodies);
#                 SelectionIntentRule[] rules = new SelectionIntentRule[1] { bodyDumbRule };
#                 scCollector.ReplaceRules(rules, false);
#                 trimBody2Builder.TargetBodyCollector = scCollector;
#                 SelectionIntentRule[] array = new SelectionIntentRule[1];
#                 DatumPlane[] faces = new DatumPlane[1] { toolDatumPlane };
#                 array[0] = part.ScRuleFactory.CreateRuleFaceDatum(faces);
#                 trimBody2Builder.BooleanTool.FacePlaneTool.ToolFaces.FaceCollector.ReplaceRules(
#                     array,
#                     false
#                 );
#                 trimBody2Builder.BooleanTool.ReverseDirection = direction;
#                 Feature feature = trimBody2Builder.CommitFeature();
#                 return (TrimBody2)feature;
#             }
#         }

#         /// <summary>Creates a "widget" body for examples and testing</summary>
#         /// <returns>An NX.Body</returns>
#         /// <remarks>
#         ///     <para>
#         ///         The widget object is shown in the pictures below.
#         ///     </para>
#         ///     <para>
#         ///         <img src="../Images/widget.png" />
#         ///     </para>
#         ///     <para>
#         ///         This object is useful for examples and testing because it has many different
#         ///         types of faces and edges. The faces are named, for easy reference in example
#         ///         code, as outlined below.
#         ///     </para>
#         ///     <para>
#         ///         <list type="table">
#         ///             <listheader>
#         ///                 <term>Face Name</term>
#         ///                 <description>Face Description</description>
#         ///             </listheader>
#         ///             <item>
#         ///                 <term>CYAN_REVOLVED</term><description>Revolved face on left end</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>MAGENTA_TORUS_BLEND</term><description>Toroidal face with minor radius = 10</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>TEAL_CONE</term><description>Large conical face</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>YELLOW_SPHERE</term><description>Spherical face with diameter = 15</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>PINK_CYLINDER_HOLE</term><description>Cylindrical hole with diameter = 20</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>RED_BSURFACE_BLEND</term>
#         ///                 <description>B-surface representing a variable radius blend</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>BLUE_CYLINDER_VERTICAL</term>
#         ///                 <description>Vertical cylindrical face with diameter = 30</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>TAN_PLANE_TOP</term><description>Planar face on top</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>ORANGE_BLEND</term><description>Blend face with radius = 7</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>GREEN_EXTRUDED</term><description>Extruded face on right-hand end</description>
#         ///             </item>
#         ///             <item>
#         ///                 <term>GREY_PLANE_BACK</term><description>Large planar face on back</description>
#         ///             </item>
#         ///         </list>
#         ///     </para>
#         /// </remarks>
#         [Obsolete(nameof(NotImplementedException))]
#         public static Body __Widget()
#         {
#             //NXOpen.Point3d origin = _Point3dOrigin;
#             //NXOpen.Vector3d axisX = Extensions._Vector3dX();
#             //NXOpen.Vector3d axisY = Extensions._Vector3dY();
#             //NXOpen.Vector3d axisZ = Extensions._Vector3dZ();
#             //double num = 48.0;
#             //double num2 = 40.0;
#             //double num3 = 30.0;
#             //double[] diameters = new double[2] { num, num2 };
#             //double num4 = 80.0;
#             //double num5 = 2.0 * num3;
#             //NXOpen.Body body = Cone(origin, axisY, diameters, 90).GetBodies()[0];
#             //NXOpen.Body body2 = Cylinder(new NXOpen.Point3d(0.0, num4 / 2.0, 0.0), axisZ, num5, num3).GetBodies()[0];
#             //NXOpen.Line line = Line(0.0 - num, 0.0, 0.9 * num, 0.0 - num, num4, 0.7 * num);
#             //NXOpen.Body body3 = ExtrudeSheet(new NXOpen.ICurve[1] { line }, axisX, 200);
#             //NXOpen.Line line2 = Line(0.0, -10.0, -2.0 * num, 0.0, num4 + 10.0, -2.0 * num);
#             //NXOpen.Body body4 = ExtrudeSheet(new NXOpen.ICurve[1] { line2 }, axisZ, 200);
#             //TrimBody(body2, body3, direction: true);
#             //NXOpen.Body body5 = TrimBody(body2, body4, direction: false).GetBodies()[0];
#             //NXOpen.Body body6 = Unite(TrimBody(body, body4, direction: false), body5);
#             //NXOpen.Edge[] edges = body6.Edges;
#             //foreach (NXOpen.Edge edge in edges)
#             //{
#             //    double[] arclengthPercents = new double[2] { 0.0, 100.0 };
#             //    double[] radii = new double[2] { 9.0, 4.0 };
#             //    bool flag = edge.SolidEdgeType == NXOpen.Edge.EdgeType.Intersection;
#             //    bool flag2 = edge.Vertices.Length > 1;
#             //    if (flag && flag2)
#             //    {
#             //        VarBlend(edge, arclengthPercents, radii);
#             //    }
#             //}

#             //NXOpen.Point3d position = new NXOpen.Point3d(0.0, 0.0, num / 2.0);
#             //NXOpen.Point3d position2 = new NXOpen.Point3d(0.0, 5.0, 0.0);
#             //NXOpen.Point3d position3 = new NXOpen.Point3d(0.0, 0.0, (0.0 - num) / 2.0);
#             //NXOpen.Spline spline = BezierCurve(position, position2, position3);
#             //NXOpen.Body body7 = ExtrudeSheet(new NXOpen.ICurve[1] { spline }, -axisX, num).Body;
#             //NXOpen.Body targetBody = TrimBody(body6, body7, direction: true);
#             //position = new NXOpen.Point3d(0.0, num4 + 10.0, 0.0);
#             //position2 = new NXOpen.Point3d(0.0, num4, 20.0);
#             //position3 = new NXOpen.Point3d(0.0, num4 - 15.0, 25.0);
#             //NXOpen.Spline spline2 = BezierCurve(position, position2, position3);
#             //NXOpen.Body body8 = RevolveSheet(new NXOpen.ICurve[1] { spline2 }, _Point3dOrigin, Extensions._AxisY());
#             //NXOpen.Body body9 = TrimBody(targetBody, body8, direction: true);
#             //NXOpen.Edge edge2 = null;
#             //NXOpen.Edge edge3 = null;
#             //edges = body9.Edges;
#             //foreach (NXOpen.Edge edge4 in edges)
#             //{
#             //    bool num6 = edge4.SolidEdgeType == NXOpen.Edge.EdgeType.Circular;
#             //    bool flag3 = edge4.ArcLength > 1.2 * num2;
#             //    if (num6 && flag3)
#             //    {
#             //        edge2 = edge4;
#             //    }

#             //    if (edge4.ObjectSubType == ObjectTypes.SubType.EdgeIntersection)
#             //    {
#             //        edge3 = edge4;
#             //    }
#             //}

#             //EdgeBlend(10, edge2);
#             //EdgeBlend(7, edge3);
#             //NXOpen.Body body10 = Cylinder(new NXOpen.Point3d(0.0 - num, 0.3 * num4, 0.0), axisX, 200, 20).Body;
#             //NXOpen.Body body11 = Subtract(body9, body10).Body;
#             //NXOpen.Body body12 = Sphere(new NXOpen.Point3d((0.0 - num2) / 2.0, 0.7 * num4, 0.0), 15).Body;
#             //Snap.NX.Feature feature = Unite(body11, body12);
#             //NXOpen.Body body13 = feature.Body;
#             //Snap.NX.Feature.Orphan(feature);
#             //Snap.NX.NXObject.Delete(body7, body4, body3, body8);
#             //Snap.NX.NXObject.Delete(line2, line, spline, spline2);
#             //body13.Color = System.Drawing.Color.Black;
#             //NXOpen.Face[] faces = body13.Faces;
#             //foreach (NXOpen.Face face in faces)
#             //{
#             //    if (face.SolidFaceType == Face.FaceType.Planar)
#             //    {
#             //        face.Color = System.Drawing.Color.Tan;
#             //        face.Name = "TAN_PLANE_TOP";
#             //        if (System.Math.Abs(face.Normal(0.5, 0.5).X) > 0.9)
#             //        {
#             //            face.Color = System.Drawing.Color.Gray;
#             //            face.Name = "GREY_PLANE_BACK";
#             //        }
#             //    }

#             //    if (face.ObjectSubType == ObjectTypes.SubType.FaceCylinder)
#             //    {
#             //        face.Color = System.Drawing.Color.Blue;
#             //        face.Name = "BLUE_CYLINDER_VERTICAL";
#             //        if (face.Edges.Length == 2)
#             //        {
#             //            face.Color = System.Drawing.Color.Salmon;
#             //            face.Name = "PINK_CYLINDER_HOLE";
#             //        }
#             //    }

#             //    if (face.ObjectSubType == ObjectTypes.SubType.FaceCone)
#             //    {
#             //        face.Color = System.Drawing.Color.Teal;
#             //        face.Name = "TEAL_CONE";
#             //    }

#             //    if (face.ObjectSubType == ObjectTypes.SubType.FaceBsurface)
#             //    {
#             //        face.Color = System.Drawing.Color.Red;
#             //        face.Name = "RED_BSURFACE_BLEND";
#             //    }

#             //    if (face.ObjectSubType == ObjectTypes.SubType.FaceTorus)
#             //    {
#             //        face.Color = System.Drawing.Color.Magenta;
#             //        face.Name = "MAGENTA_TORUS_BLEND";
#             //    }

#             //    if (face.ObjectSubType == ObjectTypes.SubType.FaceBlend)
#             //    {
#             //        face.Color = System.Drawing.Color.Orange;
#             //        face.Name = "ORANGE_BLEND";
#             //    }

#             //    if (face.ObjectSubType == ObjectTypes.SubType.FaceExtruded)
#             //    {
#             //        face.Color = System.Drawing.Color.Green;
#             //        face.Name = "GREEN_EXTRUDED";
#             //    }

#             //    if (face.ObjectSubType == ObjectTypes.SubType.FaceSphere)
#             //    {
#             //        face.Color = System.Drawing.Color.Yellow;
#             //        face.Name = "YELLOW_SPHERE";
#             //    }

#             //    if (face.ObjectSubType == ObjectTypes.SubType.FaceRevolved)
#             //    {
#             //        face.Color = System.Drawing.Color.Cyan;
#             //        face.Name = "CYAN_REVOLVED";
#             //    }
#             //}

#             //return body13;
#             throw new NotImplementedException();
#         }

#         /// <summary>Creates a BoundedPlane object</summary>
#         /// <param name="boundingCurves">Array of curves forming the boundary</param>
#         /// <returns> A <see cref="T:Snap.NX.BoundedPlane">Snap.NX.BoundedPlane</see> object</returns>
#         /// <remarks>
#         ///     <para>
#         ///         The boundary curves are input in a single list, which can include both periphery curves
#         ///         and curves bounding holes. The order of the curves in the array does not matter.
#         ///     </para>
#         /// </remarks>
#         internal static BoundedPlane __CreateBoundedPlane(
#             this BasePart basePart,
#             params Curve[] boundingCurves
#         )
#         {
#             basePart.__AssertIsWorkPart();

#             if (boundingCurves.Length == 0)
#                 throw new ArgumentOutOfRangeException();

#             Part part = __work_part_;
#             BoundedPlaneBuilder boundedPlaneBuilder = part.Features.CreateBoundedPlaneBuilder(null);

#             using (boundedPlaneBuilder.__UsingBuilder())
#             {
#                 boundedPlaneBuilder.BoundingCurves.SetAllowedEntityTypes(
#                     Section.AllowTypes.OnlyCurves
#                 );
#                 boundedPlaneBuilder.BoundingCurves.AllowSelfIntersection(false);
#                 Section section = boundedPlaneBuilder.BoundingCurves;
#                 section.__AddICurve(boundingCurves);
#                 return (BoundedPlane)boundedPlaneBuilder.Commit();
#             }
#         }

#         /// <summary>Unites an array of tool bodies with a target body</summary>
#         /// <param name="basePart"></param>
#         /// <param name="targetBody">Target body</param>
#         /// <param name="toolBodies">Array of tool bodies</param>
#         /// <returns><see cref="T:Snap.NX.Boolean">Snap.NX.Boolean</see> feature formed by uniting tools with target</returns>
#         public static BooleanFeature __CreateUnite(
#             this BasePart basePart,
#             Body targetBody,
#             params Body[] toolBodies
#         )
#         {
#             return basePart.__CreateBoolean(targetBody, toolBodies, Feature.BooleanType.Unite);
#         }

#         /// <summary>Subtracts an array of tool bodies from a target body</summary>
#         /// <param name="targetBody">Target body</param>
#         /// <param name="toolBodies">Array of tool bodies</param>
#         /// <returns><see cref="T:Snap.NX.Boolean">Snap.NX.Boolean</see> feature formed by subtracting tools from target</returns>
#         public static BooleanFeature __CreateSubtract(
#             this BasePart basePart,
#             Body targetBody,
#             params Body[] toolBodies
#         )
#         {
#             return basePart.__CreateBoolean(targetBody, toolBodies, Feature.BooleanType.Subtract);
#         }

#         /// <summary>Intersects an array of tool bodies with a target body</summary>
#         /// <param name="targetBody">Target body</param>
#         /// <param name="toolBodies">Array of tool bodies</param>
#         /// <returns><see cref="T:Snap.NX.Boolean">Snap.NX.Boolean</see> feature formed by intersecting tools with target</returns>
#         public static BooleanFeature __CreateIntersect(
#             this BasePart basePart,
#             Body targetBody,
#             params Body[] toolBodies
#         )
#         {
#             return basePart.__CreateBoolean(targetBody, toolBodies, Feature.BooleanType.Intersect);
#         }

#         public static void __SetAsDisplayPart(this BasePart part)
#         {
#             __display_part_ = (Part)part;
#         }

#         public static bool __HasReferenceSet(this BasePart part, string referenceSet)
#         {
#             return part.GetAllReferenceSets().SingleOrDefault(set => set.Name == referenceSet)
#                 != null;
#         }

#         public static ReferenceSet __FindReferenceSetOrNull(
#             this BasePart nxPart,
#             string refsetTitle
#         )
#         {
#             return nxPart.GetAllReferenceSets().SingleOrDefault(set => set.Name == refsetTitle);
#         }

#         public static ReferenceSet __FindReferenceSet(this BasePart nxPart, string refsetTitle)
#         {
#             return nxPart.__FindReferenceSetOrNull(refsetTitle)
#                 ?? throw new Exception(
#                     $"Could not find reference set with title \"{refsetTitle}\" in part \"{nxPart.Leaf}\"."
#                 );
#         }


# def single_or_none()


def part_dynamic_block_or_none(part: Part) -> Union[Block, None]:
    for feat in list(part.Features):
        if feat.Name == "DYNAMIC BLOCK" and isinstance(feat, Block):
            return feat
    return None


#         public static Block __DynamicBlockOrNull(this BasePart nxPart)
#         {
#             return nxPart.Features
#                 .OfType<Block>()
#                 .SingleOrDefault(block => block.Name == "DYNAMIC BLOCK");
#         }

#         public static Block __DynamicBlock(this BasePart nxPart)
#         {
#             return nxPart.__DynamicBlockOrNull() ?? throw new Exception("Could not find ");
#         }

#         public static bool __HasDynamicBlock(this BasePart part)
#         {
#             return part.__DynamicBlockOrNull() != null;
#         }

#         public static bool __Is999(this BasePart part)
#         {
#             Match match = Regex.Match(part.Leaf, RegexDetail);
#             //GFolderWithCtsNumber.DetailPart.DetailExclusiveRegex.Match(nxPart.Leaf);
#             if (!match.Success)
#                 return false;
#             int detailNumber = int.Parse(match.Groups[3].Value);
#             return detailNumber >= 990 && detailNumber <= 1000;
#         }

#         public static bool __IsJckScrew(this BasePart part)
#         {
#             return part.Leaf.ToLower().EndsWith("-jck-screw");
#         }

#         public static bool __IsJckScrewTsg(this BasePart part)
#         {
#             return part.Leaf.ToLower().EndsWith("-jck-screw-tsg");
#         }

#         public static bool __IsShcs(this BasePart part)
#         {
#             return part.Leaf.ToLower().Contains("-shcs-");
#         }

#         public static bool __IsFastener(this BasePart part)
#         {
#             return part.__IsDwl()
#                 || part.__IsJckScrew()
#                 || part.__IsJckScrewTsg()
#                 || part.__IsShcs();
#         }

#         public static bool __IsDwl(this BasePart part)
#         {
#             return part.Leaf.ToLower().Contains("-dwl-");
#         }

#         public static void __SetStringAttribute(this BasePart part, string title, string value)
#         {
#             part.SetUserAttribute(title, -1, value, Update.Option.Now);
#         }

#         /// <summary>
#         ///     Returns all objects in a given part on all layers regardless of their
#         ///     current status or displayability.This includes temporary (system created) objects.
#         ///     It does not return expressions.
#         ///     This function returns the tag of the object that was found. To continue
#         ///     cycling, pass the returned object in as the second argument to this
#         ///     function.
#         ///     NOTE: You are strongly advised to avoid doing anything to non-alive
#         ///     objects unless you are familiar with their use.NX may delete or reuse
#         ///     these objects at any time. Some of these objects do not get filed with
#         ///     the part.
#         ///     NOTE: This routine is invalid for partially loaded parts.If you call this
#         ///     function using a partially loaded part, it returns a NULL_TAG from
#         ///     the beginning of the cycle.
#         ///     Do not attempt to delete objects when cycling the database in a loop. Problems
#         ///     can occur when trying to read the next object when the current object has been
#         ///     deleted. To delete objects, save an array with the objects in it, and then
#         ///     when you have completed cycling, use UF_OBJ_delete_array_of_objects to delete
#         ///     the saved array of objects.
#         /// </summary>
#         /// <param name="part"></param>
#         /// <param name="_object"></param>
#         /// <returns></returns>
#         [Obsolete(nameof(NotImplementedException))]
#         public static TaggedObject[] __CycleAll(this BasePart part)
#         {
#             //var objects = new List<NXOpen.TaggedObject>();

#             //ufsession_.Obj.CycleAll

#             throw new NotImplementedException();
#         }

#         //public static BodyDumbRule __CreateRuleBodyDumb(this BasePart part, params Body[] bodies)
#         //{
#         //    if (bodies.Length == 0)
#         //        throw new ArgumentException($"Cannot create rule from 0 {nameof(bodies)}.", nameof(bodies));

#         //    return part.ScRuleFactory.CreateRuleBodyDumb(bodies);
#         //}

#         public static CurveDumbRule __CreateRuleCurveDumb(this BasePart part, params Curve[] curves)
#         {
#             if (curves.Length == 0)
#                 throw new ArgumentException(
#                     $"Cannot create rule from 0 {nameof(curves)}.",
#                     nameof(curves)
#                 );

#             return part.ScRuleFactory.CreateRuleCurveDumb(curves);
#         }

#         public static EdgeDumbRule __CreateRuleEdgeDumb(this BasePart part, params Edge[] edges)
#         {
#             if (edges.Length == 0)
#                 throw new ArgumentException(
#                     $"Cannot create rule from 0 {nameof(edges)}.",
#                     nameof(edges)
#                 );

#             return part.ScRuleFactory.CreateRuleEdgeDumb(edges);
#         }

#         //public static FaceDumbRule __CreateRuleFaceDumb(this BasePart part, params Face[] faces)
#         //{
#         //    if (faces.Length == 0)
#         //        throw new ArgumentException($"Cannot create rule from 0 {nameof(faces)}.", nameof(faces));

#         //    return part.ScRuleFactory.CreateRuleFaceDumb(faces);
#         //}

#         public static EdgeFeatureRule __CreateRuleEdgeFeature(
#             this BasePart part,
#             params Feature[] features
#         )
#         {
#             if (features.Length == 0)
#                 throw new ArgumentException(
#                     $"Cannot create rule from 0 {nameof(features)}.",
#                     nameof(features)
#                 );

#             return part.ScRuleFactory.CreateRuleEdgeFeature(features);
#         }

#         public static FaceFeatureRule __CreateRuleFaceFeature(
#             this BasePart part,
#             params Feature[] features
#         )
#         {
#             if (features.Length == 0)
#                 throw new ArgumentException(
#                     $"Cannot create rule from 0 {nameof(features)}.",
#                     nameof(features)
#                 );

#             return part.ScRuleFactory.CreateRuleFaceFeature(features);
#         }

#         public static CurveFeatureRule __CreateRuleCurveFeature(
#             this BasePart part,
#             params Feature[] features
#         )
#         {
#             if (features.Length == 0)
#                 throw new ArgumentException(
#                     $"Cannot create rule from 0 {nameof(features)}.",
#                     nameof(features)
#                 );

#             return part.ScRuleFactory.CreateRuleCurveFeature(features);
#         }

#         public static CurveFeatureChainRule __CreateRuleCurveFeatureChain(
#             this BasePart part,
#             Feature[] features,
#             Curve startCurve,
#             Curve endCurve = null,
#             bool isFromSeedStart = true,
#             double gapTolerance = 0.001
#         )
#         {
#             if (features.Length == 0)
#                 throw new ArgumentException(
#                     $@"Cannot create rule from 0 {nameof(features)}.",
#                     nameof(features)
#                 );

#             return part.ScRuleFactory.CreateRuleCurveFeatureChain(
#                 features,
#                 startCurve,
#                 endCurve,
#                 isFromSeedStart,
#                 gapTolerance
#             );
#         }

#         public static Arc __CreateCircle0(this BasePart part, Point3d origin, double radius)
#         {
#             part.__AssertIsWorkPart();

#             var builder = part.BaseFeatures.CreateAssociativeArcBuilder((AssociativeArc)null);

#             using (builder.__UsingBuilder())
#             {
#                 // Point point1 = __work_part_.Points.CreatePoint(__display_part_.WCS.Origin);
#                 builder.CenterPoint.Value = part.Points.CreatePoint(origin);
#                 builder.EndPointOptions = AssociativeArcBuilder.EndOption.Radius;
#                 builder.Limits.FullCircle = true;
#                 builder.Type = AssociativeArcBuilder.Types.ArcFromCenter;
#                 builder.Radius.SetFormula($"{radius}");
#                 builder.Associative = false;
#                 builder.Commit();
#                 return (Arc)builder.GetCommittedObjects()[0];
#             }
#         }

#         /// <summary>Constructs a circle from center, rotation matrix, radius</summary>
#         /// <param name="center">Center point (in absolute coordinates)</param>
#         /// <param name="matrix">Orientation matrix</param>
#         /// <param name="radius">Radius</param>
#         /// <returns>A <see cref="Arc_">Arc_</see> object</returns>
#         public static Arc __CreateCircle(
#             this BasePart part,
#             Point3d center,
#             Matrix3x3 matrix,
#             double radius
#         )
#         {
#             return part.__CreateArc(center, matrix.__AxisX(), matrix.__AxisY(), radius, 0, 360);
#             //return part.__CreateArc(center, matrix.__AxisX(), matrix.__AxisY(), radius, 0 * System.Math.PI / 180.0, 360 * System.Math.PI / 180.0);
#         }

#         /// <summary>Creates an NX.Arc from center, axes, radius, angles in degrees</summary>
#         /// <param name="center">Center point (in absolute coordinates)</param>
#         /// <param name="axisX">Unit NXOpen.Vector3d along X-axis (where angle = 0)</param>
#         /// <param name="axisY">Unit NXOpen.Vector3d along Y-axis (where angle = 90)</param>
#         /// <param name="radius">Radius</param>
#         /// <param name="angle1">Start angle (in degrees)</param>
#         /// <param name="angle2">End angle (in degrees)</param>
#         /// <returns>An NX.Arc object</returns>
#         public static Arc __CreateArc(
#             this BasePart basePart,
#             Point3d center,
#             Vector3d axisX,
#             Vector3d axisY,
#             double radius,
#             double angle1,
#             double angle2
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             double radians1 = __DegreesToRadians(angle1);
#             double radians2 = __DegreesToRadians(angle2);
#             Matrix3x3 ori = axisX.__ToMatrix3x3(axisY);
#             NXMatrix matrix = basePart.NXMatrices.Create(ori);
#             return basePart.Curves.CreateArc(center, matrix, radius, radians1, radians2);
#         }

#         public static void __CreateInterpartExpression(
#             this BasePart part,
#             Expression sourceExpression,
#             string destinationName
#         )
#         {
#             if (part.Tag != __display_part_.Tag)
#                 throw new Exception("Part must be displayed part to create interpart expressions");

#             InterpartExpressionsBuilder builder =
#                 __display_part_.Expressions.CreateInterpartExpressionsBuilder();

#             using (new Destroyer(builder))
#             {
#                 builder.SetExpressions(new[] { sourceExpression }, new[] { destinationName });
#                 builder.Commit();
#             }
#         }

def part_cre_constraint_distance_occ_pro(
        part:Part,
        occ_plane,#:DatumPlane, 
        pro_plane,#:DatumPlane, 
        distance_or_expression:str
    ):# ->ComponentConstraint:

#         public static ComponentConstraint __ConstrainOccProtoDistance(
#             this BasePart part,
#             DatumPlane occPlane,
#             DatumPlane protoPlane,
#             string distanceOrExpressionName
#         )
#         {
#             if (__work_part_.Tag != __display_part_.Tag)
#                 throw new Exception("Display part must be Work part");

#             if (!occPlane.IsOccurrence)
#                 throw new Exception("Occurrence plane for constraint was actually a prototype.");

#             if (protoPlane.IsOccurrence)
#                 throw new Exception("Prototype plane for constraint was actually an occurrence.");

#             part.__AssertIsDisplayPart();
#             UndoMarkId markId3 = session_.SetUndoMark(MarkVisibility.Visible, "Start");
#             ComponentPositioner componentPositioner1 = part.ComponentAssembly.Positioner;
#             componentPositioner1.ClearNetwork();
#             componentPositioner1.BeginAssemblyConstraints();
#             Network componentNetwork1 = componentPositioner1.EstablishNetwork();
#             ComponentConstraint componentConstraint1 = (ComponentConstraint)
#                 componentPositioner1.CreateConstraint(true);
#             componentConstraint1.ConstraintType = Constraint.Type.Distance;
#             componentConstraint1.__CreateConstRefOcc(occPlane);
#             componentConstraint1.__CreateConstRefProto(protoPlane);
#             componentConstraint1.SetExpression(distanceOrExpressionName);
#             componentNetwork1.AddConstraint(componentConstraint1);
#             componentNetwork1.Solve();
#             componentPositioner1.ClearNetwork();
#             session_.UpdateManager.AddToDeleteList(componentNetwork1);
#             session_.UpdateManager.DoUpdate(markId3);
#             componentPositioner1.EndAssemblyConstraints();
#             session_.DisplayManager.BlankObjects(
#                 new DisplayableObject[] { componentConstraint1.GetDisplayedConstraint() }
#             );
#             return componentConstraint1;
#         }
    pass

#         /// <summary>
#         ///     Creates a TrimBody feature by trimming with a face
#         /// </summary>
#         /// <param name="part">The part to create the feature in</param>
#         /// <param name="targetBody">The target body to be trimmed</param>
#         /// <param name="toolFace">The face used to trim the target body</param>
#         /// <param name="direction">Trim direction. The default direction is the normal of the face.</param>
#         /// <returns>A Snap.NX.TrimBody object</returns>
#         public static TrimBody2 __CreateTrimBody(
#             this BasePart part,
#             Body targetBody,
#             Face toolFace,
#             bool direction
#         )
#         {
#             part.__AssertIsWorkPart();
#             TrimBody2Builder trimBody2Builder = part.Features.CreateTrimBody2Builder(null);

#             using (session_.__UsingBuilderDestroyer(trimBody2Builder))
#             {
#                 trimBody2Builder.Tolerance = DistanceTolerance;
#                 trimBody2Builder.BooleanTool.ExtrudeRevolveTool.ToolSection.DistanceTolerance =
#                     DistanceTolerance;
#                 trimBody2Builder.BooleanTool.ExtrudeRevolveTool.ToolSection.ChainingTolerance =
#                     ChainingTolerance;
#                 ScCollector scCollector = part.ScCollectors.CreateCollector();
#                 Body[] bodies = new Body[1] { targetBody };
#                 BodyDumbRule bodyDumbRule = part.ScRuleFactory.CreateRuleBodyDumb(bodies);
#                 SelectionIntentRule[] rules = new SelectionIntentRule[1] { bodyDumbRule };
#                 scCollector.ReplaceRules(rules, false);
#                 trimBody2Builder.TargetBodyCollector = scCollector;
#                 SelectionIntentRule[] rules2 = new SelectionIntentRule[1]
#                 {
#                     part.ScRuleFactory.CreateRuleFaceBody(toolFace.GetBody())
#                 };
#                 trimBody2Builder.BooleanTool.FacePlaneTool.ToolFaces.FaceCollector.ReplaceRules(
#                     rules2,
#                     false
#                 );
#                 trimBody2Builder.BooleanTool.ReverseDirection = direction;
#                 return (TrimBody2)trimBody2Builder.Commit();
#             }
#         }

#         public static CartesianCoordinateSystem __AbsoluteCsys(this BasePart part)
#         {
#             ufsession_.Modl.AskDatumCsysComponents(
#                 part.__AbsoluteDatumCsys().Tag,
#                 out Tag csysTag,
#                 out _,
#                 out _,
#                 out _
#             );
#             return (CartesianCoordinateSystem)session_.__GetTaggedObject(csysTag);
#         }

#         public static void __ReplaceRefSets(
#             this BasePart part,
#             Component[] components,
#             string refsetName
#         )
#         {
#             part.ComponentAssembly.ReplaceReferenceSetInOwners(refsetName, components);
#         }

#         public static Expression __FindExpression(this BasePart part, string expressionName)
#         {
#             try
#             {
#                 return part.Expressions.FindObject(expressionName);
#             }
#             catch (NXException ex) when (ex.ErrorCode == 3520016)
#             {
#                 throw NXException.Create(
#                     ex.ErrorCode,
#                     $"Could not find expression '{expressionName}' in part {part.Leaf}"
#                 );
#             }
#         }

def part_fit(part:Part)->None:
    part.ModelingViews.WorkView.Fit()


#         public static void __RightClickOpenAssemblyWhole(this BasePart part)
#         {
#             if (session_.Parts.Display is null)
#                 throw new Exception("There is no open display part to right click open assembly");

#             if (__work_part_.Tag != __display_part_.Tag)
#                 throw new Exception("DisplayPart does not equal __work_part_");

#             if (__display_part_.Tag != part.Tag)
#                 throw new Exception($"Part {part.Leaf} is not the current display part");

#             __display_part_.ComponentAssembly.OpenComponents(
#                 ComponentAssembly.OpenOption.WholeAssembly,
#                 new[] { part.ComponentAssembly.RootComponent },
#                 out _
#             );
#         }


#         /// <summary>Constructs a NXOpen.Arc from center, axes, radius, angles</summary>
#         /// <param name="center">Center point (in absolute coordinates)</param>
#         /// <param name="axisX">Unit vector along X-axis (where angle = 0)</param>
#         /// <param name="axisY">Unit vector along Y-axis (where angle = 90)</param>
#         /// <param name="radius">Radius</param>
#         /// <param name="angle1">Start angle (in degrees)</param>
#         /// <param name="angle2">End angle (in degrees)</param>
#         /// <returns> A <see cref="Arc">NXOpen.Arc</see> object</returns>
#         internal static Arc __CreateArc1(
#             this BasePart basePart,
#             Point3d center,
#             Vector3d axisX,
#             Vector3d axisY,
#             double radius,
#             double angle1,
#             double angle2
#         )
#         {
#             basePart.__AssertIsWorkPart();
#             double startAngle = __DegreesToRadians(angle1);
#             double endAngle = __DegreesToRadians(angle2);
#             return __work_part_.Curves.CreateArc(
#                 center,
#                 axisX,
#                 axisY,
#                 radius,
#                 startAngle,
#                 endAngle
#             );
#         }

#         public static PartCollection.SdpsStatus __SetActiveDisplay(this BasePart part)
#         {
#             if (
#                 session_.Parts.AllowMultipleDisplayedParts
#                 != PartCollection.MultipleDisplayedPartStatus.Enabled
#             )
#                 throw new Exception("Session does not allow multiple displayed parts");

#             return session_.Parts.SetActiveDisplay(
#                 part,
#                 DisplayPartOption.AllowAdditional,
#                 PartDisplayPartWorkPartOption.UseLast,
#                 out _
#             );
#         }

#         /// <summary>Constructs a fillet arc from three points</summary>
#         /// <param name="p0">First point</param>
#         /// <param name="pa">Apex point</param>
#         /// <param name="p1">Last point</param>
#         /// <param name="radius">Radius</param>
#         /// <returns>A Geom.Arc representing the fillet</returns>
#         /// <remarks>
#         ///     <para>
#         ///         The fillet will be tangent to the lines p0-pa and pa-p1.
#         ///         Its angular span will we be less than 180 degrees.
#         ///     </para>
#         /// </remarks>
#         [Obsolete]
#         public static Arc __CreateFillet(
#             this BasePart part,
#             Point3d p0,
#             Point3d pa,
#             Point3d p1,
#             double radius
#         )
#         {
#             //NXOpen.Vector3d vector = p0._Subtract(pa)._Unit();
#             //NXOpen.Vector3d vector2 = p1._Subtract(pa)._Unit();
#             //NXOpen.Vector3d vector3 = vector._Add(vector2);
#             //double num = vector._Angle(vector2) / 2.0;
#             //double num2 = radius / Math.SinD(num);
#             //NXOpen.Point3d center = vector3._Multiply(num2)._Add(pa);
#             //NXOpen.Vector3d vector4 = vector3._Negate();
#             //NXOpen.Vector3d vector5 = vector2._Subtract(vector)._Unit();
#             //double num3 = 90.0 - num;
#             //double startAngle = 0.0 - num3;
#             //double endAngle = num3;
#             //return part.__CreateArc(center, vector4, vector5, radius, startAngle, endAngle);
#             throw new NotImplementedException();
#         }

#         ///// <summary>Creates a datum axis with a given origin and direction</summary>
#         ///// <param name="origin">The origin of the datum axis</param>
#         ///// <param name="direction">The direction of the datum axis</param>
#         ///// <returns> A <see cref="T:Snap.NX.DatumAxis">Snap.NX.DatumAxis</see> object</returns>
#         //[Obsolete(nameof(NotImplementedException))]
#         //public static DatumAxisFeature __CreateDatumAxis(this BasePart part,
#         //    Point3d origin, Vector3d direction)
#         //{
#         //    //return CreateDatumAxis(origin, direction);
#         //    throw new NotImplementedException();
#         //}

#         public static NXMatrix __CreateNXMatrix(this BasePart basePart, Matrix3x3 matrix)
#         {
#             return basePart.NXMatrices.Create(matrix);
#         }

#         internal static SelectionIntentRule[] __CreateSelectionIntentRule(
#             this BasePart basePart,
#             params ICurve[] icurves
#         )
#         {
#             List<SelectionIntentRule> list = new List<SelectionIntentRule>();

#             for (int i = 0; i < icurves.Length; i++)
#                 if (icurves[i] is Curve curve)
#                 {
#                     Curve[] curves = new Curve[1] { curve };
#                     CurveDumbRule item = basePart.ScRuleFactory.CreateRuleCurveDumb(curves);
#                     list.Add(item);
#                 }
#                 else
#                 {
#                     Edge[] edges = new Edge[1] { (Edge)icurves[i] };
#                     EdgeDumbRule item2 = basePart.ScRuleFactory.CreateRuleEdgeDumb(edges);
#                     list.Add(item2);
#                 }

#             return list.ToArray();
#         }

#         public static CoordinateSystem __CreateCsys(this BasePart basePart, Vector3d vector3D)
#         {
#             NXMatrix orientation = basePart.__CreateNXMatrix(vector3D.__ToMatrix3x3());

#             return basePart.__CreateCoordinateSystem(_Point3dOrigin, orientation);
#         }

#         /// <summary>Creates an extrude feature</summary>
#         /// <param name="section">The "section" to be extruded</param>
#         /// <param name="axis">Extrusion direction (vector magnitude not significant)</param>
#         /// <param name="extents">Extents of the extrusion (measured from input curves)</param>
#         /// <param name="draftAngle">Draft angle, in degrees (positive angle gives larger sections in direction of<br />axis)</param>
#         /// <param name="offset">If true, means that offset values are being provided</param>
#         /// <param name="offsetValues">Offset distances for section curves</param>
#         /// <param name="createSheet">If true, forces creation of a sheet body</param>
#         /// <returns>An NX.Extrude object</returns>
#         internal static Extrude __CreateExtrude(
#             this BasePart basePart,
#             Section section,
#             Vector3d axis,
#             double[] extents,
#             double draftAngle,
#             bool offset,
#             double[] offsetValues,
#             bool createSheet
#         )
#         {
#             Part part = __work_part_;
#             ExtrudeBuilder extrudeBuilder = part.Features.CreateExtrudeBuilder(null);
#             extrudeBuilder.DistanceTolerance = DistanceTolerance;
#             extrudeBuilder.BooleanOperation.Type = BooleanOperation.BooleanType.Create;

#             if (createSheet)
#                 extrudeBuilder.FeatureOptions.BodyType = FeatureOptions.BodyStyle.Sheet;

#             extrudeBuilder.Limits.StartExtend.Value.RightHandSide = extents[0].ToString();
#             extrudeBuilder.Limits.EndExtend.Value.RightHandSide = extents[1].ToString();
#             extrudeBuilder.Offset.Option = Type.NoOffset;

#             if (offset)
#             {
#                 extrudeBuilder.Offset.Option = Type.NonsymmetricOffset;
#                 extrudeBuilder.Offset.StartOffset.RightHandSide = offsetValues[0].ToString();
#                 extrudeBuilder.Offset.EndOffset.RightHandSide = offsetValues[1].ToString();
#             }

#             double num = double.Parse(draftAngle.ToString());

#             extrudeBuilder.Draft.DraftOption =
#                 System.Math.Abs(num) < 0.001
#                     ? SimpleDraft.SimpleDraftType.NoDraft
#                     : SimpleDraft.SimpleDraftType.SimpleFromProfile;

#             extrudeBuilder.Draft.FrontDraftAngle.RightHandSide = $"{num}";
#             extrudeBuilder.Section = section;
#             Point3d origin = new Point3d(30.0, 0.0, 0.0);
#             Vector3d vector = new Vector3d(axis.X, axis.Y, axis.Z);
#             Direction direction = part.Directions.CreateDirection(
#                 origin,
#                 vector,
#                 SmartObject.UpdateOption.WithinModeling
#             );
#             extrudeBuilder.Direction = direction;
#             Extrude extrude = (Extrude)extrudeBuilder.CommitFeature();
#             extrudeBuilder.Destroy();
#             return extrude;
#         }

#         public static bool __TryDynamicBlock(this BasePart basePart, out Block dynamic)
#         {
#             dynamic = basePart.Features.OfType<Block>().Single(f => f.Name == "DYNAMIC BLOCK");
#             return !(dynamic is null);
#         }

#         public static Extrude _CreateExtrusionFromClosedConic(
#             this BasePart part,
#             Conic conic,
#             double startExtend,
#             double endExtend,
#             Sense sense = NXOpen.Sense.Forward
#         )
#         {
#             // Checks to make sure that the {conic} is closed.
#             if (!conic.__IsClosed())
#                 throw new InvalidOperationException("The given conic curve is not closed.");

#             // Creates a direction based on the {conic}.
#             Direction direction = part.Directions.CreateDirection(
#                 conic,
#                 sense,
#                 SmartObject.UpdateOption.WithinModeling
#             );

#             // Creates the section from the single {conic}.
#             Section section = part.Sections.CreateSection(conic);

#             // Creates the extrusion.
#             return part.__CreateExtrusion(direction, section, startExtend, endExtend);
#         }

#         public static Extrude __CreateExtrusion(
#             this BasePart part,
#             Direction direction,
#             Section section,
#             double startExtend,
#             double endExtend
#         )
#         {
#             ExtrudeBuilder builder = part.Features.CreateExtrudeBuilder(null);
#             using (new Destroyer(builder))
#             {
#                 // We need to match the units of the {builder} to be the units of the {owningPart}.
#                 builder.Limits.StartExtend.Value.Units = part.UnitCollection.FindObject(
#                     part.PartUnits == NXOpen.BasePart.Units.Millimeters ? "MilliMeter" : "Inch"
#                 );
#                 builder.Limits.EndExtend.Value.Units = part.UnitCollection.FindObject(
#                     part.PartUnits == NXOpen.BasePart.Units.Millimeters ? "MilliMeter" : "Inch"
#                 );
#                 builder.BooleanOperation.Type = NXOpen
#                     .GeometricUtilities
#                     .BooleanOperation
#                     .BooleanType
#                     .Create;
#                 builder.BooleanOperation.SetTargetBodies(new Body[0]);
#                 builder.Offset.Option = NXOpen.GeometricUtilities.Type.NoOffset;
#                 builder.FeatureOptions.BodyType = NXOpen
#                     .GeometricUtilities
#                     .FeatureOptions
#                     .BodyStyle
#                     .Solid;
#                 builder.Draft.DraftOption = NXOpen
#                     .GeometricUtilities
#                     .SimpleDraft
#                     .SimpleDraftType
#                     .NoDraft;
#                 builder.Direction = direction;
#                 builder.Limits.SymmetricOption = false;
#                 builder.Limits.StartExtend.TrimType = NXOpen
#                     .GeometricUtilities
#                     .Extend
#                     .ExtendType
#                     .Value;
#                 builder.Limits.StartExtend.Value.RightHandSide = $"{startExtend}";
#                 builder.Limits.EndExtend.TrimType = NXOpen
#                     .GeometricUtilities
#                     .Extend
#                     .ExtendType
#                     .Value;
#                 builder.Limits.EndExtend.Value.RightHandSide = $"{endExtend}";
#                 builder.Section = section;
#                 return (Extrude)builder.Commit();
#             }
#         }


def part_get_units_in(part:Part):#->Unit:
    return part.UnitCollection.FindObject('Inch')
    

def part_get_units_mm(part:Part):#->Unit:
    return part.UnitCollection.FindObject('MilliMeter')



#         public static OffsetFace __CreateOffsetFace(
#             this BasePart part,
#             Face[] faces,
#             string exp_name
#         )
#         {
#             part.__AssertIsWorkPart();
#             var builder = __work_part_.Features.CreateOffsetFaceBuilder(null);

#             using (builder.__UsingBuilder())
#             {
#                 builder.FaceCollector.ReplaceRules(
#                     new[] { __work_part_.ScRuleFactory.CreateRuleFaceDumb(faces) },
#                     false
#                 );

#                 builder.Distance.SetFormula(exp_name);
#                 return (OffsetFace)builder.Commit();
#             }
#         }

#         public static void __Data(
#             this Block block,
#             out Point3d origin,
#             out Matrix3x3 orientation,
#             out double length,
#             out double width,
#             out double height
#         )
#         {
#             block.__OwningPart().__AssertIsWorkPart();
#             var builder = block.__OwningPart().Features.CreateBlockFeatureBuilder(block);

#             using (builder.__UsingBuilder())
#             {
#                 origin = builder.Origin;
#                 builder.GetOrientation(out var xaxis, out var yaxis);
#                 orientation = xaxis.__ToMatrix3x3(yaxis);
#                 length = builder.Length.Value;
#                 width = builder.Width.Value;
#                 height = builder.Height.Value;
#             }
#         }



#         public static Line __CreateLine(this BasePart part, Point3d start, Point3d end)
#         {
#             var line = part.Curves.CreateLine(start, end);
#             line.SetVisibility(SmartObject.VisibilityOption.Visible);
#             line.RedisplayObject();
#             return line;
#         }

#         public static Line __CreateLine(this BasePart part, Point start, Point end)
#         {
#             var line = part.Curves.CreateLine(start, end);
#             line.SetVisibility(SmartObject.VisibilityOption.Visible);
#             line.RedisplayObject();
#             return line;
#         }

#         public static Plane __CreatePlane(this BasePart part, Point3d origin, Matrix3x3 matrix)
#         {
#             return part.Planes.CreateFixedPlane(origin, matrix);
#         }

#         public static Axis __CreateAxis(this BasePart part, Point point, Direction direction)
#         {
#             return part.Axes.CreateAxis(point, direction, SmartObject.UpdateOption.WithinModeling);
#         }

#         public static Axis __CreateAxis(this BasePart part, Point3d point, Vector3d direction)
#         {
#             return part.Axes.CreateAxis(point, direction, SmartObject.UpdateOption.WithinModeling);
#         }

#         public static UserDefinedObject[] __DynamicHandles(this BasePart part)
#         {
#             UserDefinedClass myUdOclass =
#                 session_.UserDefinedClassManager.GetUserDefinedClassFromClassName(
#                     "UdoDynamicHandle"
#                 );

#             return part.UserDefinedObjectManager.GetUdosOfClass(myUdOclass);
#         }
#         public static bool __TryModleingView(this BasePart part, string name, out ModelingView view)
#         {
#             view = part.__ModelingViews(name);

#             return !(view is null);
#         }

#         public static ModelingView[] __ModelingViews(this BasePart part)
#         {
#             return part.ModelingViews.ToArray();
#         }

#         public static ModelingView __ModelingViews(this BasePart part, string name)
#         {
#             return part.__ModelingViews().FirstOrDefault(mod => mod.Name == name);
#         }

#         public static Tuple<Scalar, Expression> __CreateScalarNumberLengthExpression(
#             this BasePart part,
#             string expressionString)
#         {
#             Expression exp = part.Expressions.CreateExpression("Number", expressionString);

#             Scalar scalar = part.Scalars.CreateScalarExpression(
#                 exp,
#                 Scalar.DimensionalityType.Length,
#                 SmartObject.UpdateOption.AfterParentBody
#             );

#             return Tuple.Create(scalar, exp);
#         }

#         public static Point __CreatePoint(this BasePart part, double[] array)
#         {
#             Point p = part.Points.CreatePoint(array.__ToPoint3d());
#             p.SetVisibility(SmartObject.VisibilityOption.Visible);
#             return p;
#         }

#         public static Point __CreatePoint(this BasePart part, double x, double y, double z)
#         {
#             return part.__CreatePoint(new double[] { x, y, z });
#         }

#         public static PointFeature __CreatePointFeature(this BasePart basePart, Point3d point3D)
#         {
#             Point point = basePart.__CreatePoint(point3D);
#             PointFeatureBuilder builder = basePart.BaseFeatures.CreatePointFeatureBuilder(null);

#             using (session_.__UsingBuilderDestroyer(builder))
#             {
#                 builder.Point = point;
#                 return (PointFeature)builder.Commit();
#             }
#         }

#         public static Point __CreatePoint(this BasePart basePart, double x, double y) => basePart.__CreatePoint(x, y, 0.0);

#         public static Point __CreatePoint(this BasePart part, Point3d point3D)
#         {
#             Point p = part.Points.CreatePoint(point3D);
#             p.SetVisibility(SmartObject.VisibilityOption.Visible);
#             return p;
#         }

#         #endregion


#            #region Block

#    [Obsolete(nameof(NotImplementedException))]
#    public static Block __Mirror(this Block block, Surface.Plane plane)
#    {
#        Point3d origin = block.__Origin().__Mirror(plane);
#        Matrix3x3 orientation = block.__Orientation().__Mirror(plane);
#        double length = block.__Width();
#        double width = block.__Length();
#        double height = block.__Height();
#        BlockFeatureBuilder builder = block
#            .__OwningPart()
#            .Features.CreateBlockFeatureBuilder(null);

#        using (session_.__UsingBuilderDestroyer(builder))
#        {
#            builder.Length.Value = length;
#            builder.Width.Value = width;
#            builder.Height.Value = height;
#            builder.Origin = origin;
#            builder.SetOrientation(orientation.__AxisX(), orientation.__AxisY());
#            return (Block)builder.Commit();
#        }
#    }

#    [Obsolete(nameof(NotImplementedException))]
#    public static Block __Mirror(
#        this Block block,
#        Surface.Plane plane,
#        Component from,
#        Component to
#    )
#    {
#        throw new NotImplementedException();
#    }

#    public static Point3d __Origin(this Block block)
#    {
#        BlockFeatureBuilder builder = block.OwningPart.Features.CreateBlockFeatureBuilder(
#            block
#        );

#        using (session_.__UsingBuilderDestroyer(builder))
#        {
#            return builder.Origin;
#        }
#    }

#    public static Matrix3x3 __Orientation(this Block block)
#    {
#        BlockFeatureBuilder builder = block.OwningPart.Features.CreateBlockFeatureBuilder(
#            block
#        );

#        using (session_.__UsingBuilderDestroyer(builder))
#        {
#            builder.GetOrientation(out Vector3d xAxis, out Vector3d yAxis);
#            return xAxis.__ToMatrix3x3(yAxis);
#        }
#    }

#    public static double __Length(this Block block)
#    {
#        BlockFeatureBuilder builder = block
#            .__OwningPart()
#            .Features.CreateBlockFeatureBuilder(block);

#        using (session_.__UsingBuilderDestroyer(builder))
#        {
#            return builder.Length.Value;
#        }
#    }

#    public static double __Width(this Block block)
#    {
#        BlockFeatureBuilder builder = block
#            .__OwningPart()
#            .Features.CreateBlockFeatureBuilder(block);

#        using (session_.__UsingBuilderDestroyer(builder))
#        {
#            return builder.Width.Value;
#        }
#    }

#    public static double __Height(this Block block)
#    {
#        BlockFeatureBuilder builder = block
#            .__OwningPart()
#            .Features.CreateBlockFeatureBuilder(block);

#        using (session_.__UsingBuilderDestroyer(builder))
#        {
#            return builder.Height.Value;
#        }
#    }

#    public static void __Update(
#        this Block block,
#        Point3d origin,
#        string length,
#        string width,
#        string height
#    )
#    {
#        block.__OwningPart().__AssertIsWorkPart();

#        BlockFeatureBuilder builder = block.__OwningPart()
#                .Features
#                .CreateBlockFeatureBuilder(block);

#        using (session_.__UsingBuilderDestroyer(builder))
#        {
#            builder.SetOriginAndLengths(origin, length, width, height);
#            builder.Commit();
#        }
#    }

#    public static Expression __Dimension(this Block block, int _dim_012)
#    {
#        var builder = block.__OwningPart().Features.CreateBlockFeatureBuilder(block);

#        using (builder.__UsingBuilder())
#            switch (_dim_012)
#            {
#                case 0:
#                    return builder.Length;
#                case 1:
#                    return builder.Width;
#                case 2:
#                    return builder.Height;
#                default:
#                    throw new ArgumentOutOfRangeException();
#            }
#    }

#    #endregion


#     #region Body

#  public static void __NXOpenBody(Body body)
#  {
#      //body.Density
#      //body.GetEdges
#      //body.GetFaces
#      //body.GetFeatures
#      //body.IsConvergentBody
#      //body.IsSheetBody
#      //body.IsSolidBody
#      //body.OwningPart.Features.GetAssociatedFeaturesOfBody
#      //body.OwningPart.Features.GetParentFeatureOfBody
#  }

#  public static Box3d __Box3d(this Body body)
#  {
#      double[] minCorner = new double[3];
#      double[,] directions = new double[3, 3];
#      double[] distances = new double[3];

#      Tag tag = body.Tag;
#      ufsession_.Modl.AskBoundingBoxExact(tag, Tag.Null, minCorner, directions, distances);
#      Point3d position = minCorner.__ToPoint3d();
#      Vector3d vector = new Vector3d(directions[0, 0], directions[0, 1], directions[0, 2]);
#      Vector3d vector2 = new Vector3d(directions[1, 0], directions[1, 1], directions[1, 2]);
#      Vector3d vector3 = new Vector3d(directions[2, 0], directions[2, 1], directions[2, 2]);

#      Point3d maxXYZ = position.__Add(vector.__Multiply(distances[0]))
#          .__Add(vector2.__Multiply(distances[1]))
#          .__Add(vector3.__Multiply(distances[2]));

#      return new Box3d(position, maxXYZ);
#  }

#  public static BooleanFeature __Subtract(this Body target, params Body[] toolBodies)
#  {
#      return target.OwningPart.__CreateBoolean(target, toolBodies, Feature.BooleanType.Subtract);
#  }

#  public static BooleanFeature __Intersect(this Body target, params Body[] toolBodies)
#  {
#      return target.OwningPart.__CreateBoolean(target, toolBodies, Feature.BooleanType.Intersect);
#  }

#  public static BooleanFeature __Unite(this Body target, params Body[] toolBodies)
#  {
#      return target.OwningPart.__CreateBoolean(target, toolBodies, Feature.BooleanType.Unite);
#  }

#  public static Body __Prototype(this Body body)
#  {
#      return (Body)body.Prototype;
#  }

#  public static bool __InterferesWith(this Body target, Component component)
#  {
#      if (target.OwningPart.Tag != component.OwningPart.Tag)
#          throw new ArgumentException("Body and component are not in the same assembly.");

#      return target.__InterferesWith(component.__SolidBodyMembers());
#  }

#  public static bool __InterferesWith(this Body target, params Body[] toolBodies)
#  {
#      //if (toolBodies.Any(__b=>__b.OwningPart.Tag != target.OwningPart.Tag))
#      //    throw new ArgumentException("At least one tool body is not in the same assembly as the target body.");

#      Tag[] solid_bodies = toolBodies.Select(__b => __b.Tag).ToArray();
#      int[] results = new int[solid_bodies.Length];
#      ufsession_.Modl.CheckInterference(target.Tag, solid_bodies.Length, solid_bodies, results);

#      for (int i = 0; i < solid_bodies.Length; i++)
#          if (results[i] == 1)
#              return true;

#      return false;
#  }

#  public static Face[] __PosXFaces(this Body body)
#  {
#      return body.__FacesWithVector(__Vector3dX());
#  }

#  public static Face __SinglePosXFace(this Body body)
#  {
#      return body.__PosXFaces().Single();
#  }

#  public static Face[] __NegXFaces(this Body body)
#  {
#      return body.__FacesWithVector(__Vector3dX().__Negate());
#  }

#  public static Face __SingleNegXFace(this Body body)
#  {
#      return body.__NegXFaces().Single();
#  }

#  public static Face[] __PosYFaces(this Body body)
#  {
#      return body.__FacesWithVector(__Vector3dY());
#  }

#  public static Face __SinglePosYFace(this Body body)
#  {
#      return body.__PosYFaces().Single();
#  }

#  public static Face[] __NegYFaces(this Body body)
#  {
#      return body.__FacesWithVector(__Vector3dY().__Negate());
#  }

#  public static Face __SingleNegYFace(this Body body)
#  {
#      return body.__NegYFaces().Single();
#  }

#  public static Face[] __PosZFaces(this Body body)
#  {
#      return body.__FacesWithVector(__Vector3dZ());
#  }

#  public static Face __SinglePosZFace(this Body body)
#  {
#      return body.__PosZFaces().Single();
#  }

#  public static Face[] __NegZFaces(this Body body)
#  {
#      return body.__FacesWithVector(__Vector3dZ().__Negate());
#  }

#  public static Face __SingleNegZFace(this Body body)
#  {
#      return body.__NegZFaces().Single();
#  }

#  public static Face[] __FacesWithVector(this Body body, Vector3d vector)
#  {
#      var unit = vector.__Unit();

#      return (
#          from face in body.GetFaces()
#          where face.__IsPlanar()
#          where face.__Normal().__Equals(vector)
#          select face
#      ).ToArray();
#  }

#  public static Feature __ParentFeature(this Body body)
#  {
#      body.__AssertIsPrototype();
#      return body.__OwningPart().Features.GetParentFeatureOfBody(body);
#  }


#  #endregion


#   #region Builder

#  public static Destroyer __UsingBuilder(this Builder builder)
#  {
#      return new Destroyer(builder);
#  }

#  #endregion


#    #region CartesianCoordinateSystem

#   public static DatumPlane __DatumPlaneXZ(this CartesianCoordinateSystem datumCsys)
#   {
#       ufsession_.Modl.AskDatumCsysComponents(datumCsys.Tag, out _, out _, out _, out Tag[] dplanes);
#       return (DatumPlane)session_.__GetTaggedObject(dplanes[2]);
#   }

#   public static DatumPlane __DatumPlaneYZ(this CartesianCoordinateSystem datumCsys)
#   {
#       ufsession_.Modl.AskDatumCsysComponents(datumCsys.Tag, out _, out _, out _, out Tag[] dplanes);
#       return (DatumPlane)session_.__GetTaggedObject(dplanes[1]);
#   }

#   #endregion

#    //__work_plane_.GetPolarGridSize
#  //__work_plane_.GetRectangularNonuniformGridSize
#  //__work_plane_.GetRectangularUniformGridSize
#  //__work_plane_.GridColor
#  //__work_plane_.GridIsNonUniform
#  //__work_plane_.GridOnTop
#  //__work_plane_.GridType
#  //__work_plane_.PolarShowMajorLines
#  //__work_plane_.RectangularShowMajorLines
#  //__work_plane_.SetPolarGridSize
#  //__work_plane_.SetRectangularNonuniformGridSize
#  //__work_plane_.SetRectangularUniformGridSize
#  //__work_plane_.ShowGrid
#  //__work_plane_.ShowLabels
#  //__work_plane_.SnapToGrid

#  public static double __GridSpacing(this NXOpen.Preferences.WorkPlane work_plane)
#  {
#      return work_plane.GetRectangularUniformGridSize().MajorGridSpacing;
#  }

#  public static void __GridSpacing(this NXOpen.Preferences.WorkPlane work_plane, double grid_spacing)
#  {
#      work_plane.SetRectangularUniformGridSize(new NXOpen.Preferences.WorkPlane.GridSize()
#      {
#          MajorGridSpacing = grid_spacing,
#          MinorLinesPerMajor = 1,
#          SnapPointsPerMinor = 1
#      });
#  }

#   #region Collections

#  //[Obsolete(nameof(NotImplementedException))]
#  //public static IDictionary<double, List<Face>> __ToILookIDict<T, K>(
#  //    this IEnumerable<T> objects, Func<T, K> value)
#  //{
#  //    var dict = new Dictionary<double, List<Face>>();

#  //    foreach(var obj in objects)
#  //    {

#  //    }


#  //    throw new NotImplementedException();
#  //}

#  public static IDictionary<TKey, List<TValue>> __ToILookIDict<TKey, TValue>(
#      this IEnumerable<TValue> source,
#      Func<TValue, TKey> keySelector,
#      IEqualityComparer<TKey> keyComparer = null)
#  {
#      // Creates the dictionary with the default equality comparer if one was not provided.
#      Dictionary<TKey, List<TValue>> dictionary =
#          new Dictionary<TKey, List<TValue>>(keyComparer ?? EqualityComparer<TKey>.Default);

#      foreach (TValue value in source)
#      {
#          // Gets the key from the specified key selector.
#          TKey key = keySelector(value);

#          // Checks to see if the dictionary contains the {key}.
#          if (!dictionary.ContainsKey(key))
#              // If it doesn't we need to add it with an initialized {List<TValue>}.
#              dictionary[key] = new List<TValue>();

#          // Adds the current {value} to the specified {key} list.
#          dictionary[key].Add(value);
#      }

#      return dictionary;
#  }

#  public static TSource __MaxBy<TSource>(this IEnumerable<TSource> source, Func<TSource, double> sizeSelector)
#  {
#      TSource max_item = default;
#      double? max = null;

#      foreach (TSource item in source)
#      {
#          var num = sizeSelector(item);

#          if (!(max is null) && !(num > max))
#              continue;

#          max = num;
#          max_item = item;
#      }

#      return max_item;
#  }

#   public static TSource __MinBy<TSource>(this IEnumerable<TSource> source, Func<TSource, double> sizeSelector)
#  {
#      TSource min_item = default;
#      double? min = null;

#      foreach (TSource item in source)
#      {
#          var num = sizeSelector(item);

#          if (!(min is null) && !(num < min))
#              continue;

#          min = num;
#          min_item = item;
#      }

#      return min_item;
#  }

#  #endregion


#   #region Component

#  public static IEnumerable<Component> __DescendantsAll(this Component component)
#  {
#      return from descendant in component.__Descendants(true, true, true) select descendant;
#  }

#  public static IEnumerable<Component> __Descendants(
#      this Component rootComponent,
#      bool includeRoot = true,
#      bool includeSuppressed = false,
#      bool includeUnloaded = false
#  )
#  {
#      if (includeRoot)
#          yield return rootComponent;

#      Component[] children = rootComponent.GetChildren();

#      for (int index = 0; index < children.Length; index++)
#      {
#          if (children[index].IsSuppressed && !includeSuppressed)
#              continue;

#          if (!children[index].__IsLoaded() && !includeUnloaded)
#              continue;

#          foreach (
#              Component descendant in children[index].__Descendants(
#                  includeRoot,
#                  includeSuppressed,
#                  includeUnloaded
#              )
#          )
#              yield return descendant;
#      }
#  }

#  public static bool __IsLoaded(this Component component)
#  {
#      return component.Prototype is Part;
#  }

#  public static IEnumerable<NXObject> __Members(this Component component)
#  {
#      UFSession uFSession = ufsession_;
#      Tag tag = Tag.Null;
#      List<NXObject> list = new List<NXObject>();

#      do
#      {
#          tag = uFSession.Assem.CycleEntsInPartOcc(component.Tag, tag);

#          if (tag == Tag.Null)
#              continue;

#          try
#          {
#              NXObject nXObject = session_.__GetTaggedObject(tag) as NXObject;

#              if (nXObject is null)
#                  continue;

#              list.Add(nXObject);
#          }
#          catch (Exception ex)
#          {
#              ex.__PrintException();
#          }
#      } while (tag != 0);

#      return list;
#  }

#  public static Tag __InstanceTag(this Component component)
#  {
#      return ufsession_.Assem.AskInstOfPartOcc(component.Tag);
#  }

#  public static Component __ProtoChildComp(this Component component)
#  {
#      Tag instance = component.__InstanceTag();
#      Tag root_component = component.OwningComponent
#          .__Prototype()
#          .ComponentAssembly.RootComponent.Tag;
#      Tag proto_child_fastener_tag = ufsession_.Assem.AskPartOccOfInst(
#          root_component,
#          instance
#      );
#      return (Component)session_.__GetTaggedObject(proto_child_fastener_tag);
#  }

#  public static ExtractFace __CreateLinkedBody(this Component child)
#  {
#      WaveLinkBuilder builder = __work_part_.BaseFeatures.CreateWaveLinkBuilder(null);

#      using (session_.__UsingBuilderDestroyer(builder))
#      {
#          builder.ExtractFaceBuilder.ParentPart = ExtractFaceBuilder.ParentPartType.OtherPart;
#          builder.Type = WaveLinkBuilder.Types.BodyLink;
#          builder.ExtractFaceBuilder.Associative = true;
#          ScCollector scCollector1 = builder.ExtractFaceBuilder.ExtractBodyCollector;
#          builder.ExtractFaceBuilder.FeatureOption = ExtractFaceBuilder.FeatureOptionType.OneFeatureForAllBodies;
#          Body[] bodies1 = new Body[1];

#          BodyDumbRule bodyDumbRule1 = __work_part_.ScRuleFactory.CreateRuleBodyDumb(
#              child.__SolidBodyMembers(),
#              false
#          );

#          SelectionIntentRule[] rules1 = new SelectionIntentRule[1];
#          rules1[0] = bodyDumbRule1;
#          scCollector1.ReplaceRules(rules1, false);
#          builder.ExtractFaceBuilder.FixAtCurrentTimestamp = false;
#          return (ExtractFace)builder.Commit();
#      }
#  }

#  public static ExtractFace[] __CreateLinkedBodies(this Component child)
#  {
#      WaveLinkBuilder builder = __work_part_.BaseFeatures.CreateWaveLinkBuilder(null);

#      //var starting_features = __work_part_.Features.ToArray().ToHashSet();


#      using (session_.__UsingBuilderDestroyer(builder))
#      {
#          builder.ExtractFaceBuilder.ParentPart = ExtractFaceBuilder.ParentPartType.OtherPart;
#          builder.Type = WaveLinkBuilder.Types.BodyLink;
#          builder.ExtractFaceBuilder.Associative = true;
#          ScCollector scCollector1 = builder.ExtractFaceBuilder.ExtractBodyCollector;
#          builder.ExtractFaceBuilder.FeatureOption = ExtractFaceBuilder.FeatureOptionType.SeparateFeatureForEachBody;
#          Body[] bodies1 = new Body[1];

#          BodyDumbRule bodyDumbRule1 = __work_part_.ScRuleFactory.CreateRuleBodyDumb(
#              child.__SolidBodyMembers(),
#              false
#          );

#          SelectionIntentRule[] rules1 = new SelectionIntentRule[1];
#          rules1[0] = bodyDumbRule1;
#          scCollector1.ReplaceRules(rules1, false);
#          builder.ExtractFaceBuilder.FixAtCurrentTimestamp = false;
#          builder.Commit();
#          return builder.GetCommittedObjects()
#              .OfType<ExtractFace>()
#              .ToArray();
#      }
#  }

#  //public static bool __IsJckScrewTsg(this Component part)
#  //{
#  //    return part.DisplayName.ToLower().EndsWith("-jck-screw-tsg");
#  //}

#  //public static bool __IsDwl(this Component part)
#  //{
#  //    return part.DisplayName.ToLower().Contains("-dwl-");
#  //}

#  //public static bool __IsJckScrew(this Component part)
#  //{
#  //    return part.DisplayName.ToLower().EndsWith("-jck-screw");
#  //}

#  public static NXObject __FindOccurrence(this Component component, NXObject proto)
#  {
#      return component.FindOccurrence(proto);
#  }

#  //public static void reference_set(this NXOpen.Assemblies.Component component, string reference_set)
#  //{
#  //    component.DirectOwner.ReplaceReferenceSet(component, reference_set);
#  //}

#  public static CartesianCoordinateSystem __AbsoluteCsysOcc(this Component component)
#  {
#      return (CartesianCoordinateSystem)
#          component.FindOccurrence(component.__Prototype().__AbsoluteCsys());
#  }

#  public static DatumPlane __AbsOccDatumPlaneXY(this Component component)
#  {
#      return (DatumPlane)
#          component.FindOccurrence(
#              component.__Prototype().__AbsoluteDatumCsys().__DatumPlaneXY()
#          );
#  }

#  public static DatumPlane __AbsOccDatumPlaneXZ(this Component component)
#  {
#      return (DatumPlane)
#          component.FindOccurrence(
#              component.__Prototype().__AbsoluteDatumCsys().__DatumPlaneXZ()
#          );
#  }

#  public static DatumPlane __AbsOccDatumPlaneYZ(this Component component)
#  {
#      return (DatumPlane)
#          component.FindOccurrence(
#              component.__Prototype().__AbsoluteDatumCsys().__DatumPlaneYZ()
#          );
#  }

#  public static Component __FindComponent(
#      this Component component,
#      string __journal_identifier
#  )
#  {
#      try
#      {
#          return (Component)component.FindObject(__journal_identifier);
#      }
#      catch (NXException ex)
#      {
#          ex.AssertErrorCode(3520016);
#          throw new Exception(
#              $"Could not find component with journal identifier: '{__journal_identifier}' in component '{component.DisplayName}'"
#          );
#      }
#  }

#  public static Component __InstOfPartOcc(this Component component)
#  {
#      Tag instance = ufsession_.Assem.AskInstOfPartOcc(component.Tag);
#      return (Component)session_.__GetTaggedObject(instance);
#  }

#  public static bool __IsShcs(this Component component)
#  {
#      return component.DisplayName.__IsShcs();
#  }

#  public static bool __IsFastener(this Component component)
#  {
#      return component.DisplayName.__IsFastener();
#  }

#  public static void __ReplaceComponent(
#      this Component component,
#      string path,
#      string name,
#      bool replace_all
#  )
#  {
#      ReplaceComponentBuilder replace_builder =
#          __work_part_.AssemblyManager.CreateReplaceComponentBuilder();

#      using (session_.__UsingBuilderDestroyer(replace_builder))
#      {
#          replace_builder.ComponentNameType = ReplaceComponentBuilder
#              .ComponentNameOption
#              .AsSpecified;
#          replace_builder.ComponentsToReplace.Add(component);
#          replace_builder.ReplaceAllOccurrences = replace_all;
#          replace_builder.ComponentName = name;
#          replace_builder.ReplacementPart = path;
#          replace_builder.SetComponentReferenceSetType(
#              ReplaceComponentBuilder.ComponentReferenceSet.Maintain,
#              null
#          );
#          replace_builder.Commit();
#      }
#  }

#  public static void __DeleteSelfAndConstraints(this Component component)
#  {
#      ComponentConstraint[] constraints = component.GetConstraints();

#      if (constraints.Length > 0)
#          session_.__DeleteObjects(constraints);

#      session_.__DeleteObjects(component);
#  }

#  //public static void __SetWcsToComponent(this Component comp)
#  //{
#  //    __display_part_.WCS.SetOriginAndMatrix(comp.__Origin(), comp.__Orientation());
#  //}


#  public static string __AssemblyPathString(this Component component)
#  {
#      return $"{component._AssemblyPath().Aggregate("{ ", (str, cmp) => $"{str}{cmp.DisplayName}, ")}}}";
#  }


#  public static IEnumerable<Component> _AssemblyPath(this Component component)
#  {
#      do
#      {
#          yield return component;
#      } while ((component = component.Parent) != null);
#  }

#  public static IDisposable __UsingReferenceSetReset(this Component component)
#  {
#      return new ReferenceSetReset(component);
#  }

#  public static Part __Prototype(this Component comp)
#  {
#      return (Part)comp.Prototype;
#  }

#  public static ReferenceSet[] __ReferenceSets(this Part part)
#  {
#      return part.GetAllReferenceSets();
#  }

#  public static ReferenceSet __ReferenceSets(this Part part, string refset_name)
#  {
#      return part.GetAllReferenceSets().Single(__ref => __ref.Name == refset_name);
#  }

#  public static Component __ToComponent(this Tag __tag)
#  {
#      return (Component)session_.__GetTaggedObject(__tag);
#  }

#  public static void __DeleteInstanceUserAttribute(this Component component, string title)
#  {
#      throw new NotImplementedException();
#  }

#  public static ComponentAssembly __DirectOwner(this Component component)
#  {
#      return component.DirectOwner;
#  }

#  public static void __NXOpenAssembliesComponent(Component component)
#  {
#      //component.DisplayName
#      //component.FindObject
#      //component.FindOccurrence
#      //component.FixConstraint
#      //component.GetArrangements
#      //component.GetChildren
#      //component.GetConstraints
#      //component.GetDegreesOfFreedom
#      //component.GetInstanceStringUserAttribute
#      //component.GetLayerOption
#      //component.GetNonGeometricState
#      //component.GetPosition
#      //component.GetPositionOverrideParent
#      //component.GetPositionOverrideType
#      //component.HasInstanceUserAttribute
#      //component.IsFixed
#      //component.IsPositioningIsolated
#      //component.IsSuppressed
#      //component.Parent
#      //component.Prototype
#      //component.RedisplayObject
#      //component.ReferenceSet
#      //component.SetInstanceUserAttribute
#      //component.Suppress
#      //component.SuppressingArrangement
#      //component.UsedArrangement
#  }

#  //public static NXOpen.Point3d _Origin(this NXOpen.Assemblies.Component component)
#  //{
#  //    // ReSharper disable once UnusedVariable
#  //    component.GetPosition(out NXOpen.Point3d position, out NXOpen.Matrix3x3 orientation);
#  //    return position;
#  //}

#  //public static Orientation_ _Orientation(this NXOpen.Assemblies.Component component)
#  //{
#  //    // ReSharper disable once UnusedVariable
#  //    component.GetPosition(out NXOpen.Point3d position, out NXOpen.Matrix3x3 orientation);
#  //    return orientation;
#  //}


#  public static bool __IsLeaf(this Component component)
#  {
#      return component.GetChildren().Length == 0;
#  }

#  public static bool __IsRoot(this Component component)
#  {
#      return component.Parent is null;
#  }

#  public static void __ReferenceSet(this Component component, string referenceSetTitle)
#  {
#      if (!(component.Prototype is Part part))
#          throw new ArgumentException(
#              $"The given component \"{component.DisplayName}\" is not loaded."
#          );

#      //   part._RightClickOpen
#      switch (referenceSetTitle)
#      {
#          case RefsetEntirePart:
#          case RefsetEmpty:
#              component.DirectOwner.ReplaceReferenceSet(component, referenceSetTitle);
#              break;
#          default:
#              _ =
#                  part.__FindReferenceSetOrNull(referenceSetTitle)
#                  ?? throw new InvalidOperationException(
#                      $"Cannot set component \"{component.DisplayName}\" to the reference set \"{referenceSetTitle}\"."
#                  );

#              component.DirectOwner.ReplaceReferenceSet(component, referenceSetTitle);
#              break;
#      }
#  }

#  //public static Part __Prototype(this Component component)
#  //{
#  //    return (Part)component.Prototype;
#  //}

#  public static Body[] __SolidBodyMembers(this Component component)
#  {
#      return component.__Members().OfType<Body>().Where(__b => __b.IsSolidBody).ToArray();
#  }


def wcs_set_to_component(component: Component) -> None:
    """Sets the WCS to the position and orientation of the given component"""
    display_part().WCS.SetOriginAndMatrix(
        component_origin(component), component_orientation(component)
    )


def component_origin(component: Component) -> Point3d:
    return component.GetPosition()[0]


def component_orientation(component: Component) -> Matrix3x3:
    return component.GetPosition()[1]


#  public static void __SetWcs(this Component comp)
#  {
#      __display_part_.WCS.SetOriginAndMatrix(comp.__Origin(), comp.__Orientation());
#  }

#  public static SetWorkPartContextQuietly __SetWorkQuietly(this Component comp)
#  {
#      return new SetWorkPartContextQuietly(comp);
#  }


#  #endregion

#      #region WCS


def wcs_orientation() -> Matrix3x3:
    # wcs.CoordinateSystem.GetDirections(out Vector3d xDir, out Vector3d yDir);
    # return xDir.__ToMatrix3x3(yDir);
    raise NotImplementedError()


#     public static Matrix3x3 __Orientation(this WCS wcs)
#     {
#     }

#     public static void __Orientation(this WCS wcs, Matrix3x3 matrix)
#     {
#         wcs.SetOriginAndMatrix(wcs.Origin, matrix);
#     }

#     public static Vector3d __AxisX(this WCS wcs)
#     {
#         return wcs.CoordinateSystem.__Orientation().Element.__AxisX();
#     }

#     public static Vector3d __AxisY(this WCS wcs)
#     {
#         return wcs.CoordinateSystem.__Orientation().Element.__AxisY();
#     }

#     public static Vector3d __AxisZ(this WCS wcs)
#     {
#         return wcs.CoordinateSystem.__Orientation().Element.__AxisZ();
#     }

#     public static void __RotateAroundX(this WCS wcs, double degrees)
#     {

#     }

#     public static void __RotateAroundY(this WCS wcs, double degrees)
#     {

#     }

#     public static void __RotateAroundZ(this WCS wcs, double degrees)
#     {

#     }

#     public static void __Origin(this WCS wcs, Point3d origin)
#     {
#         wcs.SetOriginAndMatrix(origin, wcs.__Orientation());
#     }

#     #endregion


#         #region ComponentConstraint

#     public static void __Check0(ComponentConstraint componentConstraint)
#     {
#         //componentConstraint.Automatic
#         //componentConstraint.ConstraintAlignment
#         //componentConstraint.ConstraintSecondAlignment
#         //componentConstraint.ConstraintType
#         //componentConstraint.CreateConstraintReference
#         //componentConstraint.DeleteConstraintReference
#         //componentConstraint.EditConstraintReference
#         //componentConstraint.Expression
#         //componentConstraint.ExpressionDriven
#         //componentConstraint.FlipAlignment
#         //componentConstraint.GetConstraintStatus
#         //componentConstraint.GetDisplayedConstraint
#         //componentConstraint.GetInherited
#         //componentConstraint.GetReferences
#         //componentConstraint.Persistent
#         //componentConstraint.Print
#         //componentConstraint.Renew
#         //componentConstraint.ReverseDirection
#         //componentConstraint.SetAlignmentHint
#         //componentConstraint.SetExpression
#     }


#     public static ConstraintReference __CreateConstRefOcc(
#         this ComponentConstraint constraint,
#         NXObject occObject)
#     {
#         return constraint.CreateConstraintReference(
#             occObject.OwningComponent,
#             occObject,
#             false,
#             false,
#             false);
#     }

#     public static ConstraintReference __CreateConstRefProto(
#         this ComponentConstraint constraint,
#         NXObject protoObject)
#     {
#         return constraint.CreateConstraintReference(
#             protoObject.OwningPart.ComponentAssembly,
#             protoObject,
#             false,
#             false,
#             false);
#     }

#     #endregion


#      #region Conic

#  public static void __Temp(this Conic obj)
#  {
#      //obj.CenterPoint
#      //obj.GetOrientation
#      //obj.IsClosed
#      //obj.IsReference
#      //obj.Matrix
#      //obj.ProtectFromDelete
#      //obj.ReleaseDeleteProtection
#      //obj.RotationAngle
#      //obj.SetOrientation
#      //obj.SetParameters
#  }

#  #endregion

#     #region Vector3d

#    /// <summary>Map a vector from Absolute coordinates to Work coordinates</summary>
#    /// <param name="absVector">The components of the given vector wrt the Absolute Coordinate System (ACS)</param>
#    /// <returns>The components of the given vector wrt the Work Coordinate System (WCS)</returns>
#    public static Vector3d __MapAcsToWcs(this Vector3d absVector)
#    {
#        Vector3d axisX = __display_part_.WCS.__AxisX();
#        Vector3d axisY = __display_part_.WCS.__AxisY();
#        Vector3d axisZ = __display_part_.WCS.__AxisZ();
#        double x = axisX.__Multiply(absVector);
#        double y = axisY.__Multiply(absVector);
#        double z = axisZ.__Multiply(absVector);
#        return new Vector3d(x, y, z);
#    }

#    /// <summary>
#    ///     Map a vector from one coordinate system to another
#    /// </summary>
#    /// <param name="inputVector">The components of the given vector wrt the input coordinate system</param>
#    /// <param name="inputCsys">The input coordinate system</param>
#    /// <param name="outputCsys">The output coordinate system</param>
#    /// <returns>The components of the given vector wrt the output coordinate system</returns>
#    public static Vector3d __MapCsysToCsys(
#        this Vector3d inputVector,
#        CartesianCoordinateSystem inputCsys,
#        CartesianCoordinateSystem outputCsys
#    )
#    {
#        Vector3d axisX = inputCsys.__Orientation().Element.__AxisX();
#        Vector3d axisY = inputCsys.__Orientation().Element.__AxisY();
#        Vector3d axisZ = inputCsys.__Orientation().Element.__AxisZ();
#        Vector3d x = inputVector.X.__Multiply(axisX);
#        Vector3d y = inputVector.Y.__Multiply(axisY);
#        Vector3d z = inputVector.Z.__Multiply(axisZ);
#        Vector3d vector = x.__Add(y, z);
#        double x0 = vector.__Multiply(outputCsys.__Orientation().Element.__AxisX());
#        double y0 = vector.__Multiply(outputCsys.__Orientation().Element.__AxisY());
#        double z0 = vector.__Multiply(outputCsys.__Orientation().Element.__AxisZ());
#        return new Vector3d(x0, y0, z0);
#    }

#    public static Vector3d __Add(this Vector3d vector, params Vector3d[] vectors)
#    {
#        Vector3d result = vector.__Copy();

#        foreach (Vector3d v in vectors)
#            result = result.__Add(v);

#        return result;
#    }

#    /// <summary>Calculates the cross product (vector product) of two vectors</summary>
#    /// <param name="u">First vector</param>
#    /// <param name="v">Second vector</param>
#    /// <returns>Cross product</returns>
#    /// <remarks>
#    ///     <para>
#    ///         As is well known, order matters: Cross(u,v) = - Cross(v,u)
#    ///     </para>
#    /// </remarks>
#    public static Vector3d __Cross(this Vector3d u, Vector3d v)
#    {
#        return new Vector3d(
#            u.Y * v.Z - u.Z * v.Y,
#            u.Z * v.X - u.X * v.Z,
#            u.X * v.Y - u.Y * v.X
#        );
#    }

#    /// <summary>Calculates the unitized cross product (vector product) of two vectors</summary>
#    /// <param name="u">First vector</param>
#    /// <param name="v">Second vector</param>
#    /// <returns>Unitized cross product</returns>
#    /// <remarks>
#    ///     <para>
#    ///         If the cross product is the zero vector, then each component
#    ///         of the returned vector will be NaN (not a number).
#    ///     </para>
#    /// </remarks>
#    public static Vector3d __UnitCross(this Vector3d u, Vector3d v)
#    {
#        return u.__Cross(v).__Unit();
#    }

#    /// <summary>Unitizes a given vector</summary>
#    /// <param name="u">Vector to be unitized</param>
#    /// <returns>Unit vector in same direction</returns>
#    /// <remarks>
#    ///     <para>
#    ///         If the input is the zero vector is zero, then each component
#    ///         of the returned vector will be NaN (not a number).
#    ///     </para>
#    /// </remarks>
#    public static Vector3d __Unit(this Vector3d vec, double tolerance = .001)
#    {
#        double[] unit_vec = new double[3];
#        ufsession_.Vec3.Unitize(vec.__ToArray(), tolerance, out _, unit_vec);
#        return unit_vec.__ToVector3d();
#    }

#    /// <summary>Calculates the norm squared (length squared) of a vector</summary>
#    /// <param name="u">The vector</param>
#    /// <returns>Norm (length) squared of vector</returns>
#    public static double __Norm2(this Vector3d u)
#    {
#        return u.X * u.X + u.Y * u.Y + u.Z * u.Z;
#    }

#    public static Vector3d __Divide(this Vector3d vector, double divisor)
#    {
#        return new Vector3d(vector.X / divisor, vector.Y / divisor, vector.Z / divisor);
#    }

#    /// <summary>Calculates the norm (length) of a vector</summary>
#    /// <param name="u">The vector</param>
#    /// <returns>Norm (length) of vector</returns>
#    public static double __Norm(this Vector3d u)
#    {
#        return System.Math.Sqrt(u.X * u.X + u.Y * u.Y + u.Z * u.Z);
#    }

#    public static Matrix3x3 __ToMatrix3x3(this Vector3d axisZ)
#    {
#        Vector3d u = !(System.Math.Abs(axisZ.X) < System.Math.Abs(axisZ.Y))
#            ? new Vector3d(0.0, 1.0, 0.0)
#            : new Vector3d(1.0, 0.0, 0.0);

#        axisZ = axisZ.__Unit();
#        Vector3d v = u.__Cross(axisZ).__Unit();
#        Vector3d vector = axisZ.__Cross(v).__Unit();
#        return new Matrix3x3
#        {
#            Xx = v.X,
#            Xy = v.Y,
#            Xz = v.Z,
#            Yx = vector.X,
#            Yy = vector.Y,
#            Yz = vector.Z,
#            Zx = axisZ.X,
#            Zy = axisZ.Y,
#            Zz = axisZ.Z
#        };
#    }

#    public static Vector3d __Mirror(this Vector3d vector, Surface.Plane plane)
#    {
#        Transform transform = Transform.CreateReflection(plane);
#        return vector.__Copy(transform);
#    }

#    [Obsolete(nameof(NotImplementedException))]
#    public static Vector3d __Mirror(
#        this Vector3d vector,
#        Surface.Plane plane,
#        Component from,
#        Component to
#    )
#    {
#        throw new NotImplementedException();
#    }

#    public static Matrix3x3 __ToMatrix3x3(this Vector3d xDir, Vector3d yDir)
#    {
#        double[] array = new double[9];
#        ufsession_.Mtx3.Initialize(xDir.__ToArray(), yDir.__ToArray(), array);
#        return array.__ToMatrix3x3();
#    }

#    public static Matrix3x3 __ToMatrix3x3(this Vector3d axisX, Vector3d axisY, Vector3d axisZ)
#    {
#        Matrix3x3 element = default(Matrix3x3);
#        element.Xx = axisX.X;
#        element.Xy = axisX.Y;
#        element.Xz = axisX.Z;
#        element.Yx = axisY.X;
#        element.Yy = axisY.Y;
#        element.Yz = axisY.Z;
#        element.Zx = axisZ.X;
#        element.Zy = axisZ.Y;
#        element.Zz = axisZ.Z;
#        return element;
#    }

#    public static Vector3d __AskPerpendicular(this Vector3d vec)
#    {
#        double[] __vec_perp = new double[3];
#        ufsession_.Vec3.AskPerpendicular(vec.__ToArray(), __vec_perp);
#        return new Vector3d(__vec_perp[0], __vec_perp[1], __vec_perp[2]);
#    }

#    public static Vector3d __Add(this Vector3d vec0, Vector3d vec1)
#    {
#        return new Vector3d(vec0.X + vec1.X, vec0.Y + vec1.Y, vec0.Z + vec1.Z);
#    }

#    public static Vector3d __Subtract(this Vector3d vec0, Vector3d vec1)
#    {
#        Vector3d negate = vec1.__Negate();
#        return vec0.__Add(negate);
#    }


def vector3d_negate(vec: Vector3d) -> Vector3d:
    return Vector3d(-vec.X, -vec.Y, -vec.Z)


def vector3d_angle(vec0: Vector3d, vec1: Vector3d) -> float:
    #    /// <summary>Calculates the angle in degrees between two vectors</summary>
    #    /// <param name="u">First vector</param>
    #    /// <param name="v">Second vector</param>
    #    /// <returns>The angle, theta, in degrees, where 0 ≤ theta ≤ 180</returns>

    # double val = u.__Unit().__Multiply(v.__Unit());
    # val = System.Math.Min(1.0, val);
    # val = System.Math.Max(-1.0, val);
    # return System.Math.Acos(val) * 180.0 / System.Math.PI;
    raise NotImplementedError()


#    public static double __Angle(this Vector3d u, Vector3d v)
#    {
#    }

#    public static bool __IsPerpendicularTo(
#        this Vector3d vec1,
#        Vector3d vec2,
#        double tolerance = .0001
#    )
#    {
#        ufsession_.Vec3.IsPerpendicular(
#            vec1.__ToArray(),
#            vec2.__ToArray(),
#            tolerance,
#            out int result
#        );
#        return result == 1;
#    }

#    public static double[] __ToArray(this Vector3d vector3d)
#    {
#        return new[] { vector3d.X, vector3d.Y, vector3d.Z };
#    }

#    //
#    // Summary:
#    //     Transforms/copies a vector
#    //
#    // Parameters:
#    //   xform:
#    //     The transformation to apply
#    //
#    // Returns:
#    //     A transformed copy of the original input vector
#    public static Vector3d __Copy(this Vector3d vector, Transform xform)
#    {
#        double[] matrix = xform.Matrix;
#        double x = vector.X;
#        double y = vector.Y;
#        double z = vector.Z;
#        double x2 = x * matrix[0] + y * matrix[1] + z * matrix[2];
#        double y2 = x * matrix[4] + y * matrix[5] + z * matrix[6];
#        double z2 = x * matrix[8] + y * matrix[9] + z * matrix[10];
#        return new Vector3d(x2, y2, z2);
#    }

#    /// <summary>Copies a vector</summary>
#    /// <param name="vector">The vector copy from</param>
#    /// <returns>A copy of the original input vector</returns>
#    public static Vector3d __Copy(this Vector3d vector)
#    {
#        return new Vector3d(vector.X, vector.Y, vector.Z);
#    }

#    public static bool __IsEqual(this Vector3d vec0, Vector3d vec1, double tolerance = .001)
#    {
#        ufsession_.Vec3.IsEqual(
#            vec0.__ToArray(),
#            vec1.__ToArray(),
#            tolerance,
#            out int is_equal
#        );

#        switch (is_equal)
#        {
#            case 0:
#                return false;
#            case 1:
#                return true;
#            default:
#                throw NXException.Create(is_equal);
#        }
#    }

#    public static bool __IsEqualUnit(this Vector3d vec0, Vector3d vec1, double tolerance = .001)
#    {
#        return vec0.__Unit().__IsEqual(vec1.__Unit(), tolerance);
#    }

#    // public static bool __IsEqualTo(
#    //     this Vector3d vector1,
#    //     Vector3d vector2,
#    //     double tolerance = .01
#    // )
#    // {
#    //     // Compares the two vectors. If they are equal, then {isEqual} == 1, else {isEqual} == 0.
#    //     ufsession_.Vec3.IsEqual(
#    //         vector1.__ToArray(),
#    //         vector2.__ToArray(),
#    //         tolerance,
#    //         out int isEqual
#    //     );

#    //     switch (isEqual)
#    //     {
#    //         case 0:
#    //             return false;
#    //         case 1:
#    //             return true;
#    //         default:
#    //             throw NXException.Create(isEqual);
#    //     }
#    // }

#    /// <summary>
#    ///     Returns a 3x3 matrix formed from two input 3D vectors. The two<br />
#    ///     input vectors are normalized and the y-direction vector is made<br />
#    ///     orthogonal to the x-direction vector before taking the cross product<br />
#    ///     (x_vec X y_vec) to generate the z-direction vector.
#    /// </summary>
#    /// <param name="xVec">Vector for the X-direction of matrix</param>
#    /// <param name="yVec">Vector for theYX-direction of matrix</param>
#    /// <returns>The resulting matrix.</returns>
#    public static Matrix3x3 __Initialize(this Vector3d xVec, Vector3d yVec)
#    {
#        double[] mtx = new double[9];
#        ufsession_.Mtx3.Initialize(xVec.__ToArray(), yVec.__ToArray(), mtx);
#        return mtx.__ToMatrix3x3();
#    }

#    /// <summary>
#    ///     Returns a 3x3 matrix with the given X-direction vector and having<br />
#    ///     arbitrary Y- and Z-direction vectors.
#    /// </summary>
#    /// <param name="xVec">Vector for the X-direction of matrix</param>
#    /// <returns>The resulting matrix.</returns>
#    public static Matrix3x3 __InitializeX(Vector3d xVec)
#    {
#        double[] mtx = new double[9];
#        ufsession_.Mtx3.InitializeX(xVec.__ToArray(), mtx);
#        return mtx.__ToMatrix3x3();
#    }

#    /// <summary>
#    ///     Returns a 3x3 matrix with the given Z-direction vector and having<br />
#    ///     arbitrary X- and Y-direction vectors.
#    /// </summary>
#    /// <param name="z_vec">Vector for the Z-direction of matrix</param>
#    /// <returns>The resulting matrix.</returns>
#    public static Matrix3x3 __InitializeZ(Vector3d z_vec)
#    {
#        double[] mtx = new double[9];
#        ufsession_.Mtx3.InitializeZ(z_vec.__ToArray(), mtx);
#        return mtx.__ToMatrix3x3();
#    }

#    public static Point3d __Add(this Vector3d vector, Point3d point)
#    {
#        return point.__Add(vector);
#    }

#    /// <summary>Map a vector from Work coordinates to Absolute coordinates</summary>
#    /// <param name="workVector">The components of the given vector wrt the Work Coordinate System (WCS)</param>
#    /// <returns>The components of the given vector wrt the Absolute Coordinate System (ACS)</returns>
#    /// <remarks>
#    ///     <para>
#    ///         If you are given vector components relative to the WCS, then you will need to
#    ///         use this function to "map" them to the ACS before using them in SNAP functions.
#    ///     </para>
#    /// </remarks>
#    public static Vector3d __MapWcsToAcs(this Vector3d workVector)
#    {
#        Vector3d axisX = __display_part_.WCS.__AxisX();
#        Vector3d axisY = __display_part_.WCS.__AxisY();
#        Vector3d axisZ = __display_part_.WCS.__AxisZ();
#        return axisX
#            .__Multiply(workVector.X)
#            .__Add(axisY.__Multiply(workVector.Y))
#            .__Add(axisZ.__Multiply(workVector.Z));
#    }


def to_list(vec: Vector3d) -> List[float]:
    return [vec.X, vec.Y, vec.Z]


def to_vector3d(array: Sequence[float]) -> Vector3d:
    return Vector3d(array[0], array[1], array[2])


def multiply_vector(vec: Vector3d, scale: float) -> Vector3d:
    new_list = ufsession().Vec3.Scale(scale, to_list(vec))
    return to_vector3d(new_list)


#    public static Vector3d __Multiply(this Vector3d vector3d, double scale)
#    {
#        double[] scaled_vec = new double[3];
#        ufsession_.Vec3.Scale(scale, vector3d.__ToArray(), scaled_vec);
#        return scaled_vec.__ToVector3d();
#    }

#    public static double __Multiply(this Vector3d vec0, Vector3d vec1)
#    {
#        return vec0.X * vec1.X + vec0.Y * vec1.Y + vec0.Z * vec1.Z;
#    }

#    public static Vector3d __MirrorMap(
#        this Vector3d vector,
#        Surface.Plane plane,
#        Component fromComponent,
#        Component toComponent
#    )
#    {
#        Point3d origin = fromComponent.__Origin();
#        Matrix3x3 orientation = fromComponent.__Orientation();
#        __display_part_.WCS.SetOriginAndMatrix(origin, orientation);
#        Vector3d newStart = __MapWcsToAcs(vector);
#        __display_part_.WCS.SetOriginAndMatrix(
#            toComponent.__Origin(),
#            toComponent.__Orientation()
#        );
#        return __MapAcsToWcs(newStart);
#    }

#    public static Matrix3x3 __Mtx3Initialize(Vector3d x_vec, Vector3d y_vec)
#    {
#        double[] matrix = new double[9];
#        ufsession_.Mtx3.Initialize(x_vec.__ToArray(), y_vec.__ToArray(), matrix);
#        return matrix.__ToMatrix3x3();
#    }

#    public static bool _IsPerpendicularTo(
#        this Vector3d vec1,
#        Vector3d vec2,
#        double tolerance = 0.0001
#    )
#    {
#        ufsession_.Vec3.IsPerpendicular(
#            vec1.__ToArray(),
#            vec2.__ToArray(),
#            tolerance,
#            out int is_perp
#        );
#        return is_perp == 1;
#    }

#    public static bool _IsParallelTo(
#        this Vector3d vector1,
#        Vector3d vector2,
#        double tolerance = 0.0001
#    )
#    {
#        ufsession_.Vec3.IsParallel(
#            vector1.__ToArray(),
#            vector2.__ToArray(),
#            tolerance,
#            out int is_parallel
#        );
#        return is_parallel == 1;
#    }

#    public static Vector3d _UnitVector(this Vector3d vector)
#    {
#        return vector.__Unit();
#    }

#    public static double _MagnitudeLength(this Vector3d vector)
#    {
#        return vector.__Norm();
#    }

#    public static Vector3d _AbsVector(this Vector3d vector)
#    {
#        return new Vector3d(
#            System.Math.Abs(vector.X),
#            System.Math.Abs(vector.Y),
#            System.Math.Abs(vector.Z)
#        );
#    }

#    public static Vector3d _Cross(this Vector3d vector1, Vector3d vector2)
#    {
#        return new Vector3d(
#            vector1.Y * vector2.Z - vector1.Z * vector2.Y,
#            vector1.Z * vector2.X - vector1.X * vector2.Z,
#            vector1.X * vector2.Y - vector1.Y * vector2.X
#        );
#    }

def vector3d_dot_product(vec0:Vector3d, vec1:Vector3d)->float:
    return vec0.X * vec1.X + vec0.Y * vec1.Y + vec0.Z * vec1.Z

#    public static Matrix3x3 _CreateOrientationXVectorZVector(
#        this Vector3d xVector,
#        Vector3d zVector
#    )
#    {
#        if (!xVector.__IsPerpendicularTo(zVector))
#            throw new InvalidOperationException(
#                "You cannot create an orientation from two vectors that are not perpendicular to each other."
#            );

#        Matrix3x3 val = xVector.__ToMatrix3x3(zVector);
#        Vector3d axisZ = val.__AxisZ();
#        return xVector.__ToMatrix3x3(axisZ);
#    }

#    public static Matrix3x3 _CreateOrientationYVectorZVector(
#        this Vector3d yVector,
#        Vector3d zVector
#    )
#    {
#        if (!yVector.__IsPerpendicularTo(zVector))
#            throw new InvalidOperationException(
#                "You cannot create an orientation from two vectors that are not perpendicular to each other."
#            );

#        Matrix3x3 val = yVector.__ToMatrix3x3(zVector);
#        Vector3d axisZ = val.__AxisZ();
#        return axisZ.__ToMatrix3x3(yVector);
#    }

#    public static Vector3d _Mirror(this Vector3d original, Surface.Plane plane)
#    {
#        Transform val = Transform.CreateReflection(plane);
#        return original.__Copy(val);
#    }

#    public static Vector3d _MirrorMap(
#        this Vector3d vector,
#        Surface.Plane mirrorPlane,
#        Component originalComp,
#        Component newComp
#    )
#    {
#        originalComp.__SetWcsToComponent();
#        Vector3d original = vector.__MapWcsToAcs();
#        Vector3d val = original._Mirror(mirrorPlane);
#        newComp.__SetWcsToComponent();
#        return val.__MapAcsToWcs();
#    }

#    [Obsolete]
#    public static Vector3d _MirrorMap(
#        this Vector3d vector,
#        Plane mirrorPlane,
#        Component originalComp,
#        Component newComp
#    )
#    {
#        throw new NotImplementedException();
#        //return _MirrorMap(new Vector(vector), mirrorPlane, originalComp, newComp);
#    }

#    [Obsolete]
def mirror_vector3d(original:Vector3d, plane)->Vector3d:
    raise NotImplementedError()

#    public static double[] _Array(this Vector3d vector3D)
#    {
#        return new double[3] { vector3D.X, vector3D.Y, vector3D.Z };
#    }

#    public static bool __Equals(this Vector3d vec0, double[] vec1, double tol = .001)
#    {
#        return vec0.__Equals(vec1.__ToVector3d(), tol);
#    }

#    public static bool __Equals(this Vector3d vec0, Vector3d vec1, double tol = .001)
#    {
#        vec0 = vec0.__Unit();
#        vec1 = vec1.__Unit();

#        return vec0.X.__Equals(vec1.X, tol)
#            && vec0.Y.__Equals(vec1.Y, tol)
#            && vec0.Z.__Equals(vec1.Z, tol);
#    }

#    public static DatumAxis __ToDatumAxis(this Vector3d vector)
#    {
#        return __display_part_.Datums.CreateFixedDatumAxis(
#            _Point3dOrigin,
#            _Point3dOrigin.__Add(vector)
#        );
#    }

#    public static Vector3d __MultiplyX(this Vector3d vector, double x)
#    {
#        return new Vector3d(vector.X * x, vector.Y, vector.Z);
#    }

#    public static Vector3d __MultiplyY(this Vector3d vector, double y)
#    {
#        return new Vector3d(vector.X, vector.Y * y, vector.Z);
#    }

#    public static Vector3d __MultiplyZ(this Vector3d vector, double z)
#    {
#        return new Vector3d(vector.X, vector.Y, vector.Z * z);
#    }

#    #endregion

#     #region Trns

#  //ufsession_.Trns.CreateCsysMappingMatrix
#  //ufsession_.Trns.CreateReflectionMatrix
#  //ufsession_.Trns.CreateRotationMatrix
#  //ufsession_.Trns.CreateScalingMatrix
#  //ufsession_.Trns.CreateTranslationMatrix
#  //ufsession_.Trns.
#  //ufsession_.Trns.TransformObjects
#  //ufsession_.Trns.CreateCsysMappingMatrix
#  //ufsession_.Trns.CreateReflectionMatrix
#  //ufsession_.Trns.CreateRotationMatrix
#  //ufsession_.Trns.CreateScalingMatrix
#  //ufsession_.Trns.CreateTranslationMatrix
#  //ufsession_.Trns.MapPosition
#  //ufsession_.Trns.MultiplyMatrices
#  //ufsession_.Trns.TransformObjects

#  #endregion

#   #region ConstraintReference

#  public static bool __GeometryDirectionReversed(ConstraintReference cons)
#  {
#      return cons.GeometryDirectionReversed;
#  }

#  public static NXObject __GetGeometry(ConstraintReference cons)
#  {
#      return cons.GetGeometry();
#  }

#  public static bool __GetHasPerpendicularVector(ConstraintReference cons)
#  {
#      return cons.GetHasPerpendicularVector();
#  }

#  public static NXObject __GetMovableObject(ConstraintReference cons)
#  {
#      return cons.GetMovableObject();
#  }

#  public static NXObject __GetPrototypeGeometry(ConstraintReference cons)
#  {
#      return cons.GetPrototypeGeometry();
#  }

#  public static Vector3d __GetPrototypePerpendicularVector(ConstraintReference cons)
#  {
#      return cons.GetPrototypePerpendicularVector();
#  }

#  public static bool __GetUsesGeometryAxis(ConstraintReference cons)
#  {
#      return cons.GetUsesGeometryAxis();
#  }

#  public static Point3d __HelpPoint(ConstraintReference cons)
#  {
#      return cons.HelpPoint;
#  }

#  public static ConstraintReference.ConstraintOrder __Order(
#      ConstraintReference cons)
#  {
#      return cons.Order;
#  }

#  public static ConstraintReference.GeometryType __SolverGeometryType(
#      ConstraintReference cons)
#  {
#      return cons.SolverGeometryType;
#  }

#  #endregion


#      #region CoordinateSystem

#     public static Vector3d __AxisX(this CoordinateSystem coordinateSystem)
#     {
#         return coordinateSystem.Orientation.Element.__AxisX();
#     }

#     public static Vector3d __AxisY(this CoordinateSystem coordinateSystem)
#     {
#         return coordinateSystem.Orientation.Element.__AxisY();
#     }

#     public static Vector3d __AxisZ(this CoordinateSystem coordinateSystem)
#     {
#         return coordinateSystem.Orientation.Element.__AxisZ();
#     }

#     public static void __GetDirections(this CoordinateSystem obj)
#     {
#         obj.GetDirections(out _, out _);
#     }

#     [Obsolete]
#     public static void __GetSolverCardSyntax(this CoordinateSystem obj)
#     {
#     }

#     public static bool __IsTemporary(this CoordinateSystem obj)
#     {
#         return obj.IsTemporary;
#     }

#     [Obsolete]
#     public static void __Label(this CoordinateSystem obj)
#     {
#     }

#     public static NXMatrix __Orientation(this CoordinateSystem obj)
#     {
#         return obj.Orientation;
#     }

#     public static void __Orientation(this CoordinateSystem obj, Vector3d xDir, Vector3d yDir)
#     {
#         obj.SetDirections(xDir, yDir);
#     }

#     public static Point3d __Origin(this CoordinateSystem obj)
#     {
#         return obj.Origin;
#     }

#     #endregion
# }


#    #region DisplayableObject

#    public static IDisposable __UsingRedisplayObject(this DisplayableObject displayableObject)
#    {
#        return new RedisplayObject(displayableObject);
#    }

#    public static int __Color(this DisplayableObject obj)
#    {
#        return obj.Color;
#    }

#    // public static void __AskExtreme(this DisplayableObject obj)
#    // {
#    //     ufsession_.Modl.AskExtreme(obj.Tag, dirVectorX, dirVectorY, dirVectorZ, out _,
#    //                     extremePoint);
#    // }

#    public static void __Color(this DisplayableObject obj, int color, bool redisplayObj = true)
#    {
#        obj.Color = color;

#        if (redisplayObj)
#            obj.__RedisplayObject();
#    }

#    public static void __Translucency(this DisplayableObject obj, int translucency, bool redisplayObj = true)
#    {
#        ufsession_.Obj.SetTranslucency(obj.Tag, translucency);

#        if (redisplayObj)
#            obj.__RedisplayObject();
#    }

#    public static int __Layer(this DisplayableObject displayableObject)
#    {
#        return displayableObject.Layer;
#    }

#    public static void __Layer(this DisplayableObject displayableObject, int layer, bool redisplayObj = true)
#    {
#        displayableObject.Layer = layer;

#        if (redisplayObj)
#            displayableObject.__RedisplayObject();
#    }

#    public static void __RedisplayObject(this DisplayableObject obj)
#    {
#        obj.RedisplayObject();
#    }

#    public static void __Blank(this DisplayableObject obj)
#    {
#        obj.Blank();
#    }

#    public static void __Unblank(this DisplayableObject obj)
#    {
#        obj.Unblank();
#    }

#    public static void __Highlight(this DisplayableObject obj)
#    {
#        obj.Highlight();
#    }


#    public static void __Unhighlight(this DisplayableObject obj)
#    {
#        obj.Unhighlight();
#    }

#    public static bool __IsBlanked(DisplayableObject obj)
#    {
#        return obj.IsBlanked;
#    }

#    #endregion


#     #region DoubleArray

#  private static Matrix3x3 __ToMatrix3x3(this double[] array)
#  {
#      return new Matrix3x3
#      {
#          Xx = array[0],
#          Xy = array[1],
#          Xz = array[2],
#          Yx = array[3],
#          Yy = array[4],
#          Yz = array[5],
#          Zx = array[6],
#          Zy = array[7],
#          Zz = array[8]
#      };
#  }

#  public static Point3d __ToPoint3d(this double[] array)
#  {
#      return new Point3d(array[0], array[1], array[2]);
#  }

#  public static Vector3d __ToVector3d(this double[] array)
#  {
#      return new Vector3d(array[0], array[1], array[2]);
#  }

#  public static Vector3d __Multiply(this double d, Vector3d vector)
#  {
#      return vector.__Multiply(d);
#  }

#  public static double[] __Round(this double[] array, int digits)
#  {
#      return array.Select(n=>System.Math.Round(n,digits)).ToArray();
#  }


#  public static double RoundToEigth(double value, double tolerance = .001)
#  {
#      double roundValue = System.Math.Round(value, 3);
#      double truncateValue = System.Math.Truncate(roundValue);
#      double fractionValue = roundValue - truncateValue;

#      if (System.Math.Abs(fractionValue) < tolerance)
#          return roundValue;

#      for (double ii = .125; ii <= 1; ii += .125)
#          if (fractionValue <= ii)
#          {
#              return truncateValue + ii;
#          }

#      return roundValue;
#  }


#  public static void __RoundTo_125(this double[] distances)
#  {
#      for (int i = 0; i < 3; i++)
#      {
#          double roundValue = System.Math.Round(distances[i], 3);
#          double truncateValue = System.Math.Truncate(roundValue);
#          double fractionValue = roundValue - truncateValue;

#          if (fractionValue != 0)
#              for (double ii = .125; ii <= 1; ii += .125)
#              {
#                  if (fractionValue <= ii)
#                  {
#                      double finalValue = truncateValue + ii;
#                      distances[i] = finalValue;
#                      break;
#                  }
#              }
#          else
#              distances[i] = roundValue;
#      }
#  }

#  // public static double __RoundToNearest(this double num, double nearest = .125, int digits = 3, double tolerance = .001)
#  // {
#  //     double roundValue = System.Math.Round(num, digits);
#  //     double truncateValue = System.Math.Truncate(roundValue);
#  //     double fractionValue = roundValue - truncateValue;

#  //     if (Math.Abs(fractionValue) < tolerance)
#  //         return roundValue;

#  //     for (double ii = nearest; ii <= 1; ii += nearest)
#  //         if (fractionValue <= ii)
#  //             return truncateValue + ii;

#  //     throw new
#  // }

#  #endregion


#     #region FileNew

#    //
#    // Summary:
#    //     Get the application name now required by NXOpen (since NX9) from the Snap enum
#    //     value
#    //
#    // Parameters:
#    //   fileNew:
#    //     An NXOpen fileNew object
#    //
#    //   templateType:
#    //     Template type
#    //
#    // Returns:
#    //     Application name (template type name, really)
#    /// <summary>
#    /// </summary>
#    /// <param name="fileNew"></param>
#    /// <param name="templateType"></param>
#    /// <returns></returns>
#    private static string __GetAppName(FileNew fileNew, Templates templateType)
#    {
#        string result = "GatewayTemplate";
#        if (templateType == Templates.AeroSheetMetal) result = __SafeAppName(fileNew, "AeroSheetMetalTemplate");

#        if (templateType == Templates.Assembly) result = __SafeAppName(fileNew, "AssemblyTemplate");

#        if (templateType == Templates.Modeling) result = __SafeAppName(fileNew, "ModelTemplate");

#        if (templateType == Templates.NXSheetMetal) result = __SafeAppName(fileNew, "NXSheetMetalTemplate");

#        if (templateType == Templates.RoutingElectrical)
#            result = __SafeAppName(fileNew, "RoutingElectricalTemplate");

#        if (templateType == Templates.RoutingLogical) result = __SafeAppName(fileNew, "RoutingLogicalTemplate");

#        if (templateType == Templates.RoutingMechanical)
#            result = __SafeAppName(fileNew, "RoutingMechanicalTemplate");

#        if (templateType == Templates.ShapeStudio) result = __SafeAppName(fileNew, "StudioTemplate");

#        return result;
#    }

#    //
#    // Summary:
#    //     Get the names of the available template files
#    //
#    // Parameters:
#    //   fileNew:
#    //     An NXOpen fileNew object
#    //
#    //   templateType:
#    //     Template type
#    //
#    //   unit:
#    //     Part units
#    //
#    // Returns:
#    //     The appropriate template file
#    /// <summary>
#    /// </summary>
#    /// <param name="fileNew"></param>
#    /// <param name="templateType"></param>
#    /// <param name="unit"></param>
#    /// <returns></returns>
#    private static string __GetTemplateFileName(FileNew fileNew, Templates templateType, Units unit)
#    {
#        string result = "Blank";
#        if (unit == Units.MilliMeters)
#        {
#            if (templateType == Templates.AeroSheetMetal)
#                result = __SafeTemplateName(fileNew, "aero-sheet-metal-mm-template.prt");

#            if (templateType == Templates.Assembly)
#                result = __SafeTemplateName(fileNew, "assembly-mm-template.prt");

#            if (templateType == Templates.Modeling)
#                result = __SafeTemplateName(fileNew, "model-plain-1-mm-template.prt");

#            if (templateType == Templates.NXSheetMetal)
#                result = __SafeTemplateName(fileNew, "sheet-metal-mm-template.prt");

#            if (templateType == Templates.RoutingElectrical)
#                result = __SafeTemplateName(fileNew, "routing-elec-mm-template.prt");

#            if (templateType == Templates.RoutingLogical)
#                result = __SafeTemplateName(fileNew, "routing-logical-mm-template.prt");

#            if (templateType == Templates.RoutingMechanical)
#                result = __SafeTemplateName(fileNew, "routing-mech-mm-template.prt");

#            if (templateType == Templates.ShapeStudio)
#                result = __SafeTemplateName(fileNew, "shape-studio-mm-template.prt");
#        }
#        else
#        {
#            if (templateType == Templates.AeroSheetMetal)
#                result = __SafeTemplateName(fileNew, "aero-sheet-metal-inch-template.prt");

#            if (templateType == Templates.Assembly)
#                result = __SafeTemplateName(fileNew, "assembly-inch-template.prt");

#            if (templateType == Templates.Modeling)
#                result = __SafeTemplateName(fileNew, "model-plain-1-inch-template.prt");

#            if (templateType == Templates.NXSheetMetal)
#                result = __SafeTemplateName(fileNew, "sheet-metal-inch-template.prt");

#            if (templateType == Templates.RoutingElectrical)
#                result = __SafeTemplateName(fileNew, "routing-elec-inch-template.prt");

#            if (templateType == Templates.RoutingLogical)
#                result = __SafeTemplateName(fileNew, "routing-logical-inch-template.prt");

#            if (templateType == Templates.RoutingMechanical)
#                result = __SafeTemplateName(fileNew, "routing-mech-inch-template.prt");

#            if (templateType == Templates.ShapeStudio)
#                result = __SafeTemplateName(fileNew, "shape-studio-inch-template.prt");
#        }

#        return result;
#    }

#    //
#    // Summary:
#    //     Check that an application name is OK
#    //
#    // Parameters:
#    //   fileNew:
#    //     A fileNew object
#    //
#    //   testName:
#    //     The name to be validated
#    //
#    // Returns:
#    //     The input name, if it's OK, otherwise "GatewayTemplate"
#    /// <summary>
#    /// </summary>
#    /// <param name="fileNew"></param>
#    /// <param name="testName"></param>
#    /// <returns></returns>
#    private static string __SafeAppName(FileNew fileNew, string testName)
#    {
#        string[] applicationNames = fileNew.GetApplicationNames();
#        string result = "GatewayTemplate";
#        if (Array.IndexOf(applicationNames, testName) > -1) result = testName;

#        return result;
#    }

#    //
#    // Summary:
#    //     Check that a template file name is OK
#    //
#    // Parameters:
#    //   fileNew:
#    //     A fileNew object
#    //
#    //   testName:
#    //     The name to be validated
#    //
#    // Returns:
#    //     The input name, if it's OK, otherwise "Blank"
#    /// <summary>
#    /// </summary>
#    /// <param name="fileNew"></param>
#    /// <param name="testName"></param>
#    /// <returns></returns>
#    private static string __SafeTemplateName(FileNew fileNew, string testName)
#    {
#        string[] availableTemplates = fileNew.GetAvailableTemplates();
#        string result = "Blank";

#        if (Array.IndexOf(availableTemplates, testName) > -1)
#            result = testName;

#        return result;
#    }

#    #endregion


#    #region Mirror

#         // public static void __Mirror(this NXOpen.CartesianCoordinateSystem obj, Su)


#         public static void __Data(this EdgeTangentRule rule, out Edge start, out Edge end, out bool isFromStart, out double angleTolerance, out bool hasSameConvexity)
#         {
#             rule.GetData(out start, out end, out isFromStart, out angleTolerance, out hasSameConvexity);
#         }

#         public static EdgeTangentRule __Mirror(this EdgeTangentRule original, Surface.Plane plane, Component from, Component to)
#         {
#             throw new NotImplementedException();
# #pragma warning disable CS0162 // Unreachable code detected
#             original.__Data(out var fStart, out var fEnd, out var isFromStart, out var angleTolerance, out var hasSameConvexity);
# #pragma warning restore CS0162 // Unreachable code detected

#             var fStartCurve = fStart.__ToCurve();

#             CompositeCurve fStartAssemblyCurve = fStartCurve.__CreateLinkedCurve();

#             var actualCurve = (NXOpen.Curve)fStartAssemblyCurve.GetEntities()[0];

#             fStartAssemblyCurve.RemoveParameters();

#             fStartAssemblyCurve.__Delete();

# #pragma warning disable CS0618 // Type or member is obsolete
#             var tStartAssemblyCurve = actualCurve.__Mirror(plane);
# #pragma warning restore CS0618 // Type or member is obsolete

#             __work_component_ = to;

#             CompositeCurve tCompositeCurve = tStartAssemblyCurve.__CreateLinkedCurve();

#             var tActualCurve = (NXOpen.Curve)tCompositeCurve.GetEntities()[0];
#             tCompositeCurve.RemoveParameters();
#             tCompositeCurve.__Delete();

#             var tStartEdge = to.__Prototype().__MatchCurveToEdge(tActualCurve);

#         }

#         public static Edge __MatchCurveToEdge(this Part part, NXOpen.Curve curve)
#         {
#             throw new NotImplementedException();
#         }

#         public static CompositeCurve __CreateLinkedCurve(this NXOpen.Curve curve)
#         {
#             throw new NotImplementedException();
# #pragma warning disable CS0162 // Unreachable code detected
#             Session theSession = NXOpen.Session.GetSession();
# #pragma warning restore CS0162 // Unreachable code detected
#             Part workPart = theSession.Parts.Work;
#             Part displayPart = theSession.Parts.Display;
#             // ----------------------------------------------
#             //   Menu: Insert->Associative Copy->WAVE Geometry Linker...
#             // ----------------------------------------------
#             Session.UndoMarkId markId1;
#             markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start");

#             Feature nullNXOpen_Features_Feature = null;
#             WaveLinkBuilder waveLinkBuilder1;
#             waveLinkBuilder1 = workPart.BaseFeatures.CreateWaveLinkBuilder(nullNXOpen_Features_Feature);

#             WaveDatumBuilder waveDatumBuilder1;
#             waveDatumBuilder1 = waveLinkBuilder1.WaveDatumBuilder;

#             CompositeCurveBuilder compositeCurveBuilder1;
#             compositeCurveBuilder1 = waveLinkBuilder1.CompositeCurveBuilder;

#             WaveSketchBuilder waveSketchBuilder1;
#             waveSketchBuilder1 = waveLinkBuilder1.WaveSketchBuilder;

#             WaveRoutingBuilder waveRoutingBuilder1;
#             waveRoutingBuilder1 = waveLinkBuilder1.WaveRoutingBuilder;

#             WavePointBuilder wavePointBuilder1;
#             wavePointBuilder1 = waveLinkBuilder1.WavePointBuilder;

#             ExtractFaceBuilder extractFaceBuilder1;
#             extractFaceBuilder1 = waveLinkBuilder1.ExtractFaceBuilder;

#             MirrorBodyBuilder mirrorBodyBuilder1;
#             mirrorBodyBuilder1 = waveLinkBuilder1.MirrorBodyBuilder;

#             NXOpen.GeometricUtilities.CurveFitData curveFitData1;
#             curveFitData1 = compositeCurveBuilder1.CurveFitData;

#             curveFitData1.Tolerance = 0.001;

#             curveFitData1.AngleTolerance = 0.5;

#             Section section1 = ((Section)workPart.FindObject("ENTITY 113 4"));
#             section1.SetAllowRefCrvs(false);

#             extractFaceBuilder1.FaceOption = NXOpen.Features.ExtractFaceBuilder.FaceOptionType.FaceChain;

#             waveLinkBuilder1.FixAtCurrentTimestamp = true;

#             extractFaceBuilder1.ParentPart = NXOpen.Features.ExtractFaceBuilder.ParentPartType.OtherPart;

#             mirrorBodyBuilder1.ParentPartType = NXOpen.Features.MirrorBodyBuilder.ParentPart.OtherPart;

#             theSession.SetUndoMarkName(markId1, "WAVE Geometry Linker Dialog");

#             compositeCurveBuilder1.Section.DistanceTolerance = 0.001;

#             compositeCurveBuilder1.Section.ChainingTolerance = 0.00095;

#             compositeCurveBuilder1.Section.AngleTolerance = 0.5;

#             compositeCurveBuilder1.Section.DistanceTolerance = 0.001;

#             compositeCurveBuilder1.Section.ChainingTolerance = 0.00095;

#             compositeCurveBuilder1.Associative = true;

#             compositeCurveBuilder1.MakePositionIndependent = false;

#             compositeCurveBuilder1.FixAtCurrentTimestamp = true;

#             compositeCurveBuilder1.HideOriginal = false;

#             compositeCurveBuilder1.InheritDisplayProperties = false;

#             compositeCurveBuilder1.JoinOption = NXOpen.Features.CompositeCurveBuilder.JoinMethod.No;

#             compositeCurveBuilder1.Tolerance = 0.001;

#             Section section2;
#             section2 = compositeCurveBuilder1.Section;

#             NXOpen.GeometricUtilities.CurveFitData curveFitData2;
#             curveFitData2 = compositeCurveBuilder1.CurveFitData;

#             section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.CurvesAndPoints);

#             Session.UndoMarkId markId2;
#             markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark");

#             Session.UndoMarkId markId3;
#             markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, null);

#             IBaseCurve[] curves1 = new IBaseCurve[1];
#             Component component1 = ((Component)workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 001449-010-109 1"));
#             Line line1 = ((Line)component1.FindObject("PROTO#.Lines|HANDLE R-20339"));
#             curves1[0] = line1;
#             CurveDumbRule curveDumbRule1;
#             curveDumbRule1 = workPart.ScRuleFactory.CreateRuleBaseCurveDumb(curves1);

#             section2.AllowSelfIntersection(false);

#             SelectionIntentRule[] rules1 = new SelectionIntentRule[1];
#             rules1[0] = curveDumbRule1;
#             NXObject nullNXOpen_NXObject = null;
#             Point3d helpPoint1 = new Point3d(-1.2364300741239278, 10.674635720890926, -5.0515147620444623e-15);
#             section2.AddToSection(rules1, line1, nullNXOpen_NXObject, nullNXOpen_NXObject, helpPoint1, NXOpen.Section.Mode.Create, false);

#             theSession.DeleteUndoMark(markId3, null);

#             theSession.DeleteUndoMark(markId2, null);

#             Session.UndoMarkId markId4;
#             markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "WAVE Geometry Linker");

#             theSession.DeleteUndoMark(markId4, null);

#             Session.UndoMarkId markId5;
#             markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "WAVE Geometry Linker");

#             NXObject nXObject1;
#             nXObject1 = waveLinkBuilder1.Commit();

#             theSession.DeleteUndoMark(markId5, null);

#             theSession.SetUndoMarkName(markId1, "WAVE Geometry Linker");

#             waveLinkBuilder1.Destroy();

#         }

#         #endregion


#      #region Feature

#  public static string __FeatureType(Feature feat)
#  {
#      return feat.FeatureType;
#  }

#  public static Feature[] __GetAllChildren(Feature feat)
#  {
#      return feat.GetAllChildren();
#  }

#  public static Body[] __GetBodies(Feature feat)
#  {
#      return feat.GetBodies();
#  }

#  public static Feature[] __GetChildren(Feature feat)
#  {
#      return feat.GetChildren();
#  }

#  public static Edge[] __GetEdges(Feature feat)
#  {
#      return feat.GetEdges();
#  }

#  public static NXObject[] __GetEntities(Feature feat)
#  {
#      return feat.GetEntities();
#  }

#  public static Expression[] __GetExpressions(Feature feat)
#  {
#      return feat.GetExpressions();
#  }

#  public static Face[] __GetFaces(Feature feat)
#  {
#      return feat.GetFaces();
#  }

#  public static NXColor __GetFeatureColor(Feature feat)
#  {
#      return feat.GetFeatureColor();
#  }

#  public static Feature[] __GetParents(Feature feat)
#  {
#      return feat.GetParents();
#  }

#  public static Section[] __GetSections(Feature feat)
#  {
#      return feat.GetSections();
#  }

#  public static void __HideBody(Feature feat)
#  {
#      feat.HideBody();
#  }

#  public static void __HideParents(Feature feat)
#  {
#      feat.Unsuppress();
#  }

#  public static void __Highlight(Feature feat)
#  {
#      feat.Highlight();
#  }

#  public static void __LoadParentPart(Feature feat)
#  {
#      feat.LoadParentPart();
#  }

#  public static void __MakeCurrentFeature(Feature feat)
#  {
#      feat.MakeCurrentFeature();
#  }

#  public static void __RemoveParameters(Feature feat)
#  {
#      feat.RemoveParameters();
#  }

#  public static void __ShowBody(Feature feat, bool moveCurves)
#  {
#      feat.ShowBody(moveCurves);
#  }


#  public static void __Layer(this Feature feat, int layer)
#  {
#      foreach (var body in feat.GetBodies())
#          body.__Layer(layer);
#  }

#  public static void __Color(this Feature feat, int color)
#  {
#      foreach (var body in feat.GetBodies())
#          body.__Color(color);
#  }

#  #endregion


#   #region Extrude

#  [Obsolete(nameof(NotImplementedException))]
#  public static Extrude __Mirror(
#      this Extrude extrude,
#      Surface.Plane plane)
#  {
#      throw new NotImplementedException();
#  }

#  [Obsolete(nameof(NotImplementedException))]
#  public static Extrude __Mirror(
#      this Extrude extrude,
#      Surface.Plane plane,
#      Component from,
#      Component to)
#  {
#      throw new NotImplementedException();
#  }

#  #endregion


#     #region ExtractFace

#    public static int __Layer(this ExtractFace ext)
#    {
#        return ext.GetBodies()[0].Layer;
#    }

#    public static bool __IsFixedTimeStamp(this ExtractFace extractFace)
#    {
#        var builder = extractFace.__OwningPart().Features.CreateExtractFaceBuilder(extractFace);

#        using(session_.__UsingBuilderDestroyer(builder))
#            return builder.FixAtCurrentTimestamp;
#    }

#    public static void __Layer(this ExtractFace ext, int layer)
#    {
#        foreach (Body body in ext.GetBodies())
#            body.__Layer(layer);
#    }


def extract_face_is_linked_body(feature: Feature) -> bool:
    return feature.FeatureType == "LINKED_BODY"


#    /// <summary>
#    ///     Gets a value indicating whether or not this {extractFace} is broken.
#    /// </summary>
#    /// <remarks>Returns true if {extractFace} is broken, false otherwise.</remarks>
#    /// <param name="nxExtractFace">The extractFace.</param>
#    /// <returns>True or false.</returns>
#    public static bool __IsBroken(this ExtractFace nxExtractFace)
#    {
#        UFSession.GetUFSession().Wave.IsLinkBroken(nxExtractFace.Tag, out bool isBroken);
#        return isBroken;
#    }

#    public static Tag __XFormTag(this ExtractFace extractFace)
#    {
#        ufsession_.Wave.AskLinkXform(extractFace.Tag, out Tag xform);
#        return xform;
#    }

#    #endregion


#  #region Exception

#  public static void __PrintException(this Exception ex)
#  {
#      ex.__PrintException(null);
#  }

#  public static void __PrintException(this Exception ex, string userMessage)
#  {
#      _ = ex.GetType();
#      _ = ex.Message;

#      //int __nx_error_code = -1;

#      //var error_lines = new List<string>();


#      print("///////////////////////////////////////////");

#      if (!string.IsNullOrEmpty(userMessage))
#          print($"UserMessage: {userMessage}");

#      print($"Message: {ex.Message}");

#      print($"Exception: {ex.GetType()}");

#      if (ex is NXException nx)
#          print($"Error Code: {nx.ErrorCode}");

#      string[] methods = ex.StackTrace.Split('\n');

#      //for (int i = 0; i < methods.Length; i++)
#      //{
#      //    string line = methods[i];

#      //    int lastIndex = line.LastIndexOf('\\');

#      //    if (lastIndex < 0)
#      //        continue;

#      //    string substring = line.Substring(lastIndex);

#      //    print_($"[{i}]: {substring}");

#      //    error_lines.Add($"[{i}]: {substring}");
#      //}

#      for (int i = 0; i < methods.Length; i++)
#          //string line = ;
#          //int lastIndex = line.LastIndexOf('\\');
#          //if (lastIndex < 0)
#          //    continue;
#          //string substring = line.Substring(lastIndex);
#          print($"[{i}]: {methods[i]}");
#      //error_lines.Add($"[{i}]: {substring}");
#      print("///////////////////////////////////////////");
#      //foreach(var)
#      //using (var cnn = new SqlConnection(conn_str))
#      //{
#      //    cnn.Open();

#      //    using (var sql = new SqlCommand
#      //    {
#      //        Connection = cnn,

#      //        CommandText = $@"insert into ufunc_exceptions
#      //                        (ufunc_exception_type)
#      //                        values
#      //                        ('{ex.Message}')"


#      //    })
#      //        sql.ExecuteScalar();
#      //}
#  }

#  #endregion


def vector3d_unitize0(vec: Vector3d, tolerance: float = 0.001) -> Vector3d:
    return to_vector3d(vector3d_unitize1(vec, tolerance)[1])


def vector3d_unitize1(
    vec: Vector3d, tolerance: float = 0.001
) -> Tuple[float, Sequence[float]]:
    return ufsession().Vec3.Unitize(to_list(vec), tolerance)


#         #region Curve

#         /// <summary>
#         ///     Calculates the first derivative vector on the curve at a given parameter value
#         /// </summary>
#         /// <param name="curve">The curve</param>
#         /// <param name="value">Parameter value</param>
#         /// <returns>First derivative vector (not unitized)</returns>
#         /// <remarks>
#         ///     The vector returned is usually not a unit vector. In fact, it may even have zero<br />
#         ///     length, in certain unusual cases.
#         /// </remarks>
#         public static Vector3d __Derivative(this Curve curve, double value)
#         {
#             UFEval eval = ufsession_.Eval;
#             eval.Initialize2(curve.Tag, out IntPtr evaluator);
#             double[] array = new double[3];
#             double[] array2 = new double[3];
#             value /= Factor;
#             eval.Evaluate(evaluator, 1, value, array, array2);
#             eval.Free(evaluator);
#             Vector3d vector = array2.__ToVector3d();
#             return vector.__Divide(Factor);
#         }

#         //
#         // Summary:
#         //     Calculates the parameter value at a point on the curve
#         //
#         // Parameters:
#         //   point:
#         //     The point
#         //
#         // Returns:
#         //     Parameter value at the point (not unitized)
#         //
#         // Remarks:
#         //     The Parameter function and the Position function are designed to work together
#         //     smoothly -- each of these functions is the "reverse" of the other. So, if c is
#         //     any curve and t is any parameter value, then
#         //     c.Parameter(c.Position(t)) = t
#         //     Also, if p is any point on the curve c, then
#         //     c.Position(c.Parameter(p)) = p
#         public static double __Parameter(this Curve curve, Point3d point)
#         {
#             Tag nXOpenTag = curve.Tag;
#             double[] array = point.__ToArray();
#             int direction = 1;
#             const double offset = 0.0;
#             double tolerance = 0.0001;
#             double[] pointAlongCurve = new double[3];
#             ufsession_.Modl.AskPointAlongCurve2(
#                 array,
#                 nXOpenTag,
#                 offset,
#                 direction,
#                 tolerance,
#                 pointAlongCurve,
#                 out double parameter
#             );
#             return (1.0 - parameter) * curve.__MinU() + parameter * curve.__MaxU();
#         }

#         ////
#         //// Summary:
#         ////     The lower-limit parameter value (at the start-point of the curve)
#         ////
#         //// Remarks:
#         ////     If c is a curve, then c.Position(c.MinU) = c.StartPoint
#         //public static double __MinU(this Curve curve)
#         //{
#         //    var eval = ufsession_.Eval;
#         //    eval.Initialize2(curve.Tag, out var evaluator);
#         //    var array = new double[2] { 0.0, 1.0 };
#         //    eval.AskLimits(evaluator, array);
#         //    eval.Free(evaluator);
#         //    return Factor * array[0];
#         //}

#         ////
#         //// Summary:
#         ////     The upper-limit parameter value (at the end-point of the curve)
#         ////
#         //// Remarks:
#         ////     If c is a curve, then c.Position(c.MaxU) = c.EndPoint
#         //public static double __MaxU(this Curve curve)
#         //{
#         //    var eval = ufsession_.Eval;
#         //    eval.Initialize2(curve.Tag, out var evaluator);
#         //    var array = new double[2] { 0.0, 1.0 };
#         //    eval.AskLimits(evaluator, array);
#         //    eval.Free(evaluator);
#         //    return Factor * array[1];
#         //}

#         public static Curve __Copy(this Curve curve)
#         {
#             switch (curve)
#             {
#                 case Line line:
#                     return line.__Copy();
#                 case Arc arc:
# #pragma warning disable CS0618 // Type or member is obsolete
#                     return arc.__Copy();
# #pragma warning restore CS0618 // Type or member is obsolete
#                 case Ellipse ellipse:
#                     return ellipse.__Copy();
#                 case Parabola parabola:
# #pragma warning disable CS0612 // Type or member is obsolete
#                     return parabola.__Copy();
# #pragma warning restore CS0612 // Type or member is obsolete
#                 case Hyperbola _:
#                     //return hyperbola.__Copy();
#                     throw new NotImplementedException();
#                 case Spline spline:
#                     return spline.__Copy();
#                 default:
#                     throw new ArgumentOutOfRangeException();
#             }
#         }

#         //
#         // Summary:
#         //     Calculates a point on the curve at a given parameter value
#         //
#         // Parameters:
#         //   value:
#         //     Parameter value
#         //
#         // Returns:
#         //     The point corresponding to the given parameter value
#         //
#         // Remarks:
#         //     If you want to calculate several points on a curve, the PositionArray functions
#         //     might be more useful. The following example shows how the Position function can
#         //     be used to calculate a sequence of points along a curve.
#         public static Point3d __Position(this Curve curve, double value)
#         {
#             //using(session_.using_evaluator(curve.Tag))
#             //{

#             //}

#             UFEval eval = ufsession_.Eval;
#             eval.Initialize2(curve.Tag, out IntPtr evaluator);
#             double[] array = new double[3];
#             double[] array3 = new double[3];
#             value /= Factor;
#             eval.Evaluate(evaluator, 0, value, array, array3);
#             eval.Free(evaluator);
#             return array.__ToPoint3d();
#         }

#         //
#         // Summary:
#         //     Copies an array of NX.Curve (with no transform)
#         //
#         // Parameters:
#         //   original:
#         //     Original NX.Curve array
#         //
#         // Returns:
#         //     A copy of the input curves
#         //
#         // Remarks:
#         //     The new curves will be on the same layers as the original ones.
#         //
#         //     The function will throw an NXOpen.NXException, if the copy operation cannot be
#         //     performed.
#         [Obsolete(nameof(NotImplementedException))]
#         public static Curve[] __Copy(this Curve curve, params Curve[] original)
#         {
#             Curve[] array = new Curve[original.Length];
#             for (int i = 0; i < original.Length; i++)
#                 array[i] = original[i].__Copy();

#             return array;
#         }

#         //
#         // Summary:
#         //     Trim a curve to a parameter interval
#         //
#         // Parameters:
#         //   lowerParam:
#         //     The lower-limit parameter value
#         //
#         //   upperParam:
#         //     The upper-limit parameter value
#         [Obsolete(nameof(NotImplementedException))]
#         public static void __CreateTrim(this Curve curve, double lowerParam, double upperParam)
#         {
#             //Part workPart = __work_part_;
#             //TrimCurve trimCurve = null;
#             //TrimCurveBuilder trimCurveBuilder = workPart.NXOpenPart.Features.CreateTrimCurveBuilder(trimCurve);
#             //trimCurveBuilder.InteresectionMethod = TrimCurveBuilder.InteresectionMethods.UserDefined;
#             //trimCurveBuilder.InteresectionDirectionOption = TrimCurveBuilder.InteresectionDirectionOptions.RelativeToWcs;
#             //trimCurveBuilder.CurvesToTrim.AllowSelfIntersection(allowSelfIntersection: true);
#             //trimCurveBuilder.CurvesToTrim.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.CurvesAndPoints);
#             //trimCurveBuilder.CurveOptions.Associative = false;
#             //trimCurveBuilder.CurveOptions.InputCurveOption = CurveOptions.InputCurve.Replace;
#             //trimCurveBuilder.CurveExtensionType = TrimCurveBuilder.CurveExtensionTypes.Natural;
#             //Point point = Create.Point(Position(lowerParam));
#             //Point point2 = Create.Point(Position(upperParam));
#             //Section section = Section.CreateSection(point);
#             //Section section2 = Section.CreateSection(point2);
#             //trimCurveBuilder.CurveList.Add(base.NXOpenTaggedObject, null, StartPoint);
#             //SelectionIntentRule[] rules = Section.CreateSelectionIntentRule(this);
#             //trimCurveBuilder.CurvesToTrim.AddToSection(rules, (NXOpen.Curve)this, null, null, StartPoint, NXOpen.Section.Mode.Create, chainWithinFeature: false);
#             //trimCurveBuilder.FirstBoundingObject.Add(section.NXOpenSection);
#             //trimCurveBuilder.SecondBoundingObject.Add(section2.NXOpenSection);
#             //trimCurveBuilder.Commit();
#             //trimCurveBuilder.Destroy();
#             //section.NXOpenSection.Destroy();
#             //section2.NXOpenSection.Destroy();
#             //NXObject.Delete(point);
#             //NXObject.Delete(point2);
#             throw new NotImplementedException();
#         }

#         //
#         // Summary:
#         //     Divide a curve at an array of parameter values
#         //
#         // Parameters:
#         //   parameters:
#         //     The parameter values at which the curve should be divided
#         //
#         // Returns:
#         //     An array of Snap.NX.Curve objects
#         //
#         // Remarks:
#         //     The function will create new curves, and the original one will be unchanged.
#         //     If you want to modify the extents of an existing curve, please use the Snap.NX.Curve.Trim
#         //     function.
#         //
#         //     SNAP also provides functions for dividing specific types of curves, which may
#         //     be more convenient, in many cases. Links to these functions are provided in the
#         //     "See Also" section below.
#         [Obsolete(nameof(NotImplementedException))]
#         public static Curve[] __Divide(this Curve curve, params double[] parameters)
#         {
#             //Curve curve = Copy();
#             //Part workPart = __work_part_;
#             //DivideCurveBuilder divideCurveBuilder = workPart.NXOpenPart.BaseFeatures.CreateDivideCurveBuilder(null);
#             //divideCurveBuilder.Type = DivideCurveBuilder.Types.ByBoundingObjects;
#             //BoundingObjectBuilder[] array = new BoundingObjectBuilder[parameters.Length];
#             //Point[] array2 = new Point[parameters.Length];
#             //for (int i = 0; i < parameters.Length; i++)
#             //{
#             //    array[i] = workPart.NXOpenPart.CreateBoundingObjectBuilder();
#             //    array[i].BoundingPlane = null;
#             //    array[i].BoundingObjectMethod = BoundingObjectBuilder.Method.ProjectPoint;
#             //    array2[i] = Create.Point(curve.Position(parameters[i]));
#             //    array[i].BoundingProjectPoint = array2[i];
#             //    divideCurveBuilder.BoundingObjects.Append(array[i]);
#             //}

#             //NXOpen.View workView = workPart.NXOpenPart.ModelingViews.WorkView;
#             //divideCurveBuilder.DividingCurve.SetValue(curve, workView, curve.StartPoint);
#             //divideCurveBuilder.Commit();
#             //NXOpen.NXObject[] committedObjects = divideCurveBuilder.GetCommittedObjects();
#             //divideCurveBuilder.Destroy();
#             //Curve[] array3 = new Curve[committedObjects.Length];
#             //for (int j = 0; j < array3.Length; j++)
#             //{
#             //    array3[j] = CreateCurve((NXOpen.Curve)committedObjects[j]);
#             //}

#             //NXObject.Delete(array2);
#             //return array3;
#             throw new NotImplementedException();
#         }

#         //
#         // Summary:
#         //     Divide a curve at its intersection with another curve
#         //
#         // Parameters:
#         //   boundingCurve:
#         //     Bounding curve to be used to divide the given curve
#         //
#         //   helpPoint:
#         //     A point near the desired dividing point
#         //
#         // Returns:
#         //     An array of two Snap.NX.Curve objects
#         //
#         // Remarks:
#         //     This function will create two new curves, and the original one will be unchanged.
#         //     If you want to modify the extents of an existing curve, please use the Snap.NX.Curve.Trim
#         //     function.
#         //
#         //     SNAP also provides functions for dividing specific types of curves, which may
#         //     be more convenient, in many cases. Links to these functions are provided in the
#         //     "See Also" section below.
#         [Obsolete(nameof(NotImplementedException))]
#         public static Curve[] __Divide(this Curve curve, ICurve boundingCurve, Point3d helpPoint)
#         {
#             //Compute.IntersectionResult intersectionResult = Compute.IntersectInfo(this, boundingCurve, helpPoint);
#             //return Divide(intersectionResult.CurveParameter);
#             throw new NotImplementedException();
#         }

#         //
#         // Summary:
#         //     Divide a curve at its intersection with a given face
#         //
#         // Parameters:
#         //   face:
#         //     A face to be used to divide the given curve
#         //
#         //   helpPoint:
#         //     A point near the desired dividing point
#         //
#         // Returns:
#         //     An array of two Snap.NX.Curve objects
#         //
#         // Remarks:
#         //     This function will create two new curves, and the original one will be unchanged.
#         //     If you want to modify the extents of an existing curve, please use the Snap.NX.Curve.Trim
#         //     function.
#         //
#         //     SNAP also provides functions for dividing specific types of curves, which may
#         //     be more convenient, in many cases. Links to these functions are provided in the
#         //     "See Also" section below.
#         [Obsolete(nameof(NotImplementedException))]
#         public static Curve[] __Divide(this Curve curve, Face face, Point3d helpPoint)
#         {
#             //Compute.IntersectionResult intersectionResult = Compute.IntersectInfo(this, face, helpPoint);
#             //return Divide(intersectionResult.CurveParameter);
#             throw new NotImplementedException();
#         }

#         //
#         // Summary:
#         //     Divide a curve at its intersection with a given plane
#         //
#         // Parameters:
#         //   geomPlane:
#         //     A plane to be used to divide the given curve
#         //
#         //   helpPoint:
#         //     A point near the desired dividing point
#         //
#         // Returns:
#         //     An array of two Snap.NX.Curve objects
#         //
#         // Remarks:
#         //     This function will create two new curves, and the original one will be unchanged.
#         //     If you want to modify the extents of an existing curve, please use the Snap.NX.Curve.Trim
#         //     function.
#         //
#         //     SNAP also provides functions for dividing specific types of curves, which may
#         //     be more convenient, in many cases. Links to these functions are provided in the
#         //     "See Also" section below.
#         [Obsolete(nameof(NotImplementedException))]
#         public static Curve[] __Divide(
#             this Curve curve, /* Surface.Plane geomPlane,*/
#             Point3d helpPoint
#         )
#         {
#             //Compute.IntersectionResult intersectionResult = Compute.IntersectInfo(this, geomPlane, helpPoint);
#             //return Divide(intersectionResult.CurveParameter);
#             throw new NotImplementedException();
#         }

#         public static bool __IsClosed(this Curve curve)
#         {
#             int result = ufsession_.Modl.AskCurveClosed(curve.Tag);

#             switch (result)
#             {
#                 case 0:
#                     return false;
#                 case 1:
#                     return true;
#                 default:
#                     throw NXException.Create(result);
#             }
#         }

#         //
#         // Summary:
#         //     Conversion factor between NX Open and SNAP parameter values. Needed because NX
#         //     Open uses radians, where SNAP uses degrees
#         //
#         // Remarks:
#         //     When converting an NX Open parameter to a SNAP parameter, snapValue = nxopenValue
#         //     * Factor
#         //
#         //     When converting a SNAP parameter to an NX Open parameter, nxopenValue = snapValue
#         //     / Factor
#         internal static double __Factor(this Curve _)
#         {
#             return 1.0;
#         }

#         /// <summary>The lower u-value (at the start point of the curve)</summary>
#         /// <param name="curve">The curve</param>
#         /// <returns>The value at the start of the curve</returns>
#         public static double __MinU(this Curve curve)
#         {
#             UFEval eval = ufsession_.Eval;
#             eval.Initialize2(curve.Tag, out IntPtr evaluator);
#             double[] array = new double[2] { 0.0, 1.0 };
#             eval.AskLimits(evaluator, array);
#             eval.Free(evaluator);
#             return 1.0 * array[0];
#         }


def curve_max_u(curve: Curve) -> float:
    """
    #         /// <summary>The upper u-value (at the start point of the curve)</summary>
    #         /// <param name="curve">The curve</param>
    #         /// <returns>The value at the end of the curve</returns>
    """
    # UFEval
    eval = ufsession().Eval
    evaluator = eval.Initialize2(curve.Tag)
    array = [0.0, 1.0]
    eval.AskLimits(evaluator, array)
    eval.Free(evaluator)
    return 1.0 * array[1]


#         ///// <summary>Calculates a point on the icurve at a given parameter value</summary>
#         ///// <param name="curve">The curve</param>
#         ///// <param name="value">The parameter value</param>
#         ///// <returns>The <see cref="NXOpen.Point3d" /></returns>
#         //public static Point3d _Position(this Curve curve, double value)
#         //{
#         //    var eval = ufsession_.Eval;
#         //    eval.Initialize2(curve.Tag, out var evaluator);
#         //    var array = new double[3];
#         //    var array2 = array;
#         //    var array3 = new double[3];
#         //    var derivatives = array3;
#         //    value /= 1.0;
#         //    eval.Evaluate(evaluator, 0, value, array2, derivatives);
#         //    eval.Free(evaluator);
#         //    return array2.__ToPoint3d();
#         //}

#         public static Point3d __StartPoint(this Curve curve)
#         {
#             return curve.__Position(curve.__MinU());
#         }

#         public static Point3d __EndPoint(this Curve curve)
#         {
#             return curve.__Position(curve.__MaxU());
#         }

#         public static Point3d __MidPoint(this Curve curve)
#         {
#             double max = curve.__MaxU();
#             double min = curve.__MinU();
#             double diff = max - min;
#             double quotient = diff / 2;
#             double total = max - quotient;
#             return curve.__Position(total);
#         }

#         [Obsolete(nameof(NotImplementedException))]
#         public static void /* Box3d*/
#         __Box(this Curve curve)
#         {
#             //double[] array = new double[3];
#             //double[,] array2 = new double[3, 3];
#             //double[] array3 = new double[3];
#             //Tag tag = curve.Tag;
#             //ufsession_.Modl.AskBoundingBoxExact(tag, Tag.Null, array, array2, array3);
#             //var minXYZ = _Point3dOrigin;
#             //var vector = new NXOpen.Vector3d(array2[0, 0], array2[0, 1], array2[0, 2]);
#             //var vector2 = new NXOpen.Vector3d(array2[1, 0], array2[1, 1], array2[1, 2]);
#             //var vector3 = new NXOpen.Vector3d(array2[2, 0], array2[2, 1], array2[2, 2]);
#             //var maxXYZ = new NXOpen.Point3d((array + array3[0] * vector + array3[1] * vector2 + array3[2] * vector3).Array);
#             //return new Box3d(minXYZ, maxXYZ);
#             throw new NotImplementedException();
#         }


def curve_is_closed(curve: Curve) -> bool:
    status = ufsession().Modl.AskCurvePeriodicity(curve.Tag)
    #  Status of the curve. UF_MODL_OPEN_CURVE UF_MODL_CLOSED_PERIODIC_CURVE UF_MODL_CLOSED_NON_PERIODIC_CURVE
    raise Exception()


#         //
#         // Summary:
#         //     Calculates unit normal at a given parameter value
#         //
#         // Parameters:
#         //   value:
#         //     Parameter value
#         //
#         // Returns:
#         //     Unit normal vector
#         //
#         // Remarks:
#         //     The normal lies in the "osculating plane" of the curve at the given parameter
#         //     value (the plane that most closely matches the curve). So, if the curve is planar,
#         //     the normal always lies in the plane of the curve.
#         //
#         //     The normal always points towards the center of curvature of the curve. So, if
#         //     the curve has an inflexion, the normal will flip from one side to the other,
#         //     which may be undesirable.
#         //
#         //     The normal is the cross product of the binormal and the tangent: N = B*T
#         public static Vector3d __Normal(this Curve curve, double value)
#         {
#             //UFEval eval = ufsession_.Eval;
#             //eval.Initialize2(NXOpenTag, out var evaluator);
#             //double[] array = new double[3];
#             //double[] point = array;
#             //double[] array2 = new double[3];
#             //double[] tangent = array2;
#             //double[] array3 = new double[3];
#             //double[] array4 = array3;
#             //double[] array5 = new double[3];
#             //double[] binormal = array5;
#             //value /= Factor;
#             //eval.EvaluateUnitVectors(evaluator, value, point, tangent, array4, binormal);
#             //eval.Free(evaluator);
#             //return new Vector(array4);
#             throw new NotImplementedException();
#         }

#         //
#         // Summary:
#         //     Calculates the unit binormal at a given parameter value
#         //
#         // Parameters:
#         //   value:
#         //     Parameter value
#         //
#         // Returns:
#         //     Unit binormal
#         //
#         // Remarks:
#         //     The binormal is normal to the "osculating plane" of the curve at the given parameter
#         //     value (the plane that most closely matches the curve). So, if the curve is planar,
#         //     the binormal is normal to the plane of the curve.
#         //
#         //     The binormal is the cross product of the tangent and the normal: B = Cross(T,N).
#         [Obsolete(nameof(NotImplementedException))]
#         public static Vector3d __Binormal(this Curve curve, double value)
#         {
#             //UFEval eval = ufsession_.Eval;
#             //eval.Initialize2(NXOpenTag, out var evaluator);
#             //double[] array = new double[3];
#             //double[] point = array;
#             //double[] array2 = new double[3];
#             //double[] tangent = array2;
#             //double[] array3 = new double[3];
#             //double[] normal = array3;
#             //double[] array4 = new double[3];
#             //double[] array5 = array4;
#             //value /= Factor;
#             //eval.EvaluateUnitVectors(evaluator, value, point, tangent, normal, array5);
#             //eval.Free(evaluator);
#             //return new Vector(array5);
#             throw new NotImplementedException();
#         }

#         //
#         // Summary:
#         //     Calculates curvature at a given parameter value
#         //
#         // Parameters:
#         //   value:
#         //     Parameter value
#         //
#         // Returns:
#         //     Curvature value (always non-negative)
#         //
#         // Remarks:
#         //     Curvature is the reciprocal of radius of curvature. So, on a straight line, curvature
#         //     is zero and radius of curvature is infinite. On a circle of radius 5, curvature
#         //     is 0.2 (and radius of curvature is 5, of course).
#         public static double __Curvature(this Curve curve, double value)
#         {
#             //Vector[] array = Derivatives(value, 2);
#             //double num = Vector.Norm(Vector.Cross(array[1], array[2]));
#             //double num2 = Vector.Norm(array[1]);
#             //double num3 = num2 * num2 * num2;
#             //return num / num3;
#             throw new NotImplementedException();
#         }

#         ////
#         //// Summary:
#         ////     Calculates the parameter value at a point on the curve
#         ////
#         //// Parameters:
#         ////   point:
#         ////     The point
#         ////
#         //// Returns:
#         ////     Parameter value at the point (not unitized)
#         ////
#         //// Remarks:
#         ////     The Parameter function and the Position function are designed to work together
#         ////     smoothly -- each of these functions is the "reverse" of the other. So, if c is
#         ////     any curve and t is any parameter value, then
#         ////
#         ////     c.Parameter(c.Position(t)) = t
#         ////
#         ////     Also, if p is any point on the curve c, then
#         ////
#         ////     c.Position(c.Parameter(p)) = p
#         //public static double __Parameter(this Curve curve, Point3d point)
#         //{
#         //    var nXOpenTag = curve.Tag;
#         //    var array = point._ToArray();
#         //    var direction = 1;
#         //    var offset = 0.0;
#         //    var tolerance = 0.0001;
#         //    var point_along_curve = new double[3];
#         //    ufsession_.Modl.AskPointAlongCurve2(array, nXOpenTag, offset, direction, tolerance, point_along_curve,
#         //        out var parameter);
#         //    return (1.0 - parameter) * curve.__MinU() + parameter * curve.__MaxU();
#         //}

#         /// <summary>
#         ///     Calculates the parameter value defined by an arclength step along a curve
#         /// </summary>
#         /// <param name="curve">The curve to find parameter value along</param>
#         /// <param name="baseParameter">The curve parameter value at the starting location</param>
#         /// <param name="arclength">The arclength increment along the curve (the length of our step)</param>
#         /// <remarks>
#         ///     This function returns the curve parameter value at the far end of a "step" along<br />
#         ///     a curve. The start of the step is defined by a given parameter value, and the<br />
#         ///     size of the step is given by an arclength along the curve. The arclength step<br />
#         ///     may be positive or negative.
#         /// </remarks>
#         /// <returns>The curve parameter value at the far end of the step</returns>
#         public static double __Parameter(this Curve curve, double baseParameter, double arclength)
#         {
#             int direction = 1;

#             if (arclength < 0.0)
#                 direction = -1;

#             double[] array = curve.__Position(baseParameter).__ToArray();
#             double tolerance = 0.0001;
#             double[] pointAlongCurve = new double[3];
#             UFSession uFSession = ufsession_;

#             uFSession.Modl.AskPointAlongCurve2(
#                 array,
#                 curve.Tag,
#                 System.Math.Abs(arclength),
#                 direction,
#                 tolerance,
#                 pointAlongCurve,
#                 out double parameter
#             );

#             return parameter * (curve.__MaxU() - curve.__MinU()) + curve.__MinU();
#         }

#         //
#         // Summary:
#         //     Calculates the parameter value at a fractional arclength value along a curve
#         //
#         //
#         // Parameters:
#         //   arclengthFraction:
#         //     Fractional arclength along the curve
#         //
#         // Returns:
#         //     Parameter value
#         //
#         // Remarks:
#         //     The input is a fractional arclength. A value of 0 corresponds to the start of
#         //     the curve, a value of 1 corresponds to the end-point, and values between 0 and
#         //     1 correspond to interior points along the curve.
#         //
#         //     You can input arclength values outside the range 0 to 1, and this will return
#         //     parameter values corresponding to points on the extension of the curve.
#         public static double __Parameter(this Curve curve, double arclengthFraction)
#         {
#             double arclength = curve.GetLength() * arclengthFraction;
#             return curve.__Parameter(curve.__MinU(), arclength);
#         }

#         ////
#         //// Summary:
#         ////     Copies an NX.Curve (with a null transform)
#         ////
#         //// Returns:
#         ////     A copy of the input curve
#         ////
#         //// Remarks:
#         ////     The new curve will be on the same layer as the original one.
#         //[Obsolete(nameof(NotImplementedException))]
#         //public static Curve __Copy(this Curve curve)
#         //{
#         //    //Transform xform = Transform.CreateTranslation(0.0, 0.0, 0.0);
#         //    //return Copy(xform);
#         //    throw new NotImplementedException();
#         //}


#         //
#         // Summary:
#         //     Calculates points on a curve at given parameter values
#         //
#         // Parameters:
#         //   values:
#         //     Parameter values
#         //
#         // Returns:
#         //     The points corresponding to the given parameter values
#         //
#         // Remarks:
#         //     Calling this function is typically around 3× as fast as calling the Curve.Position
#         //     function in a loop.
#         [Obsolete(nameof(NotImplementedException))]
#         public static Point3d[] __PositionArray(this Curve curve, double[] values)
#         {
#             throw new NotImplementedException();
#             //UFEval eval = ufsession_.Eval;
#             //eval.Initialize2(curve.Tag, out var evaluator);
#             //double[] array = new double[3];
#             //double[] array2 = array;
#             //double[] array3 = new double[3];
#             //double[] derivatives = array3;
#             //double num = 1.0 / Factor;
#             //var array4 = new NXOpen.Point3d[values.LongLength];
#             //for (long num2 = 0L; num2 < values.LongLength; num2++)
#             //{
#             //    double parm = values[num2] * num;
#             //    eval.Evaluate(evaluator, 0, parm, array2, derivatives);
#             //    ref Position reference = ref array4[num2];
#             //    reference = new Position(array2);
#             //}

#             //eval.Free(evaluator);
#             //return array4;
#         }

#         //
#         // Summary:
#         //     Calculates the unit tangent vector at a given parameter value
#         //
#         // Parameters:
#         //   value:
#         //     Parameter value
#         //
#         // Returns:
#         //     Unit tangent vector
#         //
#         // Remarks:
#         //     This function successfully calculates a unit tangent vector even in those (rare)
#         //     cases where the derivative vector of the curve has zero length.
#         public static Vector3d __Tangent(this Curve curve, double value)
#         {
#             UFEval eval = ufsession_.Eval;
#             eval.Initialize2(curve.Tag, out IntPtr evaluator);
#             double[] array = new double[3];
#             double[] array2 = new double[3];
#             double[] array4 = new double[3];
#             double[] array5 = new double[3];
#             value /= Factor;
#             eval.EvaluateUnitVectors(evaluator, value, array, array2, array4, array5);
#             eval.Free(evaluator);
#             return array2.__ToVector3d();
#         }

#         [Obsolete(nameof(NotImplementedException))]
#         public static Curve __Mirror(this Curve original, Surface.Plane plane)
#         {
#             //if(original is NXOpen.Line line)
#             //    return line._Mi
#             throw new NotImplementedException();
#         }

#         [Obsolete(nameof(NotImplementedException))]
#         public static Curve __Mirror(
#             this Curve bodyDumbRule,
#             Surface.Plane plane,
#             Component from,
#             Component to
#         )
#         {
#             throw new NotImplementedException();
#         }

#         //
#         // Summary:
#         //     Copies an NX.Curve (with a null transform)
#         //
#         // Returns:
#         //     A copy of the input curve
#         //
#         // Remarks:
#         //     The new curve will be on the same layer as the original one.
#         public static Curve Copy(this Curve curve)
#         {
#             Transform xform = Transform.CreateTranslation(0.0, 0.0, 0.0);
#             return curve.Copy(xform);
#         }

#         //
#         // Summary:
#         //     Transforms/copies an NX.Curve
#         //
#         // Parameters:
#         //   xform:
#         //     Transform to be applied
#         //
#         // Returns:
#         //     A transformed copy of NX.Curve
#         public static Curve Copy(this Curve curve, Transform xform)
#         {
#             var nxobject = (NXObject)curve;
#             return (Curve)nxobject.Copy(xform);
#         }

#         public static CompositeCurve LinkCurve(Curve curve)
#         {
#             WaveLinkBuilder builder = __work_part_.BaseFeatures.CreateWaveLinkBuilder(null);

#             using (session_.__UsingBuilderDestroyer(builder))
#             {
#                 builder.FixAtCurrentTimestamp = true;
#                 builder.CompositeCurveBuilder.Associative = true;
#                 CurveDumbRule rule = __work_part_.ScRuleFactory.CreateRuleCurveDumb(
#                     new[] { curve }
#                 );
#                 SelectionIntentRule[] rules = new SelectionIntentRule[] { rule };
#                 builder.CompositeCurveBuilder.Section.AddToSection(
#                     rules,
#                     curve,
#                     null,
#                     null,
#                     _Point3dOrigin,
#                     Section.Mode.Create,
#                     false
#                 );
#                 return (CompositeCurve)builder.Commit();
#             }
#         }

#         #endregion


#         #region Line


def line_mirror(line: Line, plane) -> Line:
    #  [Obsolete(nameof(NotImplementedException))]
    #  public static Line __Mirror(
    #      this Line line,
    #      Surface.Plane plane)
    #  {
    #      Point3d start = line.StartPoint.__Mirror(plane);
    #      Point3d end = line.EndPoint.__Mirror(plane);
    #      return line.__OwningPart().Curves.CreateLine(start, end);
    #  }
    raise NotImplementedError()


def line_copy(line: Line) -> Line:
    assert not line.IsOccurrence, f"cannot copy an occurrence line"
    return line.OwningPart.Curves.CreateLine(line.StartPoint, line.EndPoint)


#  /// <summary>Construct a line, given x,y,z coordinates of its end-points</summary>
#  /// <param name="x0">X-coordinate of start point</param>
#  /// <param name="y0">Y-coordinate of start point</param>
#  /// <param name="z0">Z-coordinate of start point</param>
#  /// <param name="x1">X-coordinate of end   point</param>
#  /// <param name="y1">Y-coordinate of end   point</param>
#  /// <param name="z1">Z-coordinate of end   point</param>
#  /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#  public static Line __CreateLine(double x0, double y0, double z0, double x1, double y1, double z1)
#  {
#      return __CreateLine(new Point3d(x0, y0, z0), new Point3d(x1, y1, z1));
#  }

#  /// <summary>Construct a line, given x,y coordinates of its end-points (z assumed zero)</summary>
#  /// <param name="x0">X-coordinate of start point</param>
#  /// <param name="y0">Y-coordinate of start point</param>
#  /// <param name="x1">X-coordinate of end   point</param>
#  /// <param name="y1">Y-coordinate of end   point</param>
#  /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#  public static Line __CreateLine(double x0, double y0, double x1, double y1)
#  {
#      return __CreateLine(new Point3d(x0, y0, 0.0), new Point3d(x1, y1, 0.0));
#  }

#  /// <summary>Creates a line between two positions</summary>
#  /// <param name="p0">NXOpen.Point3d for start of line</param>
#  /// <param name="p1">NXOpen.Point3d for end of line</param>
#  /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#  public static Line __CreateLine(Point3d p0, Point3d p1)
#  {
#      return __work_part_.Curves.CreateLine(p0, p1);
#  }

#  //
#  // Summary:
#  //     Copies an NX.Line object (with a null transform)
#  //
#  // Returns:
#  //     A copy of the input line
#  //
#  // Remarks:
#  //     The new line will be on the same layer as the original one.
#  [Obsolete]
#  public static Line Copy(this Line line)
#  {
#      Transform xform = Transform.CreateTranslation(0.0, 0.0, 0.0);
#      return line.Copy(xform);
#  }

#  //
#  // Summary:
#  //     Transforms/copies an NX.Arc
#  //
#  // Parameters:
#  //   xform:
#  //     Transform to be applied
#  //
#  // Returns:
#  //     A transformed copy of NX.Arc
#  [Obsolete]
#  public static Line Copy(this Line line, Transform xform)
#  {
#      var curve = (NXOpen.Curve)line;
#      return (Line)curve.Copy(xform);
#  }

#  // public static void __TryMatch(this TSG_Library.Geom.Curve.Arc)

#  public static Vector3d __Vector(this Line line)
#  {
#      return line.EndPoint.__Subtract(line.StartPoint);
#  }

#  // public static void __Move(this Line line, Vector3d vector, double distance)
#  // {

#  // }


#  public static void __Move(this Line line, Vector3d vector, double distance)
#  {
#      line.__OwningPart().__AssertIsWorkPart();
#      Vector3d unit = vector.__Unit();
#      Point3d new_start = line.StartPoint.__Add(unit, distance);
#      Point3d new_end = line.EndPoint.__Add(unit, distance);
#      line.SetStartPoint(new_start);
#      line.SetEndPoint(new_end);
#      line.RedisplayObject();
#      ufsession_.Modl.Update();
#  }

#  public static Line __Copy(this Line line, Vector3d vector, double distance)
#  {
#      line.__OwningPart().__AssertIsWorkPart();
#      Vector3d unit = vector.__Unit();
#      Point3d new_start = line.StartPoint.__Add(unit, distance);
#      Point3d new_end = line.EndPoint.__Add(unit, distance);
#      return line.__OwningPart().Curves.CreateLine(new_start, new_end);
#  }

#  public static NXObject __CopyNXObject(this NXObject nxobject, Vector3d vector)
#  {
#      nxobject.__OwningPart().__AssertIsWorkPart();

#      switch (nxobject)
#      {
#          case Line line:
#              return line.__Copy(vector);
#          case Arc arc:
#              return arc.__Copy(vector);
#          case Point point:
#              return point.__Copy(vector);
#          case Block block:
#              return block.__Copy(vector);
#          case Extrude extrude:
#              return extrude.__Copy(vector);
#          default:
#              throw new InvalidOperationException($"Unknown copy type: {nxobject.GetType().Name}");
#      }
#  }

#  public static Block __Copy(this Block block, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }

#  public static Arc __Copy(this Arc arc, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }

#  public static Line __Copy(this Line line, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }

#  public static Point __Copy(this Point point, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }

#  public static Extrude __Copy(this Extrude extrude, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }


#  // public static Point __Copy()
#  // {
#  //     ufsession_.Trns.CreateReflectionMatrix()
#  // }


#  // move point


#  // try to move arc

#  #endregion


#   #region Globals

#   static Extensions()
#   {
#       try
#       {
#           __assemblyFileVersion = typeof(Program).Assembly.GetCustomAttribute<AssemblyFileVersionAttribute>().Version;
#       }
#       catch (Exception ex)
#       {
#           ex.__PrintException();
#       }
#   }

#   public static void NXMessage(string message)
#   {
#       TheUISession.NXMessageBox.Show("Error", NXMessageBox.DialogType.Error, message);
#   }

#   public static string AssemblyFileVersion => __assemblyFileVersion;

#   private static readonly string __assemblyFileVersion;


#   /// <summary>A function that evaluates a position at a point on a curve</summary>
#   /// <param name="data">Data item to be used in evaluation</param>
#   /// <param name="t">Parameter value at which to evaluate (in range 0 to 1)</param>
#   /// <returns>NXOpen.Point3d on curve at given parameter value</returns>
#   /// <remarks>
#   ///     <para>
#   ///         You use a CurvePositionFunction when constructing approximating curves using
#   ///         the
#   ///         <see cref="M:Snap.Create.BezierCurveFit(Snap.Create.CurvePositionFunction,System.Object,System.Int32)">BezierCurveFit</see>
#   ///         function.
#   ///     </para>
#   /// </remarks>
#   /// <seealso cref="M:Snap.Create.BezierCurveFit(Snap.Create.CurvePositionFunction,System.Object,System.Int32)">BezierCurveFit</seealso>
#   public delegate Point3d CurvePositionFunction(object data, double t);

#   /// <summary>A function that evaluates a position at a location on a surface</summary>
#   /// <param name="data">Data item to be used in evaluation</param>
#   /// <param name="uv">Parameter values at which to evaluate (in range [0,1] x [0,1])</param>
#   /// <returns>NXOpen.Point3d on surface at given parameter value</returns>
#   /// <remarks>
#   ///     <para>
#   ///         You use a SurfacePositionFunction when constructing approximating surfaces using
#   ///         the
#   ///         <see
#   ///             cref="M:Snap.Create.BezierPatchFit(Snap.Create.SurfacePositionFunction,System.Object,System.Int32,System.Int32)">
#   ///             BezierPatchFit
#   ///         </see>
#   ///         function.
#   ///     </para>
#   /// </remarks>
#   /// <seealso
#   ///     cref="M:Snap.Create.BezierPatchFit(Snap.Create.SurfacePositionFunction,System.Object,System.Int32,System.Int32)">
#   ///     BezierPatchFit
#   /// </seealso>
#   public delegate Point3d SurfacePositionFunction(object data, params double[] uv);

#   public const string _printerCts = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC";

#   public const string _simActive = "P:\\CTS_SIM\\Active";

#   public static readonly IDictionary<string, ISet<string>> PrefferedDict = new Dictionary<string, ISet<string>>
#   {
#       ["006"] = new HashSet<string>
#       {
#           "6mm-shcs-010",
#           "6mm-shcs-012.prt",
#           "6mm-shcs-016.prt",
#           "6mm-shcs-020.prt",
#           "6mm-shcs-025.prt",
#           "6mm-shcs-030.prt",
#           "6mm-shcs-035.prt"
#       },

#       ["008"] = new HashSet<string>
#       {
#           "8mm-shcs-012",
#           "8mm-shcs-016",
#           "8mm-shcs-020",
#           "8mm-shcs-025",
#           "8mm-shcs-030",
#           "8mm-shcs-035",
#           "8mm-shcs-040",
#           "8mm-shcs-045",
#           "8mm-shcs-050",
#           "8mm-shcs-055",
#           "8mm-shcs-060",
#           "8mm-shcs-065"
#       },

#       ["010"] = new HashSet<string>
#       {
#           "10mm-shcs-020",
#           "10mm-shcs-030",
#           "10mm-shcs-040",
#           "10mm-shcs-050",
#           "10mm-shcs-070",
#           "10mm-shcs-090"
#       },

#       ["012"] = new HashSet<string>
#       {
#           "12mm-shcs-030",
#           "12mm-shcs-040",
#           "12mm-shcs-050",
#           "12mm-shcs-070",
#           "12mm-shcs-090",
#           "12mm-shcs-110"
#       },

#       ["016"] = new HashSet<string>
#       {
#           "16mm-shcs-040",
#           "16mm-shcs-055",
#           "16mm-shcs-070",
#           "16mm-shcs-090",
#           "16mm-shcs-110"
#       },

#       ["020"] = new HashSet<string>
#       {
#           "20mm-shcs-050",
#           "20mm-shcs-070",
#           "20mm-shcs-090",
#           "20mm-shcs-110",
#           "20mm-shcs-150"
#       },

#       ["0375"] = new HashSet<string>
#       {
#           "0375-shcs-075",
#           "0375-shcs-125",
#           "0375-shcs-200",
#           "0375-shcs-300",
#           "0375-shcs-400"
#       },

#       ["0500"] = new HashSet<string>
#       {
#           "0500-shcs-125",
#           "0500-shcs-200",
#           "0500-shcs-300",
#           "0500-shcs-400",
#           "0500-shcs-500"
#       },

#       ["0625"] = new HashSet<string>
#       {
#           "0625-shcs-125",
#           "0625-shcs-200",
#           "0625-shcs-300",
#           "0625-shcs-400",
#           "0625-shcs-500"
#       },

#       ["0750"] = new HashSet<string>
#       {
#           "0750-shcs-200",
#           "0750-shcs-300",
#           "0750-shcs-400",
#           "0750-shcs-500",
#           "0750-shcs-650"
#       }
#   };

#   public static UI TheUISession =>

#       UI.GetUI();

#   public static Session session_ =>

#       GetSession();

#   public static double Factor =>

#       1.0;

#   public static Point3d _Point3dOrigin
#   {

#       get { return new[] { 0d, 0d, 0d }.__ToPoint3d(); }
#   }

#   public static Matrix3x3 _Matrix3x3Identity
#   {

#       get
#       {
#           double[] array = new double[9];
#           ufsession_.Mtx3.Identity(array);
#           return array.__ToMatrix3x3();
#       }
#   }

#   /// <summary>
#   ///     Multiply by this number to convert Part Units to Millimeters (1 or 25.4)
#   /// </summary>

#   internal static double PartUnitsToMillimeters =>

#       MillimetersPerUnit;

#   /// <summary>
#   ///     Multiply by this number to convert Millimeters to Part Units (1 or 0.04)
#   /// </summary>

#   internal static double MillimetersToPartUnits =>

#       1.0 / PartUnitsToMillimeters;

#   /// <summary>
#   ///     Multiply by this number to convert Part Units to Inches (1 or 0.04)
#   /// </summary>
#   internal static double PartUnitsToInches =>

#       InchesPerUnit;

#   /// <summary>
#   ///     Multiply by this number to convert Inches to Part Units (either 1 or 25.4)
#   /// </summary>
#   internal static double InchesToPartUnits =>

#       1.0 / PartUnitsToInches;

#   //
#   // Summary:
#   //     Multiply by this number to convert Part Units to Meters, to go to Parasolid (0.001
#   //     or 0.0254)
#   internal static double PartUnitsToMeters =>

#       0.001 * PartUnitsToMillimeters;

#   //
#   // Summary:
#   //     Multiply by this number to convert Meters to Part Units, when coming from Parasolid
#   //     (1000 or 40)
#   internal static double MetersToPartUnits =>

#       1000.0 * MillimetersToPartUnits;

#   //
#   // Summary:
#   //     Multiply by this number to convert Part Units to Points (for font sizes)

#   internal static double PartUnitsToPoints =>

#       PartUnitsToInches * 72.0;

#   //
#   // Summary:
#   //     Multiply by this number to convert Points to Part Units (for font sizes)
#   internal static double PointsToPartUnits =>

#       1.0 / 72.0 * InchesToPartUnits;


#   /// <summary>
#   ///     Returns the current workComponent origin in terms of the current DisplayPart.
#   ///     If the workPart equals the current displayPart then returns the Absolute Origin.
#   /// </summary>

#   public static Point3d WorkCompOrigin => throw

#       //if (TSG_Library.Extensions.__work_part_.Tag == TSG_Library.Extensions.DisplayPart.Tag) return BaseOrigin;
#       //if (!(NXOpen.Session.session_.Parts.WorkComponent != null)) throw new System.Exception("NullWorkComponentException");
#       //return NXOpen.Assemblies.Component.Wrap(NXOpen.Session.session_.Parts.WorkComponent.Tag).Position;
#       new NotImplementedException();

#   //"CTS Office MFC on ctsfps1.cts.toolingsystemsgroup.com";

#   public static string __PrinterCts =>

#       _printerCts;

#   public static string __SimActive =>

#       _simActive;


#   public static Part __display_part_
#   {

#       get => session_.Parts.Display;

#       set => session_.Parts.SetDisplay(value, false, false, out _);
#   }

#   public static void UpdateModl()
#   {
#       ufsession_.Modl.Update();
#   }

#   public static ModelingView __work_view_ => __display_part_.ModelingViews.WorkView;


#   public static Part __work_part_
#   {

#       get => session_.Parts.Work;

#       set => session_.Parts.SetWork(value);
#   }

#   public static Part _WorkPart
#   {

#       get => session_.Parts.Work;

#       set => session_.Parts.SetWork(value);
#   }

#   public static UFSession _UFSession =>

#       ufsession_;

#   public static UI uisession_ =>

#       UI.GetUI();


#   public static WCS __wcs_
#   {

#       get => __display_part_.WCS;
#       //{

#       //    ufsession_.Csys.AskWcs(out Tag wcs_id);
#       //    return (CartesianCoordinateSystem)session_.__GetTaggedObject(wcs_id);
#       //}
#       //
#       //set => ufsession_.Csys.SetWcs(value.Tag);
#   }


#   public static Component __work_component_
#   {

#       get => session_.Parts.WorkComponent is null
#           ? null
#           : session_.Parts.WorkComponent;

#       set => ufsession_.Assem.SetWorkOccurrence(value.Tag);
#   }


#   public static UFSession uf_ =>

#       ufsession_;

#   public static UFSession ufsession_ => NXOpen.UF.UFSession.GetUFSession();

#   public static string TodaysDate
#   {

#       get
#       {
#           string day = DateTime.Today.Day < 10
#               ? '0' + DateTime.Today.Day.ToString()
#               : DateTime.Today.Day.ToString();
#           string month = DateTime.Today.Month < 10
#               ? '0' + DateTime.Today.Month.ToString()
#               : DateTime.Today.Month.ToString();
#           return DateTime.Today.Year + "-" + month + "-" + day;
#       }
#   }

#   public static int __process_id =>

#       Process.GetCurrentProcess().Id;

#   public static string __user_name =>

#       Environment.UserName;


#   /// <summary>The work layer (the layer on which newly-created objects should be placed)</summary>
#   /// <remarks>
#   ///     <para>
#   ///         When you change the work layer, the previous work layer is given the status "Selectable".
#   ///     </para>
#   /// </remarks>
#   public static int WorkLayer
#   {

#       get => __work_part_.Layers.WorkLayer;

#       set => __work_part_.Layers.WorkLayer = value;
#   }

#   public static NXOpen.Preferences.WorkPlane __work_plane_ => __display_part_.Preferences.Workplane;

#   /// <summary>Millimeters Per Unit (either 1 or 25.4)</summary>
#   /// <remarks>
#   ///     <para>
#   ///         A constant representing the number of millimeters in one part unit.
#   ///     </para>
#   ///     <para>If UnitType == Millimeter, then MillimetersPerUnit = 1.</para>
#   ///     <para>If UnitType == Inch, then MillimetersPerUnit = 25.4</para>
#   /// </remarks>
#   public static double MillimetersPerUnit =>

#       __work_part_.PartUnits != BasePart.Units.Millimeters ? 25.4 : 1.0;

#   /// <summary>Inches per part unit (either 1 or roughly 0.04)</summary>
#   /// <remarks>
#   ///     <para>
#   ///         A constant representing the number of inches in one part unit.
#   ///     </para>
#   ///     <para>If UnitType = Millimeter, then InchesPerUnit = 0.0393700787402</para>
#   ///     <para>If UnitType = Inch, then InchesPerUnit = 1.</para>
#   /// </remarks>
#   public static double InchesPerUnit =>

#       __work_part_.PartUnits != BasePart.Units.Millimeters ? 1.0 : 5.0 / sbyte.MaxValue;

#   /// <summary>Distance tolerance</summary>
#   /// <remarks>
#   ///     <para>
#   ///         This distance tolerance is the same one that you access via Preferences → Modeling Preferences in interactive
#   ///         NX.
#   ///         In many functions in NX, an approximation process is used to construct geometry (curves or bodies).
#   ///         The distance tolerance (together with the angle tolerance) controls the accuracy of this approximation, unless
#   ///         you specify some over-riding tolerance within the function itself. For example, when you offset a curve, NX
#   ///         will construct a spline curve that approximates the true offset to within the current distance tolerance.
#   ///     </para>
#   /// </remarks>
#   public static double DistanceTolerance
#   {

#       get => __work_part_.Preferences.Modeling.DistanceToleranceData;

#       set => __work_part_.Preferences.Modeling.DistanceToleranceData = value;
#   }

#   /// <summary>Angle tolerance, in degrees</summary>
#   /// <remarks>
#   ///     <para>
#   ///         This angle tolerance is the same one that you access via Preference → Modeling Preferences in interactive NX.
#   ///         In many functions in NX, an approximation process is used to construct geometry (curves or bodies).
#   ///         The angle tolerance (together with the distance tolerance) controls the accuracy of this approximation, unless
#   ///         you specify some over-riding tolerance within the function itself. For example, when you create a Through Curve
#   ///         Mesh
#   ///         feature in NX, the resulting surface will match the input curves to within the current distance and angle
#   ///         tolerances.
#   ///     </para>
#   ///     <para>
#   ///         The angle tolerance is expressed in degrees.
#   ///     </para>
#   /// </remarks>
#   public static double AngleTolerance
#   {

#       get => __work_part_.Preferences.Modeling.AngleToleranceData;

#       set => __work_part_.Preferences.Modeling.AngleToleranceData = value;
#   }

#   /// <summary>The chaining tolerance used in building "section" objects</summary>
#   /// <remarks>
#   ///     <para>
#   ///         Most modeling features seem to set this internally to 0.95*DistanceTolerance,
#   ///         so that's what we use here.
#   ///     </para>
#   /// </remarks>
#   internal static double ChainingTolerance =>

#       0.95 * DistanceTolerance;

#   /// <summary>
#   ///     If true, indicates that the modeling mode is set to History mode
#   ///     (as opposed to History-free mode).
#   /// </summary>
#   /// <remarks>
#   ///     <para>
#   ///         This is the same setting that you access via
#   ///         Insert → Synchronous Modeling → History Mode in interactive NX.
#   ///         Please refer to the NX documentation for a discussion of the History and
#   ///         History-free modeling modes.
#   ///     </para>
#   ///     <para>
#   ///         To create features in SNAP code, you must first set HistoryMode to True.
#   ///     </para>
#   /// </remarks>
#   public static bool HistoryMode
#   {

#       get => __work_part_.Preferences.Modeling.GetHistoryMode();

#       set
#       {
#           if (value)
#               __work_part_.Preferences.Modeling.SetHistoryMode();
#           else
#               __work_part_.Preferences.Modeling.SetHistoryFreeMode();
#       }
#   }

#   ///// <summary>The unit type of the work part</summary>
#   ///// <remarks>
#   /////     <para>
#   /////         This property only gives the type of the unit.
#   /////         To get a Snap.NX.Unit object, please use the
#   /////         <see cref="P:TSG_Library.PartUnit">TSG_Library.PartUnit</see>
#   /////         property, instead.
#   /////     </para>
#   ///// </remarks>
#   //public static Utilities. Unit UnitType
#   //{
#   //
#   //    get
#   //    {
#   //        var workPart = __work_part_;
#   //        ufsession_.Part.AskUnits(workPart.Tag, out var part_units);
#   //        return part_units == 1 ? Utilities.Unit.Millimeter : Utilities.Unit.Inch;
#   //    }
#   //}

#   /// <summary>
#   ///     The work coordinate system (Wcs) of the work part
#   /// </summary>
#   public static CartesianCoordinateSystem __Wcs_
#   {

#       get
#       {
#           UFSession uFSession = ufsession_;
#           uFSession.Csys.AskWcs(out Tag wcs_id);
#           NXObject objectFromTag = (NXObject)session_.__GetTaggedObject(wcs_id);
#           CartesianCoordinateSystem csys = (CartesianCoordinateSystem)objectFromTag;
#           return csys;
#       }

#       set
#       {
#           Tag nXOpenTag = value.Tag;
#           ufsession_.Csys.SetWcs(nXOpenTag);
#       }
#   }

#   //
#   // Summary:
#   //     The orientation of the Wcs of the work part
#   public static Matrix3x3 WcsOrientation =>

#       __wcs_.CoordinateSystem.Orientation.Element;

#   //set
#   //{
#   //    __wcs_.set
#   //    NXOpen.Part __work_part_ = __work_part_;
#   //    __work_part_.WCS.SetOriginAndMatrix(Wcs.Origin, value);
#   //}
#   /// <summary>
#   /// </summary>
#   public static CartesianCoordinateSystem WcsCoordinateSystem =>

#       session_
#           .Parts.Display.CoordinateSystems
#           .CreateCoordinateSystem(__Wcs_.Origin, __display_part_.WCS.__Orientation(), true);

#   public static Vector3d __Vector3dX()
#   {
#       return new[] { 1d, 0d, 0d }.__ToVector3d();
#   }

#   public static Vector3d __Vector3dY()
#   {
#       return new[] { 0d, 1d, 0d }.__ToVector3d();
#   }

#   public static Vector3d __Vector3dZ()
#   {
#       return new[] { 0d, 0d, 1d }.__ToVector3d();
#   }


#   public static void print(object __object)
#   {
#       print($"{__object}");
#   }


#   public static void prompt(string message)
#   {
#       uf_.Ui.SetPrompt(message);
#   }


#   public static void print(bool __bool)
#   {
#       print($"{__bool}");
#   }


#   public static void print(int __int)
#   {
#       print($"{__int}");
#   }


#   public static void print(string message)
#   {
#       ListingWindow lw = session_.ListingWindow;

#       if (!lw.IsOpen)
#           lw.Open();

#       lw.WriteLine(message);
#   }

#   /// <summary>The length unit of the work part</summary>
#   /// <remarks>
#   /// <para>
#   /// This will be either Snap.NX.Unit.Millimeter or Snap.NX.Unit.Inch
#   /// </para>
#   /// </remarks>
#   //public static Unit PartUnit
#   //{
#   //    get
#   //    {
#   //        Unit unit = Unit.Millimeter;

#   //        if (UnitType == Unit.Inch)
#   //            unit = Unit.Inch;

#   //        return unit;
#   //    }
#   //}

#   /// <summary>Creates an Undo mark</summary>
#   /// <param name="markVisibility">Indicates the visibility of the undo mark</param>
#   /// <param name="name">The name to be assigned to the Undo mark</param>
#   /// <returns>The ID of the newly created Undo mark</returns>
#   /// <remarks>
#   ///     <para>
#   ///         Creating an Undo mark gives you a way to save the state of the NX session. Then,
#   ///         at some later time, you can "roll back" to the Undo mark to restore NX to the saved state.
#   ///         This is useful for error recovery, and for reversing any temporary changes you have made
#   ///         (such as creation of temporary objects).
#   ///     </para>
#   ///     <para>
#   ///         If you create a visible Undo mark, the name you assign will be shown in
#   ///         the Undo List on the NX Edit menu.
#   ///     </para>
#   ///     <para>
#   ///         Please refer to the NX/Open Programmer's Guide for more
#   ///         information about Undo marks.
#   ///     </para>
#   /// </remarks>
#   public static UndoMarkId __SetUndoMark(MarkVisibility markVisibility, string name)
#   {
#       return session_.SetUndoMark(markVisibility, name);
#   }

#   /// <summary>Deletes an Undo mark</summary>
#   /// <param name="markId">The ID of the Undo mark</param>
#   /// <param name="markName">The name of the Undo mark.</param>
#   /// <remarks>
#   ///     <para>
#   ///         You can access an Undo mark either using its ID or its name.
#   ///         The system will try to find the mark using the given ID, first.
#   ///         If this fails (because you have provided an incorrect ID), the system
#   ///         will try again to find the mark based on its name.
#   ///     </para>
#   /// </remarks>
#   public static void __DeleteUndoMark(UndoMarkId markId, string markName)
#   {
#       session_.DeleteUndoMark(markId, markName);
#   }

#   /// <summary>Roll back to an existing Undo mark</summary>
#   /// <param name="markId">The ID of the Undo mark to roll back to</param>
#   /// <param name="markName">The name of the Undo mark.</param>
#   /// <remarks>
#   ///     <para>
#   ///         You can access an Undo mark either using its ID or its name.
#   ///         The system will try to find the mark using the given ID, first.
#   ///         If this fails (because you have provided an incorrect ID), the system
#   ///         will try again to find the mark based on its name.
#   ///     </para>
#   /// </remarks>
#   public static void __UndoToMark(UndoMarkId markId, string markName)
#   {
#       session_.UndoToMark(markId, markName);
#   }

#   public static string __Op10To010(int __op)
#   {
#       if (__op == 0)
#           return "000";
#       if (__op < 10)
#           throw new Exception("op integer must be 0 or greater than 9");
#       if (__op < 100)
#           return $"0{__op}";
#       return $"{__op}";
#   }

#   public static string __Op020To010(string __op)
#   {
#       return __Op10To010(int.Parse(__op) - 10);
#   }

#   /// <summary>Get the number of objects on a specified layer</summary>
#   /// <param name="layer">The layer number</param>
#   /// <returns>The number of objects on the specified layer</returns>
#   public static int __LayerObjectCount(int layer)
#   {
#       return __work_part_.Layers.GetAllObjectsOnLayer(layer).Length;
#   }

#   /// <summary>Converts degrees to radians</summary>
#   /// <param name="angle">An angle measured in degrees</param>
#   /// <returns>The same angle measured in radians</returns>
#   public static double __DegreesToRadians(double angle)
#   {
#       return angle * Math.PI / 180.0;
#   }

#   /// <summary>Converts radians to degrees</summary>
#   /// <param name="angle">An angle measured in radians</param>
#   /// <returns>The same angle measured in degrees</returns>
#   public static double __RadiansToDegrees(double angle)
#   {
#       return angle * 180.0 / Math.PI;
#   }

#   public static IEnumerable<string> __ReadSqlAsStrings(
#       this Session session,
#       string command_text,
#       string column_name)
#   {
#       using (SqlConnection conn = new SqlConnection(conn_str))
#       using (SqlCommand sql = conn.CreateCommand())
#       {
#           conn.Open();
#           sql.CommandText = command_text;

#           using (SqlDataReader dr = sql.ExecuteReader())
#               while (dr.Read())
#                   yield return dr[column_name].ToString();
#       }
#   }

#   #endregion


#     #region Dimension

#   //public static bool _IsAssociative(this Dimension dim)
#   //{
#   //    return !dim.IsRetained;
#   //}

#   //[Obsolete]
#   //public static DrawingSheet _OwningDrawingSheet(this Dimension dim)
#   //{
#   //    throw new NotImplementedException();
#   //    // ufsession_.View.AskViewDependentStatus(dim.Tag, out _, out string drawingSheetName);
#   //    // return dim.__OwningPart().DrawingSheets.ToArray().Single(__s=>__s.Name == drawingSheetName);
#   //    //dim.__OwningPart().Dimensions.

#   //    //dim.

#   //    // ufsession_.View.AskViewDependentStatus(dim.Tag, out _, out string drawingSheetName);
#   //    //print_(drawingSheetName);
#   //    //foreach (NXOpen.Drawings.DrawingSheet s in dim.__OwningPart().DrawingSheets)
#   //    //    print_(s.Name);
#   //    // return dim.__OwningPart().DrawingSheets.ToArray().Single(__s => __s.Name.ToLower().Contains(drawingSheetName.ToLower()));
#   //}
#   //#endregion

#   //#region DisplayedConstraint
#   //public static Constraint __GetConstraint(
#   //           this DisplayedConstraint displayedConstraint)
#   //{
#   //    return displayedConstraint.GetConstraint();
#   //}

#   //public static Part __GetConstraintPart(this DisplayedConstraint displayedConstraint)
#   //{
#   //    return displayedConstraint.GetConstraintPart();
#   //}

#   //public static Component __GetContextComponent(
#   //    this DisplayedConstraint displayedConstraint)
#   //{
#   //    return displayedConstraint.GetContextComponent();
#   //}

#   #endregion


#    #region Line

#  [Obsolete(nameof(NotImplementedException))]
#  public static Line __Mirror(
#      this Line line,
#      Surface.Plane plane)
#  {
#      Point3d start = line.StartPoint.__Mirror(plane);
#      Point3d end = line.EndPoint.__Mirror(plane);
#      return line.__OwningPart().Curves.CreateLine(start, end);
#  }


#  public static Line __Copy(this Line line)
#  {
#      if (line.IsOccurrence)
#          throw new ArgumentException($@"Cannot copy {nameof(line)} that is an occurrence.", nameof(line));

#      return line.__OwningPart().Curves.CreateLine(line.__StartPoint(), line.__EndPoint());
#  }

#  public static Point3d __StartPoint(this Line line)
#  {
#      return line.StartPoint;
#  }

#  public static Point3d __EndPoint(this Line line)
#  {
#      return line.EndPoint;
#  }


#  /// <summary>Construct a line, given x,y,z coordinates of its end-points</summary>
#  /// <param name="x0">X-coordinate of start point</param>
#  /// <param name="y0">Y-coordinate of start point</param>
#  /// <param name="z0">Z-coordinate of start point</param>
#  /// <param name="x1">X-coordinate of end   point</param>
#  /// <param name="y1">Y-coordinate of end   point</param>
#  /// <param name="z1">Z-coordinate of end   point</param>
#  /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#  public static Line __CreateLine(double x0, double y0, double z0, double x1, double y1, double z1)
#  {
#      return __CreateLine(new Point3d(x0, y0, z0), new Point3d(x1, y1, z1));
#  }

#  /// <summary>Construct a line, given x,y coordinates of its end-points (z assumed zero)</summary>
#  /// <param name="x0">X-coordinate of start point</param>
#  /// <param name="y0">Y-coordinate of start point</param>
#  /// <param name="x1">X-coordinate of end   point</param>
#  /// <param name="y1">Y-coordinate of end   point</param>
#  /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#  public static Line __CreateLine(double x0, double y0, double x1, double y1)
#  {
#      return __CreateLine(new Point3d(x0, y0, 0.0), new Point3d(x1, y1, 0.0));
#  }

#  /// <summary>Creates a line between two positions</summary>
#  /// <param name="p0">NXOpen.Point3d for start of line</param>
#  /// <param name="p1">NXOpen.Point3d for end of line</param>
#  /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#  public static Line __CreateLine(Point3d p0, Point3d p1)
#  {
#      return __work_part_.Curves.CreateLine(p0, p1);
#  }

#  //
#  // Summary:
#  //     Copies an NX.Line object (with a null transform)
#  //
#  // Returns:
#  //     A copy of the input line
#  //
#  // Remarks:
#  //     The new line will be on the same layer as the original one.
#  [Obsolete]
#  public static Line Copy(this Line line)
#  {
#      Transform xform = Transform.CreateTranslation(0.0, 0.0, 0.0);
#      return line.Copy(xform);
#  }

#  //
#  // Summary:
#  //     Transforms/copies an NX.Arc
#  //
#  // Parameters:
#  //   xform:
#  //     Transform to be applied
#  //
#  // Returns:
#  //     A transformed copy of NX.Arc
#  [Obsolete]
#  public static Line Copy(this Line line, Transform xform)
#  {
#      var curve = (NXOpen.Curve)line;
#      return (Line)curve.Copy(xform);
#  }

#  // public static void __TryMatch(this TSG_Library.Geom.Curve.Arc)

#  public static Vector3d __Vector(this Line line)
#  {
#      return line.EndPoint.__Subtract(line.StartPoint);
#  }

#  // public static void __Move(this Line line, Vector3d vector, double distance)
#  // {

#  // }


#  public static void __Move(this Line line, Vector3d vector, double distance)
#  {
#      line.__OwningPart().__AssertIsWorkPart();
#      Vector3d unit = vector.__Unit();
#      Point3d new_start = line.StartPoint.__Add(unit, distance);
#      Point3d new_end = line.EndPoint.__Add(unit, distance);
#      line.SetStartPoint(new_start);
#      line.SetEndPoint(new_end);
#      line.RedisplayObject();
#      ufsession_.Modl.Update();
#  }

#  public static Line __Copy(this Line line, Vector3d vector, double distance)
#  {
#      line.__OwningPart().__AssertIsWorkPart();
#      Vector3d unit = vector.__Unit();
#      Point3d new_start = line.StartPoint.__Add(unit, distance);
#      Point3d new_end = line.EndPoint.__Add(unit, distance);
#      return line.__OwningPart().Curves.CreateLine(new_start, new_end);
#  }

#  public static NXObject __CopyNXObject(this NXObject nxobject, Vector3d vector)
#  {
#      nxobject.__OwningPart().__AssertIsWorkPart();

#      switch (nxobject)
#      {
#          case Line line:
#              return line.__Copy(vector);
#          case Arc arc:
#              return arc.__Copy(vector);
#          case Point point:
#              return point.__Copy(vector);
#          case Block block:
#              return block.__Copy(vector);
#          case Extrude extrude:
#              return extrude.__Copy(vector);
#          default:
#              throw new InvalidOperationException($"Unknown copy type: {nxobject.GetType().Name}");
#      }
#  }

#  public static Block __Copy(this Block block, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }

#  public static Arc __Copy(this Arc arc, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }

#  public static Line __Copy(this Line line, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }

#  public static Point __Copy(this Point point, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }

#  public static Extrude __Copy(this Extrude extrude, Vector3d vector)
#  {
#      throw new NotImplementedException();
#  }


#  // public static Point __Copy()
#  // {
#  //     ufsession_.Trns.CreateReflectionMatrix()
#  // }


#  // move point


#  // try to move arc

#  #endregion


#     #region DatumCsys

#    public static DatumPlane __DatumPlaneXY(this DatumCsys datumCsys)
#    {
#        ufsession_.Modl.AskDatumCsysComponents(datumCsys.Tag, out _, out _, out _, out Tag[] dplanes);
#        return (DatumPlane)session_.__GetTaggedObject(dplanes[0]);
#    }

#    public static DatumPlane __DatumPlaneXZ(this DatumCsys datumCsys)
#    {
#        ufsession_.Modl.AskDatumCsysComponents(datumCsys.Tag, out _, out _, out _, out Tag[] dplanes);
#        return (DatumPlane)session_.__GetTaggedObject(dplanes[2]);
#    }

#    public static DatumPlane __DatumPlaneYZ(this DatumCsys datumCsys)
#    {
#        ufsession_.Modl.AskDatumCsysComponents(datumCsys.Tag, out _, out _, out _, out Tag[] dplanes);
#        return (DatumPlane)session_.__GetTaggedObject(dplanes[1]);
#    }

#    public static Vector3d __Vector3dX(this DatumCsys datumCsys)
#    {
#        ufsession_.Modl.AskDatumCsysComponents(datumCsys.Tag, out _, out _, out Tag[] daxes, out _);
#        DatumAxis axis = (DatumAxis)session_.__GetTaggedObject(daxes[0]);
#        return axis.Direction;
#    }

#    public static Vector3d __Vector3dY(this DatumCsys datumCsys)
#    {
#        ufsession_.Modl.AskDatumCsysComponents(datumCsys.Tag, out _, out _, out Tag[] daxes, out _);
#        DatumAxis axis = (DatumAxis)session_.__GetTaggedObject(daxes[1]);
#        return axis.Direction;
#    }

#    public static Vector3d __Vector3dZ(this DatumCsys datumCsys)
#    {
#        ufsession_.Modl.AskDatumCsysComponents(datumCsys.Tag, out _, out _, out Tag[] daxes, out _);
#        DatumAxis axis = (DatumAxis)session_.__GetTaggedObject(daxes[2]);
#        return axis.Direction;
#    }

#    #endregion

#       #region ScCollector

#    public static void __Temp(this ScCollector scCollector)
#    {
#        scCollector.CopyCollector();
#        //scCollector.Destroy
#        //scCollector.GetMultiComponent
#        //scCollector.GetNonFeatureMode
#        //scCollector.GetObjects
#        //scCollector.GetObjectsSortedById
#        //scCollector.GetRules
#        //scCollector.RemoveMissingParents
#        //scCollector.RemoveRule
#        //scCollector.RemoveRules
#        //scCollector.ReplaceRules
#        //scCollector.SetInterpart
#        //scCollector.SetMultiComponent
#        //scCollector.SetNonFeatureMode
#    }


#    public static void __ReplaceRules(this ScCollector scCollector, Body body, SelectionIntentRule.RuleType ruleType)
#    {
#        //switch(ruleType)
#        //{
#        //    case SelectionIntentRule.RuleType.BodyDumb:

#        //}

#        throw new System.NotImplementedException();
#    }

#    #endregion


#      #region SmartObject

#   //public void RemoveParameters()

#   //public void ReplaceParameters(SmartObject otherSo)

#   //public void Evaluate


#   //public void SetVisibility(VisibilityOption visibility)


#   //public void ProtectFromDelete


#   //public void ReleaseDeleteProtection


#   public static void __Temp(this SmartObject obj)
#   {
#       //obj.CenterPoint
#       //obj.GetOrientation
#       //obj.IsClosed
#       //obj.IsReference
#       //obj.Matrix
#       //obj.ProtectFromDelete
#       //obj.ReleaseDeleteProtection
#       //obj.RotationAngle
#       //obj.SetOrientation
#       //obj.SetParameters
#   }

#   #endregion


#           #region Face

#         public static Point3d[] __EdgePositions(this Face __face)
#         {
#             //List<NXOpen.Point3d> points = new List<NXOpen.Point3d>();

#             //foreach (NXOpen.Edge edge in __face.GetEdges())
#             //{
#             //    edge.GetVertices(out NXOpen.Point3d poin1, out NXOpen.Point3d point2);

#             //    points.Add(poin1);
#             //    points.Add(point2);
#             //}

#             //return points.ToHashSet(new EqualityPosition()).ToArray();

#             throw new NotImplementedException();
#         }

#         /// <summary>
#         /// Get ths unit normal vector of the fae if it is planar.
#         /// </summary>
#         public static Vector3d __Normal(this Face face)
#         {
#             return face.__NormalVector().__Unit();
#         }

#         public static Vector3d __NormalVector(this Face __face)
#         {
#             double[] point = new double[3];
#             double[] dir = new double[3];
#             double[] box = new double[6];
#             ufsession_.Modl.AskFaceData(
#                 __face.Tag,
#                 out int type,
#                 point,
#                 dir,
#                 box,
#                 out _,
#                 out _,
#                 out _
#             );

#             if (type != 22)
#                 throw new InvalidOperationException(
#                     "Cannot ask for the normal of a non planar face"
#                 );

#             return dir.__ToVector3d();
#         }

#         //
#         // Summary:
#         //     Conversion factor between NX Open and SNAP parameter values. Needed because NX
#         //     Open uses radians, where SNAP uses degrees
#         //
#         // Remarks:
#         //     When converting an NX Open parameter to a SNAP parameter, snapU = nxopenU * FactorU
#         //
#         //
#         //     When converting a SNAP parameter to an NX Open parameter, nxopenU = snapU / FactorU
#         [Obsolete("Need to check what type of face first. Look at Snap")]
#         internal static double __FactorU(this Face _)
#         {
#             throw new NotImplementedException();
#             //return 180.0 / System.Math.PI;
#         }

#         //
#         // Summary:
#         //     Conversion factor between NX Open and SNAP parameter values. Needed because NX
#         //     Open uses radians, where SNAP uses degrees
#         //
#         // Remarks:
#         //     When converting an NX Open parameter to a SNAP parameter, snapV = nxopenV * FactorV
#         //
#         //
#         //     When converting a SNAP parameter to an NX Open parameter, nxopenV = snapV / FactorV
#         [Obsolete("Need to check what type of face first. Look at Snap")]
#         internal static double __FactorV(this Face face)
#         {
#             //switch(face.SolidFaceType) { }


#             //return UnitConversion.MetersToPartUnits;
#             throw new NotImplementedException();
#         }

#         public static bool __IsPlanar(this Face face)
#         {
#             return face.SolidFaceType == Face.FaceType.Planar;
#         }

#         //
#         // Summary:
#         //     Finds surface (u,v) parameters at (or nearest to) a given point
#         //
#         // Parameters:
#         //   point:
#         //     The given point (which should be on or near to the surface)
#         //
#         // Returns:
#         //     Surface (u,v) parameters at (or near to) the given point
#         //
#         // Remarks:
#         //     The Parameters function and the Position function are designed to work together
#         //     smoothly -- each of these functions is the "reverse" of the other. So, if f is
#         //     any face and (u,v) is any pair of parameter values, then
#         //
#         //     f.Parameters(f.Position(u,v)) = (u,v)
#         //
#         //     Also, if p is any point on the face f, then
#         //
#         //     f.Position(c.Parameters(p)) = p
#         //
#         //     Note that this function finds parameter values on the underlying surface of the
#         //     face. So, the values returned may correspond to a surface point that is actually
#         //     outside the face.
#         public static double[] __Parameters(this Face face, Point3d point)
#         {
#             UFEvalsf evalsf = ufsession_.Evalsf;
#             evalsf.Initialize2(face.Tag, out IntPtr evaluator);
#             double[] array = point.__ToArray();
#             evalsf.FindClosestPoint(evaluator, array, out UFEvalsf.Pos3 srf_pos);
#             evalsf.Free(out _);
#             double[] uv = srf_pos.uv;
# #pragma warning disable CS0618 // Type or member is obsolete
#             uv[0] = face.__FactorU() * uv[0];
#             uv[1] = face.__FactorV() * uv[1];
# #pragma warning restore CS0618 // Type or member is obsolete
#             return uv;
#         }

#         public static double __CylinderRadius(this Face face)
#         {
#             var position_on_axis = new double[3];
#             var axis_direction = new double[3];
#             var box = new double[6];
#             ufsession_.Modl.AskFaceData(
#                 face.Tag,
#                 out int type,
#                 position_on_axis,
#                 axis_direction,
#                 box,
#                 out double radius,
#                 out _,
#                 out _
#             );

#             if (type != 16)
#                 throw new InvalidOperationException(
#                     $"Can' ask radius of face with type {face.SolidFaceType}"
#                 );

#             return radius;
#         }

#         public static Vector3d __CylinderDirection(this Face face)
#         {
#             var position_on_axis = new double[3];
#             var axis_direction = new double[3];
#             var box = new double[6];
#             ufsession_.Modl.AskFaceData(
#                 face.Tag,
#                 out int type,
#                 position_on_axis,
#                 axis_direction,
#                 box,
#                 out _,
#                 out _,
#                 out _
#             );

#             if (type != 16)
#                 throw new InvalidOperationException(
#                     $"Can' ask radius of face with type {face.SolidFaceType}"
#                 );

#             return axis_direction.__ToVector3d();
#         }

#         public static Point3d __CylinderOrigin(this Face face)
#         {
#             var position_on_axis = new double[3];
#             var axis_direction = new double[3];
#             var box = new double[6];
#             ufsession_.Modl.AskFaceData(
#                 face.Tag,
#                 out int type,
#                 position_on_axis,
#                 axis_direction,
#                 box,
#                 out _,
#                 out _,
#                 out _
#             );

#             if (type != 16)
#                 throw new InvalidOperationException(
#                     $"Can' ask radius of face with type {face.SolidFaceType}"
#                 );

#             return position_on_axis.__ToPoint3d();
#         }


#         // var top_face = smart_boss.GetFaces().Single(f => __IsAbsPosZ(f.__NormalVector()));

#         #endregion

#           #region Part

#   public static DrawingSheet __GetDrawingSheetOrNull(
#       this Part part,
#       string drawingSheetName,
#       StringComparison stringComparison)
#   {
#       foreach (DrawingSheet drawingSheet in part.DrawingSheets)
#           if (drawingSheet.Name.Equals(drawingSheetName, stringComparison))
#               return drawingSheet;

#       return null;
#   }

#   public static Body __SolidBodyLayer1OrNull(this Part part)
#   {
#       Body[] bodiesOnLayer1 = part.Bodies
#           .OfType<Body>()
#           .Where(body => !body.IsOccurrence)
#           .Where(body => body.IsSolidBody)
#           .Where(body => body.Layer == 1)
#           .ToArray();

#       return bodiesOnLayer1.Length == 1 ? bodiesOnLayer1[0] : null;
#   }

#   public static Body __SingleSolidBodyOnLayer1(this Part part)
#   {
#       Body[] solidBodiesOnLayer1 = part.Bodies
#           .ToArray()
#           .Where(body => body.IsSolidBody)
#           .Where(body => body.Layer == 1)
#           .ToArray();

#       switch (solidBodiesOnLayer1.Length)
#       {
#           case 0:
#               throw new NoSolidBodyOnLayer1Exception(part.Leaf);
#           case 1:
#               return solidBodiesOnLayer1[0];
#           default:
#               throw new MoreThanOneSolidBodyOnLayer1Exception(part.Leaf);

#       }
#   }

#   #endregion


#     #region Session

#   //
#   // Summary:
#   //     Creates a new part
#   //
#   // Parameters:
#   //   pathName:
#   //     The full pathname of the part
#   //
#   //   templateType:
#   //     The type of the template to be used to create the part
#   //
#   //   unitType:
#   //     The type of the unit to be used
#   //
#   // Returns:
#   //     An NX.Part object
#   /// <summary>
#   /// </summary>
#   /// <param name="pathName"></param>
#   /// <param name="templateType"></param>
#   /// <param name="unitType"></param>
#   /// <returns></returns>
#   internal static Part __CreatePart(string pathName, Templates templateType, Units unitType)
#   {
#       Part nXOpenPart = __work_part_;
#       Part nXOpenPart2 = __display_part_;
#       FileNew fileNew = session_.Parts.FileNew();
#       fileNew.ApplicationName = __GetAppName(fileNew, templateType);
#       fileNew.TemplateFileName = __GetTemplateFileName(fileNew, templateType, unitType);
#       fileNew.UseBlankTemplate = fileNew.TemplateFileName == "Blank";

#       fileNew.Units =
#           unitType == Units.MilliMeters ? Part.Units.Millimeters : Part.Units.Inches;

#       fileNew.NewFileName = pathName;
#       fileNew.MasterFileName = "";
#       fileNew.MakeDisplayedPart = true;
#       NXObject nXObject = fileNew.Commit();
#       fileNew.Destroy();

#       if (nXOpenPart != null)
#       {
#           __work_part_ = nXOpenPart;
#           __display_part_ = nXOpenPart2;
#       }

#       return (Part)nXObject;
#   }

#   public static void __SetWcs(this Session session)
#   {
#       session.__SetWcs(_Point3dOrigin, _Matrix3x3Identity);
#   }

#   public static void __SetWcs(this Session session, double[] origin, double[][] orientation)
#   {
#       Matrix3x3 __orientation = orientation[0]
#           .__ToVector3d()
#           .__ToMatrix3x3(
#               orientation[1].__ToVector3d(),
#               orientation[2].__ToVector3d()
#       );

#       session.__SetWcs(origin.__ToPoint3d(), __orientation);
#   }

#   public static void __SetWcs(this Session session, Point3d origin, Matrix3x3 orientation)
#   {
#       session.Parts.Display.WCS.SetOriginAndMatrix(origin, orientation);
#   }


#   public static ResetWorkLayer __UsingResetWorkLayer(this Session _)
#   {
#       return new ResetWorkLayer();
#   }

# def with_rollback()

#   public static Rollback __UsingRollback(
#       this Session session,
#       NXOpen.Features.Feature feat
#   )
#   { return new Rollback(feat, "Rollback"); }

#   public static void __SetWorkPlane(
#       this Session _,
#       double gridSpace,
#       bool snapToGrid,
#       bool showGrid
#   )
#   {
#       WorkPlane workPlane1 = __display_part_.Preferences.Workplane;

#       if (workPlane1 is null)
#           return;

#       workPlane1.GridType = WorkPlane.Grid.Rectangular;
#       workPlane1.GridIsNonUniform = false;
#       WorkPlane.GridSize gridSize1 = new WorkPlane.GridSize(gridSpace, 1, 1);
#       workPlane1.SetRectangularUniformGridSize(gridSize1);
#       workPlane1.ShowGrid = showGrid;
#       workPlane1.ShowLabels = false;
#       workPlane1.SnapToGrid = snapToGrid;
#       workPlane1.GridOnTop = false;
#       workPlane1.RectangularShowMajorLines = false;
#       workPlane1.PolarShowMajorLines = false;
#       workPlane1.GridColor = 7;
#   }

#   public static LockUiFromCustom __UsingLockUiFromCustom(this Session _)
#   {
#       return new LockUiFromCustom();
#   }

#   // ReSharper disable once ParameterHidesMember
#   public static string __SelectMenuItem14gt(
#       this Session session_,
#       string title,
#       string[] items
#   )
#   {
#       IList<string[]> separated = new List<string[]>();

#       List<string> list_items = items.ToList();

#       const string __next__ = "...NEXT...";
#       const int max = 14;

#       if (items.Length == max)
#           using (session_.__UsingLockUiFromCustom())
#           {
#               int picked_item = ufsession_.Ui.DisplayMenu(title, 0, items, items.Length);

#               switch (picked_item)
#               {
#                   case 0:
#                       throw new Exception("Picked item was 0");
#                   case 1:
#                       throw new InvalidOperationException("Back was selected");
#                   case 2:
#                       throw new InvalidOperationException("Cancel was selected");
#                   case 5:
#                       return items[0];
#                   case 6:
#                       return items[1];
#                   case 7:
#                       return items[2];
#                   case 8:
#                       return items[3];
#                   case 9:
#                       return items[4];
#                   case 10:
#                       return items[5];
#                   case 11:
#                       return items[6];
#                   case 12:
#                       return items[7];
#                   case 13:
#                       return items[8];
#                   case 14:
#                       return items[9];
#                   case 15:
#                       return items[10];
#                   case 16:
#                       return items[11];
#                   case 17:
#                       return items[12];
#                   case 18:
#                       return items[13];
#                   case 19:
#                       throw new InvalidOperationException("Unable to display menu");
#                   default:
#                       throw new InvalidOperationException(
#                           $"Unknown picked item: {picked_item}"
#                       );
#               }
#           }

#       while (list_items.Count > 0)
#       {
#           string[] set_of_items = new string[max];

#           set_of_items[set_of_items.Length - 1] = __next__;

#           int end_index = set_of_items.Length - 1;

#           if (list_items.Count < max)
#           {
#               set_of_items = new string[list_items.Count];
#               end_index = list_items.Count;
#           }

#           for (int i = 0; i < end_index; i++)
#           {
#               set_of_items[i] = list_items[0];
#               list_items.RemoveAt(0);
#           }

#           separated.Add(set_of_items);
#       }

#       int current_set_index = 0;

#       while (true)
#           using (session_.__UsingLockUiFromCustom())
#           {
#               int picked_item = ufsession_.Ui.DisplayMenu(
#                   title,
#                   0,
#                   separated[current_set_index],
#                   separated[current_set_index].Length
#               );

#               switch (picked_item)
#               {
#                   case 0:
#                       throw new Exception("Picked item was 0");
#                   case 1:
#                       if (current_set_index > 0)
#                           current_set_index--;
#                       continue;
#                   case 2:
#                       throw new InvalidOperationException("Cancel was selected");
#                   case 5:
#                       return separated[current_set_index][0];
#                   case 6:
#                       return separated[current_set_index][1];
#                   case 7:
#                       return separated[current_set_index][2];
#                   case 8:
#                       return separated[current_set_index][3];
#                   case 9:
#                       return separated[current_set_index][4];
#                   case 10:
#                       return separated[current_set_index][5];
#                   case 11:
#                       return separated[current_set_index][6];
#                   case 12:
#                       return separated[current_set_index][7];
#                   case 13:
#                       return separated[current_set_index][8];
#                   case 14:
#                       return separated[current_set_index][9];
#                   case 15:
#                       return separated[current_set_index][10];
#                   case 16:
#                       return separated[current_set_index][11];
#                   case 17:
#                       return separated[current_set_index][12];
#                   case 18:
#                       if (
#                           separated[current_set_index][13] == __next__
#                           && current_set_index + 1 < separated.Count
#                       )
#                       {
#                           current_set_index++;
#                           continue;
#                       }

#                       if (current_set_index + 1 == separated.Count)
#                           continue;

#                       return separated[current_set_index][13];
#                   case 19:
#                       throw new InvalidOperationException("Unable to display menu");
#                   default:
#                       throw new InvalidOperationException(
#                           $"Unknown picked item: {picked_item}"
#                       );
#               }
#           }
#   }

#   public static DoUpdate __UsingDoUpdate(this Session _)
#   {
#       return new DoUpdate();
#   }

#   public static DoUpdate __UsingDoUpdate(this Session _, string undo_text)
#   {
#       return new DoUpdate(undo_text);
#   }

#   public static IDisposable __UsingFormShowHide(
#       this Session _,
#       Form __form,
#       bool hide_form = true
#   )
#   {
#       if (hide_form)
#           __form.Hide();

#       return new FormHideShow(__form);
#   }

#   public static Part __FindOrOpen(this Session session, string __path_or_leaf)
#   {
#       try
#       {
#           if (ufsession_.Part.IsLoaded(__path_or_leaf) == 0)
#               return session.Parts.Open(__path_or_leaf, out _);

#           return (Part)session.Parts.FindObject(__path_or_leaf);
#       }
#       catch (NXException ex) when (ex.ErrorCode == 1020038)
#       {
#           throw NXException.Create(ex.ErrorCode, $"Invalid file format: '{__path_or_leaf}'");
#       }
#       catch (NXException ex) when (ex.ErrorCode == 1020001)
#       {
#           throw NXException.Create(ex.ErrorCode, $"File not found: '{__path_or_leaf}'");
#       }
#   }

#   public static void __SaveAll(this Session session)
#   {
#       session.Parts.SaveAll(out _, out _);
#       ;
#   }

#   public static void __CloseAll(this Session _)
#   {
#       ufsession_.Part.CloseAll();
#   }

#   public static void __SetDisplayToWork(this Session _)
#   {
#       __work_part_ = __display_part_;
#   }

#   public static bool __WorkIsDisplay(this Session _)
#   {
#       return __display_part_.Tag == __work_part_.Tag;
#   }


#   public static bool __WorkIsNotDisplay(this Session session)
#   {
#       return !session.__WorkIsDisplay();
#   }

#   public static Destroyer __UsingBuilderDestroyer(this Session _, Builder __builder)
#   {
#       return new Destroyer(__builder);
#   }

#   public static DisplayPartReset __UsingDisplayPartReset(this Session _)
#   {
#       return new DisplayPartReset();
#   }

#   public static SuppressDisplayReset __UsingSuppressDisplay(this Session _)
#   {
#       return new SuppressDisplayReset();
#   }

#   public static IDisposable __UsingLockUgUpdates(this Session _)
#   {
#       return new LockUpdates();
#   }

#   public static IDisposable __UsingRegenerateDisplay(this Session _)
#   {
#       return new RegenerateDisplay();
#   }

#   public static TaggedObject __GetTaggedObject(this Session session, Tag tag)
#   {
#       return session.GetObjectManager().GetTaggedObject(tag);
#   }

#   public static PartCollection.SdpsStatus __SetActiveDisplay(
#       this Session session_1,
#       Part __part
#   )
#   {
#       if (
#           session_1.Parts.AllowMultipleDisplayedParts
#           != PartCollection.MultipleDisplayedPartStatus.Enabled
#       )
#           throw new Exception("Session does not allow multiple displayed parts");

#       return session_1.Parts.SetActiveDisplay(
#           __part,
#           DisplayPartOption.AllowAdditional,
#           PartDisplayPartWorkPartOption.UseLast,
#           out _
#       );
#   }

#   public static void __Delete(this ReferenceSet refst) =>
#       refst.OwningPart.DeleteReferenceSet(refst);

#   public static void __SelectSingleObject(
#       this Session _,
#       string message,
#       string title,
#       int scope,
#       UFUi.SelInitFnT init_proc,
#       IntPtr user_data,
#       out int response,
#       out Tag _object,
#       double[] cursor,
#       out Tag view
#   )
#   {
#       ufsession_.Ui.SelectWithSingleDialog(
#           message,
#           title,
#           scope,
#           init_proc,
#           user_data,
#           out response,
#           out _object,
#           cursor,
#           out view
#       );
#   }

#   public static void __SelectSingleObject(
#       this Session session,
#       UFUi.SelInitFnT init_proc,
#       IntPtr user_data,
#       out int response,
#       out Tag _object
#   )
#   {
#       double[] cursor = new double[3];

#       session.__SelectSingleObject(
#           "Select Component Message",
#           "Select Component Title",
#           UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY,
#           init_proc,
#           user_data,
#           out response,
#           out _object,
#           cursor,
#           out _
#       );
#   }

#   public static Initialize2EvaluatorFree __UsingEvaluator(this Session _, Tag tag) =>
#       new Initialize2EvaluatorFree(tag);

#   public static TaggedObject __FindByName(this Session session, string __name) =>
#       session.__FindAllByName(__name).First();

#   public static IEnumerable<TaggedObject> __FindAllByName(this Session _, string __name)
#   {
#       Tag __tag = Tag.Null;

#       do
#       {
#           ufsession_.Obj.CycleByName(__name, ref __tag);

#           if (__tag != Tag.Null)
#               yield return session_.__GetTaggedObject(__tag);
#       } while (__tag != Tag.Null);
#   }

#   public static void __DeleteObjects(
#       this Session session_,
#       params TaggedObject[] __objects_to_delete
#   )
#   {
#       using (GetSession().__UsingDoUpdate())
#           session_.UpdateManager.AddObjectsToDeleteList(__objects_to_delete);
#   }

#   public static void __Delete(this Tag tag) =>
#       session_.__DeleteObjects(tag.__ToTaggedObject());

#   public static void __Delete(this TaggedObject taggedObject) =>
#       session_.__DeleteObjects(taggedObject);

#   public static IDisposable __UsingGCHandle(this Session _, GCHandle __handle) =>
#       new GCHandleFree(__handle);

#   public static BasePart __New(this Session session, string file_path, BasePart.Units units)
#   {
#       using (session.__UsingDisplayPartReset())
#       {
#           int units_;

#           switch (units)
#           {
#               case BasePart.Units.Inches:
#                   units_ = 2;
#                   break;
#               case BasePart.Units.Millimeters:
#                   units_ = 1;
#                   break;
#               default:
#                   throw new ArgumentOutOfRangeException();
#           }

#           ufsession_.Part.New(file_path, units_, out Tag part);
#           return part.__To<BasePart>();
#       }
#   }

#   #endregion


#   public static ICurve SelectCurveOrEdge(Predicate<ICurve> pred = null)
#   {
#       throw new NotImplementedException();
#   }

#   // public static NXOpen.Curve SelectCurve(
#   //     string message = "Select Curve",
#   //     string title = "Select Curve")
#   // {
#   //     NXOpen.Edge e = null;
#   //     e.SolidEdgeType ==

#   //     throw new NotImplementedException();
#   // }


#   public static Edge SelectCurveOrEdge() => null;
#   public static Edge SelectEdgeLinear() => null;
#   public static Edge SelectEdge() => null;
#   public static Edge SelectEdgeCircular() => null;
#   public static Edge SelectECurve() => null;
#   public static Edge SelectLine() => null;
#   public static Edge SelectArc() => null;

#   public static void __DisplayTempLine(this Session session, Point3d start, Point3d end)
#   {
#       UFObj.DispProps attrib = new UFObj.DispProps();

#       ufsession_.Disp.DisplayTemporaryLine(__work_view_.Tag,
#               UFDisp.ViewType.UseViewTag,
#               start.__ToArray(),
#               end.__ToArray(),
#               ref attrib);
#   }

#   public static void __PushOwningLinks(this UserDefinedObject udo, params TaggedObject[] objects)
#   {
#       var links = objects.Select(t => new UserDefinedObject.LinkDefinition(t, UserDefinedObject.LinkStatus.UpToDate)).ToArray();


#       udo.PushLinks(UserDefinedObject.LinkType.Owning, links);
#   }

#   internal static object ExecuteScalar(this Session _, string commandText, params SqlParameter[] parameters)
#   {
#       using (SqlConnection connection = new SqlConnection(conn_str))
#       using (SqlCommand sql = connection.CreateCommand())
#       {
#           connection.Open();
#           sql.CommandText = commandText;
#           sql.Parameters.AddRange(parameters ?? new SqlParameter[0]);
#           return sql.ExecuteScalar();
#       }
#   }

#   internal static int ExecuteScalarInt(this Session session, string commandText, params SqlParameter[] parameters)
#   {
#       return Convert.ToInt32(session_.ExecuteScalar(commandText, parameters));
#   }

#   //internal int ExecuteScalarAsInt(string commandText, params SqlParameter[] parameters)
#   //{
#   //    using (SqlConnection connection = new SqlConnection(getConnectionString()))
#   //    using (SqlCommand sql = connection.CreateCommand())
#   //    {
#   //        connection.Open();
#   //        sql.CommandText = commandText;
#   //        sql.Parameters.AddRange(parameters ?? new SqlParameter[0]);
#   //        object scalar = sql.ExecuteScalar();
#   //        return Convert.ToInt32(scalar);
#   //        //switch (scalar)
#   //        //{
#   //        //    case decimal _decimal:
#   //        //        return Convert.ToInt32(_decimal);
#   //        //    case int _int:
#   //        //        return _int;
#   //        //    default:
#   //        //        throw new InvalidCastException(scalar.GetType().Name);
#   //        //}
#   //    }
#   //}

#   //public IDictionary<string, object>[] ExecuteReader(string commandText, params SqlParameter[] parameters)
#   //{
#   //    using (SqlConnection connection = new SqlConnection(getConnectionString()))
#   //    using (SqlCommand sql = connection.CreateCommand())
#   //    {
#   //        connection.Open();
#   //        sql.CommandText = commandText;
#   //        sql.Parameters.AddRange(parameters ?? new SqlParameter[0]);

#   //        IList<IDictionary<string, object>> dicts = new List<IDictionary<string, object>>();

#   //        using (SqlDataReader dr = sql.ExecuteReader())
#   //            while (dr.Read())
#   //            {
#   //                IDictionary<string, object> dict = new Dictionary<string, object>();

#   //                for (int i = 0; i < dr.FieldCount; i++)
#   //                    dict.Add(dr.GetName(i), dr.GetValue(i));

#   //                dicts.Add(dict);
#   //            }

#   //        return dicts.ToArray();
#   //    }
#   //}


#    #region EdgeBlend

#    [Obsolete(nameof(NotImplementedException))]
#    public static EdgeBlend __Mirror(
#        this EdgeBlend edgeBlend,
#        Surface.Plane plane)
#    {
#        throw new NotImplementedException();
#    }

#    [Obsolete(nameof(NotImplementedException))]
#    public static EdgeBlend __Mirror(
#        this EdgeBlend edgeBlend,
#        Surface.Plane plane,
#        Component from,
#        Component to)
#    {
#        throw new NotImplementedException();
#    }

#    #endregion


#  #region IntegerArray

#  public static Point3d __ToPoint3d(this int[] array)
#  {
#      return new Point3d(array[0], array[1], array[2]);
#  }

#  public static Vector3d __ToVector3d(this int[] array)
#  {
#      return new Vector3d(array[0], array[1], array[2]);
#  }

#  //public static Vector3d _ToVector3d(this int[] array)
#  //{
#  //    return new Vector3d(array[0], array[1], array[2]);
#  //}

#  #endregion

#  #region NXMatrix

#  public static Matrix3x3 __Element(this NXMatrix obj)
#  {
#      return obj.Element;
#  }

#  #endregion


#     #region String

#    public static string __DirectoryName(this string path)
#    {
#        return Path.GetDirectoryName(path);
#    }

#    public static string __FileLeaf(this string path)
#    {
#        return Path.GetDirectoryName(path);
#    }

#    private static bool __FastenerInfo(
#        string file,
#        string regex,
#        out string diameter,
#        out string length
#    )
#    {
#        if (file.Contains("\\"))
#            file = Path.GetFileNameWithoutExtension(file);

#        Match match = Regex.Match(file, regex, RegexOptions.IgnoreCase);

#        if (!match.Success)
#        {
#            diameter = string.Empty;

#            length = string.Empty;

#            return false;
#        }

#        diameter = match.Groups["diameter"].Value;

#        length = match.Groups["length"].Value;

#        return true;
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsBlhcs_(this string leafOrDisplayName)
#    {
#        return leafOrDisplayName.ToLower().Contains("0375-bhcs-062")
#            || leafOrDisplayName.ToLower().Contains("10mm-bhcs-016");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsLayout_(this string leafOrDisplayName)
#    {
#        return leafOrDisplayName.ToLower().Contains("-layout");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsShcs_(this string leaf)
#    {
#        return leaf.ToLower().Contains("-shcs-");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsShcs_(this Component component)
#    {
#        return component.DisplayName._IsShcs_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsShcs_(this Part part)
#    {
#        return part.Leaf._IsShcs_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsDwl_(this string leaf)
#    {
#        return leaf.ToLower().Contains("-dwl-");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsDwl_(this Component component)
#    {
#        return component.DisplayName._IsDwl_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsDwl_(this Part part)
#    {
#        return part.Leaf._IsDwl_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsJckScrew_(this string leaf)
#    {
#        return !leaf._IsJckScrewTsg_() && leaf.ToLower().Contains("-jck-screw-");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsJckScrew_(this Component component)
#    {
#        return component.DisplayName._IsJckScrew_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsJckScrew_(this Part part)
#    {
#        return part.Leaf._IsJckScrew_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsJckScrewTsg_(this string leaf)
#    {
#        return leaf.ToLower().Contains("-jck-screw-tsg");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsJckScrewTsg_(this Component component)
#    {
#        return component.DisplayName._IsJckScrewTsg_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsJckScrewTsg_(this Part part)
#    {
#        return part.Leaf._IsJckScrewTsg_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsLhcs_(this string leaf)
#    {
#        return leaf.ToLower().Contains("-lhcs-");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsSss_(this string leaf)
#    {
#        return leaf.ToLower().Contains("-sss-");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsBhcs_(this string leaf)
#    {
#        return leaf.ToLower().Contains("-bhcs-");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsFhcs_(this string leaf)
#    {
#        return leaf.ToLower().Contains("-fhcs-");
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsFastener_(this string leafOrDisplayName)
#    {
#        return leafOrDisplayName._IsShcs_()
#            || leafOrDisplayName._IsDwl_()
#            || leafOrDisplayName._IsJckScrew_()
#            || leafOrDisplayName._IsJckScrewTsg_();
#    }

#    //[IgnoreExtensionAspect]
#    public static bool _IsFastenerExtended_(this string leafOrDisplayName)
#    {
#        return leafOrDisplayName.__IsFastener()
#            || leafOrDisplayName._IsLhcs_()
#            || leafOrDisplayName._IsSss_()
#            || leafOrDisplayName._IsBhcs_()
#            || leafOrDisplayName._IsFhcs_()
#            || leafOrDisplayName._IsBlhcs_();
#    }

#    public static bool __TryAskDetailNumber(this string path_or_leaf, out string detail)
#    {
#        string leaf = path_or_leaf;
#        detail = null;

#        if (path_or_leaf.Contains("\\") || path_or_leaf.Contains("/"))
#            leaf = Path.GetFileNameWithoutExtension(path_or_leaf);

#        Match match = Regex.Match(leaf, "^\\d+-\\d+-(?<detail>\\d+)$");

#        if (!match.Success)
#            return false;

#        detail = match.Groups["detail"].Value;
#        return true;
#    }

#    public static string __AskDetailNumber(this string file)
#    {
#        string leaf = Path.GetFileNameWithoutExtension(file);
#        Match match = Regex.Match(leaf, "^\\d+-\\d+-(?<detail>\\d+)$");

#        if (!match.Success)
#            throw new FormatException("Could not find detail number.");

#        return match.Groups["detail"].Value;
#    }

#    public static bool __IsShcs(this string file)
#    {
#        return file.__IsShcs(out _);
#    }

#    public static bool __IsDwl(this string file)
#    {
#        return file.__IsDwl(out _);
#    }

#    public static bool __IsJckScrew(this string file)
#    {
#        return file.__IsJckScrew(out _);
#    }

#    public static bool __IsJckScrewTsg(this string file)
#    {
#        return file.__IsJckScrewTsg(out _);
#    }

#    public static bool __IsShcs(this string file, out string diameter, out string length)
#    {
#        return __FastenerInfo(file, RegexShcs, out diameter, out length);
#    }

#    public static bool __IsDwl(this string file, out string diameter, out string length)
#    {
#        return __FastenerInfo(file, RegexDwl, out diameter, out length);
#    }

#    public static bool __IsFastener(this string file)
#    {
#        return file.__IsFastener(out _);
#    }

#    public static bool __IsShcs(this string file, out string diameter)
#    {
#        return file.__IsShcs(out diameter, out _);
#    }

#    public static bool __IsDwl(this string file, out string diameter)
#    {
#        return file.__IsDwl(out diameter, out _);
#    }

#    public static bool __IsJckScrew(this string file, out string diameter)
#    {
#        return __FastenerInfo(file, RegexJckScrew, out diameter, out _);
#    }

#    public static bool __IsJckScrewTsg(this string file, out string diameter)
#    {
#        return __FastenerInfo(file, RegexJckScrewTsg, out diameter, out _);
#    }

#    public static bool __IsFastener(this string file, out string diameter)
#    {
#        if (file.__IsShcs(out diameter))
#            return true;

#        if (file.__IsDwl(out diameter))
#            return true;

#        return file.__IsJckScrew(out diameter) || file.__IsJckScrewTsg(out diameter);
#    }

#    public static bool __IsLoaded(this string partName)
#    {
#        int status = ufsession_.Part.IsLoaded(partName);

#        switch (status)
#        {
#            case 0: // not loaded
#                return false;
#            case 1: // fully loaded
#            case 2: // partially loaded
#                return true;
#            default:
#                throw NXException.Create(status);
#        }
#    }

#    public static bool __IsDetail(this string str)
#    {
#        string leaf = Path.GetFileNameWithoutExtension(str);

#        if (leaf is null)
#            return false;

#        return Regex.IsMatch(leaf, "^\\d+-\\d+-\\d+$");
#    }

#    public static string __AskDetailOp(this string path)
#    {
#        string leaf = Path.GetFileNameWithoutExtension(path);

#        Match match = Regex.Match(leaf, "^\\d+-(?<op>\\d+)-.+$");

#        if (!match.Success)
#            throw new Exception($"could not find an op: '{leaf}'");

#        return match.Groups["op"].Value;
#    }

#    //public static bool __IsAssemblyHolder(string str)
#    //{
#    //    if (string.IsNullOrEmpty(str))
#    //        return false;

#    //    str = Path.GetFileNameWithoutExtension(str);
#    //    var startIndex = str.LastIndexOf('-');

#    //    if (startIndex < 0)
#    //        return false;

#    //    var str1 = str.Substring(startIndex);

#    //    var strArray1 = new string[5]
#    //    {
#    //        "lwr",
#    //        "upr",
#    //        "lsh",
#    //        "ush",
#    //        "000"
#    //    };

#    //    var strArray2 = new string[2] { "lsp", "usp" };
#    //    return strArray1.Any(str1.EndsWith) ||
#    //           strArray2.Any(str1.Contains);
#    //}

#    //public static bool __IsFastener(string path)
#    //{
#    //    return IsScrew(path) || IsDowel(path) || IsJigJackTsg(path) || IsJigJack(path);
#    //}

#    //public static bool __IsScrew(string path)
#    //{
#    //    return path.Contains("shcs");
#    //}

#    //public static bool IsDowel(string path)
#    //{
#    //    return path.Contains("dwl");
#    //}

#    //public static bool IsJigJack(string path)
#    //{
#    //    return path.Contains("jck-screw") && !path.Contains("tsg");
#    //}

#    //public static bool IsJigJackTsg(string path)
#    //{
#    //    return path.Contains("jck-screw-tsg");
#    //}

#    public static bool __IsAssemblyHolder(this string path_or_leaf)
#    {
#        var str = path_or_leaf.Contains("\\")
#            ? System.IO.Path.GetFileNameWithoutExtension(path_or_leaf)
#            : path_or_leaf;

#        str = str.ToUpper();

#        return str.__IsLsh()
#            || str.__IsUsh()
#            || str.__IsLwr()
#            || str.__IsUpr()
#            || str.__IsLsp()
#            || str.__IsUsp()
#            || str.__Is000()
#            || str.Contains("UPPER")
#            || str.Contains("LOWER");
#    }

#    public static bool __IsPartDetail(this string partLeaf)
#    {
#        return Regex.IsMatch(partLeaf, DetailNumberRegex);
#    }

#    //public static bool __IsAssemblyHolder(this string str)
#    //{
#    //    return str._IsLsh() || str._IsUsh() || str._IsLwr() || str._IsUpr() || str._IsLsp() || str._IsUsp() ||
#    //           str._Is000();
#    //}

#    public static bool __IsLsh(this string str)
#    {
#        return Regex.IsMatch(str, RegexLsh, RegexOptions.IgnoreCase);
#    }

#    public static bool __IsUsh(this string str)
#    {
#        return Regex.IsMatch(str, RegexUsh, RegexOptions.IgnoreCase);
#    }

#    public static bool __IsLsp(this string str)
#    {
#        return Regex.IsMatch(str, RegexLsp, RegexOptions.IgnoreCase);
#    }

#    public static bool __IsUsp(this string str)
#    {
#        return Regex.IsMatch(str, RegexUsp, RegexOptions.IgnoreCase);
#    }

#    public static bool __IsLwr(this string str)
#    {
#        return Regex.IsMatch(str, RegexLwr, RegexOptions.IgnoreCase);
#    }

#    public static bool __IsUpr(this string str)
#    {
#        return Regex.IsMatch(str, RegexUpr, RegexOptions.IgnoreCase);
#    }

#    public static bool __Is000(this string str)
#    {
#        return Regex.IsMatch(str, RegexOp000Holder, RegexOptions.IgnoreCase);
#    }

#    public static string PerformStreamReaderString(
#        this string path,
#        string startSearchString,
#        string endSearchString
#    )
#    {
#        StreamReader sr = new StreamReader(path);
#        string content = sr.ReadToEnd();
#        sr.Close();
#        string[] startSplit = Regex.Split(content, startSearchString);
#        string[] endSplit = Regex.Split(startSplit[1], endSearchString);
#        string textSetting = endSplit[0];
#        textSetting = textSetting.Replace("\r\n", string.Empty);
#        return textSetting.Length > 0 ? textSetting : null;
#    }

#    public static List<CtsAttributes> PerformStreamReaderList(
#        this string path,
#        string startSearchString,
#        string endSearchString
#    )
#    {
#        StreamReader sr = new StreamReader(path);
#        string content = sr.ReadToEnd();
#        sr.Close();
#        string[] startSplit = Regex.Split(content, startSearchString);
#        string[] endSplit = Regex.Split(startSplit[1], endSearchString);
#        string textData = endSplit[0];
#        string[] splitData = Regex.Split(textData, "\r\n");
#        List<CtsAttributes> compData = (
#            from sData in splitData
#            where sData != string.Empty
#            select new CtsAttributes { AttrValue = sData }
#        ).ToList();
#        return compData.Count > 0 ? compData : null;
#    }

#    /// <summary>Ignores case</summary>
#    public static bool __EqualsCI(this string str0, string str1)
#    {
#        return str0.Equals(str1, StringComparison.OrdinalIgnoreCase);
#    }

#    /// <summary>Does not ignore case, (normal string comparison)</summary>
#    public static bool __EqualsCS(this string str0, string str1)
#    {
#        return str0.Equals(str1, StringComparison.Ordinal);
#    }

#    [Obsolete]
#    public static void __File_AllLines(this string path)
#    {
#        throw new NotImplementedException();
#    }

#    public static void __DeleteF(this string file)
#    {
#        System.IO.File.Delete(file);
#    }

#    public static void __DeleteD(this string directory, bool recursive = true)
#    {
#        Directory.Delete(directory, recursive);
#    }

#    public static bool __ExistsF(this string file)
#    {
#        return File.Exists(file);
#    }

#    public static bool __ExistsD(this string directory)
#    {
#        return Directory.Exists(directory);
#    }

#    public static void __CopyF(this string file, string destination)
#    {
#        File.Move(file, destination);
#    }

#    public static void __MoveF(this string file, string destination)
#    {
#        File.Move(file, destination);
#    }

#    public static void __MoveD(this string directory, string destination)
#    {
#        Directory.Move(directory, destination);
#    }

#    public static string[] __GetDirectories(this string directory)
#    {
#        return Directory.GetDirectories(directory);
#    }

#    public static string __LeafF(this string file)
#    {
#        return Path.GetFileNameWithoutExtension(file)
#            ??
#            throw new FormatException();
#    }


#    public static void temp111()
#    {
#        // System.IO.File.AppendAllLines
#        // System.IO.File.AppendAllText
#        // System.IO.File.ReadAllLines
#        // System.IO.File.ReadAllText
#        // System.IO.File.WriteAllLines
#        // System.IO.File.WriteAllText
#        // System.IO.Directory.CreateDirectory
#        // System.IO.Directory.Delete
#        // System.IO.Directory.Exists
#        // System.IO.Directory.GetDirectories
#        // System.IO.Directory.GetFiles
#        // System.IO.Path.ChangeExtension
#        // System.IO.Path.GetDirectoryName
#        // System.IO.Path.GetExtension
#        // System.IO.Path.GetFileName
#        // System.IO.Path.GetFileNameWithoutExtension
#        // System.IO.Path.GetRandomFileName
#        // System.IO.Path.HasExtension
#        // System.IO.Path.GetTempFileName
#        // System.IO.Path.GetTempPath
#    }

#    #endregion


#      #region Edge

#   public static Point3d __StartPoint(this Edge edge)
#   {
#       edge.GetVertices(out Point3d vertex1, out _);
#       return vertex1;
#   }

#   public static Point3d __EndPoint(this Edge edge)
#   {
#       edge.GetVertices(out _, out Point3d vertex2);
#       return vertex2;
#   }

#   public static Vector3d __NormalVector(this Edge edge)
#   {
#       if (edge.SolidEdgeType != Edge.EdgeType.Linear)
#           throw new ArgumentException("Cannot ask for the vector of a non linear edge");

#       return edge.__StartPoint().__Subtract(edge.__EndPoint());
#   }

#   /// <summary>
#   ///     Gets the start and end positions of the {edge}.
#   /// </summary>
#   /// <remarks>{[0]=StartPoint, [1]=EndPoint}</remarks>
#   /// <param name="edge">The edge to get the positions from.</param>
#   /// <returns>The edge positions.</returns>
#   public static bool __HasEndPoints(this Edge edge, Point3d pos1, Point3d pos2)
#   {
#       if (edge.__StartPoint().__IsEqualTo(pos1) && edge.__EndPoint().__IsEqualTo(pos2))
#           return true;

#       if (edge.__StartPoint().__IsEqualTo(pos2) && edge.__EndPoint().__IsEqualTo(pos1))
#           return true;

#       return false;
#   }

#   public static Curve __ToCurve(this Edge edge)
#   {
#       ufsession_.Modl.CreateCurveFromEdge(edge.Tag, out Tag ugcrv_id);
#       return (Curve)session_.__GetTaggedObject(ugcrv_id);
#   }

#   //
#   // Summary:
#   //     The lower u-value -- the parameter value at the start-point of the edge
#   public static double __MinU(this Edge edge)
#   {
#       UFEval eval = ufsession_.Eval;
#       eval.Initialize2(edge.Tag, out IntPtr evaluator);
#       double[] array = new double[2] { 0.0, 1.0 };
#       eval.AskLimits(evaluator, array);
#       eval.Free(evaluator);
#       return Factor * array[0];
#   }

#   //
#   // Summary:
#   //     The upper u-value -- the parameter value at the end-point of the edge
#   public static double __MaxU(this Edge edge)
#   {
#       UFEval eval = ufsession_.Eval;
#       eval.Initialize2(edge.Tag, out IntPtr evaluator);
#       double[] array = new double[2] { 0.0, 1.0 };
#       eval.AskLimits(evaluator, array);
#       eval.Free(evaluator);
#       return Factor * array[1];
#   }

#   //
#   // Summary:
#   //     Conversion factor between NX Open and SNAP parameter values. Needed because NX
#   //     Open uses radians, where SNAP uses degrees
#   //
#   // Remarks:
#   //     When converting an NX Open parameter to a SNAP parameter, snapValue = nxopenValue
#   //     * Factor
#   //
#   //     When converting a SNAP parameter to an NX Open parameter, nxopenValue = snapValue
#   //     / Factor
#   internal static double __Factor(this Edge edge)
#   {
#       if (
#           edge.SolidEdgeType == Edge.EdgeType.Elliptical
#           || edge.SolidEdgeType == Edge.EdgeType.Circular
#       )
#           return 180.0 / System.Math.PI;

#       return 1.0;
#   }

#   //
#   // Summary:
#   //     Calculates curvature at a given parameter value
#   //
#   // Parameters:
#   //   value:
#   //     Parameter value
#   //
#   // Returns:
#   //     Curvature value (always non-negative)
#   //
#   // Remarks:
#   //     Curvature is the reciprocal of radius of curvature. So, on a straight line, curvature
#   //     is zero and radius of curvature is infinite. On a circle of radius 5, curvature
#   //     is 0.2 (and radius of curvature is 5, of course).
#   [Obsolete]
#   public static double __Curvature(double value)
#   {
#       //Vector[] array = Derivatives(value, 2);
#       //double num = Vector.Norm(Vector.Cross(array[1], array[2]));
#       //double num2 = Vector.Norm(array[1]);
#       //double num3 = num2 * num2 * num2;
#       //return num / num3;
#       throw new NotImplementedException();
#   }

#   //
#   // Summary:
#   //     Calculates the parameter value at a point on the edge
#   //
#   // Parameters:
#   //   point:
#   //     The point
#   //
#   // Returns:
#   //     Parameter value at the point
#   [Obsolete]
#   public static double __Parameter(this Edge edge, Point3d point)
#   {
#       throw new NotImplementedException();
#       //UFSession uFSession = Globals.UFSession;
#       //Tag nXOpenTag = NXOpenTag;
#       //double[] array = point.Array;
#       //int direction = 1;
#       //double offset = 0.0;
#       //double[] point_along_curve = new double[3];
#       //double tolerance = Globals.DistanceTolerance / 10.0;
#       //double result = 0.0;
#       //double parameter = 0.0;
#       //ObjectTypes.SubType objectSubType = ObjectSubType;
#       //bool flag = objectSubType == ObjectTypes.SubType.EdgeIntersection;
#       //bool flag2 = objectSubType == ObjectTypes.SubType.EdgeIsoCurve;
#       //bool flag3 = false;
#       //if (flag || flag2)
#       //{
#       //    CURVE_t val = default(CURVE_t);
#       //    EDGE.ask_curve(PsEdge, &val);
#       //    if (CURVE_t.op_Implicit(val) != ENTITY_t.op_Implicit(ENTITY_t.@null))
#       //    {
#       //        flag3 = true;
#       //        double partUnitsToMeters = UnitConversion.PartUnitsToMeters;
#       //        double num = point.X * partUnitsToMeters;
#       //        double num2 = point.Y * partUnitsToMeters;
#       //        double num3 = point.Z * partUnitsToMeters;
#       //        VECTOR_t val2 = default(VECTOR_t);
#       //        ((VECTOR_t)(ref val2))._002Ector(num, num2, num3);
#       //        CURVE.parameterise_vector(val, val2, &result);
#       //    }
#       //}

#       //if (!flag3)
#       //{
#       //    uFSession.Modl.AskPointAlongCurve2(array, nXOpenTag, offset, direction, tolerance, point_along_curve, out parameter);
#       //    result = (1.0 - parameter) * MinU + parameter * MaxU;
#       //}

#       //return result;
#   }

#   //
#   // Summary:
#   //     Calculates the parameter value defined by an arclength step along an edge
#   //
#   // Parameters:
#   //   baseParameter:
#   //     The curve parameter value at the starting location
#   //
#   //   arclength:
#   //     The arclength increment along the edge (the length of our step)
#   //
#   // Returns:
#   //     The curve parameter value at the far end of the step
#   //
#   // Remarks:
#   //     This function returns the curve parameter value at the far end of a "step" along
#   //     an edge. The start of the step is defined by a given parameter value, and the
#   //     size of the step is given by an arclength along the edge. The arclength step
#   //     may be positive or negative.
#   [Obsolete]
#   public static double __Parameter(this Edge edge, double baseParameter, double arclength)
#   {
#       //int direction = 1;
#       //if (arclength < 0.0)
#       //{
#       //    direction = -1;
#       //}

#       //double parameter = 0.0;
#       //double tolerance = 0.0001;
#       //double[] point_along_curve = new double[3];
#       //double[] array = edge.Position(baseParameter).Array;
#       //ufsession_.Modl.AskPointAlongCurve2(array, edge.Tag, System.Math.Abs(arclength), direction, tolerance, point_along_curve, out parameter);
#       //return parameter * (edge.__MaxU() - edge.__MinU()) + edge.__MinU();
#       throw new NotImplementedException();
#   }

#   //
#   // Summary:
#   //     Calculates the parameter value at a fractional arclength value along an edge
#   //
#   // Parameters:
#   //   arclengthFraction:
#   //     Fractional arclength along the edge
#   //
#   // Returns:
#   //     Parameter value
#   //
#   // Remarks:
#   //     The input is a fractional arclength. A value of 0 corresponds to the start of
#   //     the edge, a value of 1 corresponds to the end-point, and values between 0 and
#   //     1 correspond to interior points along the edge.
#   //     You can input arclength values outside the range 0 to 1, and this will return
#   //     parameter values corresponding to points on the extension of the edge.
#   [Obsolete]
#   public static double __Parameter(double arclengthFraction)
#   {
#       //double arclength = ArcLength * arclengthFraction;
#       //return Parameter(MinU, arclength);
#       throw new NotImplementedException();
#   }

#   ////
#   //// Summary:
#   ////     The lower u-value -- the parameter value at the start-point of the edge
#   //public static double __MinU(this Edge edge)
#   //{
#   //    var eval = ufsession_.Eval;
#   //    eval.Initialize2(edge.Tag, out var evaluator);
#   //    var array = new double[2] { 0.0, 1.0 };
#   //    eval.AskLimits(evaluator, array);
#   //    eval.Free(evaluator);
#   //    return Factor * array[0];
#   //}

#   ////
#   //// Summary:
#   ////     The upper u-value -- the parameter value at the end-point of the edge
#   //public static double __MaxU(this Edge edge)
#   //{
#   //    var eval = ufsession_.Eval;
#   //    eval.Initialize2(edge.Tag, out var evaluator);
#   //    var array = new double[2] { 0.0, 1.0 };
#   //    eval.AskLimits(evaluator, array);
#   //    eval.Free(evaluator);
#   //    return Factor * array[1];
#   //}

#   //
#   // Summary:
#   //     Calculates the unit binormal at a given parameter value
#   //
#   // Parameters:
#   //   value:
#   //     Parameter value
#   //
#   // Returns:
#   //     Unit binormal
#   //
#   // Remarks:
#   //     The binormal is normal to the "osculating plane" of the curve at the given parameter
#   //     value (the plane that most closely matches the curve). So, if the curve is planar,
#   //     the binormal is normal to the plane of the curve.
#   //     The binormal is the cross product of the tangent and the normal: B = Cross(T,N).
#   public static Vector3d __Binormal(this Edge edge, double value)
#   {
#       UFEval eval = ufsession_.Eval;
#       eval.Initialize2(edge.Tag, out IntPtr evaluator);
#       double[] point = new double[3];
#       double[] tangent = new double[3];
#       double[] normal = new double[3];
#       double[] array = new double[3];
#       value /= Factor;
#       eval.EvaluateUnitVectors(evaluator, value, point, tangent, normal, array);
#       eval.Free(evaluator);
#       return array.__ToVector3d();
#   }

#   public static CompositeCurve __LinkEdge(this Edge edge)
#   {
#       throw new NotImplementedException();
#   }

#   public static CompositeCurve LinkCurve(Edge edge)
#   {
#       WaveLinkBuilder builder = __work_part_.BaseFeatures.CreateWaveLinkBuilder(null);

#       using (session_.__UsingBuilderDestroyer(builder))
#       {
#           builder.FixAtCurrentTimestamp = true;
#           builder.CompositeCurveBuilder.Associative = true;
#           EdgeTangentRule rule = __work_part_.ScRuleFactory.CreateRuleEdgeTangent(
#               edge,
#               null,
#               true,
#               0.5,
#               false,
#               false
#           );
#           SelectionIntentRule[] rules = new SelectionIntentRule[] { rule };
#           builder.CompositeCurveBuilder.Section.AddToSection(
#               rules,
#               edge,
#               null,
#               null,
#               _Point3dOrigin,
#               Section.Mode.Create,
#               false
#           );
#           return (CompositeCurve)builder.Commit();
#       }
#   }

#   #endregion

#    #region Spline

#  public static Spline __Copy(this Spline spline)
#  {
#      //if (spline.OwningPart.Tag != _WorkPart.Tag)
#      //    throw new ArgumentException($@"Cannot copy {nameof(spline)}.", nameof(spline));

#      //if (spline.IsOccurrence)
#      //    throw new ArgumentException($@"Cannot copy {nameof(spline)} that is an occurrence.", nameof(spline));

#      //return new Spline_(spline.Tag).Copy();
#      throw new NotImplementedException();
#  }

#  #endregion


#   #region Section

#  [Obsolete(nameof(NotImplementedException))]
#  public static Section __Mirror(
#      this Section section,
#      Surface.Plane plane)
#  {
#      throw new NotImplementedException();
#  }

#  [Obsolete(nameof(NotImplementedException))]
#  public static Section __Mirror(
#      this Section section,
#      Surface.Plane plane,
#      Component from,
#      Component to)
#  {
#      throw new NotImplementedException();
#  }

#  //internal static SelectionIntentRule[] CreateSelectionIntentRule(params ICurve[] icurves)
#  //{
#  //    var list = new List<SelectionIntentRule>();

#  //    for (var i = 0; i < icurves.Length; i++)
#  //        if (icurves[i] is Curve curve)
#  //        {
#  //            var curves = new Curve[1] { curve };
#  //            var item = __work_part_.ScRuleFactory.CreateRuleCurveDumb(curves);
#  //            list.Add(item);
#  //        }
#  //        else
#  //        {
#  //            var edges = new Edge[1] { (Edge)icurves[i] };
#  //            var item2 = __work_part_.ScRuleFactory.CreateRuleEdgeDumb(edges);
#  //            list.Add(item2);
#  //        }

#  //    return list.ToArray();
#  //}

#  internal static void __AddICurve(this Section section, params ICurve[] icurves)
#  {
#      section.AllowSelfIntersection(false);

#      for (int i = 0; i < icurves.Length; i++)
#      {
#          SelectionIntentRule[] rules = section.__OwningPart().__CreateSelectionIntentRule(icurves[i]);

#          section.AddToSection(
#              rules,
#              (NXObject)icurves[i],
#              null,
#              null,
#              _Point3dOrigin,
#              Section.Mode.Create,
#              false);
#      }
#  }

#  internal static SelectionIntentRule[] __CreateSelectionIntentRule(params Point[] points)
#  {
#      Point[] array = new Point[points.Length];

#      for (int i = 0; i < array.Length; i++)
#          array[i] = points[i];

#      CurveDumbRule curveDumbRule = __work_part_.ScRuleFactory.CreateRuleCurveDumbFromPoints(array);
#      return new SelectionIntentRule[1] { curveDumbRule };
#  }


#  internal static void __AddPoints(this Section section, params Point[] points)
#  {
#      section.AllowSelfIntersection(false);
#      SelectionIntentRule[] rules = __CreateSelectionIntentRule(points);

#      section.AddToSection(
#          rules,
#          points[0],
#          null,
#          null,
#          _Point3dOrigin,
#          Section.Mode.Create,
#          false);
#  }

#  public static void __Temp(this Section obj)
#  {
#      //obj.AddChainBetweenIntersectionPoints
#      //obj.
#  }

#  #endregion


#     #region Rules


#     public static CurveDumbRule __ToCurveDumbRule(this NXOpen.Curve curve)
#     {
#         return new[] { curve }.__ToCurveDumbRule();
#     }

#     public static CurveDumbRule __ToCurveDumbRule(this NXOpen.Curve[] curves)
#     {
#         return curves[0].__OwningPart().ScRuleFactory.CreateRuleCurveDumb(curves);
#     }

#     public static BodyDumbRule __ToBodyDumbRule(this Body body)
#     {
#         return new[] { body }.__ToBodyDumbRule();
#     }

#     public static BodyDumbRule __ToBodyDumbRule(this Body[] bodies)
#     {
#         return bodies[0].__OwningPart().ScRuleFactory.CreateRuleBodyDumb(bodies);
#     }

#     public static EdgeDumbRule __ToEdgeDumbRule(this Edge edge)
#     {
#         return new[] { edge }.__ToEdgeDumbRule();
#     }

#     public static EdgeDumbRule __ToEdgeDumbRule(this Edge[] edges)
#     {
#         return edges[0].__OwningPart().ScRuleFactory.CreateRuleEdgeDumb(edges);
#     }

#     public static CurveChainRule __ToCurveChainRule(this NXOpen.Curve seedCurve, ICurve endCurve = null, bool isFromSeedStart = true, double gapTol = .001)
#     {
#         return seedCurve.__OwningPart().ScRuleFactory.CreateRuleCurveChain(seedCurve, endCurve, isFromSeedStart, gapTol);
#     }

#     //public static EdgeChainRule __ToCurveChainRule(this NXOpen.Curve seedCurve, ICurve endCurve = null, bool isFromSeedStart = true, double gapTol = .001)
#     //{
#     //    return seedCurve.__OwningPart().ScRuleFactory.CreateRuleEdgeChain(seedCurve, endCurve, isFromSeedStart, gapTol);
#     //}

#     [Obsolete(nameof(NotImplementedException))]
#     public static BodyDumbRule __Mirror(
#         this BodyDumbRule bodyDumbRule,
#         Surface.Plane plane)
#     {
#         throw new NotImplementedException();
#     }

#     public static Body[] __Data(this BodyDumbRule rule)
#     {
#         rule.GetData(out Body[] bodies);
#         return bodies;
#     }

#     [Obsolete(nameof(NotImplementedException))]
#     public static BodyDumbRule __Mirror(
#         this BodyDumbRule bodyDumbRule,
#         Surface.Plane plane,
#         Component from,
#         Component to)
#     {
#         throw new NotImplementedException();
#     }

#     public static EdgeTangentRule __CreateRuleEdgeTangent(
#         this BasePart basePart,
#         Edge startEdge,
#         Edge endEdge = null,
#         bool isFromStart = false,
#         double? angleTolerance = null,
#         bool hasSameConvexity = false,
#         bool allowLaminarEdge = false)
#     {
#         double tol = angleTolerance ?? AngleTolerance;
#         return basePart.ScRuleFactory.CreateRuleEdgeTangent(startEdge, endEdge, isFromStart, tol, hasSameConvexity,
#             allowLaminarEdge);
#     }


#     public static void __Rule(this BasePart basePart)
#     {
#         //basePart.ScRuleFactory.
#         //basePart.ScRuleFactory.
#         //basePart.ScRuleFactory.
#         //basePart.ScRuleFactory.
#         //basePart.ScRuleFactory.
#         //basePart.ScRuleFactory.
#     }

#     [Obsolete]
#     public static ApparentChainingRule __CreateRuleApparentChainingRule(this BasePart basePart)
#     {
#         //basePart.ScRuleFactory.CreateRuleApparentChaining()
#         throw new NotImplementedException();
#     }

#     public static CurveDumbRule __CreateRuleBaseCurveDumb(this BasePart basePart,
#         params IBaseCurve[] ibaseCurves)
#     {
#         return basePart.ScRuleFactory.CreateRuleBaseCurveDumb(ibaseCurves);
#     }

#     public static BodyDumbRule __CreateRuleBodyDumb(this BasePart basePart,
#         params Body[] bodies)
#     {
#         return basePart.ScRuleFactory.CreateRuleBodyDumb(bodies);
#     }


#     #endregion

#     public static EdgeBodyRule __ToEdgeBodyRule(this SelectionIntentRule rule)
#     {
#         return (EdgeBodyRule)rule;
#     }

#     public static EdgeBoundaryRule __ToEdgeBoundaryRule(this SelectionIntentRule rule)
#     {
#         return (EdgeBoundaryRule)rule;
#     }

#     public static EdgeChainRule __ToEdgeChainRule(this SelectionIntentRule rule)
#     {
#         return (EdgeChainRule)rule;
#     }

#     public static void __Data(this EdgeChainRule rule, out Edge startEdge, out Edge endEdge, out bool isFromStart)
#     {
#         rule.GetData(out startEdge, out endEdge, out isFromStart);
#     }

#     public static EdgeDumbRule __ToEdgeDumbRule(this SelectionIntentRule rule)
#     {
#         return (EdgeDumbRule)rule;
#     }

#     public static Edge[] __Data(this EdgeDumbRule rule)
#     {
#         rule.GetData(out var edges);
#         return edges;
#     }

#     public static EdgeMultipleSeedTangentRule __ToEdgeMultipleSeedTangentRule(this SelectionIntentRule rule)
#     {
#         return (EdgeMultipleSeedTangentRule)rule;
#     }

#     public static void __Data(this EdgeMultipleSeedTangentRule rule, out Edge[] seedEdges, out double angleTolerance, out bool hasSameConvexity)
#     {
#         rule.GetData(out seedEdges, out angleTolerance, out hasSameConvexity);
#     }

#     public static Edge[] __Data(this EdgeMultipleSeedTangentRule rule)
#     {
#         rule.__Data(out var edges, out _, out _);
#         return edges;
#     }

#     public static EdgeTangentRule __ToEdgeTangentRule(this SelectionIntentRule rule)
#     {
#         return (EdgeTangentRule)rule;
#     }

#     public static EdgeVertexRule __ToEdgeVertexRule(this SelectionIntentRule rule)
#     {
#         return (EdgeVertexRule)rule;
#     }

#     public static FaceAndAdjacentFacesRule __ToFaceAndAdjacentFacesRule(this SelectionIntentRule rule)
#     {
#         return (FaceAndAdjacentFacesRule)rule;
#     }

#     public static FaceDumbRule __ToFaceDumbRule(this SelectionIntentRule rule)
#     {
#         return (FaceDumbRule)rule;
#     }

#     public static FaceTangentRule __ToFaceTangentRule(this SelectionIntentRule rule)
#     {
#         return (FaceTangentRule)rule;
#     }

#     public static Body __Data(this EdgeBodyRule rule)
#     {
#         rule.GetData(out Body body);
#         return body;
#     }

#     public static Face[] __Data(this FaceDumbRule rule)
#     {
#         rule.GetData(out var faces);
#         return faces;
#     }


#         #region Point3d

#     /// <summary>
#     ///     Creates a cone feature, given cone base position, direction, base diameter, top<br />
#     ///     diameter and height
#     /// </summary>
#     /// <param name="axisPoint">The cone base position of base arc</param>
#     /// <param name="direction">The cone direction vector from base to top</param>
#     /// <param name="baseDiameter">The cone base diameter. The cone base diameter cannot equal its top diameter</param>
#     /// <param name="topDiameter">The cone top diameter. The cone top diameter cannot equal its base diameter</param>
#     /// <param name="height">The cone height</param>
#     /// <returns>An NX.Cone feature object</returns>
#     internal static Cone __CreateConeFromDiametersHeight(
#         this BasePart basePart,
#         Point3d axisPoint,
#         Vector3d direction,
#         double baseDiameter,
#         double topDiameter,
#         double height
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         ConeBuilder builder = basePart.Features.CreateConeBuilder(null);

#         using (session_.__UsingBuilderDestroyer(builder))
#         {
#             builder.BooleanOption.Type = BooleanOperation.BooleanType.Create;
#             builder.Type = ConeBuilder.Types.DiametersAndHeight;
#             Direction direction2 = basePart.Directions.CreateDirection(
#                 axisPoint,
#                 direction,
#                 SmartObject.UpdateOption.WithinModeling
#             );
#             Axis axis = builder.Axis;
#             axis.Direction = direction2;
#             axis.Point = basePart.Points.CreatePoint(axisPoint);
#             builder.BaseDiameter.RightHandSide = baseDiameter.ToString();
#             builder.TopDiameter.RightHandSide = topDiameter.ToString();
#             builder.Height.RightHandSide = height.ToString();
#             return (Cone)builder.Commit();
#         }
#     }

#     /// <summary>Constructs a NXOpen.Arc parallel to the XY-plane</summary>
#     /// <param name="center">Center point (in absolute coordinates)</param>
#     /// <param name="radius">Radius</param>
#     /// <param name="angle1">Start angle (in degrees)</param>
#     /// <param name="angle2">End angle (in degrees)</param>
#     /// <returns>A <see cref="Arc">NXOpen.Arc</see> object</returns>
#     /// <remarks>
#     ///     <para>
#     ///         The arc will have its center at the given point, and will be parallel to the XY-plane.
#     ///     </para>
#     ///     <para>
#     ///         If the center point does not lie in the XY-plane, then the arc will not, either.
#     ///     </para>
#     /// </remarks>
#     [Obsolete]
#     public static Arc __Arc(Point3d center, double radius, double angle1, double angle2)
#     {
#         //NXOpen.Vector3d axisX = _Vector3dX();
#         //NXOpen.Vector3d axisY = _Vector3dY();
#         //return CreateArc(center, axisX, axisY, radius, angle1, angle2);
#         throw new NotImplementedException();
#     }

#     /// <summary>Creates an NX.Block from origin, matrix, xLength, yLength, zLength</summary>
#     /// <param name="origin">The corner-point of the block (in absolute coordinates</param>
#     /// <param name="matrix">Orientation (see remarks)</param>
#     /// <param name="xLength">Length in x-direction</param>
#     /// <param name="yLength">Length in y-direction</param>
#     /// <param name="zLength">Length in z-direction</param>
#     /// <returns>An NX.Block object</returns>
#     internal static Block __CreateBlock(
#         this BasePart basePart,
#         Point3d origin,
#         Matrix3x3 matrix,
#         double xLength,
#         double yLength,
#         double zLength
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         Matrix3x3 wcsOrientation = __display_part_.WCS.__Orientation();
#         __display_part_.WCS.__Orientation(matrix);
#         BlockFeatureBuilder builder = __work_part_.Features.CreateBlockFeatureBuilder(null);

#         using (session_.__UsingBuilderDestroyer(builder))
#         {
#             builder.Type = BlockFeatureBuilder.Types.OriginAndEdgeLengths;
#             builder.BooleanOption.Type = BooleanOperation.BooleanType.Create;
#             builder.SetOriginAndLengths(
#                 origin,
#                 xLength.ToString(),
#                 yLength.ToString(),
#                 zLength.ToString()
#             );
#             __display_part_.WCS.__Orientation(wcsOrientation);
#             return (Block)builder.Commit();
#         }
#     }

#     /// <summary>Constructs a circle from center, normal, radius</summary>
#     /// <param name="center">Center point (in absolute coordinates)</param>
#     /// <param name="axisZ">Unit vector normal to plane of circle</param>
#     /// <param name="radius">Radius</param>
#     /// <returns>A <see cref="T:NXOpen.Arc">NXOpen.Arc</see> object</returns>
#     /// <remarks>
#     ///     <para>
#     ///         This function gives you no control over how the circle is parameterized. You don't
#     ///         provide the X-axis, so you can't specify at which point the angle parameter is zero
#     ///     </para>
#     /// </remarks>
#     public static Arc __CreateCircle(
#         this BasePart basePart,
#         Point3d center,
#         Vector3d axisZ,
#         double radius
#     )
#     {
#         Matrix3x3 orientation = axisZ.__ToMatrix3x3();
#         Vector3d axisX = orientation.__AxisX();
#         Vector3d axisY = orientation.__AxisY();
#         return basePart.__CreateArc(center, axisX, axisY, radius, 0.0, 360.0);
#     }

#     /// <summary>Creates a circle through three points</summary>
#     /// <param name="p1">First point</param>
#     /// <param name="p2">Second point</param>
#     /// <param name="p3">Third point</param>
#     /// <returns>Circle (360 degrees) passing through the 3 points</returns>
#     [Obsolete]
#     public static Arc __CreateCircle(this BasePart basePart, Point3d p1, Point3d p2, Point3d p3)
#     {
#         basePart.__AssertIsWorkPart();
#         Vector3d vector = p2.__Subtract(p1);
#         Vector3d vector2 = p3.__Subtract(p1);
#         double num = vector.__Multiply(vector);
#         double num2 = vector.__Multiply(vector2);
#         double num3 = vector2.__Multiply(vector2);
#         double num4 = num * num3 - num2 * num2;
#         double num5 = (num * num3 - num2 * num3) / (2.0 * num4);
#         double num6 = (num * num3 - num * num2) / (2.0 * num4);
#         Vector3d vector3 = vector.__Multiply(num5).__Add(vector2.__Multiply(num6));
#         Point3d center = vector3.__Add(p1);
#         double radius = vector3.__Norm();
#         Matrix3x3 orientation = vector.__Cross(vector2).__ToMatrix3x3();
#         Vector3d axisX = orientation.__AxisX();
#         Vector3d axisY = orientation.__AxisY();
#         return basePart.__CreateArc(center, axisX, axisY, radius, 0.0, 360.0);
#     }

#     /// <summary>Creates a coordinate system</summary>
#     /// <param name="origin"></param>
#     /// <param name="matrix"></param>
#     /// <returns>An NX.CoordinateSystem object</returns>
#     internal static CoordinateSystem __CreateCoordinateSystem(
#         this BasePart basePart,
#         Point3d origin,
#         NXMatrix matrix
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         double[] array = origin.__ToArray();
#         ufsession_.Csys.CreateCsys(array, matrix.Tag, out Tag csys_id);
#         NXObject objectFromTag = (NXObject)session_.__GetTaggedObject(csys_id);
#         CoordinateSystem coordinateSystem = (CoordinateSystem)objectFromTag;
#         return coordinateSystem;
#     }

#     /// <summary>Constructs a CoordinateSystem from an origin and three axis vectors</summary>
#     /// <param name="origin">Origin position</param>
#     /// <param name="axisX">X axis</param>
#     /// <param name="axisY">Y axis</param>
#     /// <param name="axisZ">Z axis</param>
#     /// <remarks>
#     ///     Assumes that the three axis vectors are orthogonal, and does not perform any<br />
#     ///     checking.
#     /// </remarks>
#     /// <returns>An NX.CoordinateSystem object</returns>
#     internal static CoordinateSystem __CreateCoordinateSystem(
#         this BasePart basePart,
#         Point3d origin,
#         Vector3d axisX,
#         Vector3d axisY,
#         Vector3d axisZ
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         double[] array = origin.__ToArray();
#         NXMatrix matrix = __work_part_.NXMatrices.Create(axisX.__ToMatrix3x3(axisY, axisZ));
#         Tag nXOpenTag = matrix.Tag;
#         ufsession_.Csys.CreateCsys(array, nXOpenTag, out Tag csys_id);
#         NXObject objectFromTag = (NXObject)session_.__GetTaggedObject(csys_id);
#         CoordinateSystem coordinateSystem = (CoordinateSystem)objectFromTag;
#         return coordinateSystem;
#     }

#     public static Point3d __Mirror(this Point3d point, Surface.Plane plane)
#     {
#         Transform transform = Transform.CreateReflection(plane);
#         return point.__Copy(transform);
#     }

#     //
#     // Summary:
#     //     Copies a position
#     //
#     // Returns:
#     //     A copy of the original input position
#     public static Point3d __Copy(this Point3d point)
#     {
#         return new Point3d(point.X, point.Y, point.Z);
#     }

#     //
#     // Summary:
#     //     Transforms/copies a position
#     //
#     // Parameters:
#     //   xform:
#     //     The transformation to apply
#     //
#     // Returns:
#     //     A transformed copy of the original input position
#     //
#     // Remarks:
#     //     To create a transformation, use the functions in the Snap.Geom.Transform class.
#     public static Point3d __Copy(this Point3d point, Transform xform)
#     {
#         double[] matrix = xform.Matrix;
#         double x = point.X;
#         double y = point.Y;
#         double z = point.Z;
#         double x2 = x * matrix[0] + y * matrix[1] + z * matrix[2] + matrix[3];
#         double y2 = x * matrix[4] + y * matrix[5] + z * matrix[6] + matrix[7];
#         double z2 = x * matrix[8] + y * matrix[9] + z * matrix[10] + matrix[11];
#         return new Point3d(x2, y2, z2);
#     }

#     //public static Point3d __MapCsysToCsys(
#     //    this Point3d inputCoords,
#     //    CoordinateSystem inputCsys,
#     //    CoordinateSystem outputCsys)
#     //{
#     //    var origin = inputCsys.Origin;
#     //    var axisX = inputCsys.__Orientation().Element._AxisX();
#     //    var axisY = inputCsys.__Orientation().Element._AxisY();
#     //    var axisZ = inputCsys.__Orientation().Element._AxisZ();

#     //    var _x = axisX._Multiply(inputCoords.X);
#     //    var _y = axisY._Multiply(inputCoords.Y);
#     //    var _z = axisZ._Multiply(inputCoords.Z);

#     //    var vector = origin._Add(_x)._Add(_y)._Add(_z)._Subtract(outputCsys.Origin);
#     //    var x = vector._Multiply(outputCsys.__Orientation().Element._AxisX());
#     //    var y = vector._Multiply(outputCsys.__Orientation().Element._AxisY());
#     //    var z = vector._Multiply(outputCsys.__Orientation().Element._AxisZ());
#     //    return new Point3d(x, y, z);
#     //}


#     [Obsolete(nameof(NotImplementedException))]
#     public static Point3d __Mirror(
#         this Point3d point,
#         Surface.Plane plane,
#         Component from,
#         Component to
#     )
#     {
#         throw new NotImplementedException();
#     }

#     public static Point3d __MirrorMap(
#         this Point3d position,
#         Surface.Plane plane,
#         Component fromComponent,
#         Component toComponent
#     )
#     {
#         __display_part_.WCS.SetOriginAndMatrix(
#             fromComponent.__Origin(),
#             fromComponent.__Orientation()
#         );

#         Point3d newStart = __MapWcsToAcs(position);

#         __display_part_.WCS.SetOriginAndMatrix(
#             toComponent.__Origin(),
#             toComponent.__Orientation()
#         );

#         return __MapAcsToWcs(newStart);
#     }

#     public static int __ToHashCode(this Point3d p)
#     {
#         int hash = 17;

#         hash = hash * 23 + p.X.GetHashCode();
#         hash = hash * 23 + p.Y.GetHashCode();
#         hash = hash * 23 + p.Z.GetHashCode();

#         return hash;
#     }

#     public static Point3d __MapCsysToCsys(
#         this Point3d inputCoords,
#         CoordinateSystem inputCsys,
#         CoordinateSystem outputCsys
#     )
#     {
#         Point3d origin = inputCsys.Origin;
#         Vector3d axisX = inputCsys.__Orientation().Element.__AxisX();
#         Vector3d axisY = inputCsys.__Orientation().Element.__AxisY();
#         Vector3d axisZ = inputCsys.__Orientation().Element.__AxisZ();
#         Vector3d _x = axisX.__Multiply(inputCoords.X);
#         Vector3d _y = axisY.__Multiply(inputCoords.Y);
#         Vector3d _z = axisZ.__Multiply(inputCoords.Z);
#         Point3d position = origin.__Add(_x).__Add(_y).__Add(_z);
#         Vector3d vector = position.__Subtract(outputCsys.Origin);
#         double x = vector.__Multiply(outputCsys.__Orientation().Element.__AxisX());
#         double y = vector.__Multiply(outputCsys.__Orientation().Element.__AxisY());
#         double z = vector.__Multiply(outputCsys.__Orientation().Element.__AxisZ());
#         return new Point3d(x, y, z);
#     }

#     public static Point3d __Add(this Point3d point, Vector3d vector)
#     {
#         double x = point.X + vector.X;
#         double y = point.Y + vector.Y;
#         double z = point.Z + vector.Z;
#         return new Point3d(x, y, z);
#     }

#     public static Point3d __Add(this Point3d point, Vector3d vector, double distance)
#     {
#         Vector3d unit = vector.__Unit();
#         double x = point.X + unit.X * distance;
#         double y = point.Y + unit.Y * distance;
#         double z = point.Z + unit.Z * distance;
#         return new Point3d(x, y, z);
#     }

#     public static Vector3d __Subtract(this Point3d start, Point3d end)
#     {
#         double x = start.X - end.X;
#         double y = start.Y - end.Y;
#         double z = start.Z - end.Z;
#         return new Vector3d(x, y, z);
#     }

#     [Obsolete(nameof(NotImplementedException))]
#     public static Point3d __Subtract(this Point3d start, Vector3d end)
#     {
#         //double x = start.X - end.X;
#         //double y = start.Y - end.Y;
#         //double z = start.Z - end.Z;
#         //return new NXOpen.Vector3d(x, y, z);
#         throw new NotImplementedException();
#     }

#     /// <summary>Creates a datum axis from a position and a vector</summary>
#     /// <param name="origin">The base point of the datum axis</param>
#     /// <param name="direction">The direction vector of the datum axis (length doesn't matter)</param>
#     /// <returns>An NX.DatumAxis object</returns>
#     internal static DatumAxisFeature __CreateDatumAxis(
#         this BasePart basePart,
#         Point3d origin,
#         Vector3d direction
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         Part part = __work_part_;
#         DatumAxisBuilder datumAxisBuilder = part.Features.CreateDatumAxisBuilder(null);

#         using (session_.__UsingBuilderDestroyer(datumAxisBuilder))
#         {
#             datumAxisBuilder.Type = DatumAxisBuilder.Types.PointAndDir;
#             Direction vector = part.Directions.CreateDirection(
#                 origin,
#                 direction,
#                 SmartObject.UpdateOption.WithinModeling
#             );
#             datumAxisBuilder.IsAssociative = true;
#             datumAxisBuilder.IsAxisReversed = false;
#             datumAxisBuilder.Vector = vector;
#             datumAxisBuilder.Point = part.Points.CreatePoint(origin);
#             Feature feature = datumAxisBuilder.CommitFeature();
#             return (DatumAxisFeature)feature;
#         }
#     }

#     /// <summary>Creates a datum axis from two positions</summary>
#     /// <param name="startPoint">The start point of the axis</param>
#     /// <param name="endPoint">The end point of the axis</param>
#     /// <returns>An NX.DatumAxis object</returns>
#     internal static DatumAxisFeature __CreateDatumAxis(
#         this BasePart basePart,
#         Point3d startPoint,
#         Point3d endPoint
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         Part part = __work_part_;
#         DatumAxisBuilder datumAxisBuilder = part.Features.CreateDatumAxisBuilder(null);

#         using (session_.__UsingBuilderDestroyer(datumAxisBuilder))
#         {
#             datumAxisBuilder.Type = DatumAxisBuilder.Types.TwoPoints;
#             datumAxisBuilder.IsAssociative = true;
#             datumAxisBuilder.IsAxisReversed = false;
#             datumAxisBuilder.Point1 = part.Points.CreatePoint(startPoint);
#             datumAxisBuilder.Point2 = part.Points.CreatePoint(endPoint);
#             Feature feature = datumAxisBuilder.CommitFeature();
#             return (DatumAxisFeature)feature;
#         }
#     }

#     [Obsolete(nameof(NotImplementedException))]
#     private static double __ArcPercentage(ICurve curve, Point3d point1, Point3d point2)
#     {
#         //double arc_length = 0.0;
#         //double num = curve.MaxU - curve.MinU;
#         //double start_param = (curve.Parameter(point1) - curve.MinU) / num;
#         //double end_param = (curve.Parameter(point2) - curve.MinU) / num;
#         //UFEval eval = ufsession_.Eval;
#         //eval.Initialize2(curve.NXOpenTag, out var evaluator);
#         //double[] limits = new double[2] { 0.0, 1.0 };
#         //eval.AskLimits(evaluator, limits);
#         //eval.Free(evaluator);
#         //ufsession_.Curve.AskArcLength(curve.NXOpenTag, start_param, end_param, ModlUnits.ModlMmeter, out arc_length);
#         //return arc_length / curve.ArcLength * 100.0;
#         throw new NotImplementedException();
#     }

#     internal static DatumCsys __CreateDatumCsys(this BasePart basePart)
#     {
#         return basePart.__CreateDatumCsys(_Point3dOrigin, _Matrix3x3Identity);
#     }

#     /// <summary>
#     ///     Creates a datum csys object
#     /// </summary>
#     /// <param name="origin">The origin of the csys</param>
#     /// <param name="matrix">The orientation of the csys</param>
#     /// <returns>An NX.DatumCsys object</returns>
#     internal static DatumCsys __CreateDatumCsys(
#         this BasePart basePart,
#         Point3d origin,
#         Matrix3x3 matrix
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         Part part = __work_part_;
#         DatumCsysBuilder builder = part.Features.CreateDatumCsysBuilder(null);

#         using (session_.__UsingBuilderDestroyer(builder))
#         {
#             Xform xform = part.Xforms.CreateXform(
#                 origin,
#                 matrix.__AxisX(),
#                 matrix.__AxisY(),
#                 SmartObject.UpdateOption.WithinModeling,
#                 1.0
#             );
#             CartesianCoordinateSystem csys = part.CoordinateSystems.CreateCoordinateSystem(
#                 xform,
#                 SmartObject.UpdateOption.WithinModeling
#             );
#             builder.Csys = csys;
#             return (DatumCsys)builder.Commit();
#         }
#     }

#     /// <summary>
#     ///     Creates a datum csys object
#     /// </summary>
#     /// <param name="origin">The origin of the csys</param>
#     /// <param name="axisX">The axis in x direction</param>
#     /// <param name="axisY">The axis in y direction</param>
#     /// <returns>An NX.DatumCsys object</returns>
#     internal static DatumCsys __CreateDatumCsys(
#         this BasePart basePart,
#         Point3d origin,
#         Vector3d axisX,
#         Vector3d axisY
#     )
#     {
#         return basePart.__CreateDatumCsys(origin, axisX.__ToMatrix3x3(axisY));
#     }

#     /// <summary>Creates a Snap.NX.DatumPlane feature from a given position and orientation</summary>
#     /// <param name="origin">Origin of the datum plane</param>
#     /// <param name="orientation">Orientation of the datum plane</param>
#     /// <returns> A <see cref="T:Snap.NX.DatumPlane">Snap.NX.DatumPlane</see> object</returns>
#     [Obsolete]
#     public static DatumPlaneFeature __DatumPlane(Point3d origin, Matrix3x3 orientation)
#     {
#         //return __CreateFixedDatumPlane(origin, orientation);
#         throw new NotImplementedException();
#     }

#     /// <summary>Creates a datum plane from a point and a vector</summary>
#     /// <param name="position">NXOpen.Point3d of the datum plane</param>
#     /// <param name="direction">The normal vector of the datum plane</param>
#     /// <returns>An NX.DatumPlane object</returns>
#     internal static DatumPlaneFeature __CreateDatumPlaneFeature(
#         this BasePart basePart,
#         Point3d position,
#         Vector3d direction
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         Part part = __work_part_;
#         DatumPlaneBuilder datumPlaneBuilder = part.Features.CreateDatumPlaneBuilder(null);
#         Plane plane = datumPlaneBuilder.GetPlane();
#         plane.SetMethod(PlaneTypes.MethodType.PointDir);
#         Direction direction2 = __work_part_.Directions.CreateDirection(
#             position,
#             direction,
#             SmartObject.UpdateOption.WithinModeling
#         );
#         plane.SetGeometry(new NXObject[] { part.Points.CreatePoint(position), direction2 });
#         plane.Evaluate();
#         DatumPlaneFeature datumPlaneFeature = (DatumPlaneFeature)
#             datumPlaneBuilder.CommitFeature();
#         datumPlaneBuilder.Destroy();
#         return datumPlaneFeature;
#         throw new NotImplementedException();
#     }

#     /// <summary>Creates a datum plane from a point and an orientation</summary>
#     /// <param name="origin">Origin of the datum plane</param>
#     /// <param name="orientation">Orientation of the datum plane</param>
#     /// <returns>An NX.DatumPlane object</returns>
#     internal static DatumPlaneFeature __CreateFixedDatumPlaneFeature(
#         this BasePart basePart,
#         Point3d origin,
#         Matrix3x3 orientation
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         return (DatumPlaneFeature)
#             __work_part_.Datums.CreateFixedDatumPlane(origin, orientation).Feature;
#     }

#     /// <summary>Creates a rectangle (an array of four lines) from given center and side lengths</summary>
#     /// <param name="basePart"></param>
#     /// <param name="center">Center location</param>
#     /// <param name="width">Width in the x-direction</param>
#     /// <param name="height">Height in the y-direction</param>
#     /// <returns>Array of four lines</returns>
#     [Obsolete]
#     public static Line[] __CreateRectangle(
#         this BasePart basePart,
#         Point3d center,
#         double width,
#         double height
#     )
#     {
#         basePart.__AssertIsWorkPart();
#         Vector3d vector = new Vector3d(width / 2.0, 0.0, 0.0);
#         Vector3d vector2 = new Vector3d(0.0, height / 2.0, 0.0);
#         Point3d position = center.__Add(vector).__Subtract(vector2); // center + vector - vector2;
#         Point3d position2 = center.__Add(vector).__Add(vector2);
#         Point3d position3 = center.__Subtract(vector).__Add(vector2);
#         Point3d position4 = center.__Subtract(vector).__Subtract(vector2);
#         return __work_part_.__PolyLine(position, position2, position3, position4, position);
#     }

#     /// <summary>Creates a rectangle from two diagonal points</summary>
#     /// <param name="bottomLeft">The point at the (xmin, ymin) corner</param>
#     /// <param name="topRight">The point at the (xmax, ymax) corner</param>
#     /// <returns>Array of four lines</returns>
#     [Obsolete(nameof(NotImplementedException))]
#     public static Line[] __Rectangle(Point3d bottomLeft, Point3d topRight)
#     {
#         //NXOpen.Point3d center = (bottomLeft + topRight) / 2.0;
#         //double width = topRight.X - bottomLeft.X;
#         //double height = topRight.Y - bottomLeft.Y;
#         //return Rectangle(center, width, height);
#         throw new NotImplementedException();
#     }

#     /// <summary>
#     ///     Creates a polyline (an array of lines connecting given positions)
#     /// </summary>
#     /// <param name="basePart">The base part to place the lines in.<br />Must be the work part</param>
#     /// <param name="points">Array of positions forming the vertices of the polyline</param>
#     /// <returns>Array of lines forming the segments of the polyline</returns>
#     /// <remarks>
#     ///     The i-th line has startPoint = points[i] and endPoint = points[i+1].
#     /// </remarks>
#     public static Line[] __PolyLine(this BasePart basePart, params Point3d[] points)
#     {
#         int num = points.Length;
#         Line[] array = new Line[num - 1];

#         for (int i = 0; i < num - 1; i++)
#             array[i] = __CreateLine(points[i], points[i + 1]);

#         return array;
#     }

#     //
#     // Summary:
#     //     Creates a polygon (an array of lines forming a closed figure)
#     //
#     // Parameters:
#     //   points:
#     //     Array of positions forming the vertices of the polygon
#     //
#     // Returns:
#     //     Array of lines forming the sides of the polygon
#     //
#     // Remarks:
#     //     The i-th line has startPoint = points[i] and endPoint = points[i+1]. The last
#     //     line closes the figure -- it has startPoint = points[n-1] and endPoint = points[0].
#     /// <summary>
#     /// </summary>
#     /// <param name="points"></param>
#     /// <returns></returns>
#     public static Line[] __Polygon(params Point3d[] points)
#     {
#         int num = points.Length;
#         Line[] array = new Line[num];
#         for (int i = 0; i < num - 1; i++)
#             array[i] = __CreateLine(points[i], points[i + 1]);

#         array[num - 1] = __CreateLine(points[num - 1], points[0]);
#         return array;
#     }

#     public static bool __IsEqualTo(this Point3d point3d, Point3d other)
#     {
#         return point3d.__IsEqualTo(other.__ToArray());
#     }

#     public static bool __IsEqualTo(this Point3d point3d, double[] array)
#     {
#         return System.Math.Abs(point3d.X - array[0]) < .001
#             && System.Math.Abs(point3d.Y - array[1]) < .001
#             && System.Math.Abs(point3d.Z - array[2]) < .001;
#     }

#     public static double[] __ToArray(this Point3d point3d)
#     {
#         return new[] { point3d.X, point3d.Y, point3d.Z };
#     }

#     //
#     // Summary:
#     //     Projects a position onto a plane (along the plane normal)
#     //
#     // Parameters:
#     //   plane:
#     //     The plane onto which we want to project
#     //
#     // Returns:
#     //     The projected position
#     [Obsolete(nameof(NotImplementedException))]
#     public static Point3d __Project(this Point3d point, Surface.Plane plane)
#     {
#         //Vector normal = plane.Normal;
#         //Vector vector =  (point - plane.Origin) * normal * normal;
#         //return this - vector;
#         throw new NotImplementedException();
#     }

#     //
#     // Summary:
#     //     Projects a position onto a ray (along a ray normal)
#     //
#     // Parameters:
#     //   ray:
#     //     The ray onto which we want to project
#     //
#     // Returns:
#     //     The projected position
#     [Obsolete(nameof(NotImplementedException))]
#     public static Point3d __Project(this Point3d point, Curve.Ray ray)
#     {
#         //Vector axis = ray.Axis;
#         //double num = (this - ray.Origin) * axis;
#         //return ray.Origin + num * ray.Axis;
#         throw new NotImplementedException();
#     }

#     public static double[] __Array(this Point3d point)
#     {
#         return new[] { point.X, point.Y, point.Z };
#     }

#     /// <summary>Creates a line through a given point, tangent to a curve</summary>
#     /// <param name="basePoint">Point through which the line passes</param>
#     /// <param name="icurve">A curve or edge</param>
#     /// <param name="helpPoint">A point near the desired tangency point</param>
#     /// <returns>A <see cref="T:Snap.NX.Line">Snap.NX.Line</see> object</returns>
#     /// <remarks>
#     ///     <para>
#     ///         The line will start at the given point, and end at the tangent point on the curve.
#     ///     </para>
#     ///     <para>
#     ///         The help point does not have to lie on the curve, just somewhere near the desired tangency point.
#     ///     </para>
#     ///     <para>
#     ///         If the base point lies on the curve, then an infinite line is generated. In this case, the help point has no
#     ///         influence.
#     ///     </para>
#     ///     <para>
#     ///         If the base point and the curve are not in the same plane, then the base point is projected to the plane of the
#     ///         curve,
#     ///         and a tangent line is generated between the projected point and the given curve.
#     ///     </para>
#     /// </remarks>
#     [Obsolete(nameof(NotImplementedException))]
#     public static Line __CreateLineTangent(Point3d basePoint, ICurve icurve, Point3d helpPoint)
#     {
#         //IsLinearCurve(icurve);
#         //if (Compute.Distance(basePoint, (Snap.NX.NXObject)icurve) < 1E-05)
#         //{
#         //    double value = icurve.Parameter(basePoint);
#         //    NXOpen.Vector3d axis = icurve.Tangent(value);
#         //    NXOpen.Point3d[] array = Compute.ClipRay(new Snap.Geom.Curve.Ray(basePoint, axis));
#         //    return Line(array[0], array[1]);
#         //}

#         //double value2 = icurve.Parameter(icurve._StartPoint());
#         //Surface.Plane plane = new Surface.Plane(icurve._StartPoint(), icurve.Binormal(value2));
#         //NXOpen.Point3d p = basePoint.Project(plane);
#         //NXOpen.Point3d position = helpPoint.Project(plane);
#         //var workPart = __work_part_;
#         //AssociativeLine associativeLine = null;
#         //AssociativeLineBuilder associativeLineBuilder = workPart.NXOpenPart.BaseFeatures.CreateAssociativeLineBuilder(associativeLine);
#         //associativeLineBuilder.StartPointOptions = AssociativeLineBuilder.StartOption.Point;
#         //associativeLineBuilder.StartPoint.Value = Point(p);
#         //associativeLineBuilder.EndPointOptions = AssociativeLineBuilder.EndOption.Tangent;
#         //associativeLineBuilder.EndTangent.SetValue(icurve, null, position);
#         //associativeLineBuilder.Associative = false;
#         //associativeLineBuilder.Commit();
#         //NXOpen.NXObject nXObject = associativeLineBuilder.GetCommittedObjects()[0];
#         //associativeLineBuilder.Destroy();
#         //return new Snap.NX.Line((NXOpen.Line)nXObject);
#         throw new NotImplementedException();
#     }

#     ///// <summary>Creates an NX.Point object from given coordinates</summary>
#     ///// <param name="p">NXOpen.Point3d</param>
#     ///// <returns>An invisible NXOpen.Point object (a "smart point")</returns>
#     //internal static NXOpen.Point CreatePointInvisible(NXOpen.Point3d p)
#     //{
#     //    return CreatePointInvisible(p.X, p.Y, p.Z);
#     //}


#     /// <summary>Creates an NX.Arc from three points</summary>
#     /// <param name="basePart"></param>
#     /// <param name="startPoint">Start point</param>
#     /// <param name="pointOn">Point that the arc passes through</param>
#     /// <param name="endPoint">End point</param>
#     /// <returns>An NX.Arc object</returns>
#     internal static Arc __CreateArc(
#         this BasePart basePart,
#         Point3d startPoint,
#         Point3d pointOn,
#         Point3d endPoint
#     )
#     {
#         return basePart.Curves.CreateArc(startPoint, pointOn, endPoint, false, out _);
#     }

#     /// <summary>Map a position from Work coordinates to Absolute coordinates</summary>
#     /// <param name="workCoords">The coordinates of the given point wrt the Work Coordinate System (WCS)</param>
#     /// <returns>The coordinates of the given point wrt the Absolute Coordinate System (ACS)</returns>
#     /// <remarks>
#     ///     <para>
#     ///         If you are given point coordinates relative to the WCS, then you will need to
#     ///         use this function to "map" them to the ACS before using them in SNAP functions.
#     ///     </para>
#     /// </remarks>
#     public static Point3d __MapWcsToAcs(this Point3d workCoords)
#     {
#         int input_csys = UF_CSYS_ROOT_WCS_COORDS;
#         int output_csys = UF_CSYS_ROOT_COORDS;
#         double[] numArray = new double[3];
#         ufsession_.Csys.MapPoint(input_csys, workCoords.__ToArray(), output_csys, numArray);
#         return numArray.__ToPoint3d();
#     }

#     /// <summary>Map a position from Absolute coordinates to Work coordinates</summary>
#     /// <param name="absCoords">The coordinates of the given point wrt the Absolute Coordinate System (ACS)</param>
#     /// <returns>The coordinates of the given point wrt the Work Coordinate System (WCS)</returns>
#     public static Point3d __MapAcsToWcs(this Point3d absCoords)
#     {
#         int output_csys = UF_CSYS_ROOT_WCS_COORDS;
#         int input_csys = UF_CSYS_ROOT_COORDS;
#         double[] numArray = new double[3];
#         ufsession_.Csys.MapPoint(input_csys, absCoords.__ToArray(), output_csys, numArray);
#         return numArray.__ToPoint3d();
#     }

#     public static double __Distance(this Point3d p, Point3d q)
#     {
#         return p.__Subtract(q).__Norm();
#     }

#     public static double __Distance2(this Point3d p, Point3d q)
#     {
#         return p.__Subtract(q).__Norm2();
#     }

#     public static Point3d __MidPoint(this Point3d p, Point3d q)
#     {
#         double x = (p.X + q.X) / 2;
#         double y = (p.Y + q.Y) / 2;
#         double z = (p.Z + q.Z) / 2;
#         return new Point3d(x, y, z);
#     }

#     public static Point3d __AddX(this Point3d p, double x)
#     {
#         return new Point3d(p.X + x, p.Y, p.Z);
#     }

#     public static Point3d __AddY(this Point3d p, double y)
#     {
#         return new Point3d(p.X, p.Y + y, p.Z);
#     }

#     public static Point3d __AddZ(this Point3d p, double z)
#     {
#         return new Point3d(p.X, p.Y, p.Z + z);
#     }

#     [Obsolete]
#     public static Point3d _Transform(this Point3d original, Transform transform)
#     {
#         throw new NotImplementedException();
#         //return ((Point3d)(ref original)).Copy(transform);
#     }

#     public static double[] _Array(this Point3d point3D)
#     {
#         return new double[3] { point3D.X, point3D.Y, point3D.Z };
#     }

#     public static Point3d _Mirror(this Point3d original, Surface.Plane plane)
#     {
#         Transform val = Transform.CreateReflection(plane);
#         return original.__Copy(val);
#     }

#     public static Point3d _MirrorMap(
#         this Point3d origin,
#         Surface.Plane mirrorPlane,
#         Component originalComp,
#         Component newComp
#     )
#     {
#         originalComp.__SetWcsToComponent();
#         Point3d original = origin.__MapWcsToAcs();
#         Point3d val = original._Mirror(mirrorPlane);
#         newComp.__SetWcsToComponent();
#         return val.__MapAcsToWcs();
#     }

#     //public static bool _IsEqualTo(this Point3d position1, Point3d position2, double tolerance)
#     //{
#     //    //IL_0006: Unknown result type (might be due to invalid IL or missing references)
#     //    //IL_0007: Unknown result type (might be due to invalid IL or missing references)
#     //    return new EqualityPosition(tolerance).Equals(position1, position2);
#     //}

#     //public static bool _IsEqualTo(this Point3d position1, Point3d position2)
#     //{
#     //    //IL_0000: Unknown result type (might be due to invalid IL or missing references)
#     //    //IL_0001: Unknown result type (might be due to invalid IL or missing references)
#     //    return position1._IsEqualTo(position2, 0.01);
#     //}

#     //public static bool _IsEqualTo(this Point3d vector1, Point3d vector2, double tolerance = 0.01)
#     //{
#     //    ufsession_.Vec3.IsEqual(((Vector)(ref vector1)).Array, ((Vector)(ref vector2)).Array, tolerance, out var is_equal);
#     //    return is_equal switch
#     //    {
#     //        0 => false,
#     //        1 => true,
#     //        _ => throw NXException.Create(is_equal),
#     //    };
#     //}

#     public static Point3d _MidPoint(this Point3d position1, Point3d position2)
#     {
#         return new Point3d(
#             (position1.X + position2.X) / 2.0,
#             (position1.Y + position2.Y) / 2.0,
#             (position1.Z + position2.Z) / 2.0
#         );
#     }


def point3d_midpoint_point3d(pnt0: Point3d, pnt1: Point3d) -> Point3d:
    #     //public static Point3d _MidPoint(this Point3d position1, Point3d position2)
    #     //{
    #     //    return new Point3d((position1.X + position2.X) / 2.0, (position1.Y + position2.Y) / 2.0, (position1.Z + position2.Z) / 2.0);
    #     //}
    pass


#     public static Point _CreatePoint(this Part part, Point3d origin)
#     {
#         return part.Points.CreatePoint(origin);
#     }

#     public static Point3d _AveragePosition(this Point3d[] positions)
#     {
#         if (positions == null)
#             throw new ArgumentNullException("positions");

#         if (positions.Length == 0)
#             throw new ArgumentOutOfRangeException("positions");

#         double num = 0.0;
#         double num2 = 0.0;
#         double num3 = 0.0;
#         for (int i = 0; i < positions.Length; i++)
#         {
#             num += positions[i].X;
#             num2 += positions[i].Y;
#             num3 += positions[i].Z;
#         }

#         return new Point3d(num, num2, num3);
#     }

#     public static Point3d _AveragePosition(this NXOpen.Curve[] curves)
#     {
#         return curves
#             .SelectMany(c => new Point3d[2] { c.__StartPoint(), c.__EndPoint() })
#             .ToArray()
#             ._AveragePosition();
#     }


def point3d_to_nxpoint(pnt3d: Point3d, name: str = None) -> Point:
    point = work_part().Points.CreatePoint(pnt3d)
    point.SetVisibility(SmartObject.VisibilityOption.Visible)
    point.RedisplayObject()
    if name is not None:
        point.SetName(name)
    return point


#     public static PointFeature __ToPointFeature(this Point3d point3d)
#     {
#         var builder = __work_part_.BaseFeatures.CreatePointFeatureBuilder(null);

#         using (builder.__UsingBuilder())
#         {
#             builder.Point = point3d.__ToPoint();
#             return (PointFeature)builder.Commit();
#         }
#     }

#     public static Point3d __Round(this Point3d point, int digits)
#     {
#         return new Point3d(point.X.__Round(digits), point.Y.__Round(digits), point.Z.__Round(digits));
#     }

#     public static double __DistanceToPlane(
#         this Point3d point,
#         Point3d point_on_plane,
#         Vector3d plane_normal,
#         double tolerance = .001)
#     {
#         ufsession_.Vec3.DistanceToPlane(
#             point.__ToArray(),
#             point_on_plane.__ToArray(),
#             plane_normal.__ToArray(),
#             tolerance,
#             out double distance
#         );

#         return distance;
#     }

#     public static Point __ToPoint(this Point3d point3d)
#     {
#         Point point = __work_part_.Points.CreatePoint(point3d);
#         point.SetVisibility(SmartObject.VisibilityOption.Visible);
#         return point;
#     }

#     #endregion


#       public static Point __Point(this PointFeature feature)
#   {
#       ufsession_.Point.AskPointOutput(feature.Tag, out Tag point_id);
#       return (Point)session_.__GetTaggedObject(point_id);
#   }

#   public static DatumAxisFeature __ToDatumAxisFeature(this Point origin, Vector3d vector)
#   {
#       NXOpen.Features.DatumAxisBuilder datumAxisBuilder1;
#       datumAxisBuilder1 = origin.__OwningPart().Features.CreateDatumAxisBuilder(null);

#       using (datumAxisBuilder1.__UsingBuilder())
#       {
#           datumAxisBuilder1.IsAssociative = true;
#           datumAxisBuilder1.Type = NXOpen.Features.DatumAxisBuilder.Types.PointAndDir;
#           datumAxisBuilder1.Point = origin;
#           var direction1 = origin
#               .__OwningPart()
#               .Directions.CreateDirection(
#                   origin.Coordinates,
#                   vector,
#                   NXOpen.SmartObject.UpdateOption.WithinModeling
#               );
#           datumAxisBuilder1.Vector = direction1;
#           datumAxisBuilder1.ResizedEndDistance = 4.0;
#           var nXObject1 = datumAxisBuilder1.Commit();
#           return (DatumAxisFeature)nXObject1;
#       }
#   }


def point_move(point: Point, vec: Vector3d, distance: float) -> None:
    #   public static void __Move(this Point point, Vector3d vector, double distance)
    #   {
    #       Vector3d unit = vector.__Unit().__Multiply(distance);
    #       point.SetCoordinates(point.Coordinates.__Add(unit));
    #       point.RedisplayObject();
    #   }
    pass


#   public static Point __Copy(this Point point, Vector3d vector, double distance)
#   {
#       Vector3d unit = vector.__Unit().__Multiply(distance);
#       return point.Coordinates.__Add(unit).__ToPoint();
#   }

#   public static UserDefinedObject __ToDynamicHandle(this Point point)
#   {
#       UserDefinedClass myUdOclass =
#           session_.UserDefinedClassManager.GetUserDefinedClassFromClassName(
#               "UdoDynamicHandle"
#           );

#       var myUdo = __display_part_.UserDefinedObjectManager.CreateUserDefinedObject(
#           myUdOclass
#       );

#       UserDefinedObject.LinkDefinition[] myLinks = new UserDefinedObject.LinkDefinition[1];
#       myUdo.SetDoubles(point.Coordinates.__ToArray());
#       int[] displayFlag = new int[] { 1 };
#       myUdo.SetIntegers(displayFlag);
#       myLinks[0].AssociatedObject = point;
#       myLinks[0].Status = UserDefinedObject.LinkStatus.UpToDate;
#       myUdo.SetLinks(UserDefinedObject.LinkType.Type1, myLinks);
#       ufsession_.Disp.AddItemToDisplay(myUdo.Tag);
#       return myUdo;
#   }

#   private static int GenericCallback(UserDefinedEvent eventObject)
#   {
#       //print("edit");

#       print(eventObject.EventReason);
#       ufsession_.Disp.AddItemToDisplay(eventObject.UserDefinedObject.Tag);

#       return 0;
#   }


#   #region NXObject


def nxobject_delete_user_attribute():
    #   public static void __DeleteUserAttribute(
    #       this NXObject nxobject,
    #       string title,
    #       Update.Option update_option = Update.Option.Now
    #   )
    #   {
    #       nxobject.DeleteUserAttribute(NXObject.AttributeType.String, title, true, update_option);
    #   }
    raise NotImplementedError()


def nxobject_remove_parameters(nxobject: NXObject) -> None:
    #   public static void __RemoveParameters(this NXObject nxobject)
    #   {
    #       RemoveParametersBuilder removeBuilder;

    #       if (nxobject is BasePart base_part)
    #       {
    #           removeBuilder = base_part.Features.CreateRemoveParametersBuilder();

    #           using (session_.__UsingBuilderDestroyer(removeBuilder))
    #           {
    #               removeBuilder.Objects.Add(base_part.Features.ToArray());
    #               removeBuilder.Commit();
    #           }

    #           return;
    #       }
    raise NotImplementedError()


#       removeBuilder = nxobject
#           .__OwningPart()
#           .Features.CreateRemoveParametersBuilder();

#       using (session_.__UsingBuilderDestroyer(removeBuilder))
#       {
#           removeBuilder.Objects.Add(nxobject);
#           removeBuilder.Commit();
#       }
#   }


def nxobject_get_attribute(nxobject: NXObject, title: str) -> str:
    # return nxobject.GetUserAttributeAsString(title, NXObject.AttributeType.String, -1)
    raise Exception()


def nxobject_has_attribute(nxobject: NXObject, title: str) -> bool:
    return nxobject.HasUserAttribute(title, NXObject.AttributeType.String, -1)


def nxobject_del_attribute(nxobject: NXObject, title: str) -> None:
    return nxobject.DeleteUserAttribute(
        NXObject.AttributeType.String, title, True, Update.Option.Now
    )


def nxobject_set_attribute(
    nxobject: NXObject,
    title: str,
    value: str,
    option: Update.Option = Update.Option.Later,
) -> None:
    nxobject.SetUserAttribute(title, -1, value, option)


#   //
#   // Summary:
#   //     Copies an NX.NXObject (with no transform)
#   //
#   // Returns:
#   //     A copy of the input object
#   //
#   // Exceptions:
#   //   T:System.ArgumentException:
#   //     The object is an edge. Edges cannot be copied.
#   //
#   //   T:System.ArgumentException:
#   //     The object is a face. Faces cannot be copied.
#   //
#   //   T:System.ArgumentException:
#   //     A feature cannot be copied unless all of its ancestors are copied too.
#   //
#   // Remarks:
#   //     The new object will be on the same layer as the original one.
#   public static NXObject Copy(this NXObject nxObject)
#   {
#       Transform xform = Transform.CreateTranslation(0.0, 0.0, 0.0);
#       return nxObject.Copy(xform);
#   }

#   //
#   // Summary:
#   //     Transforms/copies an object
#   //
#   // Parameters:
#   //   xform:
#   //     Transform to be applied
#   //
#   // Returns:
#   //     Output object
#   //
#   // Exceptions:
#   //   T:System.ArgumentException:
#   //     The object is an edge. Edges cannot be copied.
#   //
#   //   T:System.ArgumentException:
#   //     The object is a face. Faces cannot be copied.
#   //
#   //   T:System.ArgumentException:
#   //     A feature cannot be copied unless all of its ancestors are copied too.
#   //
#   //   T:System.ArgumentException:
#   //     A transform that does not preserve angles cannot be applied to a coordinate system.
#   //
#   // Remarks:
#   //     To create a transformation, use the functions in the Snap.Geom.Transform class.
#   public static NXObject Copy(this NXObject nxObject, Transform xform)
#   {
#       _ = new double[16];
#       int n_objects = 1;
#       Tag[] objects = new Tag[1] { nxObject.Tag };
#       int move_or_copy = 2;
#       int dest_layer = 0;
#       int trace_curves = 2;
#       Tag[] array = new Tag[n_objects];
#       int status = 0;

#       try
#       {
#           ufsession_.Trns.TransformObjects(
#               xform.Matrix,
#               objects,
#               ref n_objects,
#               ref move_or_copy,
#               ref dest_layer,
#               ref trace_curves,
#               array,
#               out var _,
#               out status
#           );

#           switch (status)
#           {
#               case 3:
#                   throw NXException.Create(674861);
#               case 4:
#                   throw new ArgumentException("The matrix does not preserve angles");
#               case 5:
#                   throw NXException.Create(670024);
#               case 6:
#                   throw NXException.Create(670008);
#               case 7:
#                   throw NXException.Create(670009);
#               case 8:
#                   throw NXException.Create(37);
#               case 9:
#                   throw NXException.Create(670022);
#               case 10:
#                   throw NXException.Create(670023);
#               case 11:
#                   throw NXException.Create(660002);
#               case 0:
#                   if (array[0] == Tag.Null)
#                   {
#                       throw NXException.Create(674861);
#                   }

#                   break;
#           }

#           NXObject[] array2 = new NXObject[n_objects];

#           for (int i = 0; i < n_objects; i++)
#               array2[i] = (NXObject)array[i].__ToTaggedObject();

#           return array2[0];
#       }
#       catch (NXException innerException)
#       {
#           switch (nxObject)
#           {
#               case Edge _:
#                   throw new ArgumentException(
#                       "The object is an edge. Edges cannot be copied",
#                       innerException
#                   );
#               case Face _:
#                   throw new ArgumentException(
#                       "The object is a face. Faces cannot be copied",
#                       innerException
#                   );
#               case Feature _:
#               case DatumPlane _:
#               case DatumAxis _:
#                   throw new ArgumentException(
#                       "A feature cannot be copied unless all of its ancestors are copied too",
#                       innerException
#                   );
#               case CoordinateSystem _:
#               default:
#                   throw;
#           }
#       }
#   }

#   public static bool __TryGetAtt(this NXObject nxobj, string title, out string value)
#   {
#       if (nxobj.__HasAttribute(title))
#       {
#           value = nxobj.__GetAttribute(title);
#           return true;
#       }

#       value = "";
#       return false;
#   }

#   #endregion


#           #region Matrix3x3

#         /// <summary>
#         ///     Maps an orientation from one coordinate system to another.
#         /// </summary>
#         /// <param name="orientation">The components of the given Orientation with the input coordinate system.</param>
#         /// <param name="inputCsys">The input coordinate system.</param>
#         /// <param name="outputCsys">The output coordinate system.</param>
#         /// <returns>The components of the Orientation with the output coordinate system.</returns>
#         public static Matrix3x3 __MapCsysToCsys(
#             Matrix3x3 orientation,
#             CartesianCoordinateSystem inputCsys,
#             CartesianCoordinateSystem outputCsys)
#         {
# #pragma warning disable CS0612 // Type or member is obsolete
#             Vector3d mappedXVector = __MapCsysToCsys(orientation.__AxisX(), inputCsys, outputCsys);
#             Vector3d mappedYVector = __MapCsysToCsys(orientation.__AxisY(), inputCsys, outputCsys);
# #pragma warning restore CS0612 // Type or member is obsolete
#             return mappedXVector.__ToMatrix3x3(mappedYVector);
#         }


#         public static Matrix3x3 __MirrorMap(this Matrix3x3 orientation, Surface.Plane plane,
#             Component fromComponent, Component toComponent)
#         {
#             Vector3d newXVector = __MirrorMap(orientation.__AxisY(), plane, fromComponent, toComponent);

#             Vector3d newYVector = __MirrorMap(orientation.__AxisX(), plane, fromComponent, toComponent);

#             return newXVector.__ToMatrix3x3(newYVector);
#         }

#         public static Vector3d __AxisY(this Matrix3x3 matrix)
#         {
#             return new Vector3d(matrix.Yx, matrix.Yy, matrix.Yz);
#         }

#         public static Vector3d __AxisZ(this Matrix3x3 matrix)
#         {
#             return new Vector3d(matrix.Zx, matrix.Zy, matrix.Zz);
#         }


def matrix3x3_to_sequence(matrix: Matrix3x3) -> Sequence[float]:
    return [
        matrix.Xx,
        matrix.Xy,
        matrix.Xz,
        matrix.Yx,
        matrix.Yy,
        matrix.Yz,
        matrix.Zx,
        matrix.Zy,
        matrix.Zz,
    ]


#         public static Vector3d __AxisX(this Matrix3x3 matrix)
#         {
#             return new Vector3d(matrix.Xx, matrix.Xy, matrix.Xz);
#         }

#         /// <summary>
#         /// Gets the vector x , y , z
#         /// with indexes 0, 1, 2, respectively
#         /// </summary>
#         public static Vector3d __Axis(this Matrix3x3 matrix, int index)
#         {
#             switch (index)
#             {
#                 case 0:
#                     return matrix.__AxisX().__Unit();
#                 case 1:
#                     return matrix.__AxisY().__Unit();
#                 case 2:
#                     return matrix.__AxisZ().__Unit();
#                 default:
#                     throw new ArgumentOutOfRangeException(nameof(index), $"index == {index}");
#             }
#         }

#         public static Matrix3x3 __Mirror(this Matrix3x3 matrix, Surface.Plane plane)
#         {
#             Vector3d newY = matrix.__AxisX().__Mirror(plane);
#             Vector3d newX = matrix.__AxisY().__Mirror(plane);
#             return newX.__ToMatrix3x3(newY);
#         }

#         [Obsolete(nameof(NotImplementedException))]
#         public static Matrix3x3 __Mirror(
#             this Matrix3x3 vector,
#             Surface.Plane plane,
#             Component from,
#             Component to)
#         {
#             throw new NotImplementedException();
#         }


#         public static Matrix3x3 __Copy(this Matrix3x3 matrix)
#         {
#             double[] mtxDst = new double[9];
#             ufsession_.Mtx3.Copy(matrix.__Array(), mtxDst);
#             return mtxDst.__ToMatrix3x3();
#         }

#         public static double[,] __ToTwoDimArray(this Matrix3x3 matrix)
#         {
#             return new[,]
#             {
#                 { matrix.Xx, matrix.Xy, matrix.Xz },
#                 { matrix.Yx, matrix.Yy, matrix.Yz },
#                 { matrix.Zx, matrix.Zy, matrix.Zz }
#             };
#         }

#         public static double __Determinant(this Matrix3x3 matrix)
#         {
#             ufsession_.Mtx3.Determinant(matrix.__Array(), out double determinant);
#             return determinant;
#         }

#         public static Matrix3x3 __MapAcsToWcs(this Matrix3x3 orientation)
#         {
#             var axisx = orientation.__AxisX().__MapAcsToWcs();
#             var axisy = orientation.__AxisY().__MapAcsToWcs();
#             return axisx.__ToMatrix3x3(axisy);
#         }

#         public static Matrix3x3 __MapWcsToAcs(this Matrix3x3 orientation)
#         {
#             var axisx = orientation.__AxisX().__MapWcsToAcs();
#             var axisy = orientation.__AxisY().__MapWcsToAcs();
#             return axisx.__ToMatrix3x3(axisy);
#         }

#         #endregion

#   #region Masks

#   public static Selection.MaskTriple[] Mask = new Selection.MaskTriple[5];

#   public static Selection.MaskTriple ComponentType =
#       new Selection.MaskTriple(UF_component_type, 0, 0);

#   public static Selection.MaskTriple EdgeType =
#       new Selection.MaskTriple(UF_solid_type, 0, UF_UI_SEL_FEATURE_ANY_EDGE);

#   public static Selection.MaskTriple BodyType =
#       new Selection.MaskTriple(UF_solid_type, 0, UF_UI_SEL_FEATURE_BODY);

#   public static Selection.MaskTriple SolidBodyType =
#       new Selection.MaskTriple(UF_solid_type, 0, UF_UI_SEL_FEATURE_SHEET_BODY);

#   public static Selection.MaskTriple PointType = new Selection.MaskTriple(UF_caegeom_type, 0, 0);
#   public static Selection.MaskTriple PlaneType = new Selection.MaskTriple(UF_plane_type, 0, 0);

#   public static Selection.MaskTriple DatumPlaneType =
#       new Selection.MaskTriple(UF_datum_plane_type, 0, 0);

#   public static Selection.MaskTriple DatumCsysType =
#       new Selection.MaskTriple(UF_csys_normal_subtype, 0, UF_csys_wcs_subtype);

#   public static Selection.MaskTriple SplineType = new Selection.MaskTriple(UF_spline_type, 0, 0);

#   public static Selection.MaskTriple HandlePointYpe =
#       new Selection.MaskTriple(UF_point_type, UF_point_subtype, 0);

#   public static Selection.MaskTriple ObjectType =
#       new Selection.MaskTriple(UF_solid_type, UF_solid_body_subtype, 0);

#   public static Selection.MaskTriple FaceType =
#       new Selection.MaskTriple(UF_face_type, UF_bounded_plane_type, 0);

#   public static Selection.MaskTriple FeatureType =
#       new Selection.MaskTriple(UF_feature_type, UF_feature_subtype, 0);

#   public static Selection.MaskTriple ObjColorType =
#       new Selection.MaskTriple(UF_solid_type, UF_face_type, UF_UI_SEL_FEATURE_ANY_FACE);

#   /// <summary>
#   ///     Returns the mask for an NXOpen.Assemblies.Component.
#   /// </summary>
#   public static UFUi.Mask ComponentMask =>
#       //[IgnoreExtensionAspect]
#       new UFUi.Mask
#       {
#           object_type = UF_component_type,
#           object_subtype = 0,
#           solid_type = 0
#       };

#   public static UFUi.Mask BodyMask
#   {
#       //[IgnoreExtensionAspect]
#       get
#       {
#           UFUi.Mask mask1 = new UFUi.Mask
#               { object_type = 70, object_subtype = 0, solid_type = 0 };
#           return mask1;
#       }
#   }

#   #endregion


#   #region Int

#   public static string __PadInt(this int integer, int padLength)
#   {
#       if (integer < 0)
#           throw new ArgumentOutOfRangeException(nameof(integer), @"You cannot pad a negative integer.");

#       if (padLength < 1)
#           throw new ArgumentOutOfRangeException(nameof(padLength),
#               @"You cannot have a pad length of less than 1.");

#       string integerString = $"{integer}";

#       int counter = 0;

#       while (integerString.Length < padLength)
#       {
#           integerString = $"0{integerString}";

#           if (counter++ > 100)
#               throw new TimeoutException(nameof(__PadInt));
#       }

#       return integerString;
#   }


def math_pow(number: float, power: float) -> float:
    #       return System.Math.Pow(number, power);
    raise NotImplementedError()


#   #endregion


#           #region ICurve

#         public static double __Parameter(this ICurve icurve, Point3d point)
#         {
#             switch (icurve)
#             {
#                 case Curve __curve__:
#                     return __curve__.__Parameter(point);
#                 case Edge __edge__:
# #pragma warning disable CS0612 // Type or member is obsolete
#                     return __edge__.__Parameter(point);
# #pragma warning restore CS0612 // Type or member is obsolete
#                 default:
#                     throw new ArgumentException("Unknown curve type");
#             }
#         }

#         [Obsolete(nameof(NotImplementedException))]
#         public static Point3d __StartPoint(this ICurve icurve)
#         {
#             throw new NotImplementedException();
#         }

#         [Obsolete(nameof(NotImplementedException))]
#         public static Point3d __EndPoint(this ICurve icurve)
#         {
#             throw new NotImplementedException();
#         }

#         //
#         // Summary:
#         //     Calculates the unit binormal at a given parameter value
#         //
#         // Parameters:
#         //   value:
#         //     Parameter value
#         //
#         // Returns:
#         //     Unit binormal
#         //
#         // Remarks:
#         //     The binormal is normal to the "osculating plane" of the curve at the given parameter
#         //     value (the plane that most closely matches the curve). So, if the curve is planar,
#         //     the binormal is normal to the plane of the curve.
#         //
#         //     The binormal is the cross product of the tangent and the normal: B = Cross(T,N).
#         public static Vector3d __Binormal(this ICurve curve, double value)
#         {
#             UFEval eval = ufsession_.Eval;
#             eval.Initialize2(curve.__Tag(), out IntPtr evaluator);
#             double[] array = new double[3];
#             double[] array2 = new double[3];
#             double[] array3 = new double[3];
#             double[] array4 = new double[3];
#             value /= Factor;
#             eval.EvaluateUnitVectors(evaluator, value, array, array2, array3, array4);
#             eval.Free(evaluator);
#             return array4.__ToVector3d();
#         }

#         public static Tag __Tag(this ICurve curve)
#         {
#             if (curve is TaggedObject taggedObject)
#                 return taggedObject.Tag;

#             throw new ArgumentException("Curve was not a tagged object");
#         }

#         public static bool __IsCurve(this ICurve icurve)
#         {
#             return icurve is Curve;
#         }

#         public static bool __IsEdge(this ICurve icurve)
#         {
#             return icurve is Edge;
#         }

#         [Obsolete]
#         public static void __IsLinearCurve(this ICurve icurve)
#         {
#             //if (icurve.ObjectType == ObjectTypes.Type.Line)
#             //{
#             //    throw new ArgumentException("The input curve is a straight line.");
#             //}

#             //if (icurve.ObjectType == ObjectTypes.Type.Edge && icurve.ObjectSubType == ObjectTypes.SubType.EdgeLine)
#             //{
#             //    throw new ArgumentException("The input curve is a straight line.");
#             //}
#             throw new NotImplementedException();
#         }

#         public static void __IsPlanar(this ICurve icurve)
#         {
#             double[] data = new double[6];
#             ufsession_.Modl.AskObjDimensionality(icurve.__Tag(), out int dimensionality, data);

#             if (dimensionality == 3)
#                 throw new ArgumentException("The input curve is not planar.");
#         }

#         [Obsolete]
#         public static void __IsParallelToXYPlane(this ICurve icurve)
#         {
#             //double num = Vector.Angle(icurve.Binormal(icurve.MinU), Vector.AxisZ);
#             //if (num > 1E-06 || num > 179.999999)
#             //{
#             //    throw new ArgumentException("The input curve does not lie in a plane parallel to X-Y plane.");
#             //}
#             throw new NotImplementedException();
#         }


class UFuncAddPierceComponents:
    #     public partial class AddPierceComponents : _UFuncForm
    #     {
    #         private static List<Tuple<Component, Face>> _addedComponents;

    #         public AddPierceComponents()
    #         {
    #             InitializeComponent();
    #         }

    #         internal static string PunchDetail { get; set; }

    #         internal static string ButtonDetail { get; set; }

    #         internal static string RetainerDetail { get; set; }

    #         private void btnSelect_Click(object sender, EventArgs e)
    #         {
    #             try
    #             {
    #                 Hide();

    #                 #region Revision • 1.1 – 2017 / 11 / 28

    #                 string[] controls = session_.Parts.ToArray().Select(part => part.FullPath)
    #                     .Where(s => s.Contains("strip-control")).ToArray();
    #                 switch (controls.Length)
    #                 {
    #                     case 0:
    #                         print("There is no strip control loaded. Please load one before continuing.");
    #                         return;
    #                     case 1:
    #                         break;
    #                     default:
    #                         print("More than one strip control is loaded:");
    #                         controls.ToList().ForEach(print);
    #                         return;
    #                 }

    #                 #endregion

    #                 ButtonDetail = txtButton.Text;
    #                 PunchDetail = txtPunch.Text;
    #                 RetainerDetail = txtRetainer.Text;
    #                 using (session_.__UsingDisplayPartReset())
    #                 {
    #                     if (chkAssembly.Checked)
    #                         SameAssembly(rdoMetric.Checked, chkButton.Checked, chkPunch.Checked, chkRetainer.Checked);
    #                     else
    # #pragma warning disable CS0612 // Type or member is obsolete
    #                         DifferentAssemblies(rdoMetric.Checked, chkButton.Checked, chkPunch.Checked,
    #                             chkRetainer.Checked);
    # #pragma warning restore CS0612 // Type or member is obsolete
    #                 }
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException();
    #             }
    #             finally
    #             {
    #                 Show();
    #             }
    #         }

    #         public static string GetNextDetailNumber(Part snapUspLsp)
    #         {
    #             string detailDirectory = Path.GetDirectoryName(snapUspLsp.FullPath);
    #             string partLeaf = snapUspLsp.Leaf.ToLower();
    #             Regex shortRegex = new Regex("^([0-9]+)-([0-9]{3,})-(lsp|usp)([0-9]{1})$");
    #             Match match = shortRegex.Match(partLeaf);
    #             if (match.Success)
    #             {
    #                 string customerJobNumber = match.Groups[1].Value;
    #                 string partOp = match.Groups[2].Value;
    #                 string uspLsp = match.Groups[3].Value;
    #                 int uspLspOp = int.Parse(match.Groups[4].Value);
    #                 bool isLower = uspLsp == "lsp";
    #                 int detailNumber = isLower
    #                     ? GetLspDetailNumberShort(uspLspOp)
    #                     : GetUspDetailNumberShort(uspLspOp);
    #                 string newDisplayName;
    #                 do
    #                 {
    #                     newDisplayName = $"{customerJobNumber}-{partOp}-{detailNumber++}";

    #                     if (snapUspLsp.ComponentAssembly.RootComponent.GetChildren()
    #                         .Any(component => component.DisplayName == newDisplayName))
    #                         continue;

    #                     string newFullPath = $"{detailDirectory}\\{newDisplayName}.prt";

    #                     if (File.Exists(newFullPath))
    #                         continue;

    #                     if (isLower && detailNumber > 499)
    #                         throw new Exception("Exceeded the detail numbers for the Lower");

    #                     if (detailNumber > 990)
    #                         throw new Exception("Exceeded the detail numbers for the Upper");

    #                     return newFullPath;
    #                 }
    #                 while (true);
    #             }

    #             Regex longRegex = new Regex("^([0-9]{4,5})-([0-9]{3,})-(lsp|usp)([0-9]{3})$");
    #             match = longRegex.Match(partLeaf);
    #             if (!match.Success) throw new ArgumentException("Part is not a valid Usp or Lsp.", nameof(snapUspLsp));
    #             {
    #                 string customerJobNumber = match.Groups[1].Value;
    #                 string partOp = match.Groups[2].Value;
    #                 string uspLsp = match.Groups[3].Value;
    #                 int uspLspOp = int.Parse(match.Groups[4].Value);
    #                 bool isLower = uspLsp == "lsp";
    #                 int detailNumber = isLower
    #                     ? GetLspDetailNumberLong(uspLspOp)
    #                     : GetUspDetailNumberLong(uspLspOp);
    #                 string newDisplayName;
    #                 do
    #                 {
    #                     newDisplayName = $"{customerJobNumber}-{partOp}-{detailNumber++}";

    #                     if (snapUspLsp.ComponentAssembly.RootComponent.GetChildren()
    #                         .Any(component => component.DisplayName == newDisplayName))
    #                         continue;

    #                     string newFullPath = $"{detailDirectory}\\{newDisplayName}.prt";

    #                     if (File.Exists(newFullPath))
    #                         continue;

    #                     if (isLower && detailNumber > 499)
    #                         throw new Exception("Exceeded the detail numbers for the Lower");

    #                     if (detailNumber > 990)
    #                         throw new Exception("Exceeded the detail numbers for the Upper");

    #                     return newFullPath;
    #                 }
    #                 while (true);
    #             }
    #         }

    #         /// <summary>
    #         ///     The path to the "Smart Button Metric.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartButtonMetric => "G:\\0Library\\Button\\Smart Button Metric.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Button English.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartButtonEnglish => "G:\\0Library\\Button\\Smart Button English.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Punch Metric.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartPunchMetric => "G:\\0Library\\PunchPilot\\Metric\\Smart Punch Metric.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Punch English.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartPunchEnglish => "G:\\0Library\\PunchPilot\\English\\Smart Punch English.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Ball Lock Retainer Metric.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartBallLockRetainerMetric =>
    #             "G:\\0Library\\Retainers\\Metric\\Smart Ball Lock Retainer Metric.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Ball Lock Retainer English.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartBallLockRetainerEnglish =>
    #             "G:\\0Library\\Retainers\\English\\Smart Ball Lock Retainer English.prt";

    #         /// <summary>
    #         ///     Returns the name of the reference set to be used for AddPierceComponents.
    #         /// </summary>
    #         public static string SlugRefsetName => "SLUG BUTTON ALIGN";

    #         // ReSharper disable once StringLiteralTypo
    #         public static string RetainerAlignPunchFaceName => "ALIGNPUNCH";

    #         // ReSharper disable once StringLiteralTypo
    #         public static string PunchTopFaceName => "PUNCHTOPFACE";

    #         public static string PiercedP => "PIERCED_P";

    #         public static string PiercedW => "PIERCED_W";

    #         public static string PiercedType => "PIERCED_TYPE";

    #         public static Regex PiercedFaceRegex => new Regex("^PIERCED_([0-9]{1,})$");

    #         public static int GetUspDetailNumberShort(int number)
    #         {
    #             switch (number)
    #             {
    #                 case 1:
    #                     return 600;
    #                 case 2:
    #                     return 700;
    #                 case 3:
    #                     return 800;
    #                 case 4:
    #                     return 900;
    #                 case 5:
    #                     return 650;
    #                 case 6:
    #                     return 750;
    #                 case 7:
    #                     return 850;
    #                 case 8:
    #                     return 950;
    #                 case 9:
    #                     return 675;
    #                 case 10:
    #                     return 775;
    #                 case 11:
    #                     return 875;
    #                 case 12:
    #                     return 975;
    #                 case 13:
    #                     return 680;
    #                 case 14:
    #                     return 780;
    #                 case 15:
    #                     return 880;
    #                 default:
    #                     return 881;
    #             }
    #         }

    #         public static int GetLspDetailNumberShort(int number)
    #         {
    #             switch (number)
    #             {
    #                 case 1:
    #                     return 100;
    #                 case 2:
    #                     return 200;
    #                 case 3:
    #                     return 300;
    #                 case 4:
    #                     return 400;
    #                 case 5:
    #                     return 150;
    #                 case 6:
    #                     return 250;
    #                 case 7:
    #                     return 350;
    #                 case 8:
    #                     return 450;
    #                 case 9:
    #                     return 175;
    #                 case 10:
    #                     return 275;
    #                 case 11:
    #                     return 375;
    #                 case 12:
    #                     return 475;
    #                 case 13:
    #                     return 180;
    #                 case 14:
    #                     return 280;
    #                 case 15:
    #                     return 380;
    #                 default:
    #                     return 381;
    #             }
    #         }

    #         public static int GetUspDetailNumberLong(int number)
    #         {
    #             switch (number)
    #             {
    #                 case 10:
    #                     return 600;
    #                 case 20:
    #                     return 700;
    #                 case 30:
    #                     return 800;
    #                 case 40:
    #                     return 900;
    #                 case 50:
    #                     return 650;
    #                 case 60:
    #                     return 750;
    #                 case 70:
    #                     return 850;
    #                 case 80:
    #                     return 950;
    #                 case 90:
    #                     return 675;
    #                 case 100:
    #                     return 775;
    #                 case 110:
    #                     return 875;
    #                 case 120:
    #                     return 975;
    #                 case 130:
    #                     return 680;
    #                 case 140:
    #                     return 780;
    #                 case 150:
    #                     return 880;
    #                 default:
    #                     return 881;
    #             }
    #         }

    #         public static int GetLspDetailNumberLong(int number)
    #         {
    #             switch (number)
    #             {
    #                 case 10:
    #                     return 100;
    #                 case 20:
    #                     return 200;
    #                 case 30:
    #                     return 300;
    #                 case 40:
    #                     return 400;
    #                 case 50:
    #                     return 150;
    #                 case 60:
    #                     return 250;
    #                 case 70:
    #                     return 350;
    #                 case 80:
    #                     return 450;
    #                 case 90:
    #                     return 175;
    #                 case 100:
    #                     return 275;
    #                 case 110:
    #                     return 375;
    #                 case 120:
    #                     return 475;
    #                 case 130:
    #                     return 180;
    #                 case 140:
    #                     return 280;
    #                 case 150:
    #                     return 380;
    #                 default:
    #                     return 381;
    #             }
    #         }

    #         /// <summary>
    #         ///     Gets the current detail number of all the children of <paramref name="snapComponent" /> who passes the Regex
    #         ///     <see cref="Constants.Regex_Detail" />, or returns -1 if no valid children are found.
    #         /// </summary>
    #         /// <param name="snapComponent">The component.</param>
    #         /// <returns>The highest/current detail or -1 if <paramref name="snapComponent" /> doesn't have any child who are valid.</returns>
    #         public static int GetCurrentDetailNumberOfChildren(Component snapComponent)
    #         {
    #             int[] validDetailNumbers = snapComponent.GetChildren()
    #                 .Select(component => component.DisplayName)
    #                 .Select(s => Regex.Match(s, RegexDetail))
    #                 .Where(match => match.Success)
    #                 .Select(match => int.Parse(match.Groups[3].Value))
    #                 .ToArray();

    #             return validDetailNumbers.Length >= 0
    #                 ? -1
    #                 : validDetailNumbers.Max();
    #         }

    #         /// <summary>
    #         ///     Checks to see if a face is named properly for AddPierceComponents.
    #         /// </summary>
    #         /// <param name="snapFace">The face whose name is to be checked.</param>
    #         /// <remarks>
    #         ///     The integer that is tagged at the end of the face name will be used to find the
    #         ///     <see cref="NXOpen.Features. DatumCsys" /> that
    #         ///     is associated with the face.
    #         /// </remarks>
    #         /// <exception cref="ArgumentNullException">When <paramref name="snapFace" /> is null.</exception>
    #         /// <returns>True if the name of the face starts with "PIERCED_FACE_" followed immediately by a non-negative integer.</returns>
    #         public static bool IsFaceNameValid(Face snapFace)
    #         {
    #             if (snapFace == null) throw new ArgumentNullException(nameof(snapFace));
    #             return PiercedFaceRegex.IsMatch(snapFace.Name);
    #         }

    #         /// <summary>
    #         ///     Gets the integer used to find a <see cref="NXOpen.Features. DatumCsys" />.
    #         /// </summary>
    #         /// <param name="snapFace">The face to parse an integer from it's name.</param>
    #         /// <exception cref="ArgumentNullException">When <paramref name="snapFace" /> is null.</exception>
    #         /// <exception cref="FormatException">If <paramref name="snapFace" />.Name isn't valid.</exception>
    #         /// <returns>Returns integer that corresponds to a <see cref="NXOpen.Features. DatumCsys" />. </returns>
    #         public static int GetFaceNameInteger(Face snapFace)
    #         {
    #             if (snapFace == null) throw new ArgumentNullException(nameof(snapFace));
    #             Match match = PiercedFaceRegex.Match(snapFace.Name);
    #             if (!match.Success) throw new FormatException("\"" + snapFace.Name + "\" is invalid.");
    #             return int.Parse(match.Groups[1].Value);
    #         }

    #         /// <summary>
    #         ///     Creates a new a snapButton and adds it to the current __work_part_.
    #         /// </summary>
    #         /// <remarks>
    #         ///     Adds the snapButton using the <paramref name="csys" /> layer, Origin, and Orientation as parameters for the
    #         ///     added snapButton.
    #         /// </remarks>
    #         /// <param name="buttonUnit">The unit type of the added component.</param>
    #         /// <param name="csys">The csys whose parameters will be used for the added component.</param>
    #         /// <exception cref="ArgumentNullException"><paramref name="csys" /> is null.</exception>
    #         /// <returns>The added snapButton.</returns>
    #         public static Component AddButton(BasePart.Units buttonUnit, CoordinateSystem csys)
    #         {
    #             if (csys == null) throw new ArgumentNullException(nameof(csys));
    #             double multiplier;

    #             string buttonPath;
    #             switch (buttonUnit)
    #             {
    #                 case BasePart.Units.Inches:
    #                     buttonPath = SmartButtonEnglish;
    #                     multiplier = 1.0;
    #                     break;
    #                 case BasePart.Units.Millimeters:
    #                     buttonPath = SmartButtonMetric;
    #                     multiplier = 25.4;
    #                     break;
    #                 default:
    #                     throw new ArgumentOutOfRangeException(nameof(buttonUnit));
    #             }

    #             CartesianCoordinateSystem absCys = __display_part_.__CreateCsys();
    #             CartesianCoordinateSystem tempCsys = __display_part_.__CreateCsys(csys.Origin, csys.Orientation.Element);
    #             Point3d mappedOrigin = csys.Origin.__MapCsysToCsys(absCys, tempCsys);
    #             mappedOrigin = new Point3d(mappedOrigin.X, mappedOrigin.Y, mappedOrigin.Z + 6 / multiplier);
    #             Point3d newOrigin = mappedOrigin.__MapCsysToCsys(tempCsys, absCys);
    #             return __work_part_.ComponentAssembly.AddComponent(buttonPath, "ALIGN",
    #                 Path.GetFileNameWithoutExtension(buttonPath), newOrigin, csys.Orientation.Element, csys.Layer, out _);
    #         }

    #         public static Component AddPunch(BasePart.Units buttonUnit, CoordinateSystem csys)
    #         {
    #             if (csys == null) throw new ArgumentNullException(nameof(csys));
    #             string punchPath;
    #             switch (buttonUnit)
    #             {
    #                 case BasePart.Units.Inches:
    #                     punchPath = SmartPunchEnglish;
    #                     break;
    #                 case BasePart.Units.Millimeters:
    #                     punchPath = SmartPunchMetric;
    #                     break;
    #                 default:
    #                     throw new ArgumentOutOfRangeException(nameof(buttonUnit));
    #             }

    #             return AddComponent(punchPath, csys, "ALIGN");
    #         }

    #         public static Component AddRetainer(BasePart.Units buttonUnit, CoordinateSystem csys)
    #         {
    #             if (csys == null) throw new ArgumentNullException(nameof(csys));
    #             string retainerPath;
    #             switch (buttonUnit)
    #             {
    #                 case BasePart.Units.Inches:
    #                     retainerPath = SmartBallLockRetainerEnglish;
    #                     break;
    #                 case BasePart.Units.Millimeters:
    #                     retainerPath = SmartBallLockRetainerMetric;
    #                     break;
    #                 default:
    #                     throw new ArgumentOutOfRangeException(nameof(buttonUnit));
    #             }

    #             return AddComponent(retainerPath, csys, "MATE");
    #         }

    #         private static Component AddComponent(string path, CoordinateSystem csys, string referenceSet)
    #         {
    #             CartesianCoordinateSystem absCys = __display_part_.__CreateCsys();
    #             CartesianCoordinateSystem tempCsys = __display_part_.__CreateCsys(csys.Origin, csys.Orientation.Element);
    #             Point3d mappedOrigin = csys.Origin.__MapCsysToCsys(absCys, tempCsys);
    #             Point3d newOrigin = mappedOrigin.__MapCsysToCsys(tempCsys, absCys);

    #             return __work_part_.ComponentAssembly.AddComponent(
    #                 path,
    #                 referenceSet,
    #                 Path.GetFileNameWithoutExtension(path),
    #                 newOrigin,
    #                 csys.Orientation.Element,
    #                 csys.Layer,
    #                 out _);
    #         }

    #         private static bool IsUsp(Part snapPart)
    #         {
    #             return snapPart.Leaf.Contains("usp");
    #         }

    #         private static void GetPartPaths(bool isMetric, out string buttonPath, out string retainerPath,
    #             out string punchPath)
    #         {
    #             string directory = Path.GetDirectoryName(__display_part_.FullPath);

    #             var details = (from file in Directory.GetFiles(directory, "*.prt", SearchOption.TopDirectoryOnly)
    #                            where file.__IsDetail()
    #                            let detailNumber = file.__AskDetailNumber()
    #                            select new { file, detailNumber }).ToArray();

    #             if (string.IsNullOrEmpty(ButtonDetail))
    #             {
    #                 buttonPath = isMetric ? SmartButtonMetric : SmartButtonEnglish;
    #             }
    #             else
    #             {
    #                 var argDetail = details.SingleOrDefault(arg => arg.file == ButtonDetail)
    #                                 ??
    #                                 throw new InvalidOperationException("Could not find a detail with # \'" + ButtonDetail +
    #                                                                     "\' in folderWithCtsNumber \'" + directory + "\'.");

    #                 Part tempPart = session_.__FindOrOpen(argDetail.file);

    #                 if (!tempPart.HasUserAttribute("LIBRARY", NXObject.AttributeType.String, -1))
    #                     throw new InvalidOperationException("The selected part does not have a \'LIBRARY\' attribute.");

    #                 string expectedLibraryAttributeValue = Path.GetFileNameWithoutExtension(isMetric
    #                     ? SmartButtonMetric
    #                     : SmartButtonEnglish);
    #                 string libraryAttributeValue =
    #                     tempPart.GetUserAttributeAsString("LIBRARY", NXObject.AttributeType.String, -1);

    #                 if (expectedLibraryAttributeValue != libraryAttributeValue)
    #                     throw new InvalidOperationException(
    #                         $"The library attribute value {tempPart.Leaf} does not equal {expectedLibraryAttributeValue}.");

    #                 buttonPath = tempPart.FullPath;
    #             }

    #             if (string.IsNullOrEmpty(PunchDetail))
    #             {
    #                 punchPath = isMetric ? SmartPunchMetric : SmartPunchEnglish;
    #             }
    #             else
    #             {
    #                 var argDetail = details.SingleOrDefault(arg => arg.file == PunchDetail)
    #                                 ??
    #                                 throw new InvalidOperationException("Could not find a detail with # \'" + PunchDetail +
    #                                                                     "\' in folderWithCtsNumber \'" + directory + "\'.");

    #                 Part tempPart = session_.__FindOrOpen(argDetail.file);

    #                 if (!tempPart.HasUserAttribute("LIBRARY", NXObject.AttributeType.String, -1))
    #                     throw new InvalidOperationException("The selected part does not have a \'LIBRARY\' attribute.");

    #                 string expectedLibraryAttributeValue =
    #                     Path.GetFileNameWithoutExtension(isMetric
    #                         ? SmartPunchMetric
    #                         : SmartPunchEnglish);
    #                 string libraryAttributeValue =
    #                     tempPart.GetUserAttributeAsString("LIBRARY", NXObject.AttributeType.String, -1);

    #                 if (expectedLibraryAttributeValue != libraryAttributeValue)
    #                     throw new InvalidOperationException(
    #                         $"The library attribute value {tempPart.Leaf} does not equal {expectedLibraryAttributeValue}.");

    #                 punchPath = tempPart.FullPath;
    #             }

    #             if (string.IsNullOrEmpty(RetainerDetail))
    #             {
    #                 retainerPath = isMetric
    #                     ? SmartBallLockRetainerMetric
    #                     : SmartBallLockRetainerEnglish;
    #             }
    #             else
    #             {
    #                 var argDetail = details.SingleOrDefault(arg => arg.file == RetainerDetail)
    #                                 ??
    #                                 throw new InvalidOperationException("Could not find a detail with # \'" +
    #                                                                     RetainerDetail + "\' in folderWithCtsNumber \'" +
    #                                                                     directory + "\'.");

    #                 Part tempPart = session_.__FindOrOpen(argDetail.file);

    #                 if (!tempPart.HasUserAttribute("LIBRARY", NXObject.AttributeType.String, -1))
    #                     throw new InvalidOperationException("The selected part does not have a \'LIBRARY\' attribute.");

    #                 string expectedLibraryAttributeValue =
    #                     Path.GetFileNameWithoutExtension(isMetric
    #                         ? SmartBallLockRetainerMetric
    #                         : SmartBallLockRetainerEnglish);
    #                 string libraryAttributeValue =
    #                     tempPart.GetUserAttributeAsString("LIBRARY", NXObject.AttributeType.String, -1);

    #                 if (expectedLibraryAttributeValue != libraryAttributeValue)
    #                     throw new InvalidOperationException(
    #                         $"The library attribute value {tempPart.Leaf} does not equal {expectedLibraryAttributeValue}.");

    #                 retainerPath = tempPart.FullPath;
    #             }
    #         }

    #         private static void ConfirmStripControlAndEExpression()
    #         {
    #             string[] stripControls = session_.Parts
    #                 .OfType<Part>()
    #                 .Select(part => part.Leaf.ToLower())
    #                 .Where(s => s.Contains("strip-control"))
    #                 .ToArray();

    #             if (stripControls.Length < 1)
    #                 throw new InvalidOperationException("You need to have a strip control loaded.");

    #             string[] expressions = __display_part_.Expressions
    #                 .ToArray()
    #                 .Select(expression => expression.Name.ToLower())
    #                 .Where(s => s == "e")
    #                 .ToArray();

    #             if (expressions.Length < 1)
    #                 throw new InvalidOperationException("Unable to find an expression with the name of \'e\'.");
    #         }

    #         public static void SameAssembly(bool isMetric, bool addButton, bool addPunch, bool addRetainer)
    #         {
    #             ConfirmStripControlAndEExpression();
    #             _addedComponents = new List<Tuple<Component, Face>>();
    #             GetPartPaths(isMetric, out string buttonPath, out string retainerPath, out string punchPath);
    #             Regex uspLspRegex = new Regex("^[0-9]{4,5}-([0-9]{3})-[l|u]sp([0-9]{1,})$");
    #             string _display_part_DisplayName = Path.GetFileNameWithoutExtension(__display_part_.FullPath);
    #             if (_display_part_DisplayName == null) throw new NullReferenceException("_display_part_DisplayName");
    #             Match nameMatch = uspLspRegex.Match(_display_part_DisplayName);
    #             if (!nameMatch.Success)
    #                 throw new FormatException(_display_part_DisplayName + " is not a valid usp or lsp.");
    #             GFolder folder = GFolder.create_or_null(__work_part_);
    #             if (folder is null)
    #                 throw new InvalidOperationException("The current displayed part does not reside within a GFolder.");
    #             string op = nameMatch.Groups[1].Value;
    #             int uspLspNumberAsInteger = int.Parse(nameMatch.Groups[2].Value);
    #             Part uspLspPart = session_.__FindOrOpen(_display_part_DisplayName);

    #             /////////////////////////////////////////////
    #             /////////////////////////////////////////////

    #             __SetUndoMark(MarkVisibility.Visible, "FastClass");

    #             try
    #             {
    #                 Face[] faces = Ui.Selection.SelectManyFaces();

    #                 IDictionary<string, List<Face>> dictionaryShape =
    #                     faces.__ToILookIDict(face => face.GetStringUserAttribute("PIERCED_TYPE", -1));

    #                 foreach (string keyShape in dictionaryShape.Keys)
    #                 {
    #                     List<Face> shapeFaces = dictionaryShape[keyShape];
    #                     // Revision • 1.2 – 2017 / 12 / 07
    #                     IDictionary<double, List<Face>> dictionaryP = shapeFaces.__ToILookIDict(face =>
    #                         System.Math.Round(face.GetRealUserAttribute("PIERCED_P", -1), 4));
    #                     foreach (double keyP in dictionaryP.Keys)
    #                     {
    #                         List<Face> pFaces = dictionaryP[keyP];
    #                         // Revision • 1.2 – 2017 / 12 / 07
    #                         IDictionary<double, List<Face>> dictionaryW = pFaces.__ToILookIDict(face =>
    #                             System.Math.Round(face.GetRealUserAttribute("PIERCED_W", -1), 4));
    #                         foreach (double keyW in dictionaryW.Keys)
    #                         {
    #                             string partOfThePath = $"{folder.dir_op(op)}\\{folder.CustomerNumber}-{op}-";
    #                             int currentLowerDetailNumber =
    #                                 GetCurrentDetailNumberOfChildren(uspLspPart.__RootComponent());
    #                             if (currentLowerDetailNumber == -1)
    #                                 // Revision • 1.2 – 2017 / 12 / 07
    #                                 currentLowerDetailNumber = IsUsp(uspLspPart)
    #                                     ? !folder.is_cts_job()
    #                                         ? GetUspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetUspDetailNumberShort(uspLspNumberAsInteger)
    #                                     : !folder.is_cts_job()
    #                                         ? GetLspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetLspDetailNumberShort(uspLspNumberAsInteger);
    #                             string newButtonPath = buttonPath.StartsWith("G:\\0Library")
    #                                 ? GetNewPartPath(partOfThePath, buttonPath, currentLowerDetailNumber)
    #                                 : buttonPath;
    #                             string newRetainerPath = retainerPath.StartsWith("G:\\0Library")
    #                                 ? GetNewPartPath(partOfThePath, retainerPath, currentLowerDetailNumber)
    #                                 : retainerPath;
    #                             string newPunchPath = punchPath.StartsWith("G:\\0Library")
    #                                 ? GetNewPartPath(partOfThePath, punchPath, currentLowerDetailNumber)
    #                                 : punchPath;
    #                             foreach (Face faceW in dictionaryW[keyW])
    #                             {
    #                                 Component button = null, punch = null, retainer = null;
    #                                 Component layoutComponent = faceW.OwningComponent;
    #                                 string originalRefset = layoutComponent.ReferenceSet;
    #                                 layoutComponent.__ReferenceSet(SlugRefsetName);
    #                                 Expression expression = __display_part_.Expressions
    #                                     .ToArray()
    #                                     .SingleOrDefault(tempExpression => tempExpression.Name == "e");
    #                                 int layer = uspLspPart.Leaf.Contains("lsp") ? 1 : 101;

    #                                 if (addPunch)
    #                                     punch = AddComponentAndConstrain(faceW, newPunchPath, uspLspPart, "ALIGN", layer,
    #                                         expression);

    #                                 if (addRetainer)
    #                                     retainer = AddComponentAndConstrain(faceW, newRetainerPath, uspLspPart, "MATE",
    #                                         layer);

    #                                 if (addButton)
    #                                     button = AddComponentAndConstrain(faceW, newButtonPath, uspLspPart, "ALIGN", layer,
    #                                         expression);

    #                                 if (retainer != null && punch != null)
    #                                     ConstrainPunchAndRetainer(punch, retainer);

    #                                 List<Component> listComps = new List<Component>();

    #                                 if (button != null)
    #                                     listComps.Add(button);

    #                                 if (retainer != null)
    #                                     listComps.Add(retainer);

    #                                 if (punch != null)
    #                                     listComps.Add(punch);

    #                                 ChangeRefsets("BODY", listComps.ToArray());
    #                                 layoutComponent.__ReferenceSet(originalRefset);
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #             finally
    #             {
    # #pragma warning disable CS0612 // Type or member is obsolete
    #                 PrintResults(isMetric);
    # #pragma warning restore CS0612 // Type or member is obsolete
    #             }
    #         }

    #         [Obsolete]
    #         public static void DifferentAssemblies(bool isMetric, bool addButton, bool addPunch, bool addRetainer)
    #         {
    #             GFolder folder = GFolder.create_or_null(__work_part_)
    #                              ??
    #                              throw new InvalidOperationException(
    #                                  "The current work part does not reside within a job folder.");

    #             ConfirmStripControlAndEExpression();
    #             _addedComponents = new List<Tuple<Component, Face>>();
    #             GetPartPaths(isMetric, out string buttonPath, out string retainerPath, out string punchPath);

    #             string _display_part_DisplayName = Path.GetFileNameWithoutExtension(__display_part_.FullPath)
    #                                                ??
    #                                                throw new NullReferenceException("_display_part_DisplayName");

    #             Match nameMatch = Regex.Match(_display_part_DisplayName, RegexLspUsp);

    #             if (!nameMatch.Success)
    #                 throw new FormatException($"{_display_part_DisplayName} is not a valid usp or lsp.");

    #             string op = nameMatch.Groups["opNum"].Value;
    #             string uspLspNumberAsString = nameMatch.Groups["extraOpNum"].Value;
    #             int uspLspNumberAsInteger = int.Parse(uspLspNumberAsString);
    #             string lspName = $"{folder.CustomerNumber}-{op}-lsp{uspLspNumberAsString}";
    #             string uspName = $"{folder.CustomerNumber}-{op}-usp{uspLspNumberAsString}";
    #             BasePart lspPart = session_.Parts.ToArray().SingleOrDefault(part => part.FullPath.Contains(lspName));
    #             BasePart uspPart = session_.Parts.ToArray().SingleOrDefault(part => part.FullPath.Contains(uspName));

    #             if (addButton && lspPart == null)
    #                 throw new InvalidOperationException($"Could not find part \"{lspName}\" loaded in your session.");

    #             if ((addPunch || addRetainer) && uspPart == null)
    #                 throw new InvalidOperationException("Could not find part " + "\"" + uspName +
    #                                                     "\" loaded in your session.");

    #             /////////////////////////////////////////////
    #             /////////////////////////////////////////////

    #             __SetUndoMark(MarkVisibility.Visible, "FastClass");
    #             try
    #             {
    #                 Face[] faces = Ui.Selection.SelectManyFaces();

    #                 IDictionary<string, List<Face>> dictionaryShape =
    #                     faces.__ToILookIDict(face => face.GetStringUserAttribute("PIERCED_TYPE", -1));

    #                 foreach (string keyShape in dictionaryShape.Keys)
    #                 {
    #                     List<Face> shapeFaces = dictionaryShape[keyShape];
    #                     // Revision • 1.2 – 2017 / 12 / 01
    #                     IDictionary<double, List<Face>> dictionaryP = shapeFaces.__ToILookIDict(face =>
    #                         System.Math.Round(face.GetRealUserAttribute("PIERCED_P", -1), 4));
    #                     foreach (double keyP in dictionaryP.Keys)
    #                     {
    #                         List<Face> pFaces = dictionaryP[keyP];
    #                         // Revision • 1.2 – 2017 / 12 / 01
    #                         IDictionary<double, List<Face>> dictionaryW = pFaces.__ToILookIDict(face =>
    #                             System.Math.Round(face.GetRealUserAttribute("PIERCED_W", -1), 4));
    #                         foreach (double keyW in dictionaryW.Keys)
    #                         {
    #                             string partOfThePath = $"{folder.dir_op(op)}\\{folder.CustomerNumber}-{op}-";
    #                             string newPunchPath = null, newRetainerPath = null, newButtonPath = null;
    #                             if (lspPart != null)
    #                             {
    #                                 int currentLowerDetailNumber =
    #                                     GetCurrentDetailNumberOfChildren(lspPart.ComponentAssembly.RootComponent);
    #                                 if (currentLowerDetailNumber == -1)
    #                                     // Revision • 1.2 – 2017 / 12 / 07
    #                                     currentLowerDetailNumber = !folder.is_cts_job()
    #                                         ? GetLspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetLspDetailNumberShort(uspLspNumberAsInteger);
    #                                 newButtonPath = buttonPath.StartsWith("G:\\0Library")
    #                                     ? GetNewPartPath(partOfThePath, buttonPath, currentLowerDetailNumber)
    #                                     : buttonPath;
    #                             }

    #                             if (uspPart != null)
    #                             {
    #                                 int currentUpperDetailNumber =
    #                                     GetCurrentDetailNumberOfChildren(uspPart.ComponentAssembly.RootComponent);
    #                                 if (currentUpperDetailNumber == -1)
    #                                     // Revision • 1.2 – 2017 / 12 / 07
    #                                     currentUpperDetailNumber = !folder.is_cts_job()
    #                                         ? GetUspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetUspDetailNumberShort(uspLspNumberAsInteger);

    #                                 newRetainerPath = retainerPath.StartsWith("G:\\0Library")
    #                                     ? GetNewPartPath(partOfThePath, retainerPath, currentUpperDetailNumber)
    #                                     : retainerPath;
    #                                 currentUpperDetailNumber =
    #                                     GetCurrentDetailNumberOfChildren(uspPart.ComponentAssembly.RootComponent);
    #                                 if (currentUpperDetailNumber == -1)
    #                                     // Revision • 1.2 – 2017 / 12 / 07
    #                                     currentUpperDetailNumber = !folder.is_cts_job()
    #                                         ? GetUspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetUspDetailNumberShort(uspLspNumberAsInteger);
    #                                 newPunchPath = punchPath.StartsWith("G:\\0Library")
    #                                     ? GetNewPartPath(partOfThePath, punchPath, currentUpperDetailNumber)
    #                                     : punchPath;
    #                             }

    #                             foreach (Face faceW in dictionaryW[keyW])
    #                             {
    #                                 Component button = null, punch = null, retainer = null;
    #                                 Component layoutComponent = faceW.OwningComponent;
    #                                 string originalRefset = layoutComponent.ReferenceSet;
    #                                 layoutComponent.__ReferenceSet(SlugRefsetName);
    #                                 Expression expression = __display_part_.Expressions
    #                                     .ToArray()
    #                                     .SingleOrDefault(tempExpression => tempExpression.Name == "e");

    #                                 if (addPunch)
    #                                     punch = AddComponentAndConstrain(faceW, newPunchPath, (Part)uspPart, "ALIGN", 101,
    #                                         expression);

    #                                 // Revision • 1.3 – 2017 / 12 / 28
    #                                 if (addRetainer)
    #                                     retainer = AddComponentAndConstrain(faceW, newRetainerPath, (Part)uspPart, "MATE",
    #                                         101);

    #                                 // Revision • 1.3 – 2017 / 12 / 28
    #                                 if (addButton)
    #                                     button = AddComponentAndConstrain(faceW, newButtonPath, (Part)lspPart, "ALIGN", 1,
    #                                         expression);

    #                                 if (retainer != null && punch != null)
    #                                     ConstrainPunchAndRetainer(punch, retainer);

    #                                 List<Component> listComps = new List<Component>();

    #                                 if (button != null)
    #                                     listComps.Add(button);

    #                                 if (retainer != null)
    #                                     listComps.Add(retainer);

    #                                 if (punch != null)
    #                                     listComps.Add(punch);

    #                                 ChangeRefsets("BODY", listComps.ToArray());
    #                                 layoutComponent.__ReferenceSet(originalRefset);
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #             finally
    #             {
    #                 PrintResults(isMetric);
    #             }
    #         }

    #         [Obsolete]
    #         private static void PrintResults(bool isMetric)
    #         {
    #             throw new NotImplementedException();
    #             //try
    #             //{
    #             //    print_("Results:");
    #             //    BasePart stripControl = session_.Parts.ToArray().Single(part => part.Leaf.Contains("strip-control"));
    #             //    Expression materialThicknessExp = stripControl.Expressions.ToArray()
    #             //        .SingleOrDefault(expression => expression.Name == "M");
    #             //    if (materialThicknessExp == null)
    #             //        print_("Unable to find Material Thickness.");
    #             //    else
    #             //        print_("Material Thickness (M): " + materialThicknessExp.RightHandSide);

    #             //    if (_addedComponents == null)
    #             //    {
    #             //        print_("  addedComponents was null");
    #             //        return;
    #             //    }

    #             //    if (_addedComponents.Count <= 0)
    #             //    {
    #             //        print_("  addedComponents was empty");
    #             //        return;
    #             //    }

    #             //    IOrderedEnumerable<Tuple<Component, Face>> trimmedTuples = _addedComponents
    #             //        .DistinctBy(tup => tup.Item1.DisplayName)
    #             //        .OrderBy(tuple => tuple, new Comparer());

    #             //    double divider = isMetric ? 1.0 : 25.4;

    #             //    foreach (Tuple<NXOpen.Assemblies.Component, NXOpen.Face> tuple in trimmedTuples)
    #             //    {
    #             //        const string circle = "Circle";
    #             //        const string roundedRectangle = "RoundedRectangle";
    #             //        double p = Math.Round(tuple.Item1.GetRealUserAttribute(PiercedP, -1) / divider, 4);
    #             //        double w = Math.Round(tuple.Item1.GetRealUserAttribute(PiercedW, -1) / divider, 4);
    #             //        string type = tuple.Item1.GetStringUserAttribute(PiercedType, -1);
    #             //        switch (type)
    #             //        {
    #             //            case circle:
    #             //                print_($"{tuple.Item1.DisplayName}, P = {p}");
    #             //                break;
    #             //            case roundedRectangle:
    #             //                double radius = tuple.Item2.GetEdges().Select(edge => Snap.NX.Edge.Wrap(edge.Tag)).OfType<Snap.NX.Edge.Arc>().First().Geometry.Radius;
    #             //                print_($"{tuple.Item1.DisplayName}, P = {p}, W = {w}, R = {radius}");
    #             //                break;
    #             //            default:
    #             //                print_($"{tuple.Item1.DisplayName}, P = {p}, W = {w}");
    #             //                break;
    #             //        }
    #             //    }
    #             //    throw new NotImplementedException();
    #             //}
    #             //catch (Exception ex)
    #             //{
    #             //    ex.__PrintException();
    #             //}
    #         }

    #         private static void ConstrainPunchAndRetainer(Component punch, Component retainer)
    #         {
    #             __display_part_ = (Part)punch.OwningComponent.Prototype;
    #             __work_part_ = __display_part_;
    #             Constraints.ConstrainFixPunch(punch);
    #             Constraints.ConstrainZAxes(__work_part_, punch, retainer);
    #             Constraints.ConstrainFaces(__work_part_, punch, retainer);
    #             Constraints.ConstrainAlignBallSetAndPlane(punch, retainer);
    #         }

    #         private static void ChangeRefsets(string refsetName, params Component[] components)
    #         {
    #             components?.Where(component => component != null).ToList()
    #                 .ForEach(component => component.__ReferenceSet(refsetName));
    #         }

    #         private static string GetNewPartPath(string partOfThePath, string originalPartPath,
    #             int currentUpperDetailNumber)
    #         {
    #             string newPath = "";
    #             for (int i = 0; i < 1000; i++)
    #             {
    #                 newPath = partOfThePath + (currentUpperDetailNumber + i) + ".prt";
    #                 if (File.Exists(newPath)) continue;
    #                 File.Copy(originalPartPath, newPath);
    #                 break;
    #             }

    #             return newPath;
    #         }

    #         public static Component AddComponentAndConstrain(
    #             Face snapFace,
    #             string path,
    #             Part part,
    #             string referenceSet,
    #             int layer,
    #             Expression zOffsetExpression = null)
    #         {
    #             __display_part_ = part;
    #             __work_part_ = __display_part_;
    #             snapFace.Unhighlight();
    #             int integer = GetFaceNameInteger(snapFace);

    #             // Revision • 1.2 – 2017 / 12 / 07
    #             Component layout = snapFace.OwningComponent;
    #             DatumAxis xAxis = layout.__Members().OfType<DatumAxis>()
    #                 .Single(axis => axis.Name == "PIERCED_AXIS_X_" + integer);
    #             DatumAxis yAxis = layout.__Members().OfType<DatumAxis>()
    #                 .Single(axis => axis.Name == "PIERCED_AXIS_Y_" + integer);
    #             DatumAxis zAxis = layout.__Members().OfType<DatumAxis>()
    #                 .Single(axis => axis.Name == "PIERCED_AXIS_Z_" + integer);
    #             Matrix3x3 orientation = xAxis.Direction.__ToMatrix3x3(yAxis.Direction);
    #             Point3d newOrigin = xAxis.Origin;
    #             if (zOffsetExpression != null)
    #                 newOrigin = new Point3d(xAxis.Origin.X, xAxis.Origin.Y, xAxis.Origin.Z + zOffsetExpression.Value);

    #             Component addedComponent = part.ComponentAssembly.AddComponent(
    #                 path,
    #                 referenceSet,
    #                 Path.GetFileNameWithoutExtension(path),
    #                 newOrigin,
    #                 orientation,
    #                 layer,
    #                 out _);

    #             addedComponent.SetUserAttribute(PiercedP, -1,
    #                 snapFace.GetStringUserAttribute(PiercedP, -1), NXOpen.Update.Option.Now);

    #             addedComponent.SetUserAttribute(PiercedW, -1,
    #                 snapFace.GetStringUserAttribute(PiercedW, -1), NXOpen.Update.Option.Now);

    #             addedComponent.SetUserAttribute(PiercedType, -1,
    #                 snapFace.GetStringUserAttribute(PiercedType, -1), NXOpen.Update.Option.Now);

    #             addedComponent.__ReferenceSet(referenceSet);

    #             using (new ReferenceSetReset(addedComponent))
    #             {
    #                 addedComponent.__ReferenceSet("BODY");
    #                 Part owningPart = addedComponent.OwningComponent.__Prototype();
    #                 ReferenceSet bodyReferenceSet = owningPart.__FindReferenceSetOrNull("BODY");
    #                 bodyReferenceSet?.AddObjectsToReferenceSet(new NXObject[] { addedComponent });
    #             }

    #             DatumAxis zAxisComponent = addedComponent.__Members()
    #                 .OfType<DatumAxis>()
    #                 .Single(axis => axis.Direction.__IsEqual(__Vector3dZ()));

    #             DisplayedConstraint constraint = Constraints.CreateAlign(__work_part_, zAxisComponent, zAxis);
    #             session_.__DeleteObjects(constraint);

    #             if (!addedComponent.GetStringUserAttribute("LIBRARY", -1).ToLower().Contains("retainer"))
    #                 _addedComponents.Add(new Tuple<Component, Face>(addedComponent, snapFace));

    #             return addedComponent;
    #         }

    #         [Obsolete]
    #         public static class Selection
    #         {
    #             // ReSharper disable once ReturnTypeCanBeEnumerable.Global
    #             [Obsolete]
    #             public static Face[] SelectFaces()
    #             {
    #                 //const string message = "Select Faces";
    #                 //const int scope = UFConstants.UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY;
    #                 //UFUi.SelInitFnT initialProcess = InitialProcess;
    #                 //IntPtr userData = IntPtr.Zero;
    #                 //Tag[] objects = null;
    #                 //try
    #                 //{
    #                 //    TheUFSession.Ui.LockUgAccess(UFConstants.UF_UI_FROM_CUSTOM);
    #                 //    TheUFSession.Ui.SelectWithClassDialog(message, message, scope, initialProcess, userData, out _,
    #                 //        out _, out objects);
    #                 //}
    #                 //catch (Exception ex)
    #                 //{
    #                 //    ex.__PrintException();
    #                 //}
    #                 //finally
    #                 //{
    #                 //    TheUFSession.Ui.UnlockUgAccess(UFConstants.UF_UI_FROM_CUSTOM);
    #                 //}

    #                 //return objects == null || objects.Length == 0 ? new NXOpen.Face[0] : objects.Select(tag => Snap.NX.Face.Wrap(tag).NXOpenFace).ToArray();

    #                 throw new NotImplementedException();
    #             }

    #             private static int InitialProcess(IntPtr select, IntPtr userData)
    #             {
    #                 UFUi.Mask mask = new UFUi.Mask
    #                 {
    #                     object_type = UFConstants.UF_face_type,
    #                     object_subtype = 0,
    #                     solid_type = 0
    #                 };
    #                 ufsession_.Ui.SetSelMask(select, UFUi.SelMaskAction.SelMaskClearAndEnableSpecific, 1, new[] { mask });
    #                 ufsession_.Ui.SetSelProcs(select, FilterProcess, null /* SelectionCallback*/, userData);
    #                 return UFConstants.UF_UI_SEL_SUCCESS;
    #             }

    #             private static int FilterProcess(Tag _object, int[] type, IntPtr userData, IntPtr select)
    #             {
    #                 var snapFace = _object.__To<Face>();

    #                 if (!snapFace.Name.StartsWith("PIERCED_"))
    #                     return NXOpen.UF.UFConstants.UF_UI_SEL_REJECT;

    #                 if (!snapFace.IsOccurrence)
    #                     return NXOpen.UF.UFConstants.UF_UI_SEL_REJECT;

    #                 if (!snapFace.__IsPlanar())
    #                     return NXOpen.UF.UFConstants.UF_UI_SEL_REJECT;

    #                 return snapFace.__NormalVector().__IsEqual(__Vector3dZ().__Negate())
    #                     ? NXOpen.UF.UFConstants.UF_UI_SEL_REJECT
    #                     : NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT;
    #             }
    #         }

    #         private class Comparer : IComparer<Tuple<Component, Face>>
    #         {
    #             #region Implementation of IComparer<in Tuple<Component,Face>>

    #             public int Compare(Tuple<Component, Face> x, Tuple<Component, Face> y)
    #             {
    #                 if (x == null) throw new ArgumentNullException(nameof(x));
    #                 if (y == null) throw new ArgumentNullException(nameof(y));
    #                 return string.Compare(x.Item1.DisplayName, y.Item1.DisplayName, StringComparison.Ordinal);
    #             }

    #             #endregion
    #         }

    #         public static class Constraints
    #         {
    #             /// <summary>
    #             ///     The path to the "Smart Button Metric.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartButtonMetric => "G:\\0Library\\Button\\Smart Button Metric.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Button English.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartButtonEnglish => "G:\\0Library\\Button\\Smart Button English.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Punch Metric.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartPunchMetric => "G:\\0Library\\PunchPilot\\Metric\\Smart Punch Metric.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Punch English.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartPunchEnglish => "G:\\0Library\\PunchPilot\\English\\Smart Punch English.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Ball Lock Retainer Metric.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartBallLockRetainerMetric =>
    #                 "G:\\0Library\\Retainers\\Metric\\Smart Ball Lock Retainer Metric.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Ball Lock Retainer English.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartBallLockRetainerEnglish =>
    #                 "G:\\0Library\\Retainers\\English\\Smart Ball Lock Retainer English.prt";

    #             /// <summary>
    #             ///     Returns the name of the reference set to be used for AddPierceComponents.
    #             /// </summary>
    #             public static string SlugRefsetName => "SLUG BUTTON ALIGN";

    #             // ReSharper disable once StringLiteralTypo
    #             public static string RetainerAlignPunchFaceName => "ALIGNPUNCH";

    #             // ReSharper disable once StringLiteralTypo
    #             public static string PunchTopFaceName => "PUNCHTOPFACE";

    #             // ReSharper disable once InconsistentNaming
    #             public static string Pierced_P => "PIERCED_P";

    #             // ReSharper disable once InconsistentNaming
    #             public static string Pierced_W => "PIERCED_W";

    #             // ReSharper disable once InconsistentNaming
    #             public static string Pierced_Type => "PIERCED_TYPE";

    #             public static Regex PiercedFaceRegex => new Regex("^PIERCED_([0-9]{1,})$");

    #             public static DisplayedConstraint CreateAlign(
    #                 Part part,
    #                 NXObject movableObject,
    #                 NXObject nonMovableObject)
    #             {
    #                 return CreateTouchAlignImpl(part, Constraint.Alignment.CoAlign, movableObject, nonMovableObject);
    #             }

    #             public static void ConstrainZAxes(Part part, Component punch, Component retainer)
    #             {
    #                 punch.__ReferenceSet("ALIGN");
    #                 retainer.__ReferenceSet("MATE");
    #                 DatumAxis retainerZAxis = (DatumAxis)retainer.__Members().Single(o => o.Name == "ZAXIS");
    #                 CartesianCoordinateSystem punchCartesian = punch.__Members().OfType<CartesianCoordinateSystem>().Single();
    #                 var punchOrientation = punchCartesian.Orientation.Element;

    #                 DatumAxis punchZAxis = punch.__Members()
    #                     .OfType<DatumAxis>()
    #                     .Single(axis => new Vector3d(axis.Direction.X, axis.Direction.Y, axis.Direction.Z)
    #                         .__IsEqual(punchOrientation.__AxisZ()));

    #                 DisplayedConstraint constraint = CreateAlign(part, retainerZAxis, punchZAxis);
    #                 constraint.__Layer(254);
    #             }

    #             public static DisplayedConstraint CreateTouchAlignImpl(
    #                 Part part,
    #                 Constraint.Alignment alignmentType,
    #                 NXObject movableObject, NXObject nonMovableObject)
    #             {
    #                 ComponentAssembly componentAssembly = part.ComponentAssembly;
    #                 ComponentPositioner positioner = componentAssembly.Positioner;
    #                 positioner.ClearNetwork();
    #                 positioner.PrimaryArrangement = componentAssembly.Arrangements.FindObject("Arrangement 1");
    #                 positioner.BeginAssemblyConstraints();
    #                 ComponentNetwork componentNetwork = (ComponentNetwork)positioner.EstablishNetwork();
    #                 componentNetwork.MoveObjectsState = true;
    #                 componentNetwork.NetworkArrangementsMode = ComponentNetwork.ArrangementsMode.Existing;
    #                 ComponentConstraint constraint = (ComponentConstraint)positioner.CreateConstraint(true);
    #                 constraint.ConstraintAlignment = alignmentType;
    #                 constraint.ConstraintType = Constraint.Type.Touch;
    #                 constraint.CreateConstraintReference(movableObject.OwningComponent, movableObject, false, false, false);
    #                 constraint.CreateConstraintReference(nonMovableObject.OwningComponent, nonMovableObject, false, false,
    #                     false);
    #                 componentNetwork.Solve();
    #                 positioner.ClearNetwork();
    #                 session_.__DeleteObjects(componentNetwork);
    #                 positioner.EndAssemblyConstraints();
    #                 return constraint.GetDisplayedConstraint();
    #             }

    #             public static DisplayedConstraint CreateTouch(Part part, NXObject movableObject, NXObject nonMovableObject)
    #             {
    #                 return CreateTouchAlignImpl(part, Constraint.Alignment.ContraAlign, movableObject, nonMovableObject);
    #             }

    #             public static void ConstrainFaces(Part part, Component punch, Component retainer)
    #             {
    #                 punch.__ReferenceSet("ALIGN");
    #                 retainer.__ReferenceSet("MATE");

    #                 Face punchFace = punch.__Members()
    #                     .OfType<Face>()
    #                     .Single(face => face.Name == PunchTopFaceName);

    #                 Face retainerFace = retainer.__Members()
    #                     .OfType<Face>()
    #                     .Single(face => face.Name == RetainerAlignPunchFaceName);

    #                 DisplayedConstraint constraint = CreateTouch(part, retainerFace, punchFace);
    #                 constraint.__Layer(254);
    #             }

    #             public static DisplayedConstraint CreateParallelConstraint(NXObject movableObject, NXObject geometry)
    #             {
    #                 ComponentPositioner positioner = _WorkPart.ComponentAssembly.Positioner;
    #                 positioner.ClearNetwork();
    #                 positioner.PrimaryArrangement = _WorkPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1");
    #                 positioner.BeginAssemblyConstraints();
    #                 ComponentNetwork componentNetwork = (ComponentNetwork)positioner.EstablishNetwork();
    #                 componentNetwork.MoveObjectsState = true;
    #                 componentNetwork.NetworkArrangementsMode = 0;
    #                 Constraint constraint = positioner.CreateConstraint(true);
    #                 ComponentConstraint componentConstraint = (ComponentConstraint)constraint;
    #                 componentConstraint.ConstraintType = (Constraint.Type)5;
    #                 componentConstraint.CreateConstraintReference(movableObject.OwningComponent, movableObject, false, false, false);
    #                 componentConstraint.CreateConstraintReference(geometry.OwningComponent, geometry, false, false, false);
    #                 componentNetwork.Solve();
    #                 positioner.ClearNetwork();
    #                 componentNetwork.__Delete();
    #                 positioner.DeleteNonPersistentConstraints();
    #                 positioner.EndAssemblyConstraints();
    #                 return constraint.GetDisplayedConstraint();
    #                 throw new NotImplementedException();
    #             }

    #             public static void ConstrainAlignBallSetAndPlane(Component punch, Component retainer)
    #             {
    #                 punch.__ReferenceSet("MATE");
    #                 retainer.__ReferenceSet("MATE");
    #                 DatumPlane retainerXZPlane = (DatumPlane)retainer.__Members().Single(o => o.Name == "XZPLANE");
    #                 DatumPlane punchBallSeatPlane = (DatumPlane)punch.__Members().Single(o => o.Name == "BALL_SEAT_ANGLE");
    #                 DisplayedConstraint constraint = CreateParallelConstraint(retainerXZPlane, punchBallSeatPlane);
    #                 constraint.__Layer(254);
    #             }

    #             public static void ConstrainFixPunch(Component punch)
    #             {
    #                 DisplayedConstraint constraint = CreateFixedConstraint(punch);
    #                 constraint.__Layer(254);
    #             }

    #             public static DisplayedConstraint CreateFixedConstraint(Component component)
    #             {
    #                 ComponentPositioner positioner = __work_part_.ComponentAssembly.Positioner;
    #                 positioner.ClearNetwork();
    #                 positioner.PrimaryArrangement = __work_part_.ComponentAssembly.Arrangements.FindObject("Arrangement 1");
    #                 positioner.BeginAssemblyConstraints();
    #                 ComponentConstraint constraint = (ComponentConstraint)positioner.CreateConstraint(true);
    #                 constraint.ConstraintType = (Constraint.Type)3;
    #                 constraint.CreateConstraintReference(component, component, false, false, false);
    #                 positioner.EndAssemblyConstraints();
    #                 return constraint.GetDisplayedConstraint();
    #             }
    #         }

    #         #region Obsolete Methods, look before you delete.

    #         public static DatumAxis GetZAxisOccurenceOfSlug(Face face)
    #         {
    #             int integer = GetFaceNameInteger(face);
    #             return face.OwningComponent.__Members()
    #                 .OfType<DatumAxis>()
    #                 .Single(plane => plane.Name == "PIERCED_AXIS_Z_" + integer);
    #         }

    #         public static DatumPlane GetYZPlaneOccurenceOfSlug(Face face)
    #         {
    #             int integer = GetFaceNameInteger(face);
    #             return face.OwningComponent.__Members()
    #                 .OfType<DatumPlane>()
    #                 .Single(plane => plane.Name == "PIERCED_PLANE_YZ_" + integer);
    #         }

    #         [Obsolete(nameof(NotImplementedException))]
    #         public static DatumAxis GetZAxisOccurence(Component snapButton)
    #         {
    #             //NXOpen.CoordinateSystem tempCsys = snapButton.__Members().OfType<NXOpen.CoordinateSystem>().Single();
    #             //IEnumerable<NXOpen.DatumAxis> DatumAxis = snapButton.__Members()
    #             //    .OfType<NXOpen.DatumAxis>();
    #             //foreach (NXOpen.DatumAxis axis in DatumAxis)
    #             //    if (((NXOpen.Assemblies.Component)(tempCsys.Tag)).orientation.z_vec._IsEqualTo(axis.Direction))
    #             //        return axis;
    #             //throw new ArgumentException("End Exception");
    #             throw new NotImplementedException();
    #         }

    #         [Obsolete(nameof(NotImplementedException))]
    #         public static DatumPlane GetYZPlaneOccurence(Component snapButton)
    #         {
    #             //NXOpen.CoordinateSystem tempCsys = snapButton.__Members().OfType<NXOpen.CoordinateSystem>().Single();
    #             //IEnumerable<NXOpen.DatumPlane> planes = snapButton.__Members()
    #             //    .OfType<NXOpen.DatumPlane>();
    #             //foreach (NXOpen.DatumPlane plane in planes)
    #             //    if (((NXOpen.Assemblies.Component)(tempCsys.Tag)).orientation.z_vec._IsEqualTo(plane.Normal))
    #             //        return plane;

    #             //throw new ArgumentException("End Exception");
    #             throw new NotImplementedException();
    #         }

    #         public static Face GetTopFaceOfPunch(Component snapPunch)
    #         {
    #             // ReSharper disable once StringLiteralTypo
    #             return snapPunch.__Members().OfType<Face>().Single(face => face.Name == "PUNCHTOPFACE");
    #         }

    #         public static Face GetAlignFaceOfRetainer(Component snapPunch)
    #         {
    #             // ReSharper disable once StringLiteralTypo
    #             return snapPunch.__Members().OfType<Face>().Single(face => face.Name == "ALIGNPUNCH");
    #         }

    #         internal static string EditInteger(int integer)
    #         {
    #             if (integer < 0)
    #                 throw new ArgumentOutOfRangeException(nameof(integer));
    #             if (integer < 10)
    #                 return "00" + integer;
    #             if (integer < 100)
    #                 return "0" + integer;
    #             return integer.ToString();
    #         }

    #         public static Part _Prototype(Component component) => component.Prototype as Part ?? throw new Exception();

    #         [Obsolete]
    #         internal static DatumAxis GetZAxisOccurenceOfRetainer(Component retainer)
    #         {
    #             //string retainerRefset = retainer.ReferenceSet;

    #             //print_(retainer.__Prototype().GetAllReferenceSets().Single(set => set.Name == retainerRefset).AskMembersInReferenceSet()
    #             //    .OfType<NXOpen.CoordinateSystem>().Count());

    #             //Snap.NX.CoordinateSystem tempCsys = retainer.__Members().Select(obj => (Snap.NX.NXObject)obj).OfType<Snap.NX.CoordinateSystem>().Single();
    #             //IEnumerable<NXOpen.DatumAxis> k = retainer.__Members()
    #             //    .OfType<NXOpen.DatumAxis>();
    #             //foreach (NXOpen.DatumAxis axis in k)
    #             //    if (new NXOpen.Vector3d(axis.Direction.X, axis.Direction.Y, axis.Direction.Z).__IsEqualTo(tempCsys.AxisZ))
    #             //        return axis;

    #             //throw new ArgumentException("End Exception");

    #             throw new NotImplementedException();
    #         }

    #         #endregion

    #         private void AddPierceComponents_Load(object sender, EventArgs e)
    #         {
    #             Text = AssemblyFileVersion;
    #             Location = Properties.Settings.Default.add_pierce_components_form_window_location;
    #         }

    #         private void AddPierceComponents_FormClosed(object sender, System.Windows.Forms.FormClosedEventArgs e)
    #         {
    #             Properties.Settings.Default.add_pierce_components_form_window_location = Location;
    #             Properties.Settings.Default.Save();
    #         }
    #     }
    pass


class UFuncAssemblyExportDesignData:
    #  public partial class AssemblyExportDesignData : _UFuncForm
    #  {
    #      public AssemblyExportDesignData()
    #      {
    #          InitializeComponent();
    #      }

    #      public static Part _WorkPart => Session.GetSession().Parts.Work;

    #      private void ResetForm()
    #      {
    #          if (__display_part_ is null)
    #          {
    #              Enabled = false;
    #              return;
    #          }

    #          Enabled = true;

    #          if (!rdoChange.Checked && !rdoRto.Checked && !rdoReview50.Checked && !rdoReview90.Checked &&
    #              !rdoReview100.Checked && !rdoOther.Checked)
    #              rdoReview50.Checked = true;

    #          GFolder folder = GFolder.create_or_null(_WorkPart);

    #          if (folder is null)
    #              return;

    #          if (folder.CustomerNumber.Length == 6)
    #          {
    #              if (rdoRto.Checked || rdoChange.Checked)
    #              {
    #                  txtFolderName.Text = "";
    #                  txtFolderName.Enabled = false;
    #                  return;
    #              }

    #              txtFolderName.Enabled = true;

    #              return;
    #          }

    #          txtFolderName.Enabled = true;
    #      }

    #      private void BtnData_Clicked(object sender, EventArgs e)
    #      {
    #          Hide();

    #          try
    #          {
    #              if (sender == btnDesignAccept)
    #                  Export_Design();
    #              else if (sender == btnSelectComponents)
    #                  ManualExport(false);
    #              else if (sender == btnSelectAll)
    #                  ManualExport(true);
    #          }
    #          catch (Exception ex)
    #          {
    #              ex.__PrintException();
    #          }
    #          finally
    #          {
    #              print("Complete");
    #              Show();
    #          }

    #          //stopwatch.Stop();

    #          //print_($"Time: {stopwatch.Elapsed.TotalMinutes:f2}");
    #      }

    #      private void ManualExport(bool selectAll)
    #      {
    #          Part __display_part_ = Session.GetSession().Parts.Display;

    #          List<Component> components = selectAll
    #              ? __display_part_.ComponentAssembly.RootComponent.__Descendants().ToList()
    #              : Selection.SelectManyComponents().ToList();

    #          if (components.Count == 0)
    #              return;

    #          components.Add(__display_part_.ComponentAssembly.RootComponent);

    #          if (chk4ViewDwg.Checked)
    #              try
    #              {
    #                  ExportDwg4Views(components);
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }

    #          Export1.Design(
    #              __display_part_,
    #              components.ToArray(),
    #              null,
    #              false,
    #              false,
    #              chk4ViewPDF.Checked,
    #              false,
    #              chkDetailStep.Checked,
    #              chkSee3DData.Checked,
    #              chkBurnout.Checked,
    #              chkParasolids.Checked,
    #              chkCastings.Checked,
    #              chkPrintData.Checked,
    #              rdoChange.Checked);
    #      }

    #      private void ExportDwg4Views(List<Component> components)
    #      {
    #          GFolder folder = GFolder.Create(__display_part_.FullPath);

    #          Part[] parts = components.Select(c => c.Prototype)
    #              .OfType<Part>()
    #              .Where(p => p.__HasDrawingSheet("4-VIEW"))
    #              .Distinct()
    #              .ToArray();

    #          var parts_to_export = from part in parts
    #                                where part.__IsPartDetail()
    #                                let op = part.__AskDetailOp()
    #                                let match = Regex.Match(part.Leaf, "^(\\d+-\\d+)-\\d+$")
    #                                where match.Success
    #                                let dir = $"{folder.dir_op(op)}\\{match.Groups[1].Value}-dwg-4-views"
    #                                let output = $"{dir}\\{part.Leaf}.dwg"
    #                                select new
    #                                {
    #                                    input_part = part.FullPath,
    #                                    output_part = output,
    #                                };

    #          foreach (var p in parts_to_export)
    #              try
    #              {
    #                  string dir = Path.GetDirectoryName(p.output_part);

    #                  if (!Directory.Exists(dir))
    #                      Directory.CreateDirectory(dir);

    #                  DxfdwgCreator dwgCreator = session_.DexManager.CreateDxfdwgCreator();

    #                  using (session_.__UsingBuilderDestroyer(dwgCreator))
    #                  {
    #                      dwgCreator.ExportData = DxfdwgCreator.ExportDataOption.Drawing;
    #                      dwgCreator.SettingsFile = "C:\\Program Files\\Siemens\\NX1899\\dxfdwg\\dxfdwg.def";
    #                      dwgCreator.OutputFileType = DxfdwgCreator.OutputFileTypeOption.Dwg;
    #                      dwgCreator.InputFile = p.input_part;
    #                      dwgCreator.OutputFile = p.output_part;
    #                      dwgCreator.DrawingList = "4-VIEW";
    #                      dwgCreator.ProcessHoldFlag = true;
    #                      dwgCreator.Commit();

    #                  }
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #      }

    #      private void Export_Design()
    #      {
    #          Component[] components;

    #          bool isRto = false;

    #          if (rdoRto.Checked)
    #          {
    #              isRto = true;
    #              components = __display_part_.ComponentAssembly.RootComponent.__Descendants().ToArray();
    #          }
    #          else if (rdoChange.Checked)
    #          {
    #              isRto = true;
    #              components = Selection.SelectManyComponents();
    #          }
    #          else if (rdoReview50.Checked || rdoReview90.Checked || rdoReview100.Checked || rdoOther.Checked)
    #          {
    #              isRto = false;
    #              components = __display_part_.ComponentAssembly.RootComponent.__Descendants().ToArray();
    #          }
    #          else
    #          {
    #              throw new ArgumentException();
    #          }

    #          if (components.Length == 0)
    #              return;

    #          Export1.Design(
    #              __display_part_,
    #              components,
    #              txtFolderName.Text,
    #              isRto || rdoChange.Checked,
    #              true,
    #              print4Views: isRto && chkPrintDesign.Checked,
    #              isChange: rdoChange.Checked);
    #      }

    #      private void Rdo_CheckedChanged(object sender, EventArgs e)
    #      {
    #          try
    #          {
    #              chkPrintDesign.Enabled = rdoRto.Checked || rdoChange.Checked;

    #              btnDesignAccept.Text = rdoChange.Checked
    #                  ? "Select"
    #                  : "Execute";

    #              if (__display_part_ is null)
    #                  return;

    #              GFolder folder = GFolder.create_or_null(_WorkPart);

    #              if (folder is null)
    #                  return;

    #              switch (folder.CustomerNumber.Length)
    #              {
    #                  case 6:
    #                      txtFolderName.Enabled = !rdoChange.Checked && !rdoRto.Checked;
    #                      break;
    #                  default:
    #                      txtFolderName.Enabled = true;
    #                      break;
    #              }

    #              string folderName = $"{TodaysDate}-----{__display_part_.Leaf}-----";

    #              if (sender == rdoReview50)
    #                  txtFolderName.Text = folderName + @"50% Review";

    #              else if (sender == rdoReview90)
    #                  txtFolderName.Text = folderName + @"90% Review";

    #              else if (sender == rdoReview100)
    #                  txtFolderName.Text = folderName + @"100% Review";

    #              else if (sender == rdoRto)
    #                  txtFolderName.Text = folderName + @"RTO";

    #              else if (sender == rdoOther)
    #                  txtFolderName.Text = folderName + @"-----";

    #              else if (sender == rdoChange)
    #                  txtFolderName.Text = folderName + @"-----";
    #          }
    #          catch (Exception ex)
    #          {
    #              ex.__PrintException();
    #          }
    #      }

    #      private void TabControl_Selected(object sender, TabControlEventArgs e)
    #      {
    #          if (tabControl.SelectedTab == tabDesign)
    #              Size = new Size(275, 249);
    #          else if (tabControl.SelectedTab == tabData)
    #              Size = new Size(182, 385);
    #      }

    #      private void AssemblyExportDesignDataForm_Load(object sender, EventArgs e)
    #      {
    #          Text = $"{AssemblyFileVersion} - Assembly Export";
    #          ResetForm();
    #          Location = Settings.Default.assembly_export_design_data_form_window_location;
    #      }

    #      private void AssemblyExportDesignDataForm_FormClosed(object sender, FormClosedEventArgs e)
    #      {
    #          Settings.Default.assembly_export_design_data_form_window_location = Location;
    #          Settings.Default.Save();
    #      }

    #      public class Export1
    #      {
    #          private const string ExportImportExe =
    #              @"U:\NX110\Concept\NX110library\Ufunc\ExportImportData\ExportImportData.exe";

    #          private const string Step214Ug = @"C:\Program Files\Siemens\NX 11.0\STEP214UG\step214ug.exe";

    #          public const string _printerCts = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC";

    #          // sql
    #          public static readonly int[] Layers = { 1, 94, 100, 111, 200, 230 };

    #          public static void Design(
    #              Part topLevelAssembly,
    #              Component[] __components,
    #              string outgoingDirectoryName = null,
    #              bool isRto = false,
    #              bool zipAssembly = false,
    #              bool pdf4Views = false,
    #              bool stp999 = false,
    #              bool stpDetails = false,
    #              bool stpSee3DData = false,
    #              bool dwgBurnout = false,
    #              bool parasolid = false,
    #              bool paraCasting = false,
    #              bool print4Views = false,
    #              bool isChange = false)
    #          {
    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  //using (session_.__UsingSuppressDisplay())
    #                  {
    #                      ufsession_.Ui.SetPrompt("Filtering components to export.");
    #                      GFolder folder = GFolder.Create(topLevelAssembly.FullPath);

    #                      if (!__components.All(comp => comp.OwningPart.Tag == topLevelAssembly.Tag))
    #                          throw new InvalidOperationException(
    #                              "All valid components must be under the top level display part.");

    #                      bool isSixDigit = folder.CustomerNumber.Length == 6;
    #                      HashSet<Part> hashedParts = new HashSet<Part>();

    #                      foreach (Component comp in __components)
    #                      {
    #                          if (!(comp.Prototype is Part part))
    #                              continue;

    #                          hashedParts.Add(part);
    #                      }

    #                      Part[] validParts = hashedParts.ToArray();

    #                      // sql
    #                      const string sevenZip = @"C:\Program Files\7-Zip\7z.exe";

    #                      if (!File.Exists(sevenZip))
    #                          throw new FileNotFoundException($"Could not find \"{sevenZip}\".");

    #                      string parentFolder = isSixDigit
    #                          ? folder.DirDesignInformation
    #                          : folder.DirOutgoing;

    #                      string exportDirectory = string.IsNullOrEmpty(outgoingDirectoryName)
    #                          ? null
    #                          : $"{parentFolder}\\{outgoingDirectoryName}";

    #                      if (!(isRto && isSixDigit) && zipAssembly && exportDirectory != null && Directory.Exists(exportDirectory))
    #                          switch (MessageBox.Show($@"{exportDirectory} already exisits, would you like to overwrite it?",
    #                                      @"Warning", MessageBoxButtons.YesNo))
    #                          {
    #                              case DialogResult.Yes:
    #                                  Directory.Delete(exportDirectory, true);
    #                                  break;
    #                              default:
    #                                  return;
    #                          }

    #                      if (!(isRto && isSixDigit))
    #                          if (!string.IsNullOrEmpty(outgoingDirectoryName))
    #                              Directory.CreateDirectory(exportDirectory);

    #                      // If this is an RTO, then we need to delete the data files in the appropriate op folders.
    #                      if (isRto && !isChange)
    #                          try
    #                          {
    #                              DeleteOpFolders(__display_part_, folder);
    #                          }
    #                          catch (Exception ex)
    #                          {
    #                              ex.__PrintException();
    #                          }

    #                      if (exportDirectory != null)
    #                          Directory.CreateDirectory(exportDirectory);

    #                      Regex detailRegex = new Regex(RegexDetail, RegexOptions.IgnoreCase);
    #                      validParts = validParts.Distinct(new EqualityLeaf()).ToArray();

    #                      IDictionary<string, ISet<Part>> exportDict = SortPartsForExport(validParts);

    #                      //#pragma warning disable CS0612 // Type or member is obsolete
    #                      //                        if (!CheckSizeDescriptions(exportDict["PDF_4-VIEW"]))
    #                      //                            switch (MessageBox.Show(
    #                      //                                        "At least one block did not match its' description. Would you like to continue?",
    #                      //                                        "Warning", MessageBoxButtons.YesNo))
    #                      //                            {
    #                      //                                case DialogResult.Yes:
    #                      //                                    break;
    #                      //                                default:
    #                      //                                    return;
    #                      //                            }
    #                      //#pragma warning restore CS0612 // Type or member is obsolete

    #                      __display_part_.__Save();

    #                      Stopwatch stop_watch = new Stopwatch();

    #                      stop_watch.Start();

    #                      try
    #                      {
    #                          /////////////////////
    #                          Process assemblyProcess = null;

    #                          // Sets up the strip.
    #                          if (isRto || stpDetails || zipAssembly)
    #                              using (session_.__UsingDisplayPartReset())
    #                                  SetUpStrip(folder);

    #                          UpdateParts(
    #                              isRto,
    #                              pdf4Views, stpDetails, exportDict["PDF_4-VIEW"],
    #                              print4Views, exportDict["PDF_4-VIEW"],
    #                              dwgBurnout, exportDict["DWG_BURNOUT"],
    #                              stp999, exportDict["STP_999"],
    #                              stpSee3DData, exportDict["STP_SEE3D"],
    #                              paraCasting, exportDict["X_T_CASTING"],
    #                              __components);

    #                          Dictionary<string, Process> dict = new Dictionary<string, Process>();

    #                          if (isRto && detailRegex.IsMatch(topLevelAssembly.Leaf))
    #                          {
    #                              string stpPath = CreatePath(folder, topLevelAssembly, "-Step-Assembly", ".stp");

    #                              string dir = Path.GetDirectoryName(stpPath);

    #                              if (!Directory.Exists(dir))
    #                                  Directory.CreateDirectory(dir);

    #                              AssemblyExportDesignDataStp(topLevelAssembly.FullPath, stpPath, FilePathExternalStepAssemblyDef);
    #                          }

    #                          // Prints the parts with 4-Views.
    #                          if (print4Views)
    #                              using (session_.__UsingDisplayPartReset())
    #                              {
    #                                  PrintPdfs(exportDict["PDF_4-VIEW"]);
    #                              }

    #                          // Gets the processes that will create the pdf 4-Views.
    #                          if (isRto || pdf4Views)
    #                              foreach (Part part in exportDict["PDF_4-VIEW"])
    #                                  try
    #                                  {
    #                                      if (part.Leaf.EndsWith("000"))
    #                                          continue;

    #                                      string pdfPath = CreatePath(folder, part, "-Pdf-4-Views", ".pdf");

    #                                      string dir = Path.GetDirectoryName(pdfPath);

    #                                      if (!Directory.Exists(dir))
    #                                          Directory.CreateDirectory(dir);

    #                                      if (File.Exists(pdfPath))
    #                                          File.Delete(pdfPath);

    #                                      print($"PDF 4-VIEW -> {pdfPath}");
    #                                      AssemblyExportDesignDataPdf(part, "4-VIEW", pdfPath);
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          // If this is a RTO then
    #                          if (isRto || stpDetails)
    #                              foreach (Part part in exportDict["PDF_4-VIEW"])
    #                              {
    #                                  string stpPath = CreatePath(folder, part, "-Step-Details", ".stp");

    #                                  string dir = Path.GetDirectoryName(stpPath);

    #                                  if (!Directory.Exists(dir))
    #                                      Directory.CreateDirectory(dir);

    #                                  if (File.Exists(stpPath))
    #                                      File.Delete(stpPath);

    #                                  print($"Step Details -> {part.FullPath}");
    #                                  AssemblyExportDesignDataStp(part.FullPath, stpPath, FilePathExternalStepDetailDef);
    #                              }

    #                          if (zipAssembly && !(isRto || stpDetails))
    #                              try
    #                              {
    #                                  string path = $"{exportDirectory}\\{topLevelAssembly.Leaf}.stp";

    #                                  string dir = Path.GetDirectoryName(path);

    #                                  if (!Directory.Exists(dir))
    #                                      Directory.CreateDirectory(dir);

    #                                  print($"{nameof(AssemblyExportDesignDataStp)} - {topLevelAssembly}");

    #                                  AssemblyExportDesignDataStp(topLevelAssembly.FullPath, path, FilePathExternalStepDetailDef);
    #                              }
    #                              catch (Exception ex)
    #                              {
    #                                  ex.__PrintException();
    #                              }

    #                          // Gets the processes that create stp see 3d data.
    #                          if (isRto || stpSee3DData)
    #                              foreach (Part part in exportDict["STP_SEE3D"])
    #                                  try
    #                                  {
    #                                      string output = CreatePath(folder, part, "-Step-See-3D-Data", ".stp");

    #                                      string dir = Path.GetDirectoryName(output);

    #                                      if (!Directory.Exists(dir))
    #                                          Directory.CreateDirectory(dir);

    #                                      print($"STEP See 3d - {part.FullPath}");

    #                                      AssemblyExportDesignDataStp(part.FullPath, output, @"U:\nxFiles\Step Translator\ExternalStep_Detail.def");
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          // Gets the processes that create stp 999 details.
    #                          if (isRto || stp999)
    #                              foreach (Part part in exportDict["STP_999"])
    #                                  try
    #                                  {
    #                                      string output = CreatePath(folder, part, "-Step-999", ".stp");

    #                                      string dir = Path.GetDirectoryName(output);

    #                                      if (!Directory.Exists(dir))
    #                                          Directory.CreateDirectory(dir);

    #                                      print($"999 - {part.FullPath}");
    #                                      AssemblyExportDesignDataStp(part.FullPath, output, @"U:\nxFiles\Step Translator\ExternalStep_Detail.def");
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          // Gets the processes that create burnout dwgs.
    #                          if (isRto || dwgBurnout)
    #                              foreach (Part part in exportDict["DWG_BURNOUT"])
    #                                  try
    #                                  {
    #                                      string output = CreatePath(folder, part, "-Dwg-Burnouts", ".dwg");

    #                                      string dir = Path.GetDirectoryName(output);

    #                                      if (!Directory.Exists(dir))
    #                                          Directory.CreateDirectory(dir);

    #                                      print($"BURNOUT - {part.FullPath}");

    #                                      AssemblyExportDesignDataDwg(part.FullPath, "BURNOUT", output);
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          //if (dwg4Views)
    #                          //    foreach (Part part in hashedParts)
    #                          //        try
    #                          //        {
    #                          //            string output = CreatePath(folder, part, "-Dwg-4-Views", ".dwg");

    #                          //            string dir = Path.GetDirectoryName(output);

    #                          //            if (!Directory.Exists(dir))
    #                          //                Directory.CreateDirectory(dir);

    #                          //            //print($"BURNOUT - {part.FullPath}");

    #                          //            Dwg(part.FullPath, "4-VIEW", output);
    #                          //        }
    #                          //        catch (Exception ex)
    #                          //        {
    #                          //            ex.__PrintException();
    #                          //        }

    #                          // Creates casting parasolids.
    #                          if (isRto || paraCasting)
    #                              foreach (Part castingPart in exportDict["X_T_CASTING"])
    #                                  try
    #                                  {
    #                                      print($"{nameof(CreateCasting)} - {castingPart.FullPath}");
    #                                      CreateCasting(castingPart, folder);
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          HashSet<string> expectedFiles = new HashSet<string>(dict.Keys);

    #                          HashSet<string> directoriesToExport = new HashSet<string>(expectedFiles.Select(Path.GetDirectoryName));

    #                          CreateDirectoriesDeleteFiles(expectedFiles);

    #                          string zipPath = $"{exportDirectory}\\{topLevelAssembly.Leaf}_NX.7z";

    #                          if ((isRto && !isSixDigit) || (zipAssembly && !isRto))
    #                          {
    #                              print(nameof(Assembly));
    #                              assemblyProcess = Assembly(topLevelAssembly, false, zipPath);
    #                              assemblyProcess.Start();
    #                          }

    #                          prompt("Validating Stp Files.");

    #                          print(nameof(WriteStpCyanFiles));
    #                          WriteStpCyanFiles(expectedFiles);

    #                          prompt("Zipping up data folders.");

    #                          // Gets all the data folders that were created and zips them up and places them in the proper outgoingData folderWithCtsNumber if this is an RTO.
    #                          if (isRto && !isSixDigit)
    #                          {
    #                              print(nameof(ZipUpDataFolders));
    #                              ZipUpDataFolders(directoriesToExport, exportDirectory);
    #                          }

    #                          if (isRto && !isSixDigit)
    #                          {
    #                              print(nameof(ZipupDirectories));
    #                              ZipupDirectories(sevenZip, directoriesToExport, zipPath);
    #                          }

    #                          foreach (string file_key in dict.Keys)
    #                              try
    #                              {
    #                                  Process process = dict[file_key];

    #                                  if (File.Exists(file_key))
    #                                      continue;

    #                                  print($"Recreating: {file_key}");
    #                                  prompt($"Recreating: {file_key}");

    #                                  process.Start();

    #                                  process.WaitForExit();
    #                              }
    #                              catch (Exception ex)
    #                              {
    #                                  ex.__PrintException();
    #                              }

    #                          // Checks to make sure that any expected data files were actually created.
    #                          if (expectedFiles.Count > 0)
    #                          {
    #                              print(nameof(ErrorCheck));
    #                              ErrorCheck(isRto, zipAssembly, expectedFiles);
    #                          }

    #                          // Moves the sim report to the out going folderWithCtsNumber if one exists.
    #                          if (isRto && !isSixDigit && !(exportDirectory is null))
    #                          {
    #                              print(nameof(MoveSimReport));
    #                              MoveSimReport(folder, exportDirectory);
    #                          }

    #                          // Moves the stock list to the outgoing folderWithCtsNumber if one exists.
    #                          if (isRto && !isSixDigit && !(exportDirectory is null))
    #                          {
    #                              print(nameof(MoveStocklist));
    #                              MoveStocklist(folder, topLevelAssembly.Leaf, exportDirectory);
    #                          }

    #                          if (!(exportDirectory is null))
    #                          {
    #                              print(nameof(ZipupDataDirectories));
    #                              ZipupDataDirectories(exportDirectory, assemblyProcess);
    #                          }

    #                          /////////////////////////
    #                      }
    #                      finally
    #                      {
    #                          stop_watch.Stop();

    #                          print($"{stop_watch.Elapsed.Minutes}:{stop_watch.Elapsed.Seconds}");
    #                      }
    #                  }
    #              }
    #          }

    #          public static void DeleteOpFolders(Part part, GFolder folder)
    #          {
    #              if (folder is null)
    #                  throw new ArgumentException();

    #              // Matches the {part.Leaf} to 000 regex.
    #              Match top_match = Regex.Match(part.Leaf, RegexOp000Holder, RegexOptions.IgnoreCase);

    #              // If the {match} is not a success, then {part} is not a "000".
    #              if (!top_match.Success)
    #                  throw new Exception($"Part \"{part.FullPath}\" is not a 000.");

    #              // Gets the op of the {part}.
    #              string op = top_match.Groups["opNum"].Value;

    #              // The set that holds the data directories to delete.
    #              HashSet<string> directoriesToDelete = new HashSet<string>();

    #              switch (op)
    #              {
    #                  // Matches the 900 000's.
    #                  case "900":
    #                      {
    #                          directoriesToDelete.Add($"{folder.dir_op("900")}\\{folder.CustomerNumber}-900-Step-Assembly");

    #                          foreach (Component component in part.ComponentAssembly.RootComponent.GetChildren())
    #                          {
    #                              Match match = Regex.Match(component.DisplayName, RegexLwr);

    #                              if (!match.Success)
    #                                  continue;

    #                              string assembly_op = match.Groups["opNum"].Value;

    #                              if (assembly_op.Length % 2 != 0)
    #                                  continue;

    #                              for (int i = 0; i < assembly_op.Length - 1; i += 2)
    #                              {
    #                                  string temp_op = assembly_op[i] + "" + assembly_op[i + 1] + "0";

    #                                  string directory = folder.dir_op(temp_op);

    #                                  directoriesToDelete.Add(
    #                                      $"{directory}\\{folder.CustomerNumber}-{temp_op}-Parasolids-Castings");
    #                                  directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Pdf-4-Views");
    #                                  directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-Details");
    #                                  directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-Assembly");
    #                                  directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Dwg-Burnouts");
    #                                  directoriesToDelete.Add(
    #                                      $"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-See-3D-Data");
    #                              }
    #                          }
    #                      }
    #                      break;

    #                  // This matches all the regular op 010, 020, 030 and so 000's.
    #                  case var _ when op.Length == 3:
    #                      {
    #                          // Gets the assembly folderWithCtsNumber correpsonding to the {assemblyOp000}.
    #                          string assemblyFolder = folder.dir_op(op);

    #                          // If the directory {assemblyFolder} doesn't exist, then we want to throw.
    #                          if (!Directory.Exists(assemblyFolder))
    #                              throw new DirectoryNotFoundException($"Could not find directory \"{assemblyFolder}\".");

    #                          foreach (string directory in Directory.GetDirectories(assemblyFolder))
    #                          {
    #                              string dirName = Path.GetFileName(directory);

    #                              if (dirName == null)
    #                                  continue;

    #                              if (!dirName.StartsWith($"{folder.CustomerNumber}-{op}"))
    #                                  continue;

    #                              // Adds the {directory} to the {directoriesToDelete}.
    #                              directoriesToDelete.Add(directory);
    #                          }
    #                      }
    #                      break;

    #                  // Matches the assembly holder by ensuring that the op has an even amount of characters.
    #                  case var _ when op.Length % 2 == 0:
    #                      {
    #                          // A list to hold the ops.
    #                          List<string> opList = new List<string>();

    #                          // Gets the character array of the {assemblyHolder}.
    #                          char[] charArray = op.ToCharArray();

    #                          // Grab the op characters two at a time.
    #                          for (int i = 0; i < charArray.Length; i += 2)
    #                              opList.Add(charArray[i] + "" + charArray[i + 1] + "0");

    #                          foreach (string assemblyOp in opList)
    #                          {
    #                              // Gets the assembly folderWithCtsNumber correpsonding to the {assemblyOp000}.
    #                              string assemblyFolder = folder.dir_op(assemblyOp);

    #                              // If the directory {assemblyFolder} doesn't exist, then we want to throw.
    #                              if (!Directory.Exists(assemblyFolder))
    #                                  throw new DirectoryNotFoundException($"Could not find directory \"{assemblyFolder}\".");

    #                              foreach (string directory in Directory.GetDirectories(assemblyFolder))
    #                              {
    #                                  string dirName = Path.GetFileName(directory);

    #                                  if (dirName == null)
    #                                      continue;

    #                                  if (!dirName.StartsWith($"{folder.CustomerNumber}-{assemblyOp}"))
    #                                      continue;

    #                                  // Adds the {directory} to the {directoriesToDelete}.
    #                                  directoriesToDelete.Add(directory);
    #                              }
    #                          }
    #                      }
    #                      break;
    #              }

    #              foreach (string dir in directoriesToDelete)
    #                  if (Directory.Exists(dir))
    #                      Directory.Delete(dir, true);
    #          }

    #          public static void WriteStpCyanFiles(IEnumerable<string> expectedFiles)
    #          {
    #              foreach (string expected in expectedFiles)
    #              {
    #                  if (!expected.EndsWith(".stp") || !File.Exists(expected))
    #                      continue;

    #                  string fileText = File.ReadAllText(expected);

    #                  if (!fileText.Contains("Cyan"))
    #                      continue;

    #                  File.WriteAllText(expected, fileText.Replace("Cyan", "cyan"));
    #              }
    #          }

    #          public static void CreateDirectoriesDeleteFiles(IEnumerable<string> expectedFiles)
    #          {
    #              foreach (string file in expectedFiles)
    #                  try
    #                  {
    #                      string directory = Path.GetDirectoryName(file);
    #                      Directory.CreateDirectory(directory ?? throw new Exception());
    #                      File.Delete(file);
    #                  }
    #                  catch (Exception ex)
    #                  {
    #                      ex.__PrintException();
    #                  }
    #          }

    #          [Obsolete]
    #          public static bool CheckSizeDescriptions(IEnumerable<Part> partsInBom)
    #          {
    #              //bool allPassed = true;
    #              //foreach (Part part in partsInBom)
    #              //    try
    #              //    {
    #              //        if (!SizeDescription1.Validate(part, out string message))
    #              //        {
    #              //            if (message == "Part does not contain a Dynamic Block.")
    #              //                continue;
    #              //            allPassed = false;
    #              //            print_($"{part.Leaf}:\n{message}\n");
    #              //        }
    #              //    }
    #              //    catch (Exception ex)
    #              //    {
    #              //        ex.__PrintException();
    #              //    }

    #              //return allPassed;

    #              throw new NotImplementedException();
    #          }

    #          public static string CreatePath(GFolder folder, Part part, string directoryTag, string extension)
    #          {
    #              string directory =
    #                  $"{folder.DirJob}\\{folder.CustomerNumber}-{part.__AskDetailOp()}\\{folder.CustomerNumber}-{part.__AskDetailOp()}{directoryTag}";
    #              string stpPath = $"{directory}\\{part.Leaf}{extension}";
    #              return stpPath;
    #          }

    #          public static void SetLayers()
    #          {
    #              __display_part_.Layers.SetState(1, NXOpen.Layer.State.WorkLayer);

    #              for (int i = 2; i <= 256; i++)
    #                  if (Layers.Contains(i))
    #                      __display_part_.Layers.SetState(i, NXOpen.Layer.State.Selectable);
    #                  else
    #                      __display_part_.Layers.SetState(i, NXOpen.Layer.State.Hidden);
    #          }

    #          public static void CreateCasting(Part part, GFolder folder)
    #          {
    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  __display_part_ = part;

    #                  string op = part.__AskDetailOp();

    #                  string castingDirectory =
    #                      $"{folder.DirJob}\\{folder.CustomerNumber}-{op}\\{folder.CustomerNumber}-{op}-Parasolids-Castings";

    #                  if (!Directory.Exists(castingDirectory))
    #                      Directory.CreateDirectory(castingDirectory);

    #                  print($"Casting Step - {part.FullPath}");
    #                  CreateCastingStep(part, castingDirectory);

    #                  string castingPath = $"{castingDirectory}\\{part.Leaf}.x_t";

    #                  if (File.Exists(castingPath))
    #                      File.Delete(castingPath);

    #                  List<Tag> tagBodies = part.Bodies
    #                      .ToArray()
    #                      .OfType<Body>()
    #                      .Where(body => body.Layer == 1)
    #                      .Select(body => body.Tag)
    #                      .ToList();

    #                  if (tagBodies.Count == 0)
    #                  {
    #                      print($"Did not find any solid bodies on layer 1 in part {part.Leaf}");

    #                      return;
    #                  }

    #                  if (!(part.ComponentAssembly.RootComponent is null))
    #                      foreach (Component child in part.ComponentAssembly.RootComponent.GetChildren())
    #                      {
    #                          if (child.IsSuppressed)
    #                              continue;

    #                          if (child.Layer != 96)
    #                              continue;

    #                          if (child.ReferenceSet == "Empty")
    #                              continue;

    #                          foreach (Body __body in child.__Members().OfType<Body>().Where(__b => __b.IsSolidBody))
    #                              tagBodies.Add(__body.Tag);
    #                      }

    #                  string castingFile =
    #                      $"{folder.DirJob}\\{folder.CustomerNumber}-{op}\\{folder.CustomerNumber}-{op}-Parasolids-Castings\\{part.Leaf}.x_t";

    #                  ufsession_.Ps.ExportData(tagBodies.ToArray(), castingFile);
    #              }

    #              string FullPath = part.FullPath;

    #              part.Close(BasePart.CloseWholeTree.False, BasePart.CloseModified.CloseModified, null);

    #              session_.__FindOrOpen(FullPath);
    #          }

    #          private static void CreateCastingStep(Part part, string castingDirectory)
    #          {
    #              try
    #              {
    #                  string step_path = $"{castingDirectory}\\{part.Leaf}.stp";

    #                  if (File.Exists(step_path))
    #                      File.Delete(step_path);

    #                  using (session_.__UsingLockUgUpdates())

    #                  {
    #                      foreach (Component child in __display_part_.ComponentAssembly.RootComponent.GetChildren())
    #                      {
    #                          // sql
    #                          if (child.Layer == 96)
    #                              continue;

    #                          if (child.IsSuppressed)
    #                              continue;

    #                          child.Suppress();
    #                      }
    #                  }

    #                  Session theSession = Session.GetSession();
    #                  Part workPart = theSession.Parts.Work;
    #                  Part displayPart = theSession.Parts.Display;
    #                  // ----------------------------------------------
    #                  //   Menu: File->Export->STEP...
    #                  // ----------------------------------------------
    #                  Session.UndoMarkId markId1;
    #                  markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start");

    #                  StepCreator stepCreator1;
    #                  stepCreator1 = theSession.DexManager.CreateStepCreator();

    #                  // sql
    #                  stepCreator1.ExportAs = StepCreator.ExportAsOption.Ap214;

    #                  stepCreator1.BsplineTol = 0.001;

    #                  stepCreator1.SettingsFile = "C:\\Program Files\\Siemens\\NX1899\\step214ug\\ugstep214.def";

    #                  stepCreator1.BsplineTol = 0.001;

    #                  stepCreator1.InputFile = part.FullPath;

    #                  theSession.SetUndoMarkName(markId1, "Export STEP File Dialog");

    #                  Session.UndoMarkId markId2;
    #                  markId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Export STEP File");

    #                  theSession.DeleteUndoMark(markId2, null);

    #                  Session.UndoMarkId markId3;
    #                  markId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Export STEP File");

    #                  stepCreator1.OutputFile = step_path;

    #                  stepCreator1.FileSaveFlag = false;

    #                  stepCreator1.LayerMask = "1,96";

    #                  stepCreator1.ProcessHoldFlag = true;

    #                  NXObject nXObject1;
    #                  nXObject1 = stepCreator1.Commit();

    #                  theSession.DeleteUndoMark(markId3, null);

    #                  theSession.SetUndoMarkName(markId1, "Export STEP File");

    #                  stepCreator1.Destroy();
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void SetLayersInBlanksAndLayoutsAndAddDummies(Part snapStrip010)
    #          {
    #              if (!Regex.IsMatch(snapStrip010.Leaf, RegexStrip, RegexOptions.IgnoreCase))
    #                  throw new ArgumentException(@"Must be an op 010 strip.", nameof(snapStrip010));

    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  // sql
    #                  Regex blankNameRegex = new Regex("^BLANK-([0-9]{1,})$");

    #                  Regex layoutNameRegex = new Regex("^LAYOUT-([0-9]{1,})$");

    #                  Part layoutPart = __display_part_.ComponentAssembly.RootComponent.__Descendants()
    #                      .Select(component => component.Prototype)
    #                      .OfType<Part>()
    #                      .FirstOrDefault(component => Regex.IsMatch(component.Leaf, RegexLayout, RegexOptions.IgnoreCase));

    #                  Part blankPart = __display_part_.ComponentAssembly.RootComponent.__Descendants()
    #                      .Select(component => component.Prototype)
    #                      .OfType<Part>()
    #                      .FirstOrDefault(component => Regex.IsMatch(component.Leaf, RegexBlank, RegexOptions.IgnoreCase));

    #                  HashSet<int> layoutLayers = new HashSet<int>();

    #                  HashSet<int> blankLayers = new HashSet<int>();

    #                  foreach (Component child in __display_part_.ComponentAssembly.RootComponent.__Descendants())
    #                  {
    #                      if (!(child.Prototype is Part))
    #                          continue;

    #                      if (child.IsSuppressed)
    #                          continue;

    #                      Match blankMatch = blankNameRegex.Match(child.Name);
    #                      Match layoutMatch = layoutNameRegex.Match(child.Name);

    #                      if (blankMatch.Success)
    #                      {
    #                          int layer = int.Parse(blankMatch.Groups[1].Value) + 10;
    #                          blankLayers.Add(layer);
    #                      }

    #                      if (!layoutMatch.Success) continue;
    #                      {
    #                          int layer = int.Parse(layoutMatch.Groups[1].Value) * 10;
    #                          layoutLayers.Add(layer);
    #                          layoutLayers.Add(layer + 1);
    #                      }
    #                  }

    #                  if (blankLayers.Count != 0 && blankPart != null)
    #                  {
    #                      __display_part_ = blankPart;
    #                      __work_part_ = __display_part_;
    #                      AddDummy(blankPart, blankLayers);
    #                      ufsession_.Ui.SetPrompt($"Saving: {blankPart.Leaf}.");
    #                      Session.GetSession().Parts.Display
    #                          .Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False);
    #                  }

    #                  if (layoutLayers.Count != 0 && layoutPart != null)
    #                  {
    #                      __display_part_ = layoutPart;
    #                      __work_part_ = __display_part_;
    #                      AddDummy(layoutPart, layoutLayers);
    #                      ufsession_.Ui.SetPrompt($"Saving: {layoutPart.Leaf}.");
    #                      session_.Parts.Display.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False);
    #                  }
    #              }

    #              snapStrip010.__Save();
    #          }

    #          private static void AddDummy(Part part, IEnumerable<int> layers)
    #          {
    #              ufsession_.Ui.SetPrompt($"Setting layers in {__display_part_.Leaf}.");
    #              int[] layerArray = layers.ToArray();
    #              __display_part_.Layers.SetState(1, NXOpen.Layer.State.WorkLayer);

    #              for (int i = 2; i < +256; i++)
    #                  __display_part_.Layers.SetState(i, layerArray.Contains(i)
    #                      ? NXOpen.Layer.State.Selectable
    #                      : NXOpen.Layer.State.Hidden);

    #              __display_part_.Layers.SetState(layerArray.Min(), NXOpen.Layer.State.WorkLayer);
    #              __display_part_.Layers.SetState(1, NXOpen.Layer.State.Hidden);

    #              if (!(part.ComponentAssembly.RootComponent is null))
    #              {
    #                  Component validChild = part.ComponentAssembly.RootComponent
    #                      .GetChildren()
    #                      .Where(component => component.__IsLoaded())
    #                      .FirstOrDefault(component => !component.IsSuppressed);

    #                  if (validChild != null)
    #                      return;
    #              }

    #              Part dummyPart = session_.__FindOrOpen(DummyPath);
    #              ufsession_.Ui.SetPrompt($"Adding dummy file to {part.Leaf}.");
    #              __work_part_.ComponentAssembly.AddComponent(dummyPart, "Entire Part", "DUMMY", _Point3dOrigin,
    #                  _Matrix3x3Identity, 1, out _);
    #          }

    #          public static void CheckAssemblyDummyFiles()
    #          {
    #              ufsession_.Ui.SetPrompt("Checking Dummy files exist.");

    #              if (__display_part_.ComponentAssembly.RootComponent == null)
    #                  return;

    #              foreach (Component childOfStrip in __display_part_.ComponentAssembly.RootComponent.GetChildren())
    #              {
    #                  if (childOfStrip.IsSuppressed)
    #                      continue;

    #                  if (!childOfStrip.__IsLoaded())
    #                      continue;

    #                  if (!Regex.IsMatch(childOfStrip.DisplayName, RegexPressAssembly, RegexOptions.IgnoreCase))
    #                      continue;

    #                  if (childOfStrip.GetChildren().Length == 0)
    #                      throw new InvalidOperationException(
    #                          $"A press exists in your assembly without any children. {childOfStrip.__AssemblyPathString()}");

    #                  switch (childOfStrip.GetChildren().Length)
    #                  {
    #                      case 1:
    #                          throw new InvalidOperationException(
    #                              $"A press exists in your assembly with only one child. Expecting a ram and a bolster. {childOfStrip.__AssemblyPathString()}");
    #                      case 2:
    #                          foreach (Component childOfPress in childOfStrip.GetChildren())
    #                          {
    #                              if (!childOfPress.__IsLoaded())
    #                                  throw new InvalidOperationException(
    #                                      $"The child of a press must be loaded. {childOfPress.__AssemblyPathString()}");

    #                              if (childOfPress.IsSuppressed)
    #                                  throw new InvalidOperationException(
    #                                      $"The child of a press cannot be suppressed. {childOfPress.__AssemblyPathString()}");

    #                              if (childOfPress.GetChildren().Length != 0 && childOfPress.GetChildren()
    #                                      .Select(component => component)
    #                                      .Any(component => !component.IsSuppressed && component.Prototype is Part))
    #                                  continue;

    #                              throw new InvalidOperationException(
    #                                  $"The child of a bolster or ram under a press must be the Dummy file: {DummyPath}. {childOfPress.__AssemblyPathString()}");
    #                          }

    #                          break;
    #                  }
    #              }
    #          }

    #          public static void ZipupDataDirectories(string exportDirectory, Process assemblyProcess)
    #          {
    #              try
    #              {
    #                  string[] stpFilesInOutGoingFolder =
    #                      Directory.GetFiles(exportDirectory, "*.stp", SearchOption.TopDirectoryOnly);

    #                  if (stpFilesInOutGoingFolder.Length != 0)
    #                  {
    #                      string displayName = Path.GetFileNameWithoutExtension(stpFilesInOutGoingFolder.First());

    #                      Process stpZipProcess = AssemblyExportDesignDataCreate7ZipProcess($"{exportDirectory}\\{displayName}_STP.7z",
    #                          stpFilesInOutGoingFolder);

    #                      stpZipProcess.Start();

    #                      stpZipProcess.WaitForExit();

    #                      foreach (string file in stpFilesInOutGoingFolder)
    #                          try
    #                          {
    #                              if (File.Exists(file)) File.Delete(file);
    #                          }
    #                          catch (Exception ex)
    #                          {
    #                              ex.__PrintException();
    #                          }
    #                  }

    #                  assemblyProcess?.WaitForExit();
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          /// <summary>
    #          ///     Gets the file paths of all Sim Reports with the specified <paramref name="ctsJobNumber" />.
    #          /// </summary>
    #          /// <param name="ctsJobNumber">The job number.</param>
    #          /// <returns>An array of SimReport file paths.</returns>
    #          public static string[] GetReports(string ctsJobNumber)
    #          {
    #              return (from directory in Directory.GetDirectories("X:\\")
    #                      let directoryName = Path.GetFileName(directory)
    #                      where directoryName != null
    #                      // sql
    #                      let match = new Regex("^Reports-([0-9]{4})-([0-9]{4})$").Match(directoryName)
    #                      where match.Success
    #                      let startRange = int.Parse(match.Groups[1].Value)
    #                      let endRange = int.Parse(match.Groups[2].Value)
    #                      let jobNumber = int.Parse(ctsJobNumber)
    #                      where startRange <= jobNumber && jobNumber <= endRange
    #                      from report in Directory.GetFiles(directory, "*.7z")
    #                      let fileName = Path.GetFileNameWithoutExtension(report)
    #                      where fileName.StartsWith(ctsJobNumber)
    #                      select report).ToArray();
    #          }

    #          public static IDictionary<string, ISet<Part>> SortPartsForExport(IEnumerable<Part> validParts)
    #          {
    #              Regex detailRegex = new Regex(RegexDetail, RegexOptions.IgnoreCase);

    #              IDictionary<string, ISet<Part>> exportDict = new Dictionary<string, ISet<Part>>
    #          {
    #              { "PDF_4-VIEW", new HashSet<Part>() },
    #              { "STP_DETAIL", new HashSet<Part>() },
    #              { "DWG_BURNOUT", new HashSet<Part>() },
    #              { "STP_999", new HashSet<Part>() },
    #              { "STP_SEE3D", new HashSet<Part>() },
    #              { "X_T_CASTING", new HashSet<Part>() },
    #              { "X_T", new HashSet<Part>() }
    #          };

    #              foreach (Part part in validParts)
    #              {
    #                  Match match = detailRegex.Match(part.Leaf);

    #                  if (!match.Success)
    #                      continue;

    #                  if (part.Leaf.__IsAssemblyHolder())
    #                      continue;

    #                  if (part.Leaf.EndsWith("000"))
    #                      continue;

    #                  if (part.__HasDrawingSheet("4-VIEW"))
    #                      exportDict["PDF_4-VIEW"].Add(part);

    #                  if (part.__HasDrawingSheet("BURNOUT"))
    #                      exportDict["DWG_BURNOUT"].Add(part);

    #                  if (part.__IsSee3DData())
    #                      exportDict["STP_SEE3D"].Add(part);

    #                  if (part.__Is999())
    #                      exportDict["STP_999"].Add(part);

    #                  if (part.__IsCasting())
    #                      exportDict["X_T_CASTING"].Add(part);

    #                  if (part.__HasReferenceSet("BODY"))
    #                      exportDict["X_T"].Add(part);
    #              }

    #              return exportDict;
    #          }

    #          public static void UpdateParts(
    #              bool isRto,
    #              bool pdf4Views, bool stpDetails, IEnumerable<Part> partsWith4ViewsNoAssemblyHolders,
    #              bool print4Views, IEnumerable<Part> partsWith4Views,
    #              bool dwgBurnout, IEnumerable<Part> burnoutParts,
    #              bool stp999, IEnumerable<Part> nine99Parts,
    #              bool stpSee3DData, IEnumerable<Part> see3DDataParts,
    #              bool paraCasting, IEnumerable<Part> castingParts,
    #              Component[] selected_components)
    #          {
    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  ISet<Part> selected_parts =
    #                      new HashSet<Part>(selected_components.Select(__c => __c.Prototype).OfType<Part>());

    #                  ISet<Part> partsToUpdate = new HashSet<Part>();

    #                  if (isRto || pdf4Views || stpDetails)
    #                      foreach (Part part in partsWith4ViewsNoAssemblyHolders)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || dwgBurnout)
    #                      foreach (Part part in burnoutParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || print4Views)
    #                      foreach (Part part in partsWith4Views)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || paraCasting)
    #                      foreach (Part part in castingParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || stp999)
    #                      foreach (Part part in nine99Parts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || stpSee3DData)
    #                      foreach (Part part in see3DDataParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (partsToUpdate.Count > 0)
    #                      UpdateParts(partsToUpdate.ToArray());
    #              }
    #          }

    #          public static void ZipupDirectories(string sevenZip, IEnumerable<string> directoriesToExport, string zipPath)
    #          {
    #              try
    #              {
    #                  // Constructs the arguments that deletes the sub data folders in the newly created assembly zip folderWithCtsNumber.
    #                  string arguments = $"d \"{zipPath}\" -r {directoriesToExport.Select(Path.GetFileName).Where(dir => dir != null).Aggregate("", (s1, s2) => $"{s1} \"{s2}\"")}";

    #                  // Starts the actual delete process.
    #                  Process deleteProcess = Process.Start(sevenZip, arguments);

    #                  // Waits for the {deleteProcess} to finish.
    #                  deleteProcess?.WaitForExit();
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void MoveSimReport(GFolder folder, string exportDirectory)
    #          {
    #              try
    #              {
    #                  if (!folder.is_cts_job())
    #                      return;

    #                  if (GetReports(folder.CtsNumber).Length != 0)
    #                      foreach (string report in GetReports(folder.CtsNumber))
    #                      {
    #                          string reportName = Path.GetFileName(report);

    #                          if (reportName == null)
    #                              continue;

    #                          string exportedReportPath = $"{exportDirectory}\\{reportName}";

    #                          if (File.Exists(exportedReportPath))
    #                          {
    #                              print($"Sim report \"{exportedReportPath}\" already exists.");
    #                              continue;
    #                          }

    #                          File.Copy(report, exportedReportPath);
    #                      }
    #                  else
    #                      print("Unable to find a sim report to transfer.");
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void LaunchProcesses(int numberOfProcesses, params Process[] processes)
    #          {
    #              int processesCompleted = 0;

    #              try
    #              {
    #                  int length = numberOfProcesses > processes.Length
    #                      ? processes.Length
    #                      : numberOfProcesses;
    #                  HashSet<Process> hashProcesses = new HashSet<Process>();
    #                  for (int i = 0; i < length; i++)
    #                  {
    #                      processes[i].Start();
    #                      hashProcesses.Add(processes[i]);
    #                      prompt($"{processesCompleted} of {processes.Length}");
    #                  }

    #                  for (int i = length; processesCompleted < processes.Length; i++)
    #                  {
    #                      Process first = hashProcesses.FirstOrDefault(process => process != null && process.HasExited);
    #                      if (first == null)
    #                      {
    #                          i--;
    #                          continue;
    #                      }

    #                      hashProcesses.Remove(first);
    #                      processesCompleted++;
    #                      if (i < processes.Length)
    #                      {
    #                          Process nextProcess = processes[i];
    #                          nextProcess.Start();
    #                          hashProcesses.Add(nextProcess);
    #                      }

    #                      prompt($"{processesCompleted} of {processes.Length}");
    #                  }

    #                  processes.ToList().ForEach(proc => proc.WaitForExit());
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }

    #              ufsession_.Ui.SetPrompt("All processes have finished.");
    #          }

    #          public static void UpdateParts(params Part[] parts)
    #          {
    #              Part[] validParts = parts.Where(part => !part.Leaf.__IsAssemblyHolder()).Distinct(new EqualityLeaf())
    #                  .ToArray();

    #              for (int i = 0; i < validParts.Length; i++)
    #                  try
    #                  {
    #                      string report = $"Updating: {i + 1} of {validParts.Length}. ";
    #                      Part part = validParts[i];
    #                      ufsession_.Ui.SetPrompt($"{report}Setting Display Part to {part.Leaf}. ");
    #                      __display_part_ = part;
    #                      __work_part_ = __display_part_;

    #                      if (part.__IsCasting() && !(part.ComponentAssembly.RootComponent is null))
    #                          // If it is a casting then it cannot contain a child that is a lift lug and set to entire part.
    #                          if ((from child in part.ComponentAssembly.RootComponent.GetChildren()
    #                               where child.Prototype is Part
    #                               where child.__Prototype().FullPath.Contains("LiftLugs")
    #                               where child.ReferenceSet != RefsetEmpty
    #                               select child)
    #                              .Any(child => child.ReferenceSet == RefsetEntirePart))
    #                              print(
    #                                  $"Casting part {__display_part_.Leaf} contains a Lift Lug that is set to Entire Part. Casting Part cannot be made.");

    #                      ufsession_.Ui.SetPrompt($"{report}Setting layers in {part.Leaf}.");
    #                      SetLayers();
    #                      ufsession_.Ui.SetPrompt($"{report}Finding DisplayableObjects in {part.Leaf}.");
    #                      List<DisplayableObject> objects = new List<DisplayableObject>();

    #                      foreach (int layer in Layers)
    #                          objects.AddRange(__display_part_.Layers.GetAllObjectsOnLayer(layer)
    #                              .OfType<DisplayableObject>());

    #                      ufsession_.Ui.SetPrompt($"{report}Unblanking objects in {part.Leaf}.");
    #                      session_.DisplayManager.UnblankObjects(objects.ToArray());

    #                      foreach (DraftingView view in __display_part_.DraftingViews)
    #                          view.Update();

    #                      ufsession_.Ui.SetPrompt($"{report}Switching back to modeling in {part.Leaf}.");
    #                      session_.ApplicationSwitchImmediate("UG_APP_MODELING");
    #                      __work_part_.Drafting.ExitDraftingApplication();
    #                      ufsession_.Ui.SetPrompt($"{report}Saving {part.Leaf}.");
    #                      part.__Save();
    #                  }
    #                  catch (Exception ex)
    #                  {
    #                      ex.__PrintException(validParts[i].Leaf);
    #                  }
    #          }

    #          public static void SetUpStrip(GFolder folder)
    #          {
    #              try
    #              {
    #                  string strip_010 = folder.file_strip("010");

    #                  if (!File.Exists(strip_010))
    #                      return;

    #                  Part op010Strip = session_.__FindOrOpen(strip_010);

    #                  SetLayersInBlanksAndLayoutsAndAddDummies(op010Strip);

    #                  CheckAssemblyDummyFiles();

    #                  op010Strip.__Save();
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static Process Assembly(Part snapPart, bool waitForProcess, string zipPath)
    #          {
    #              HashSet<string> filePaths = new HashSet<string>();

    #              foreach (Component component in GetAssembly(snapPart.ComponentAssembly.RootComponent))
    #                  filePaths.Add(component.__Prototype().FullPath);

    #              return AssemblyExportDesignDataCreate7ZipProcess(zipPath, filePaths.ToArray());
    #          }

    #          /// <summary>Gets all the components under the given <paramref name="snapComponent" />.</summary>
    #          /// <remarks>The program will not go past components that are suppressed or end with "simulation"</remarks>
    #          /// <param name="snapComponent">The component to get the descendants from.</param>
    #          private static IEnumerable<Component> GetAssembly(Component snapComponent)
    #          {
    #              if (!snapComponent.__IsLoaded())
    #                  yield break;

    #              if (snapComponent.DisplayName.ToLower().EndsWith("-simulation"))
    #                  yield break;

    #              if (snapComponent.IsSuppressed)
    #                  yield break;

    #              yield return snapComponent;

    #              foreach (Component child in snapComponent.GetChildren())
    #                  foreach (Component comp in GetAssembly(child))
    #                      yield return comp;
    #          }

    #          public static void PrintPdfs(IEnumerable<Part> partsWith4Views)
    #          {
    #              using (session_.__UsingSuppressDisplay())
    #              {
    #                  try
    #                  {
    #                      UFSession.GetUFSession().Disp.SetDisplay(UFConstants.UF_DISP_UNSUPPRESS_DISPLAY);
    #                      UFSession.GetUFSession().Disp.RegenerateDisplay();
    #                      Print4Views(partsWith4Views);
    #                  }
    #                  catch (Exception ex)
    #                  {
    #                      ex.__PrintException();
    #                  }
    #              }
    #          }

    #          public static void ErrorCheck(bool isRto, bool zipAssembly, IEnumerable<string> expectedFiles)
    #          {
    #              string[] enumerable = expectedFiles as string[] ?? expectedFiles.ToArray();

    #              int fileCreatedCount = enumerable.Where(File.Exists).Count();

    #              print($"Created {fileCreatedCount} file(s).");

    #              if (!isRto && !zipAssembly)
    #                  print(
    #                      "Created files will have to be manually moved to outgoingData folderWithCtsNumber if that is desired. (Example: RTO)");

    #              List<string> filesThatWereNotCreated = enumerable.Where(s => !File.Exists(s)).ToList();

    #              List<Tuple<string, string>> errorList = new List<Tuple<string, string>>();

    #              foreach (string file in filesThatWereNotCreated)
    #              {
    #                  string extension = Path.GetExtension(file);

    #                  if (extension == null)
    #                      continue;

    #                  string errorFilePath = file.Replace(extension, ".err");

    #                  if (File.Exists(errorFilePath))
    #                  {
    #                      string[] fileContents = File.ReadAllLines(errorFilePath);

    #                      errorList.Add(new Tuple<string, string>(file, fileContents[0]));

    #                      File.Delete(errorFilePath);
    #                  }
    #                  else
    #                  {
    #                      errorList.Add(new Tuple<string, string>(file, "Unknown error."));
    #                  }
    #              }

    #              if (errorList.Count <= 0)
    #                  return;

    #              print("Files that were not created.");

    #              errorList.ForEach(print);
    #          }

    #          public static void ZipUpDataFolders(IEnumerable<string> directoriesToExport, string exportDirectory)
    #          {
    #              LaunchProcesses(10, (
    #                  from directory in directoriesToExport
    #                  let directoryName = Path.GetFileName(directory)
    #                  select AssemblyExportDesignDataCreate7ZipProcess($"{exportDirectory}\\{directoryName}.7z", directory)
    #              ).ToArray());
    #          }

    #          public static void Print4Views(IEnumerable<Part> allParts)
    #          {
    #              try
    #              {
    #                  bool IsNotAssembly(Part part)
    #                  {
    #                      string name = Path.GetFileNameWithoutExtension(part.FullPath);

    #                      if (name == null)
    #                          return false;

    #                      name = name.ToLower();

    #                      if (name.EndsWith("000") || name.EndsWith("lsh") || name.EndsWith("ush") || name.EndsWith("lwr") ||
    #                          name.EndsWith("upr"))
    #                          return false;

    #                      return !name.Contains("lsp") && !name.Contains("usp");
    #                  }

    #                  List<Part> parts = allParts
    #                      .Where(part => Regex.IsMatch(part.Leaf, RegexDetail, RegexOptions.IgnoreCase))
    #                      .Where(IsNotAssembly)
    #                      .Where(part => part.DraftingDrawingSheets.ToArray().Any(__d => __d.Name.ToUpper() == "4-VIEW"))
    #                      .ToList();

    #                  parts.Sort((part1, part2) => string.Compare(part1.Leaf, part2.Leaf, StringComparison.Ordinal));

    #                  for (int i = 0; i < parts.Count; i++)
    #                  {
    #                      Part part = parts[i];

    #                      ufsession_.Ui.SetPrompt($"{i + 1} of {parts.Count}. Printing 4-VIEW of {part.Leaf}.");

    #                      __display_part_ = part;

    #                      __work_part_ = __display_part_;

    #                      PrintBuilder printBuilder = __work_part_.PlotManager.CreatePrintBuilder();

    #                      using (new Destroyer(printBuilder))
    #                      {
    #                          // sql
    #                          printBuilder.Copies = 1;

    #                          printBuilder.ThinWidth = 1.0;

    #                          printBuilder.NormalWidth = 2.0;

    #                          printBuilder.ThickWidth = 3.0;

    #                          printBuilder.Output = PrintBuilder.OutputOption.WireframeBlackWhite;

    #                          printBuilder.ShadedGeometry = true;

    #                          DrawingSheet drawingSheet = __work_part_.DraftingDrawingSheets.FindObject("4-VIEW");

    #                          drawingSheet.Open();

    #                          printBuilder.SourceBuilder.SetSheets(new NXObject[] { drawingSheet });

    #                          printBuilder.PrinterText = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC";

    #                          printBuilder.Orientation = PrintBuilder.OrientationOption.Landscape;

    #                          printBuilder.Paper = PrintBuilder.PaperSize.Letter;

    #                          printBuilder.Commit();
    #                      }
    #                  }
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void MoveStocklist(GFolder folder, string topDisplayName, string exportDirectory)
    #          {
    #              try
    #              {
    #                  string stocklist = (from file in Directory.GetFiles(folder.DirStocklist)
    #                                      let name = Path.GetFileNameWithoutExtension(file)
    #                                      where name != null
    #                                      where name.EndsWith($"{topDisplayName}-stocklist")
    #                                      select file).SingleOrDefault();

    #                  if (stocklist is null)
    #                  {
    #                      print($"Could not find a stocklist named: {topDisplayName}-stocklist");
    #                      return;
    #                  }

    #                  File.Copy(stocklist, $"{exportDirectory}\\{Path.GetFileName(stocklist)}");
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static Process AssemblyExportDesignDataCreate7ZipProcess(string zipPath, params string[] filesToZip)
    #          {
    #              string tempFile = $"{Path.GetTempPath()}zipData{filesToZip.GetHashCode()}.txt";

    #              using (FileStream fs = File.Open(tempFile, FileMode.Create))
    #              {
    #                  fs.Close();
    #              }

    #              using (StreamWriter writer = new StreamWriter(tempFile))
    #              {
    #                  filesToZip.ToList().ForEach(writer.WriteLine);
    #              }

    #              return new Process
    #              {
    #                  EnableRaisingEvents = false,
    #                  StartInfo =
    #              {
    #                  CreateNoWindow = false,
    #                  FileName = "C:\\Program Files\\7-Zip\\7z",
    #                  WindowStyle = ProcessWindowStyle.Normal,
    #                  UseShellExecute = true,
    #                  Arguments = $"a -t7z \"{zipPath}\" \"@{tempFile}\" -mx9"
    #              }
    #              };
    #          }

    #          public static void AssemblyExportDesignDataSevenZip(string path, bool wait, params string[] fileNames)
    #          {
    #              string directory = Path.GetDirectoryName(path);

    #              string str = directory + "\\" + "zipData.txt";

    #              try
    #              {
    #                  using (FileStream fileStream = File.Open(str, FileMode.Create))
    #                  {
    #                      fileStream.Close();
    #                  }

    #                  using (StreamWriter streamWriter = new StreamWriter(str))
    #                  {
    #                      foreach (string fileName in fileNames)
    #                          streamWriter.WriteLine(fileName);
    #                  }

    #                  AssemblyExportDesignDataSevenZip(path, wait, str);
    #              }
    #              finally
    #              {
    #                  File.Delete(str);
    #              }
    #          }

    #          public static void AssemblyExportDesignDataSevenZip(string path, bool wait, string textFileToRead)
    #          {
    #              if (string.IsNullOrEmpty(path))
    #                  throw new ArgumentException(@"Invalid path.", nameof(path));

    #              if (File.Exists(path))
    #                  throw new IOException("The specified output_path already exists.");

    #              if (!File.Exists(textFileToRead))
    #                  throw new FileNotFoundException();

    #              // sql
    #              string fileToRead = "a -t7z \"" + path + "\" \"@" + textFileToRead + "\" -mx9";

    #              Process process = new Process
    #              {
    #                  EnableRaisingEvents = false,
    #                  StartInfo =
    #              {
    #                  FileName = "C:\\Program Files\\7-Zip\\7z",
    #                  Arguments = fileToRead
    #              }
    #              };

    #              process.Start();

    #              if (!wait)
    #                  return;

    #              process.WaitForExit();

    #              print(File.Exists(path)
    #                  ? $"Successfully created \"{path}\"."
    #                  : $"Unsuccessfully created \"{path}\".");
    #          }

    #          public static void AssemblyExportDesignDataPdf(Part part, string drawingSheetName, string filePath)
    #          {
    #              string directory = Path.GetDirectoryName(filePath);

    #              if (!filePath.EndsWith(".pdf"))
    #                  throw new InvalidOperationException("File path for PDF must end with \".pdf\".");

    #              if (File.Exists(filePath))
    #                  throw new ArgumentOutOfRangeException("output_path", "PDF \"" + filePath + "\" already exists.");

    #              //We can use SingleOrDefault here because NX will prevent the naming of two drawing sheets the exact same string.
    #              DrawingSheet sheet = part.DrawingSheets
    #                                       .ToArray()
    #                                       .SingleOrDefault(drawingSheet => drawingSheet.Name == drawingSheetName)
    #                                   ??
    #                                   throw new ArgumentException(
    #                                       $@"Part ""{part.Leaf}"" does not have a sheet named ""{drawingSheetName}"".",
    #                                       "drawingSheetName");

    #              __display_part_ = part;
    #              session_.__SetDisplayToWork();
    #              SetLayers();

    #              PrintPDFBuilder pdfBuilder = part.PlotManager.CreatePrintPdfbuilder();

    #              using (session_.__UsingBuilderDestroyer(pdfBuilder))
    #              {
    #                  // sql
    #                  pdfBuilder.Scale = 1.0;
    #                  pdfBuilder.Size = PrintPDFBuilder.SizeOption.ScaleFactor;
    #                  pdfBuilder.OutputText = PrintPDFBuilder.OutputTextOption.Polylines;
    #                  pdfBuilder.Units = PrintPDFBuilder.UnitsOption.English;
    #                  pdfBuilder.XDimension = 8.5;
    #                  pdfBuilder.YDimension = 11.0;
    #                  pdfBuilder.RasterImages = true;
    #                  pdfBuilder.Colors = PrintPDFBuilder.Color.BlackOnWhite;
    #                  pdfBuilder.Watermark = "";
    #                  UFSession.GetUFSession().Draw.IsObjectOutOfDate(sheet.Tag, out bool flag);

    #                  if (flag)
    #                  {
    #                      UFSession.GetUFSession().Draw.UpdOutOfDateViews(sheet.Tag);
    #                      part.__Save();
    #                  }

    #                  sheet.Open();
    #                  pdfBuilder.SourceBuilder.SetSheets(new NXObject[] { sheet });
    #                  pdfBuilder.Filename = filePath;
    #                  pdfBuilder.Commit();
    #              }
    #          }

    #          public static void AssemblyExportDesignDataStp(string partPath, string output_path, string settings_file)
    #          {
    #              try
    #              {
    #                  if (!output_path.EndsWith(".stp"))
    #                      throw new InvalidOperationException("File path for STP must end with \".stp\".");

    #                  if (File.Exists(output_path))
    #                      throw new ArgumentOutOfRangeException("output_path", "STP \"" + output_path + "\" already exists.");

    #                  if (!File.Exists(partPath))
    #                      throw new FileNotFoundException("Could not find file location \"" + partPath + "\".");

    #                  session_.__FindOrOpen(partPath);

    #                  StepCreator stepCreator = Session.GetSession().DexManager.CreateStepCreator();

    #                  using (session_.__UsingBuilderDestroyer(stepCreator))
    #                  {
    #                      // sql
    #                      stepCreator.ExportAs = StepCreator.ExportAsOption.Ap214;
    #                      stepCreator.SettingsFile = settings_file;
    #                      stepCreator.ObjectTypes.Solids = true;
    #                      stepCreator.OutputFile = output_path;
    #                      stepCreator.BsplineTol = 0.0254;
    #                      stepCreator.ObjectTypes.Annotations = true;
    #                      stepCreator.ExportFrom = StepCreator.ExportFromOption.ExistingPart;
    #                      stepCreator.InputFile = partPath;
    #                      stepCreator.FileSaveFlag = false;
    #                      stepCreator.LayerMask = "1, 96";
    #                      stepCreator.ProcessHoldFlag = true;
    #                      stepCreator.Commit();
    #                  }

    #                  string switchFilePath = output_path.Replace(".stp", ".log");

    #                  if (File.Exists(switchFilePath))
    #                      File.Delete(switchFilePath);
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void AssemblyExportDesignDataDwg(string partPath, string drawingSheetName, string filePath)
    #          {
    #              string directory = Path.GetDirectoryName(filePath);

    #              if (File.Exists(filePath))
    #                  throw new ArgumentOutOfRangeException("output_path", "DWG \"" + filePath + "\" already exists.");

    #              Part part = session_.__FindOrOpen(partPath);

    #              DrawingSheet sheet = part.DrawingSheets
    #                                       .ToArray()
    #                                       .SingleOrDefault(drawingSheet => drawingSheet.Name == drawingSheetName)
    #                                   ??
    #                                   throw new ArgumentException(
    #                                       $"Part \"{part.Leaf}\" does not have a sheet named \"{drawingSheetName}\".",
    #                                       "drawingSheetName");

    #              UFSession.GetUFSession().Draw.IsObjectOutOfDate(sheet.Tag, out bool flag);

    #              if (flag)
    #              {
    #                  SetLayers();
    #                  UFSession.GetUFSession().Draw.UpdOutOfDateViews(sheet.Tag);
    #                  part.__Save();
    #              }

    #              DxfdwgCreator dxfdwgCreator1 = session_.DexManager.CreateDxfdwgCreator();
    #              using (session_.__UsingBuilderDestroyer(dxfdwgCreator1))
    #              {
    #                  // sql
    #                  dxfdwgCreator1.ExportData = DxfdwgCreator.ExportDataOption.Drawing;
    #                  dxfdwgCreator1.AutoCADRevision = DxfdwgCreator.AutoCADRevisionOptions.R2004;
    #                  dxfdwgCreator1.ViewEditMode = true;
    #                  dxfdwgCreator1.FlattenAssembly = true;
    #                  dxfdwgCreator1.SettingsFile = "C:\\Program Files\\Siemens\\NX 11.0\\dxfdwg\\dxfdwg.def";
    #                  dxfdwgCreator1.ExportFrom = DxfdwgCreator.ExportFromOption.ExistingPart;
    #                  dxfdwgCreator1.OutputFileType = DxfdwgCreator.OutputFileTypeOption.Dwg;
    #                  dxfdwgCreator1.ObjectTypes.Curves = true;
    #                  dxfdwgCreator1.ObjectTypes.Annotations = true;
    #                  dxfdwgCreator1.ObjectTypes.Structures = true;
    #                  dxfdwgCreator1.FlattenAssembly = false;
    #                  dxfdwgCreator1.ExportData = DxfdwgCreator.ExportDataOption.Drawing;
    #                  dxfdwgCreator1.InputFile = part.FullPath;
    #                  dxfdwgCreator1.ProcessHoldFlag = true;
    #                  dxfdwgCreator1.OutputFile = filePath;
    #                  dxfdwgCreator1.WidthFactorMode = DxfdwgCreator.WidthfactorMethodOptions.AutomaticCalculation;
    #                  dxfdwgCreator1.LayerMask = "1-256";
    #                  dxfdwgCreator1.DrawingList = drawingSheetName;
    #                  dxfdwgCreator1.Commit();
    #              }

    #              string switchFilePath = filePath.Replace(".dwg", ".log");

    #              if (File.Exists(switchFilePath))
    #                  File.Delete(switchFilePath);
    #          }
    #      }
    #  }

    pass


class UFuncAssemblyWaveLink:
    #      public partial class AssemblyWavelink : _UFuncForm
    #  {
    #      public AssemblyWavelink()
    #      {
    #          InitializeComponent();
    #      }

    #      private void AssemblyWavelink_Load(object sender, EventArgs e)
    #      {
    #          Location = Settings.Default.assembly_wave_link_form_window_location;
    #          Text = AssemblyFileVersion;
    #      }

    #      private void AssemblyWavelink_FormClosed(object sender, FormClosedEventArgs e)
    #      {
    #          Settings.Default.assembly_wave_link_form_window_location = Location;
    #          Settings.Default.Save();
    #      }

    #      private void buttonShortTapReam_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkFasteners(chkBlankTools.Checked, RefsetShortTap, RefsetReamShort, null);
    #      }

    #      private void buttonTapReam_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkFasteners(chkBlankTools.Checked, RefsetTap, RefsetReam, null);
    #      }

    #      private void buttonTap_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkFasteners(chkBlankTools.Checked, RefsetTap, null, null);
    #      }

    #      private void buttonReam_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkFasteners(chkBlankTools.Checked, null, RefsetReam, null);
    #      }

    #      private void buttonShortTap_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkFasteners(chkBlankTools.Checked, RefsetShortTap, null, null);
    #      }

    #      private void buttonReamShort_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkFasteners(chkBlankTools.Checked, null, RefsetReamShort, null);
    #      }

    #      private void buttonClrHole_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkFasteners(chkBlankTools.Checked, RefsetClrHole, RefsetClrHole, RefsetClrHole);
    #      }

    #      private void buttonCbore_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkFasteners(chkBlankTools.Checked, RefsetCBore, RefsetCBore, null);
    #      }

    #      private void buttonSubTool_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WavelinkSubtool();
    #      }

    #      private void buttonSubtract_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkBoolean(chkBlankTools.Checked, Feature.BooleanType.Subtract);
    #      }

    #      private void buttonUnite_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkBoolean(chkBlankTools.Checked, Feature.BooleanType.Unite);
    #      }

    #      private void buttonLink_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkBoolean(chkBlankTools.Checked, Feature.BooleanType.Create);
    #      }

    #      private void buttonIntersect_Click(object sender, EventArgs e)
    #      {
    #          using (session_.__UsingFormShowHide(this))
    #              WaveLinkBoolean(chkBlankTools.Checked, Feature.BooleanType.Intersect);
    #      }

    #      public void WavelinkSubtool()
    #      {
    #          session_.SetUndoMark(Session.MarkVisibility.Visible, $"{ufunc_rev_name} - {nameof(WavelinkSubtool)}");

    #          Body target = SelectSingleSolidBody1(body => true);

    #          if (target is null)
    #              return;

    #          Component[] tools = SelectManyComponents1(c =>
    #          {
    #              if (!(c is Component comp))
    #                  return false;

    #              return comp.Tag != target.OwningComponent.Tag
    #              && (from refset in comp.__Prototype().GetAllReferenceSets()
    #                  let name = refset.Name.ToUpper()
    #                  where name == "SUB_TOOL" || Name == "SUB-TOOL" || name == "SUBTOOL"
    #                  select refset
    #                   ).Any() && !comp.DisplayName.__IsAssemblyHolder();
    #          }

    #                   );

    #          if (tools.Length == 0)
    #              return;

    #          using (session_.__UsingDisplayPartReset())
    #          using (session_.__UsingSuppressDisplay())
    #              try
    #              {

    #                  var current = __display_part_.Layers.WorkLayer;

    #                  try
    #                  {

    #                      __work_component_ = target.OwningComponent;

    #                      __display_part_.Layers.SetState(96, NXOpen.Layer.State.WorkLayer);
    #                      foreach (Component tool in tools)
    #                          using (tool.__UsingReferenceSetReset())
    #                              try
    #                              {
    #                                  ReferenceSet reference_set = tool.__Prototype()
    #                                      .GetAllReferenceSets()
    #                                      .SingleOrDefault(refset => refset.Name == "SUB_TOOL" || refset.Name == "SUB-TOOL" || refset.Name == "SUBTOOL");

    #                                  if (reference_set is null)
    #                                  {
    #                                      print($"Didn't find any sub tool reference sets for {tool.DisplayName} - {tool.Name} - {tool.Tag}");
    #                                      continue;
    #                                  }

    #                                  tool.__ReferenceSet(reference_set.Name);
    #                                  ExtractFace linked_body = tool.__CreateLinkedBody();
    #                                  print("//////////////////");
    #                                  print($"Created {linked_body.GetFeatureName()} in {linked_body.OwningPart.Leaf}");
    #                                  BooleanFeature boolean_feature = target.__Subtract(linked_body.GetBodies());
    #                                  print($"Created {boolean_feature.GetFeatureName()} in {linked_body.OwningPart.Leaf}");

    #                              }
    #                              catch (NXException ex) when (ex.ErrorCode == 670030)
    #                              {
    #                                  print($"Error occurred when trying to subtract {tool.DisplayName}, no interference.");
    #                              }
    #                              catch (InvalidOperationException)
    #                              {
    #                                  print($"Found more than one sub tool reference set for {tool.DisplayName} - {tool.Name} - {tool.Tag}");
    #                              }
    #                  }
    #                  finally
    #                  {
    #                      __display_part_.Layers.SetState(current, NXOpen.Layer.State.WorkLayer);
    #                  }
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #      }

    #      public void WaveLinkFasteners(bool blank_tools, string shcs_ref_set, string dwl_ref_set, string jck_ref_set)
    #      {
    #          session_.SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name);

    #          using (session_.__UsingDisplayPartReset())
    #              try
    #              {
    #                  Body[] targets = SelectMultipleTaggedObjects1(
    #                      "Select Target Body",
    #                      "select Target Body",
    #                      new[] { BodyMask },
    #                      k =>
    #                      {

    #                          if (!(k is Body b))
    #                              return false;

    #                          return b.IsOccurrence
    #                          && !b.OwningComponent.DisplayName.ToLower().Contains("strip")
    #                          && !b.OwningComponent.DisplayName.ToLower().Contains("press")
    #                          && !b.OwningComponent.DisplayName.ToLower().Contains("layout")
    #                          && !b.OwningComponent.DisplayName.__IsAssemblyHolder();
    #                      }).Cast<Body>().ToArray();

    #                  if (targets.Length == 0)
    #                      return;

    #                  Component[] tools = SelectMultipleTaggedObjects1(
    #                      "Select Tool Components",
    #                      "Select Tool Components",
    #                      new[] { Masks.ComponentMask },
    #                      tool1 =>
    #                      {

    #                          if (!(tool1 is Component tool))
    #                              return false;

    #                          return !tool.DisplayName._IsLayout_()
    #                          && !tool.DisplayName.ToLower().Contains("strip")
    #                          && !tool.DisplayName._IsFastenerExtended_()
    #                          && !tool.DisplayName.__IsAssemblyHolder()
    #                          && targets.All(t => t.OwningComponent.Tag != tool.Tag);
    #                      }).Cast<Component>().ToArray();

    #                  if (tools.Length == 0)
    #                      return;

    #                  using (session_.__UsingSuppressDisplay())
    #                      foreach (var target in targets)
    #                          foreach (Component tool in tools)
    #                              using (session_.__UsingDisplayPartReset())
    #                              using (session_.__UsingResetWorkLayer())
    #                                  try
    #                                  {
    #                                      __work_component_ = target.OwningComponent;
    #                                      __display_part_.Layers.SetState(96, NXOpen.Layer.State.WorkLayer);

    #                                      foreach (Component child in tool.GetChildren())
    #                                          try
    #                                          {
    #                                              if (!child.__IsLoaded())
    #                                              {
    #                                                  print($"Child fastener {child.DisplayName} was not loaded.");
    #                                                  continue;
    #                                              }

    #                                              if (child.IsSuppressed)
    #                                                  continue;

    #                                              //if (child._IsJckScrewTsg_() || child._IsJckScrew_())
    #                                              //    continue;

    #                                              using (child.__UsingReferenceSetReset())
    #                                              {
    #                                                  string original_ref_set = child.ReferenceSet;
    #                                                  Component proto_child_fastener = child.__ProtoChildComp();

    #                                                  if (proto_child_fastener.Layer != LayerFastener)
    #                                                      continue;

    #                                                  try
    #                                                  {
    #                                                      string[] ref_sets = new[] { shcs_ref_set, dwl_ref_set, jck_ref_set }
    #                                                          .Where(__r => !string.IsNullOrEmpty(__r))
    #                                                          .ToArray();

    #                                                      string[] fastener_ref_set_names = proto_child_fastener.__Prototype()
    #                                                          .GetAllReferenceSets()
    #                                                          .Select(__r => __r.Name)
    #                                                          .Intersect(ref_sets)
    #                                                          .ToArray();

    #                                                      switch (fastener_ref_set_names.Length)
    #                                                      {
    #                                                          case 0:
    #                                                              if ((!(shcs_ref_set is null)&& child._IsShcs_())
    #                                                                  || (!(dwl_ref_set is null) && child._IsDwl_())
    #                                                                  || (!(jck_ref_set is null) && child._IsJckScrewTsg_() || child._IsJckScrew_()))
    #                                                                  print(
    #                                                                      $"Coulnd't find any valid ref sets for {child.DisplayName}");
    #                                                              continue;
    #                                                          case 1:
    #                                                              child.__ReferenceSet(fastener_ref_set_names[0]);
    #                                                              break;
    #                                                          default:
    #                                                              print(
    #                                                                  $"Found more than one valid ref set for {child.DisplayName}");
    #                                                              continue;
    #                                                      }

    #                                                      if (!target.__InterferesWith(child))
    #                                                      {
    #                                                          print(
    #                                                              $"Could not subtract fastener {child.DisplayName}, no interference.");
    #                                                          continue;
    #                                                      }

    #                                                      ExtractFace ext = child.__CreateLinkedBody();
    #                                                      //ext.__Layer(96);
    #                                                      print("//////////////////");
    #                                                      print($"Created {ext.GetFeatureName()} in {ext.OwningPart.Leaf}");
    #                                                      BooleanFeature boolean_feature = target.__Subtract(ext.GetBodies());
    #                                                      print($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}");
    #                                                  }
    #                                                  catch (Exception ex)
    #                                                  {
    #                                                      ex.__PrintException(child.DisplayName);
    #                                                  }
    #                                              }
    #                                          }
    #                                          catch (Exception ex)
    #                                          {
    #                                              ex.__PrintException();
    #                                          }

    #                                      if (blank_tools)
    #                                          tool.Blank();
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #              }
    #              catch (NothingSelectedException)
    #              {
    #                  //Control jump
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #      }

    #      public static void WaveLinkBoolean(bool blank_tools, Feature.BooleanType booleanType)
    #      {
    #          session_.SetUndoMark(Session.MarkVisibility.Visible, "Assembly Wavelink");

    #          using (session_.__UsingDisplayPartReset())
    #          {
    #              try
    #              {
    #                  Body[] targets = SelectManySolidBodies1();

    #                  if (targets.Length == 0)
    #                      return;

    #                  Component[] tools = SelectManyComponents1(c =>
    #                  {
    #                      if (!(c is Component comp))
    #                          return false;

    #                      return targets.All(b => b.OwningComponent.Tag != c.Tag)
    #                      && !comp.DisplayName.__IsAssemblyHolder();
    #                  });

    #                  if (tools.Length == 0)
    #                      return;

    #                  var referenceSets = tools.Select(snapComponent => new { snapComponent, snapComponent.ReferenceSet }).ToList();
    #                  RefSetForm formCts = new RefSetForm(tools);

    #                  if (booleanType != Feature.BooleanType.Create)
    #                      formCts.RemoveReferenceSet("BODY");

    #                  formCts.ShowDialog();

    #                  if (!formCts.IsSelected)
    #                      return;

    #                  foreach (var target in targets)
    #                      foreach (var child in tools)
    #                          using (session_.__UsingDisplayPartReset())
    #                          using (child.__UsingReferenceSetReset())
    #                          using (session_.__UsingResetWorkLayer())
    #                          {
    #                              var current = __display_part_.Layers.WorkLayer;

    #                              try
    #                              {
    #                                  __work_component_ = target.OwningComponent;

    #                                  __display_part_.Layers.SetState(96, NXOpen.Layer.State.WorkLayer);

    #                                  child.__ReferenceSet(formCts.SelectedReferenceSetName);

    #                                  foreach (var ext in child.__CreateLinkedBodies())
    #                                      try
    #                                      {
    #                                          print("//////////////////");

    #                                          print($"Created {ext.GetFeatureName()} in {ext.OwningPart.Leaf}");

    #                                          switch (booleanType)
    #                                          {
    #                                              case Feature.BooleanType.Subtract:
    #                                                  {
    #                                                      BooleanFeature boolean_feature = target.__Subtract(ext.GetBodies());
    #                                                      print($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}");
    #                                                  }
    #                                                  break;

    #                                              case Feature.BooleanType.Unite:
    #                                                  {
    #                                                      BooleanFeature boolean_feature = target.__Unite(ext.GetBodies());
    #                                                      print($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}");
    #                                                  }
    #                                                  break;

    #                                              case Feature.BooleanType.Intersect:
    #                                                  {
    #                                                      BooleanFeature boolean_feature = target.__Intersect(ext.GetBodies());
    #                                                      print($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}");
    #                                                  }
    #                                                  break;
    #                                          }
    #                                      }
    #                                      catch (NXException ex) when (ex.ErrorCode == 670030)
    #                                      {
    #                                          print($"Error occurred when trying to subtract {child.DisplayName}, no interference.");
    #                                      }
    #                                      catch (Exception ex)
    #                                      {
    #                                          ex.__PrintException();
    #                                      }
    #                              }
    #                              finally
    #                              {
    #                                  __display_part_.Layers.SetState(current, NXOpen.Layer.State.WorkLayer);
    #                              }
    #                          }

    #                  if (blank_tools)
    #                      foreach (var tool in tools)
    #                          tool.Blank();
    #              }
    #              catch (NothingSelectedException)
    #              {
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }
    #      }

    #  }
    pass


class UFuncAutoDetail:
    #         public partial class AutoDetail : _UFuncForm
    #     {
    #         private static readonly List<Component> _allComponents = new List<Component>();
    #         private static readonly IDictionary<string, List<string>> _holeChart = new Dictionary<string, List<string>>();
    #         private static string _borderFile;
    #         private static string _sizeFile;

    #         public AutoDetail()
    #         {
    #             InitializeComponent();
    #             Location = Settings.Default.assembly_auto_detail_form_window_location;
    #         }

    #         private void MainForm_Load(object sender, EventArgs e)
    #         {
    #             Text = AssemblyFileVersion;

    # 			// sql
    #             _sizeFile = FilePathUcf.PerformStreamReaderString(
    #                 ":HOLESIZE_FILE_LOCATION:",
    #                 ":END_HOLESIZE_FILE_LOCATION:");

    # 			// sql
    #             _borderFile =FilePathUcf.PerformStreamReaderString(
    #                 ":BORDER_FILE_LOCATION:",
    #                 ":END_BORDER_FILE_LOCATION:");

    #             string[] lines = File.ReadAllLines(_sizeFile)
    #                 .Where(__s => !__s.StartsWith("--"))
    #                 .Where(__s => !string.IsNullOrEmpty(__s))
    #                 .Where(__s => !string.IsNullOrWhiteSpace(__s))
    #                 .ToArray();

    #             for (int i = 0; i < lines.Length - 1; i += 2)
    #                 _holeChart[lines[i + 1]] = lines[i].Split(',').ToList();

    #             SetFormDefaults();
    #         }

    #         private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
    #         {
    #             Settings.Default.assembly_auto_detail_form_window_location = Location;
    #             Settings.Default.Save();
    #         }

    #         private void ButtonSelectBorderFile_Click(object sender, EventArgs e)
    #         {
    # 			// sql
    #             openFileDialog.InitialDirectory = "G:\\0Library\\Drafting";
    #             DialogResult dialogResult = openFileDialog.ShowDialog();

    # 			// sql
    #             _borderFile = dialogResult == DialogResult.OK
    #                 ? openFileDialog.FileName
    #                 : FilePathUcf.PerformStreamReaderString(
    #                     ":BORDER_FILE_LOCATION:",
    #                     ":END_BORDER_FILE_LOCATION:");
    #         }

    #         private void CheckBox_Clicked(object sender, EventArgs e)
    #         {
    #             bool flag = chkDetailSheet.Checked || chkHoleChart.Checked || chkUpdateViews.Checked ||
    #                         chkDrillChart.Checked;
    #             btnSelect.Enabled = flag;
    #             btnSelectAll.Enabled = flag;
    #         }

    #         private void CheckBoxDelete4Views_CheckedChanged(object sender, EventArgs e)
    #         {
    #             chkHoleChart.Checked = false;
    #             chkUpdateViews.Checked = false;

    #             if (chkDelete4Views.Checked)
    #                 chkDetailSheet.Checked = false;

    #             chkDetailSheet.Enabled = !chkDelete4Views.Checked;
    #             chkHoleChart.Enabled = !chkDelete4Views.Checked;
    #             chkUpdateViews.Enabled = !chkDelete4Views.Checked;
    #             btnSelect.Enabled = chkDelete4Views.Checked;
    #             btnSelectAll.Enabled = chkDelete4Views.Checked;
    #         }

    #         private void ButtonSelect_Click(object sender, EventArgs e)
    #         {
    #             using (session_.__UsingFormShowHide(this))
    #             {
    #                 try
    #                 {
    #                     _allComponents.Clear();

    #                     Component[] selectComponents = Selection.SelectManyComponents();

    #                     if (selectComponents.Length == 0)
    #                         return;

    #                     _allComponents.AddRange(selectComponents);

    #                     List<Component> trimmedComponents = _allComponents.Where(comp => !comp.IsSuppressed)
    #                         .Distinct(new EqualityDisplayName())
    #                         .ToList();

    #                     trimmedComponents.Sort((c1, c2) => string.Compare(c1.Name, c2.Name, StringComparison.Ordinal));

    #                     DetailComponents(trimmedComponents);
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException();
    #                 }
    #             }
    #         }

    #         private void ButtonSelectAll_Click(object sender, EventArgs e)
    #         {
    #             using (session_.__UsingFormShowHide(this))
    #             {
    #                 try
    #                 {
    #                     if (__display_part_.ComponentAssembly.RootComponent is null)
    #                         return;

    #                     _allComponents.Clear();
    #                     GetChildComponents(__display_part_.ComponentAssembly.RootComponent);

    #                     if (_allComponents.Count == 0)
    #                     {
    #                         print("No valid components");
    #                         return;
    #                     }

    #                     List<CtsAttributes> materials = CreateMaterialList();
    #                     List<Component> passedComponents = new List<Component>();

    #                     foreach (Component comp in _allComponents)
    #                         try
    #                         {
    #                             foreach (NXObject.AttributeInformation attr in comp.GetUserAttributes())
    #                             {
    #                                 if (attr.Title.ToUpper() == "MATERIAL")
    #                                 {
    #                                     string value = comp.GetUserAttributeAsString("MATERIAL",
    #                                         NXObject.AttributeType.String,
    #                                         -1);

    #                                     if (value != "")
    #                                         passedComponents.AddRange(from matAttr in materials
    #                                                                   where matAttr.AttrValue == value
    #                                                                   select comp);
    #                                     else
    #                                         print($"\n{comp.DisplayName} : MATERIAL attribute equals nothing");
    #                                 }

    #                                 // Rev1.1 Change - Added for Scrap Chutes

    #                                 if (attr.Title.ToUpper() != "DESCRIPTION")
    #                                     continue;

    #                                 string dValue = comp.GetUserAttributeAsString("DESCRIPTION",
    #                                     NXObject.AttributeType.String,
    #                                     -1);

    #                                 if (dValue is null)
    #                                 {
    #                                     print("////////////////////////////////////");
    #                                     print($"Component: {comp.DisplayName} has a null DESCRIPTION value.");
    #                                     print(comp.__AssemblyPathString());
    #                                     print("////////////////////////////////////");
    #                                     continue;
    #                                 }

    #                                 if (dValue.ToUpper() == "CHUTE TO SUIT")
    #                                     passedComponents.Add(comp);

    #                                 if (dValue.ToLower().Contains("diemaker to alter"))
    #                                     passedComponents.Add(comp);
    #                                 // End of Rev1.1 change
    #                             }
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException(comp.DisplayName);
    #                         }

    #                     if (passedComponents.Count == 0)
    #                     {
    #                         print("No valid components");
    #                         return;
    #                     }

    #                     Component[] selectDeselectComps = passedComponents.ToArray();
    #                     passedComponents = Preselect.GetUserSelections(selectDeselectComps);

    #                     if (passedComponents.Count == 0)
    #                     {
    #                         print("No valid components");
    #                         return;
    #                     }

    #                     passedComponents = passedComponents.Where(comp => !comp.IsSuppressed)
    #                         .Distinct(new EqualityDisplayName())
    #                         .ToList();

    #                     passedComponents.Sort((c1, c2) => string.Compare(c1.Name, c2.Name, StringComparison.Ordinal));
    #                     DetailComponents(passedComponents);
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException();
    #                 }
    #             }
    #         }

    #         private void DetailComponents(IEnumerable<Component> selectedComponents)
    #         {
    #             using (session_.__UsingDisplayPartReset())
    #             {
    #                 Component[] componentArray = selectedComponents.ToArray();

    #                 for (int index = 0; index < componentArray.Length; index++)
    #                 {
    #                     Component detailComp = componentArray[index];

    #                     try
    #                     {
    #                         prompt($"({index + 1} of {componentArray.Length})");
    #                         DetailComponent(detailComp);
    #                     }
    #                     catch (Exception ex)
    #                     {
    #                         ex.__PrintException(detailComp.DisplayName);
    #                     }
    #                 }

    #                 SetFormDefaults();
    #             }
    #         }

    #         public static void SetWcsToWorkPart()
    #         {
    #             Block dynamic = __work_part_.__DynamicBlock();

    #             if (__work_part_.Tag == __display_part_.Tag)
    #             {
    #                 __display_part_.WCS.SetOriginAndMatrix(dynamic.__Origin(), dynamic.__Orientation());
    #                 return;
    #             }

    #             using (__work_component_.__UsingReferenceSetReset())
    #             {
    #                 __work_component_.__ReferenceSet("Entire Part");

    #                 CartesianCoordinateSystem system = __work_part_.CoordinateSystems.CreateCoordinateSystem(
    #                     _Point3dOrigin,
    #                     dynamic.__Orientation(),
    #                     false);

    #                 NXObject ject = __work_component_.FindOccurrence(system);

    #                 if (!(ject is CartesianCoordinateSystem cart))
    #                     throw new Exception();

    #                 __display_part_.WCS.SetOriginAndMatrix(_Point3dOrigin, cart.Orientation.Element);
    #                 ufsession_.Obj.DeleteObject(system.Tag);
    #             }
    #         }

    #         public static ModelingView GetPlanView()
    #         {
    #             ModelingView planView = null;

    #             foreach (ModelingView view in __work_part_.ModelingViews)
    #                 if (view.Name == ViewPlan)
    #                 {
    #                     planView = view;
    #                     break;
    #                 }

    #             return planView;
    #         }

    #         public static void MakePlanView(CartesianCoordinateSystem csys)
    #         {
    # 			// sql
    #             const string l1 = "L1";
    #             const string top = "Top";
    #             const string plan = "PLAN";
    #             __display_part_ = __work_part_;
    #             ModelingView planView = GetPlanView();
    #             ModelingView modelingView1, modelingView2;
    #             Layout layout;

    #             if (planView != null)
    #             {
    #                 layout = __work_part_.Layouts.FindObject(l1);
    #                 modelingView1 = __work_part_.ModelingViews.WorkView;
    #                 modelingView2 = __work_part_.ModelingViews.FindObject(top);
    #                 layout.ReplaceView(modelingView1, modelingView2, true);
    #                 ModelingView tempView = __work_part_.ModelingViews.FindObject(plan);
    #                 ufsession_.Obj.DeleteName(tempView.Tag);
    #             }

    #             ufsession_.View.SetViewMatrix("", 3, csys.Tag, null);
    #             View newView = __display_part_.Views.SaveAs(__display_part_.ModelingViews.WorkView, plan, false, false);
    #             layout = __display_part_.Layouts.FindObject(l1);
    #             modelingView1 = (ModelingView)newView;
    #             modelingView2 = __display_part_.ModelingViews.FindObject(top);
    #             layout.ReplaceView(modelingView1, modelingView2, true);
    #             session_.__DeleteObjects(csys);
    #         }

    #         private void DetailComponent(Component detailComp)
    #         {
    #             print("////////////////////////");

    #             if (!detailComp.__IsLoaded())
    #             {
    #                 print($"Component {detailComp.DisplayName} is not loaded");
    #                 print("4-VIEW will not be created for this component");

    #                 return;
    #             }

    #             using (session_.__UsingSuppressDisplay())
    #             {
    #                 __display_part_ = detailComp.__Prototype();

    #                 new CleanBodyRefSet().execute(__display_part_);

    #                 try
    #                 {
    #                     if (__work_part_.__HasDynamicBlock())
    #                         SetWcsToWorkPart();
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException();
    #                 }

    #                 //try
    #                 //{
    #                 //    MakePlanView(__display_part_.WCS.Save());
    #                 //}
    #                 //catch (NXException ex) when (ex.ErrorCode == 925019)
    #                 //{
    #                 //    print_($"Could not replace view in {__work_part_.Leaf}");
    #                 //}
    #                 //catch (Exception ex)
    #                 //{
    #                 //    ex.__PrintException();
    #                 //}

    #                 if (__display_part_.Layers.GetState(111) != State.WorkLayer)
    #                     __display_part_.Layers.SetState(111, State.Selectable);

    #                 using (new ResetShadeRendering())
    #                 {
    #                     PreferencesBuilder preferencesBuilder1 = __work_part_.SettingsManager.CreatePreferencesBuilder();

    #                     using (new Destroyer(preferencesBuilder1))
    #                         if (chkColorDetailSheet.Checked)
    #                         {
    #                             preferencesBuilder1.ViewStyle.ViewStyleShading.RenderingStyle = ShadingRenderingStyleOption.FullyShaded;
    #                             preferencesBuilder1.Commit();
    #                         }

    #                     ufsession_.Draw.SetDisplayState(1);
    #                     __display_part_.ModelingViews.WorkView.RenderingStyle = View.RenderingStyleType.ShadedWithEdges;

    #                     if (__display_part_.__TryGetRefset("BODY", out var dispRefSet))
    #                         foreach (NXObject refMember in dispRefSet.AskMembersInReferenceSet())
    #                         {
    #                             if (!(refMember is Curve lineLayer))
    #                                 continue;

    #                             if (lineLayer.Layer != 1)
    #                                 continue;

    #                             dispRefSet.RemoveObjectsFromReferenceSet(new[] { refMember });
    #                             lineLayer.Layer = 10;
    #                         }

    #                     if (chkHoleChart.Checked)
    #                         try
    #                         {
    #                             // set WCS to "PLAN" view and set "Top" as the work view
    #                             SetCsysToPlanView();
    #                             SetHoleChartLayers();
    #                             // get work view and part units and set lettering preferences
    #                             View workView = __display_part_.Views.WorkView;
    #                             SetLetteringPreferences(__display_part_.PartUnits);

    #                             List<NXObject> deleteNote = __display_part_.Notes
    #                                 .Cast<Note>()
    # 									// sql
    #                                 .Where(holeNote => holeNote.Layer == 230)
    #                                 .Cast<NXObject>()
    #                                 .ToList();

    #                             if (deleteNote.Count > 0)
    #                                 session_.__DeleteObjects(deleteNote.ToArray());

    #                             foreach (Body solidBody in __display_part_.Bodies)
    #                             {
    #                                 solidBody.Unblank();

    #                                 if (solidBody.Layer != 1 && solidBody.Layer != 94 && solidBody.Layer != 96)
    #                                     continue;

    #                                 foreach (Face cylFace in solidBody.GetFaces())
    #                                 {
    #                                     double[] point = new double[3];
    #                                     double[] dir = new double[3];
    #                                     double[] box = new double[6];
    #                                     ufsession_.Modl.AskFaceData(cylFace.Tag, out int type, point, dir, box,
    #                                         out double radius, out _, out _);

    #                                     if (cylFace.SolidFaceType != Face.FaceType.Cylindrical)
    #                                         continue;

    #                                     // Revision 1.45
    #                                     if (!cylFace.Name.ToUpper().Contains("HOLECHART"))
    #                                         continue;

    #                                     Point3d cfOrigin = point.__ToPoint3d();
    #                                     string[] cfNote = new string[1];
    #                                     double multiplier = __display_part_.PartUnits == BasePart.Units.Inches ? 1.0 : 25.4;

    #                                     foreach (string key in _holeChart.Keys)
    #                                         foreach (string value in _holeChart[key])
    #                                         {
    #                                             double holeDiameter = Convert.ToDouble(value);
    #                                             double faceDiameter = Convert.ToDouble(radius * 2);
    #                                             double difference = holeDiameter * .000000001;
    #                                             double abs = System.Math.Abs(holeDiameter * multiplier - faceDiameter);

    #                                             if (abs > difference * multiplier)
    #                                                 continue;

    #                                             cfNote[0] = key;
    #                                             break;
    #                                         }

    #                                     CreateHoleChartNote(cfOrigin, cfNote, workView.Tag);
    #                                 }
    #                             }

    #                             SetDefaultLayers();
    #                             print($"HoleCharted {__display_part_.Leaf}");
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException();
    #                         }

    #                     if (chkDetailSheet.Checked)
    #                         try
    #                         {
    #                             SetHoleChartLayers();
    #                             SetCsysToPlanView();

    #                             // delete existing 4-VIEW
    #                             List<NXObject> deleteView = __display_part_.DrawingSheets
    #                                 .Cast<DrawingSheet>()
    #                                 .Where(dwg => dwg.Name == "4-VIEW")
    #                                 .Cast<NXObject>()
    #                                 .ToList();

    #                             if (deleteView.Count > 0)
    #                                 session_.__DeleteObjects(deleteView.ToArray());

    #                             string[] drillChart = null;

    #                             if (chkDrillChart.Checked)
    #                             {
    # #pragma warning disable CS0612 // Type or member is obsolete
    #                                 drillChart = DrillChart.Main();
    # #pragma warning restore CS0612 // Type or member is obsolete
    #                                 print($"Drill Charted in {__display_part_.Leaf}");
    #                             }

    #                             CreateDetailSheet(drillChart);
    #                             SetDefaultLayers();
    #                             print($"Created 4-View in {__display_part_.Leaf}");
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException();
    #                         }

    #                     if (chkUpdateViews.Checked)
    #                         try
    #                         {
    #                             // update all views
    #                             SetDefaultLayers();

    #                             foreach (DrawingSheet dwg in __display_part_.DrawingSheets)
    #                             {
    #                                 // Revision 1.7 – 2018 / 02 / 09
    #                                 ufsession_.Draw.IsObjectOutOfDate(dwg.Tag, out bool outOfDate);

    #                                 if (!outOfDate)
    #                                     continue;

    #                                 dwg.Open();

    #                                 foreach (DraftingView drfView in dwg.GetDraftingViews())
    #                                 {
    #                                     drfView.Update();
    #                                     print($"Updated view {drfView.Name} in {__display_part_.Leaf}");
    #                                 }
    #                             }
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException();
    #                         }

    #                     if (!chkDelete4Views.Checked)
    #                         return;
    #                     // Revision • 1.62 – 2017 / 12 / 13
    #                     try
    #                     {
    #                         __display_part_.Notes
    #                             .ToArray()
    #                             .Where(note => note.Layer == 230)
    #                             .ToList()
    #                             .ForEach(__n => ufsession_.Obj.DeleteObject(__n.Tag));
    #                     }
    #                     catch (Exception ex)
    #                     {
    #                         ex.__PrintException();
    #                     }

    #                     // delete existing 4-VIEW
    #                     List<NXObject> deleteView1 = __display_part_.DrawingSheets.Cast<DrawingSheet>()
    #                         .Where(dwg => dwg.Name == "4-VIEW")
    #                         .Cast<NXObject>()
    #                         .ToList();

    #                     if (deleteView1.Count > 0)
    #                         session_.__DeleteObjects(deleteView1.ToArray());
    #                 }
    #             }
    #         }

    #         private static DraftingView ImportPlanView(double xPlacement, double yPlacement)
    #         {
    #             BaseViewBuilder baseViewBuilder = __work_part_.DraftingViews.CreateBaseViewBuilder(null);

    #             using (new Destroyer(baseViewBuilder))
    #             {
    #                 ModelingView planView = null;
    #                 ModelingView topView = null;
    #                 bool isPlan = false;
    #                 foreach (ModelingView mView in __work_part_.ModelingViews)
    #                     switch (mView.Name)
    #                     {
    #                         case "PLAN":
    #                             isPlan = true;
    #                             planView = mView;
    #                             break;
    #                         case "Top":
    #                             topView = mView;
    #                             break;
    #                     }

    #                 baseViewBuilder.SelectModelView.SelectedView = isPlan ? planView : topView;
    #                 baseViewBuilder.Style.ViewStyleBase.Part = __work_part_;
    #                 baseViewBuilder.Style.ViewStyleBase.PartName = __work_part_.FullPath;
    #                 using (__work_part_.LoadFully()) { }
    #                 baseViewBuilder.Style.ViewStyleGeneral.UVGrid = false;
    #                 baseViewBuilder.Style.ViewStyleGeneral.AutomaticAnchorPoint = false;
    #                 baseViewBuilder.Style.ViewStyleGeneral.Centerlines = false;
    #                 Point3d point = new Point3d(xPlacement, yPlacement, 0.0);
    #                 baseViewBuilder.Placement.Placement.SetValue(null, __work_part_.Views.WorkView, point);
    #                 NXObject nXObject1 = baseViewBuilder.Commit();
    #                 DraftingView nPlanView = (DraftingView)nXObject1;
    #                 return nPlanView;
    #             }
    #         }

    #         private static void AssignDraftObject(DraftingView drfView, CtsDimensionData dataToUse,
    #             ref UFDrf.Object dataToAssign)
    #         {
    #             dataToAssign.object_tag = dataToUse.DimEntity;
    #             dataToAssign.object_view_tag = drfView.Tag;
    #             dataToAssign.object_assoc_modifier = dataToUse.ExtPointId;
    #         }

    #         private static void DimensionView(
    #             DraftingView drfView,
    #             IReadOnlyList<double> drfViewPosition,
    #             double viewScale,
    #             IReadOnlyList<double> size,
    #             BasePart.Units partUnits
    #         )
    #         {
    #             // get all displayable objects for the current drafting view
    #             drfView.Update();
    #             Matrix3x3 viewMatrix = drfView.Matrix;
    #             List<DisplayableObject> objInView = new List<DisplayableObject>();
    #             Tag visObj = NXOpen.Tag.Null;

    #             do
    #             {
    #                 ufsession_.View.CycleObjects(drfView.Tag, UFView.CycleObjectsEnum.VisibleObjects, ref visObj);

    #                 if (visObj == NXOpen.Tag.Null)
    #                     continue;

    #                 ufsession_.Obj.AskTypeAndSubtype(visObj, out _, out _);
    #                 DisplayableObject visEdge = (DisplayableObject)NXObjectManager.Get(visObj);
    #                 objInView.Add(visEdge);
    #             }
    #             while (visObj != NXOpen.Tag.Null);

    #             // ask extreme of all displayed edges and then create CtsDimensionData for each edge
    #             List<CtsDimensionData> dimData = new List<CtsDimensionData>();

    #             foreach (DisplayableObject dispObj in objInView)
    #             {
    #                 double[] drfLocation = new double[2];
    #                 double[] extremePoint = new double[3];

    #                 switch (dispObj)
    #                 {
    #                     case Edge _:
    #                         double[] dirVectorX = viewMatrix.__AxisX().__ToArray();
    #                         double[] dirVectorY = viewMatrix.__AxisY().__ToArray();
    #                         double[] dirVectorZ = viewMatrix.__AxisZ().__ToArray();

    #                         ufsession_.Modl.AskExtreme(
    #                             dispObj.Tag,
    #                             dirVectorX,
    #                             dirVectorY,
    #                             dirVectorZ,
    #                             out _,
    #                             extremePoint);
    #                         break;
    #                     case Line _:
    #                         Line line = (Line)dispObj;
    #                         extremePoint = line.StartPoint.__ToArray();
    #                         break;
    #                     default:
    #                         continue;
    #                 }

    #                 ufsession_.View.MapModelToDrawing(drfView.Tag, extremePoint, drfLocation);

    #                 CtsDimensionData dimObject = new CtsDimensionData
    #                 {
    #                     DimXvalue = drfLocation[0],
    #                     DimYvalue = drfLocation[1],
    #                     DimEntity = dispObj.Tag,
    #                     Type = dispObj.GetType().ToString()
    #                 };

    #                 dimData.Add(dimObject);
    #             }

    #             // sort all CtsDimensionData objects to find mins and max
    #             if (dimData.Count <= 0)
    #                 return;

    #             CtsDimensionData[] objInfo = dimData.ToArray();
    #             Array.Sort(objInfo, CtsDimensionData.SortXdescending());

    #             CtsDimensionData CreateCtsData(int index, CtsDimensionData.ExtremePointId id)
    #             {
    #                 return new CtsDimensionData
    #                 {
    #                     DimEntity = objInfo[index].DimEntity,
    #                     DimXvalue = objInfo[index].DimXvalue,
    #                     DimYvalue = objInfo[index].DimYvalue,
    #                     ExtPointId = (int)id,
    #                     Type = objInfo[index].Type
    #                 };
    #             }

    #             CtsDimensionData minX = CreateCtsData(objInfo.Length - 1, CtsDimensionData.ExtremePointId.MinX);
    #             CtsDimensionData maxX = CreateCtsData(0, CtsDimensionData.ExtremePointId.MaxX);
    #             Array.Sort(objInfo, CtsDimensionData.SortYdescending());
    #             CtsDimensionData minY = CreateCtsData(objInfo.Length - 1, CtsDimensionData.ExtremePointId.MinY);
    #             CtsDimensionData maxY = CreateCtsData(0, CtsDimensionData.ExtremePointId.MaxY);
    #             minY.ExtPointId = (int)CtsDimensionData.ExtremePointId.MaxY;
    #             maxY.Type = objInfo[0].Type;

    #             switch (drfView.Name)
    #             {
    #                 case "4-VIEW-BOTTOM":
    #                     {
    #                         // get minX greatest Y vertex
    #                         FindEndPoints(ref minX, out Point3d vertex1, out Point3d vertex2);

    #                         double[] drfVertex1 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex1.__ToArray(), drfVertex1);

    #                         double[] drfVertex2 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex2.__ToArray(), drfVertex2);

    #                         minX.DimXvalue = drfVertex1[0] <= drfVertex2[0] ? drfVertex1[0] : drfVertex2[0];
    #                         minX.ExtPointId = drfVertex1[0] <= drfVertex2[0] ? (int)FirstEndPoint : (int)LastEndPoint;
    #                         minX.DimYvalue = drfVertex1[1] >= drfVertex2[1] ? drfVertex1[1] : drfVertex2[1];

    #                         // get maxX greatest Y vertex
    #                         FindEndPoints(ref maxX, out Point3d vertex3, out Point3d vertex4);

    #                         double[] drfVertex3 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex3.__ToArray(), drfVertex3);

    #                         double[] drfVertex4 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex4.__ToArray(), drfVertex4);

    #                         maxX.DimXvalue = drfVertex3[0] >= drfVertex4[0] ? drfVertex3[0] : drfVertex4[0];
    #                         maxX.ExtPointId = drfVertex3[0] >= drfVertex4[0] ? (int)FirstEndPoint : (int)LastEndPoint;
    #                         maxX.DimYvalue = drfVertex3[1] >= drfVertex4[1] ? drfVertex3[1] : drfVertex4[1];

    #                         // get minY greatest X vertex
    #                         FindEndPoints(ref minY, out Point3d vertex5, out Point3d vertex6);

    #                         double[] drfVertex5 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex5.__ToArray(), drfVertex5);

    #                         double[] drfVertex6 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex6.__ToArray(), drfVertex6);
    #                         minY.DimXvalue = drfVertex5[0] >= drfVertex6[0] ? drfVertex5[0] : drfVertex6[0];
    #                         minY.DimYvalue = drfVertex5[1] <= drfVertex6[1] ? drfVertex5[1] : drfVertex6[1];
    #                         minY.ExtPointId = drfVertex5[0] >= drfVertex6[0]
    #                             ? drfVertex5[1] <= drfVertex6[1] ? (int)FirstEndPoint : (int)LastEndPoint
    #                             : drfVertex5[1] <= drfVertex6[1]
    #                                 ? (int)FirstEndPoint
    #                                 : (int)LastEndPoint;

    #                         // get maxY greatest X vertex
    #                         FindEndPoints(ref maxY, out Point3d vertex7, out Point3d vertex8);

    #                         double[] drfVertex7 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex7.__ToArray(), drfVertex7);

    #                         double[] drfVertex8 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex8.__ToArray(), drfVertex8);

    #                         maxY.DimXvalue = drfVertex7[0] >= drfVertex8[0] ? drfVertex7[0] : drfVertex8[0];
    #                         maxY.DimYvalue = drfVertex7[0] >= drfVertex8[0]
    #                             ? drfVertex7[1] >= drfVertex8[1] ? drfVertex7[1] : drfVertex8[1]
    #                             : drfVertex7[1] >= drfVertex8[1]
    #                                 ? drfVertex7[1]
    #                                 : drfVertex8[1];
    #                         maxY.ExtPointId = drfVertex7[0] >= drfVertex8[0]
    #                             ? drfVertex7[1] >= drfVertex8[1] ? (int)FirstEndPoint : (int)LastEndPoint
    #                             : drfVertex7[1] >= drfVertex8[1]
    #                                 ? (int)FirstEndPoint
    #                                 : (int)LastEndPoint;
    #                         break;
    #                     }
    #                 case "4-VIEW-RIGHT":
    #                     {
    #                         // get minY least X vertex
    #                         FindEndPoints(ref minY, out Point3d vertex1, out Point3d vertex2);
    #                         double[] drfVertex1 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex1.__ToArray(), drfVertex1);
    #                         double[] drfVertex2 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex2.__ToArray(), drfVertex2);
    #                         minY.DimXvalue = drfVertex1[0] <= drfVertex2[0] ? drfVertex1[0] : drfVertex2[0];
    #                         minY.DimYvalue = drfVertex1[0] <= drfVertex2[0]
    #                             ? drfVertex1[1] <= drfVertex2[1] ? drfVertex1[1] : drfVertex2[1]
    #                             : drfVertex1[1] <= drfVertex2[1]
    #                                 ? drfVertex1[1]
    #                                 : drfVertex2[1];
    #                         minY.ExtPointId = drfVertex1[0] <= drfVertex2[0]
    #                             ? drfVertex1[1] <= drfVertex2[1] ? (int)FirstEndPoint : (int)LastEndPoint
    #                             : drfVertex1[1] <= drfVertex2[1]
    #                                 ? (int)FirstEndPoint
    #                                 : (int)LastEndPoint;
    #                         // get maxY least X vertex
    #                         FindEndPoints(ref maxY, out Point3d vertex3, out Point3d vertex4);
    #                         double[] drfVertex3 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex3.__ToArray(), drfVertex3);
    #                         double[] drfVertex4 = new double[2];
    #                         ufsession_.View.MapModelToDrawing(drfView.Tag, vertex4.__ToArray(), drfVertex4);
    #                         if (drfVertex3[0] <= drfVertex4[0])
    #                             maxY.DimXvalue = drfVertex3[0];
    #                         else
    #                             minY.DimXvalue = drfVertex4[0];
    #                         maxY.DimYvalue = drfVertex3[0] <= drfVertex4[0]
    #                             ? drfVertex3[1] >= drfVertex4[1] ? drfVertex3[1] : drfVertex4[1]
    #                             : drfVertex3[1] >= drfVertex4[1]
    #                                 ? drfVertex3[1]
    #                                 : drfVertex4[1];
    #                         maxY.ExtPointId = drfVertex3[0] <= drfVertex4[0]
    #                             ? drfVertex3[1] >= drfVertex4[1] ? (int)FirstEndPoint : (int)LastEndPoint
    #                             : drfVertex3[1] >= drfVertex4[1]
    #                                 ? (int)FirstEndPoint
    #                                 : (int)LastEndPoint;
    #                         break;
    #                     }
    #             }

    #             double dimSpace = partUnits == BasePart.Units.Inches ? .75 : 20;
    #             double xDistance = size[0];
    #             double zDistance = size[2];

    #             // orthoRight dimension placement and text value
    #             UFDrf.Text orthoRightDimText = new UFDrf.Text();
    #             double[] orthoRightDimOrigin = new double[3];
    #             orthoRightDimOrigin[0] = drfViewPosition[0] - zDistance / 2 - dimSpace * viewScale;
    #             orthoRightDimOrigin[1] = drfViewPosition[1];
    #             orthoRightDimOrigin[2] = 0;

    #             // orthoBottom horizontal dimension placement and text value
    #             UFDrf.Text orthoBtmDimText = new UFDrf.Text();
    #             double[] orthoBtmHorizDimOrigin = new double[3];
    #             orthoBtmHorizDimOrigin[0] = drfViewPosition[0];
    #             orthoBtmHorizDimOrigin[1] = drfViewPosition[1] + zDistance / 2 + dimSpace * viewScale;
    #             orthoBtmHorizDimOrigin[2] = 0;

    #             // orthoBottom vertical dimension placement and text value
    #             UFDrf.Text orthoBtmVertDimText = new UFDrf.Text();
    #             double[] orthoBtmVertDimOrigin = new double[3];
    #             orthoBtmVertDimOrigin[0] = drfViewPosition[0] + xDistance / 2 + dimSpace * viewScale;
    #             orthoBtmVertDimOrigin[1] = drfViewPosition[1];
    #             orthoBtmVertDimOrigin[2] = 0;
    #             UFDrf.Object drfObjMaxX = new UFDrf.Object();
    #             UFDrf.Object drfObjMinX = new UFDrf.Object();
    #             UFDrf.Object drfObjMaxY = new UFDrf.Object();
    #             UFDrf.Object drfObjMinY = new UFDrf.Object();
    #             ufsession_.Drf.InitObjectStructure(ref drfObjMaxX);
    #             ufsession_.Drf.InitObjectStructure(ref drfObjMinX);
    #             ufsession_.Drf.InitObjectStructure(ref drfObjMaxY);
    #             ufsession_.Drf.InitObjectStructure(ref drfObjMinY);

    #             if (drfView.Name == "4-VIEW-BOTTOM")
    #             {
    #                 AssignDraftObject(drfView, minX, ref drfObjMinX);
    #                 AssignDraftObject(drfView, maxX, ref drfObjMaxX);
    #                 AssignDraftObject(drfView, minY, ref drfObjMinY);
    #                 AssignDraftObject(drfView, maxY, ref drfObjMaxY);
    #                 ufsession_.Drf.CreateVerticalDim(ref drfObjMinY, ref drfObjMaxY, ref orthoBtmVertDimText,
    #                     orthoBtmVertDimOrigin, out _);
    #                 ufsession_.Drf.CreateHorizontalDim(ref drfObjMinX, ref drfObjMaxX, ref orthoBtmDimText,
    #                     orthoBtmHorizDimOrigin, out _);
    #             }

    #             if (drfView.Name != "4-VIEW-RIGHT")
    #                 return;

    #             AssignDraftObject(drfView, minY, ref drfObjMinY);
    #             AssignDraftObject(drfView, maxY, ref drfObjMaxY);

    #             ufsession_.Drf.CreateVerticalDim(
    #                 ref drfObjMinY,
    #                 ref drfObjMaxY,
    #                 ref orthoRightDimText,
    #                 orthoRightDimOrigin,
    #                 out _);
    #         }

    #         private static void FindEndPoints(ref CtsDimensionData maxY, out Point3d vertex3, out Point3d vertex4)
    #         {
    #             if (maxY.DimEntity.__ToTaggedObject() is Line line1)
    #             {
    #                 vertex3 = line1.StartPoint;
    #                 vertex4 = line1.EndPoint;
    #                 return;
    #             }

    #             Edge edge = (Edge)NXObjectManager.Get(maxY.DimEntity);
    #             edge.GetVertices(out vertex3, out vertex4);
    #         }

    #         private static void CreateHoleChartNote(Point3d noteOrigin, string[] holeDia, Tag view)
    #         {
    #             Session.UndoMarkId markIdNote = session_.SetUndoMark(Session.MarkVisibility.Invisible, "CreateOrNull Annotation");
    #             LetteringPreferences letteringPreferences1 = __work_part_.Annotations.Preferences.GetLetteringPreferences();

    #             UserSymbolPreferences userSymbolPreferences1 = __work_part_.Annotations.NewUserSymbolPreferences(
    #                 UserSymbolPreferences.SizeType.ScaleAspectRatio,
    #                 1.0,
    #                 1.0);

    #             Note note1 = __work_part_.Annotations.CreateNote(
    #                 holeDia,
    #                 noteOrigin,
    #                 AxisOrientation.Horizontal,
    #                 letteringPreferences1,
    #                 userSymbolPreferences1);

    #             note1.SetName("HOLECHARTNOTE");
    #             ufsession_.View.ConvertToModel(view, note1.Tag);
    #             letteringPreferences1.Dispose();
    #             userSymbolPreferences1.Dispose();
    #             session_.UpdateManager.DoUpdate(markIdNote);
    #             session_.DeleteUndoMark(markIdNote, "CreateOrNull Annotation");
    #         }

    #         private static void SetLayerVisibility(Tag viewToSet)
    #         {
    #             View viewObj = (View)NXObjectManager.Get(viewToSet);
    #             StateInfo[] layerVisibleInView = new StateInfo[256];

    #             for (int i = 0; i < layerVisibleInView.Length - 1; i++)
    #             {
    #                 layerVisibleInView[i].Layer = i + 1;
    #                 layerVisibleInView[i].State = State.Hidden;
    #             }

    #             layerVisibleInView[0].Layer = 1;
    #             layerVisibleInView[0].State = State.Visible;
    #             layerVisibleInView[95].Layer = 96;
    #             layerVisibleInView[95].State = State.Visible;
    #             layerVisibleInView[111].State = State.Visible;
    #             __display_part_.Layers.SetObjectsVisibilityOnLayer(viewObj, layerVisibleInView, true);
    #         }

    #         private static TextCfw CreateCfw(int color)
    #         {
    #             return new TextCfw(color, 1, LineWidth.Normal);
    #         }

    #         private static void SetLetteringPreferences(BasePart.Units units)
    #         {
    #             double size = units == BasePart.Units.Inches ? .125 : 3.175;

    #             using (var letteringPreferences = __display_part_.Annotations.Preferences.GetLetteringPreferences())
    #             {
    #                 Lettering generalText = new Lettering
    #                 {
    #                     Size = size,
    #                     CharacterSpaceFactor = 1.0,
    #                     AspectRatio = 1.0,
    #                     LineSpaceFactor = 1.0,
    #                     Cfw = CreateCfw(31),
    #                     Italic = false
    #                 };

    #                 letteringPreferences.SetGeneralText(generalText);

    #                 __display_part_.Annotations.Preferences.SetLetteringPreferences(letteringPreferences);
    #             }
    #         }

    #         private void SetDraftingPreferences(BasePart.Units units, double scale)
    #         {
    #             double unitMultiplier = units == BasePart.Units.Inches ? 1.0 : 25.4;

    #             using (LetteringPreferences letteringPreferences1 =
    #                    __work_part_.Annotations.Preferences.GetLetteringPreferences())
    #             {
    #                 Lettering CreateLettering(double value)
    #                 {
    #                     return new Lettering
    #                     {
    #                         Size = value * unitMultiplier * scale,
    #                         CharacterSpaceFactor = 0.9,
    #                         AspectRatio = 1.0,
    #                         LineSpaceFactor = 1.0,
    #                         Cfw = CreateCfw(7),
    #                         Italic = false
    #                     };
    #                 }

    #                 letteringPreferences1.SetDimensionText(CreateLettering(.125));
    #                 letteringPreferences1.SetAppendedText(CreateLettering(.0625));
    #                 letteringPreferences1.SetToleranceText(CreateLettering(.0625));
    #                 letteringPreferences1.SetGeneralText(CreateLettering(.125));
    #                 __work_part_.Annotations.Preferences.SetLetteringPreferences(letteringPreferences1);
    #             }

    #             using (LineAndArrowPreferences lineAndArrowPreferences1 = __work_part_.Annotations.Preferences.GetLineAndArrowPreferences())
    #             {
    #                 LineCfw Cfw(int color)
    #                 {
    #                     return new LineCfw(
    #                         color,
    #                         DisplayableObject.ObjectFont.Solid,
    #                         LineWidth.Thin);
    #                 }

    #                 lineAndArrowPreferences1.SetFirstExtensionLineCfw(Cfw(141));
    #                 lineAndArrowPreferences1.SetFirstArrowheadCfw(Cfw(173));
    #                 lineAndArrowPreferences1.SetFirstArrowLineCfw(Cfw(173));
    #                 lineAndArrowPreferences1.SetSecondExtensionLineCfw(Cfw(173));
    #                 lineAndArrowPreferences1.SetSecondArrowheadCfw(Cfw(173));
    #                 lineAndArrowPreferences1.SetSecondArrowLineCfw(Cfw(173));
    #                 lineAndArrowPreferences1.ArrowheadLength = .125 * unitMultiplier;
    #                 lineAndArrowPreferences1.ArrowheadIncludedAngle = 30.0;
    #                 lineAndArrowPreferences1.StubLength = 0.25 * unitMultiplier;
    #                 lineAndArrowPreferences1.TextToLineDistance = 0.0625 * unitMultiplier;
    #                 lineAndArrowPreferences1.LinePastArrowDistance = 0.125 * unitMultiplier;
    #                 lineAndArrowPreferences1.FirstPosToExtLineDist = 0.0625 * unitMultiplier;
    #                 lineAndArrowPreferences1.SecondPosToExtLineDist = 0.0625 * unitMultiplier;
    #                 lineAndArrowPreferences1.DatumLengthPastArrow = 0.0625 * unitMultiplier;
    #                 lineAndArrowPreferences1.TextOverStubSpaceFactor = 0.1 * unitMultiplier;
    #                 __display_part_.Annotations.Preferences.SetLineAndArrowPreferences(lineAndArrowPreferences1);
    #             }

    #             using (var dimensionPreferences = __display_part_.Annotations.Preferences.GetDimensionPreferences())
    #             {
    #                 dimensionPreferences.ExtensionLineDisplay = ExtensionLineDisplay.Two;
    #                 dimensionPreferences.ArrowDisplay = ArrowDisplay.Two;
    #                 dimensionPreferences.TextPlacement = TextPlacement.Automatic;
    #                 dimensionPreferences.TextOrientation = TextOrientation.Horizontal;
    #                 LinearTolerance linearTolerance1 = __display_part_.Annotations.Preferences.GetLinearTolerances();
    #                 linearTolerance1.PrimaryDimensionDecimalPlaces = units == BasePart.Units.Inches ? 3 : 2;
    #                 __display_part_.Annotations.Preferences.SetLinearTolerances(linearTolerance1);

    #                 using (var unitsFormatPreferences = dimensionPreferences.GetUnitsFormatPreferences())
    #                 {
    #                     if (chkDualDimensions.Checked)
    #                         unitsFormatPreferences.DualDimensionPlacement = DualDimensionPlacement.Below;

    #                     unitsFormatPreferences.PrimaryDimensionUnit = units == BasePart.Units.Inches
    #                         ? DimensionUnit.Inches
    #                         : DimensionUnit.Millimeters;

    #                     unitsFormatPreferences.PrimaryDimensionTextFormat = DimensionTextFormat.Decimal;
    #                     unitsFormatPreferences.DecimalPointCharacter = DecimalPointCharacter.Period;
    #                     unitsFormatPreferences.DisplayTrailingZeros = true;
    #                     unitsFormatPreferences.TolerancePlacement = TolerancePlacement.After;
    #                     dimensionPreferences.SetUnitsFormatPreferences(unitsFormatPreferences);
    #                     __work_part_.Annotations.Preferences.SetDimensionPreferences(dimensionPreferences);
    #                 }
    #             }
    #         }

    #         private static void SetViewPreferences()
    #         {
    #             ViewPreferences viewPreferences = __work_part_.ViewPreferences;
    #             viewPreferences.HiddenLines.HiddenlineColor = 0;
    #             viewPreferences.HiddenLines.HiddenlineFont = NXOpen.Preferences.Font.Dashed;
    #             viewPreferences.VisibleLines.VisibleColor = 0;
    #             viewPreferences.VisibleLines.VisibleWidth = NXOpen.Preferences.Width.Original;
    #             viewPreferences.SmoothEdges.SmoothEdgeColor = 0;
    #             viewPreferences.SmoothEdges.SmoothEdgeFont = NXOpen.Preferences.Font.Invisible;
    #             viewPreferences.SmoothEdges.SmoothEdgeWidth = NXOpen.Preferences.Width.Original;
    #             viewPreferences.General.AutomaticAnchorPoint = false;
    #             viewPreferences.General.Centerlines = false;
    #             __work_part_.Preferences.ColorSettingVisualization.MonochromeDisplay = false;
    #             __work_part_.Preferences.Drafting.DisplayBorders = false;
    #         }

    #         private static void SetCsysToPlanView()
    #         {
    #             // Revision 1.4 – 2017 – 06 – 15
    #             // This entire method was rewritten.
    #             try
    #             {
    #                 Layout layout = __work_part_.Layouts.FindObject("L1");
    #                 ModelingView backView = __work_part_.ModelingViews.FindObject("Back");
    #                 layout.ReplaceView(__work_part_.ModelingViews.WorkView, backView, true);

    #                 string viewName = __display_part_.ModelingViews.ToArray().Any(__k => __k.Name == "PLAN")
    #                     ? "PLAN"
    #                     : "Top";

    #                 ModelingView view = __display_part_.__FindModelingView(viewName);
    #                 layout.ReplaceView(backView, view, true);
    #                 __display_part_.WCS.SetOriginAndMatrix(view.Origin, view.Matrix);
    #             }
    #             catch (NXException ex) when (ex.ErrorCode == 925019)
    #             {
    #                 print($"Could not replace view in {__work_part_.Leaf}");
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException($"Part: {__work_part_.Leaf}");
    #             }
    #             finally
    #             {
    #                 __work_part_.ModelingViews.WorkView.UpdateDisplay();
    #             }
    #         }

    #         private void GetChildComponents(Component assembly)
    #         {
    #             foreach (Component child in assembly.GetChildren())
    #             {
    #                 if (child.IsSuppressed)
    #                 {
    #                     if (!IsNameValid(child))
    #                         continue;
    #                     print($"{child.DisplayName} is suppressed");
    #                     continue;
    #                 }

    #                 if (assembly.GetChildren() is null)
    #                     continue;

    #                 if (!IsNameValid(child))
    #                 {
    #                     GetChildComponents(child);
    #                     continue;
    #                 }

    #                 Tag instance = ufsession_.Assem.AskInstOfPartOcc(child.Tag);

    #                 if (instance == NXOpen.Tag.Null)
    #                     continue;

    #                 ufsession_.Assem.AskPartNameOfChild(instance, out string partName);

    #                 if (ufsession_.Part.IsLoaded(partName) == 1)
    #                 {
    #                     _allComponents.Add(child);
    #                     GetChildComponents(child);
    #                     continue;
    #                 }

    #                 ufsession_.Cfi.AskFileExist(partName, out int status);

    #                 if (status != 0)
    #                     continue;

    #                 ufsession_.Part.OpenQuiet(partName, out Tag partOpen, out _);

    #                 if (partOpen == NXOpen.Tag.Null)
    #                     continue;

    #                 _allComponents.Add(child);
    #                 GetChildComponents(child);
    #             }
    #         }

    #         public static bool IsNameValid(Component comp)
    #         {
    #             return Regex.IsMatch(comp.DisplayName, RegexDetail);
    #         }

    #         public static List<CtsAttributes> CreateMaterialList()
    #         {
    #             string getMaterial = FilePathUcf.PerformStreamReaderString(
    #                 ":MATERIAL_ATTRIBUTE_NAME:",
    #                 ":END_MATERIAL_ATTRIBUTE_NAME:");

    #             List<CtsAttributes> compMaterials = FilePathUcf.PerformStreamReaderList(
    #                 ":COMPONENT_MATERIALS:",
    #                 ":END_COMPONENT_MATERIALS:");

    #             foreach (CtsAttributes cMaterial in compMaterials)
    #                 cMaterial.AttrName = getMaterial != string.Empty ? getMaterial : "MATERIAL";

    #             return compMaterials;
    #         }

    #         private static void SetHoleChartLayers()
    #         {
    #             __display_part_.Layers.SetState(230, State.WorkLayer);
    #             SetLayers(1, 94, 96, 200, 231);
    #         }

    #         private static void SetDefaultLayers()
    #         {
    #             __display_part_.Layers.SetState(1, State.WorkLayer);
    #             SetLayers(94, 96, 99, 100, 111, 200, 230);
    #         }

    #         private static void SetLayers(params int[] layers)
    #         {
    #             using (StateCollection layerState = __display_part_.Layers.GetStates())
    #             {
    #                 foreach (Category category in __display_part_.LayerCategories)
    #                     if (category.Name == "ALL")
    #                         layerState.SetStateOfCategory(category, State.Hidden);
    #                 __display_part_.Layers.SetStates(layerState, true);
    #             }

    #             layers.Where(layer => __display_part_.Layers.GetState(layer) != State.WorkLayer)
    #                 .ToList()
    #                 .ForEach(layer => __display_part_.Layers.SetState(layer, State.Selectable));
    #         }

    #         private void SetFormDefaults()
    #         {
    #             chkHoleChart.Checked = false;
    #             chkDetailSheet.Checked = false;
    #             chkUpdateViews.Checked = false;
    #             chkDelete4Views.Checked = false;
    #             chkHoleChart.Checked = false;
    #             btnSelect.Enabled = false;
    #             btnSelectAll.Enabled = false;
    #             _allComponents.Clear();
    #         }

    #         private void ChkChart_CheckedChanged(object sender, EventArgs e)
    #         {
    #             if (chkDrillChart.Checked)
    #                 chkHoleChart.Checked = false;

    #             if (chkHoleChart.Checked)
    #                 chkDrillChart.Checked = false;
    #         }

    #         private double[][] GetMinsMaxs(Body body)
    #         {
    #             double[] minCorner = new double[3];
    #             double[] distances = new double[3];

    #             ufsession_.Modl.AskBoundingBoxAligned(body.Tag, __display_part_.WCS.CoordinateSystem.Tag, false, minCorner,
    #                 new double[3, 3], distances);

    #             return new[]
    #             {
    #                 minCorner,
    #                 distances
    #             };
    #         }

    #         private void CreateDetailSheet(string[] drillChart)
    #         {
    #             PreferencesBuilder prefBld = __work_part_.SettingsManager.CreatePreferencesBuilder();

    #             using (new Destroyer(prefBld))
    #             {
    #                 prefBld.ViewStyle.ViewStyleGeneral.ViewRepresentation = GeneralViewRepresentationOption.PreNx85Exact;
    #                 prefBld.ViewStyle.ViewStyleGeneral.ExtractedEdges = GeneralExtractedEdgesOption.None;
    #                 prefBld.Commit();
    #             }

    #             try
    #             {
    #                 const double baseWidthXDir = 11;
    #                 const double fitSheetXDir = .7;
    #                 const double baseHeightYDir = 8.5;
    #                 const double fitSheetYDir = .7;
    #                 const double borderSpace = 1;
    #                 const double viewSpace = 2;
    #                 const double viewMinFromBtm = 1;
    #                 double scale = 1;
    #                 const double increment = .125;

    #                 int bodyCount = __display_part_.Bodies
    #                     .Cast<Body>()
    #                     .Count(sBody1 => sBody1.Layer == 1);

    #                 if (bodyCount != 1)
    #                 {
    #                     print(
    #                             $"DetailPart Sheet will not be created.  {__display_part_.FullPath} :" +
    #                             $" Solid bodies on layer one = {bodyCount}"
    #                     );

    #                     return;
    #                 }

    #                 Body sBody = __display_part_.__SolidBodyLayer1OrNull();

    #                 if (sBody is null)
    #                 {
    #                     print($"Could not find solid body on layer 1 :' {__display_part_.Leaf}'");
    #                     return;
    #                 }

    #                 BasePart.Units units = __display_part_.PartUnits;
    #                 double scaledWidth;
    #                 double scaledHeight;
    #                 double[] minCorner = new double[3];
    #                 double[] distances = new double[3];

    #                 // import 4-VIEW border part
    #                 ImportPartModes modes = new ImportPartModes
    #                 {
    #                     layer_mode = 1,
    #                     group_mode = 1,
    #                     csys_mode = 0,
    #                     plist_mode = 0,
    #                     view_mode = 0,
    #                     cam_mode = false,
    #                     use_search_dirs = false
    #                 };

    #                 double[][] results = GetMinsMaxs(sBody);

    #                 Box3d_ boxSolid1 = new Box3d_(sBody);

    #                 //minCorner = boxSolid1.Origin.__ToArray();
    #                 distances = new[] { boxSolid1.XDistance, boxSolid1.YDistance, boxSolid1.ZDistance };

    #                 Body[] layer111SolidBodies = __display_part_.Bodies
    #                     .ToArray()
    #                     .Where(b => b.IsSolidBody && b.Layer == 111)
    #                     .ToArray();

    #                 double x = default;
    #                 double y = default;
    #                 double z = default;

    #                 foreach (Body body111 in layer111SolidBodies)
    #                 {
    #                     var box111 = new Box3d_(body111);
    #                     x = Math.Max(boxSolid1.XDistance, box111.XDistance);
    #                     y = Math.Max(boxSolid1.YDistance, box111.YDistance);
    #                     z = Math.Max(boxSolid1.ZDistance, box111.ZDistance);
    #                 }

    #                 double unitMultiplier = units == BasePart.Units.Inches ? 1.0 : 25.4;

    #                 double measureWidth = (distances[0] + distances[2]
    #                     + borderSpace * unitMultiplier * 2
    #                     + viewSpace * unitMultiplier)
    #                     / unitMultiplier;

    #                 double measureHeight = (distances[1] + distances[2] + borderSpace * unitMultiplier +
    #                                         viewSpace * unitMultiplier +
    #                                         viewMinFromBtm * unitMultiplier) / unitMultiplier;

    #                 if (measureWidth > baseWidthXDir * fitSheetXDir || measureHeight > baseHeightYDir * fitSheetYDir)
    #                     do
    #                     {
    #                         scale += increment;
    #                         scaledWidth = baseWidthXDir * fitSheetXDir * scale;
    #                         scaledHeight = baseHeightYDir * fitSheetYDir * scale;
    #                     }
    #                     while (scaledWidth < measureWidth || scaledHeight < measureHeight);

    #                 if (__display_part_.Expressions.ToArray().All(expression => expression.Name != "borderScale"))
    #                     using (session_.__UsingDoUpdate("Expression"))
    #                     {
    #                         __work_part_.Expressions.CreateWithUnits($"borderScale={scale}", null);
    #                     }

    #                 double sheetWidth = baseWidthXDir * unitMultiplier * scale;
    #                 double sheetHeight = baseHeightYDir * unitMultiplier * scale;

    #                 DrawingSheet.Unit drawingSheetUnits = units == BasePart.Units.Inches
    #                     ? DrawingSheet.Unit.Inches
    #                     : DrawingSheet.Unit.Millimeters;

    #                 DrawingSheet fourViewSheet = __display_part_.DraftingDrawingSheets.InsertSheet(
    #                     "4-VIEW",
    #                     drawingSheetUnits,
    #                     sheetHeight,
    #                     sheetWidth,
    #                     1,
    #                     1,
    #                     DrawingSheet.ProjectionAngleType.ThirdAngle);

    #                 SetDraftingPreferences(units, scale);
    #                 SetViewPreferences();

    #                 ufsession_.Part.Import(
    #                     _borderFile,
    #                     ref modes,
    #                     new double[] { 1, 0, 0, 0, 1, 0 },
    #                     new double[] { 0, 0, 0 },
    #                     scale,
    #                     out _);

    #                 Part temp = __display_part_;

    #                 try
    #                 {
    #                     if (chkDrillChart.Checked && drillChart.Length > 0)
    #                     {
    #                         Note note = (Note)session_.__FindByName(@"GRUMBLEGRUMBLE");
    #                         note.SetText(drillChart);
    #                     }
    #                     else
    #                         session_.__FindByName(@"GRUMBLEGRUMBLE").__Delete();
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException();
    #                 }

    #                 try
    #                 {
    #                     if (chkDtsPath.Checked)
    #                     {
    #                         Note note = (Note)session_.__FindByName(@"DTS_FILE_PATH");
    #                         note.SetText(new[] { __display_part_.FullPath });
    #                     }
    #                     else
    #                         session_.__FindByName(@"DTS_FILE_PATH").__Delete();
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException();
    #                 }

    #                 double xDistance = distances[0];
    #                 double yDistance = distances[1];
    #                 double zDistance = distances[2];
    #                 double[] pvRefPoint = new double[2];

    #                 pvRefPoint[0] = sheetWidth * .333 > xDistance
    #                     ? sheetWidth * .333
    #                     : borderSpace * unitMultiplier * scale + xDistance / 2;

    #                 pvRefPoint[1] = sheetHeight * .667 > yDistance
    #                     ? sheetHeight * .667
    #                     : (viewMinFromBtm * unitMultiplier + viewSpace * unitMultiplier) * scale + zDistance +
    #                       yDistance / 2;

    #                 DraftingView planDrfView = ImportPlanView(pvRefPoint[0], pvRefPoint[1]);
    #                 planDrfView.Update();
    #                 double[] orthogonalBtm = new double[2];
    #                 double[] orthogonalRight = new double[2];
    #                 orthogonalRight[0] = pvRefPoint[0] + xDistance / 2 + viewSpace * unitMultiplier * scale + zDistance / 2;
    #                 orthogonalRight[1] = pvRefPoint[1];
    #                 ufsession_.Draw.AddOrthographicView(fourViewSheet.Tag, planDrfView.Tag, UFDraw.ProjDir.ProjectRight,
    #                     orthogonalRight, out Tag rOrthoTag);
    #                 DraftingView rightDrfView = (DraftingView)NXObjectManager.Get(rOrthoTag);
    #                 rightDrfView.SetName("4-VIEW-RIGHT");
    #                 SetLayerVisibility(rOrthoTag);
    #                 StateInfo stateArray = new StateInfo(111, State.Visible);
    #                 __display_part_.Layers.SetObjectsVisibilityOnLayer(rightDrfView, new[] { stateArray }, true);
    #                 orthogonalBtm[0] = pvRefPoint[0];
    #                 orthogonalBtm[1] = pvRefPoint[1] - yDistance / 2 - viewSpace * unitMultiplier * .667 * scale -
    #                                    zDistance / 2;
    #                 ufsession_.Draw.AddOrthographicView(fourViewSheet.Tag, planDrfView.Tag, UFDraw.ProjDir.ProjectBelow,
    #                     orthogonalBtm, out Tag bOrthoTag);
    #                 DraftingView btmDrfView = (DraftingView)NXObjectManager.Get(bOrthoTag);
    #                 btmDrfView.SetName("4-VIEW-BOTTOM");
    #                 SetLayerVisibility(bOrthoTag);
    #                 __display_part_.Layers.SetObjectsVisibilityOnLayer(btmDrfView, new[] { stateArray }, true);

    #                 if (!__display_part_.__HasAttribute("DESCRIPTION"))
    #                     print("Does not have DESCRIPTION att");
    #                 else
    #                 {
    #                     string descValue = __display_part_.__GetAttribute("DESCRIPTION");

    #                     if (descValue.ToUpper() == "NITROGEN PLATE SYSTEM")
    #                         return;
    #                 }

    #                 DimensionView(btmDrfView, orthogonalBtm, scale, distances, units);
    #                 DimensionView(rightDrfView, orthogonalRight, scale, distances, units);

    #                 bool isWireTaper = false;
    #                 bool isWaitForDev = false;

    #                 foreach (NXObject.AttributeInformation attrNote in __display_part_.GetUserAttributes())
    #                 {
    #                     if (attrNote.Title.ToUpper() == "WTN")
    #                     {
    #                         string wtnValue = __display_part_.__GetAttribute(attrNote.Title);

    #                         if (wtnValue.ToUpper() == "YES")
    #                             isWireTaper = true;
    #                     }

    #                     if (attrNote.Title.ToUpper() != "WFTD")
    #                         continue;

    #                     string wfftValue =
    #                         __display_part_.__GetAttribute(attrNote.Title);

    #                     if (wfftValue.ToUpper() == "YES")
    #                         isWaitForDev = true;
    #                 }

    #                 List<NXObject> addToDelete = new List<NXObject>();

    #                 foreach (Note drfNote in __display_part_.Notes)
    #                 {
    #                     if (drfNote.Layer != 200)
    #                         continue;

    #                     string[] noteText = drfNote.GetText();

    #                     //Changed from "TSG STANDARD" to "STANDARD" - to work with the GE Border file. 2016-11-16 Duane VW
    #                     if (noteText[0].Contains("STANDARD") && !isWireTaper)
    #                         addToDelete.Add(drfNote);

    #                     if (noteText[0].Contains("WAITING FOR FINAL TRIM") && !isWaitForDev)
    #                         addToDelete.Add(drfNote);
    #                 }

    #                 if (addToDelete.Count != 0)
    #                     session_.__DeleteObjects(addToDelete.ToArray());
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException(__display_part_.Leaf);
    #             }
    #         }

    #         public struct CtsDimensionData : IComparable
    #         {
    #             public CtsDimensionData(string objType, Tag objectTag, double x, double y, ExtremePointId extremeId) : this()
    #             {
    #                 Type = objType;
    #                 DimEntity = objectTag;
    #                 DimXvalue = x;
    #                 DimYvalue = y;
    #             }

    #             public string Type { get; set; }

    #             public Tag DimEntity { get; set; }

    #             public double DimXvalue { get; set; }

    #             public double DimYvalue { get; set; }

    #             public int ExtPointId { get; set; }

    #             int IComparable.CompareTo(object obj)
    #             {
    #                 return string.CompareOrdinal(Type, ((CtsDimensionData)obj).Type);
    #             }

    #             private class SortXdescending_ : IComparer
    #             {
    #                 int IComparer.Compare(object x, object x1)
    #                 {
    #                     if (x is null && x1 is null) return 0;
    #                     if (x is null ^ x1 is null) return 1;
    #                     if (((CtsDimensionData)x).DimXvalue > ((CtsDimensionData)x1).DimXvalue) return -1;
    #                     return ((CtsDimensionData)x).DimXvalue < ((CtsDimensionData)x1).DimXvalue ? 1 : 0;
    #                 }
    #             }

    #             private class SortYdescending_ : IComparer
    #             {
    #                 public int Compare(object y, object y1)
    #                 {
    #                     if (y is null && y1 is null) return 0;
    #                     if (y is null ^ y1 is null) return 1;
    #                     if (((CtsDimensionData)y).DimYvalue > ((CtsDimensionData)y1).DimYvalue) return -1;
    #                     return ((CtsDimensionData)y).DimYvalue < ((CtsDimensionData)y1).DimYvalue ? 1 : 0;
    #                 }
    #             }

    #             public static IComparer SortXdescending()
    #             {
    #                 return new SortXdescending_();
    #             }

    #             public static IComparer SortYdescending()
    #             {
    #                 return new SortYdescending_();
    #             }

    #             public enum ExtremePointId
    #             {
    #                 None,
    #                 MinX,
    #                 MaxX,
    #                 MinY,
    #                 MaxY,
    #                 MinZ,
    #                 MaxZ
    #             }

    #             public enum EndPointAssociativity
    #             {
    #                 None = 0,
    #                 FirstEndPoint = UFConstants.UF_DRF_first_end_point,
    #                 LastEndPoint = UFConstants.UF_DRF_last_end_point
    #             }
    #         }

    #         [Obsolete]
    #         public static class DrillChart
    #         {
    #             private const string HoleChartText = @"U:\nxFiles\UfuncFiles\HoleChart.txt";

    #             private static Part __display_part_ => Session.GetSession().Parts.Display;

    #             public static string[] Main()
    #             {
    #                 string[] lines = File.ReadAllLines(HoleChartText)
    #                     .Where(s => !string.IsNullOrEmpty(s))
    #                     .Where(s => !string.IsNullOrWhiteSpace(s))
    #                     .Where(s => !s.StartsWith("//"))
    #                     .ToArray();

    #                 IList<string[]> holeChart = new List<string[]>();

    #                 for (int i = 1; i < lines.Length; i++)
    #                 {
    #                     string[] split = lines[i].Split('\t');

    #                     holeChart.Add(split);
    #                 }

    #                 // Get the solid body on layer 1
    #                 Body solidBody = __display_part_.__SolidBodyLayer1OrNull();

    #                 if (solidBody is null)
    #                     throw new ArgumentException("Display part does not have solid body on layer 1");

    #                 IDictionary<double, Tuple<int[], IList<Face>, string[]>> dict =
    #                     new Dictionary<double, Tuple<int[], IList<Face>, string[]>>();

    #                 foreach (Face face in solidBody.GetFaces())
    #                 {
    #                     if (face.SolidFaceType != Face.FaceType.Cylindrical)
    #                         continue;

    #                     if (!face.Name.ToUpper().Contains("HOLECHART"))
    #                         continue;

    #                     double[] point = new double[3];
    #                     double[] dir = new double[3];
    #                     double[] box = new double[6];

    #                     ufsession_.Modl.AskFaceData(face.Tag, out int _, point, dir, box, out double radius, out _, out _);

    #                     double diameter = radius * 2; // * 25.4;

    #                     string[] actualLine =
    #                     (
    #                         from line in holeChart
    #                         let tempRadius = double.Parse(line[1])
    #                         where System.Math.Abs(tempRadius - diameter) < .000000001
    #                         select line
    #                     ).FirstOrDefault();

    #                     if (actualLine is null)
    #                     {
    #                         print($"Couldn't find hole chart: {diameter}");

    #                         continue;
    #                     }

    #                     if (!dict.ContainsKey(diameter))
    #                         dict.Add(diameter,
    #                             new Tuple<int[], IList<Face>, string[]>(new[] { 0 }, new List<Face>(), actualLine));

    #                     dict[diameter].Item1[0]++;

    #                     dict[diameter].Item2.Add(face);
    #                 }

    #                 session_.__DeleteObjects(__display_part_.Layers.GetAllObjectsOnLayer(230).OfType<Note>().ToArray());

    #                 char letter = 'A';

    #                 IList<IList<string>> actualLines = new List<IList<string>>();

    #                 foreach (double diameter in dict.Keys)
    #                 {
    #                     Tuple<int[], IList<Face>, string[]> tuple = dict[diameter];
    #                     int count = tuple.Item1[0];
    #                     IList<string> list = new List<string>();
    #                     IList<Face> faces = tuple.Item2;
    #                     string[] message = tuple.Item3;
    #                     list.Add($"{letter} ");
    #                     string temp = message.Length == 3 ? $"{message[2]} " : $"{message[0]} ";
    #                     string[] split = Regex.Split(temp, "FOR\\s");
    #                     list.Add($"{split[0]}FOR");
    #                     list.Add(split[1]);
    #                     list.Add($"QTY {count}");
    #                     actualLines.Add(list);

    #                     foreach (Face face in faces)
    #                     {
    #                         double[] point = new double[3];
    #                         double[] dir = new double[3];
    #                         double[] box = new double[6];

    #                         ufsession_.Modl.AskFaceData(face.Tag, out int _, point, dir, box, out double _, out _, out _);

    #                         using (session_.__UsingDoUpdate())
    #                         {
    #                             using (LetteringPreferences letteringPreferences1 =
    #                                    __work_part_.Annotations.Preferences.GetLetteringPreferences())
    #                             using (UserSymbolPreferences userSymbolPreferences1 =
    #                                    __work_part_.Annotations.NewUserSymbolPreferences(
    #                                        UserSymbolPreferences.SizeType.ScaleAspectRatio,
    #                                        1.0,
    #                                        1.0))
    #                             {
    #                                 userSymbolPreferences1.SetLengthAndHeight(.125, .125);

    #                                 Note note1 = __work_part_.Annotations.CreateNote(
    #                                     new[] { $"{letter}" },
    #                                     point.__ToPoint3d(),
    #                                     AxisOrientation.Horizontal,
    #                                     letteringPreferences1,
    #                                     userSymbolPreferences1);

    #                                 note1.Layer = 230;

    #                                 note1.RedisplayObject();

    #                                 note1.SetName("HOLECHARTNOTE");
    #                                 ufsession_.View.ConvertToModel(__display_part_.ModelingViews.WorkView.Tag, note1.Tag);

    #                                 DraftingNoteBuilder draftingNoteBuilder1 =
    #                                     __work_part_.Annotations.CreateDraftingNoteBuilder(note1);

    #                                 using (session_.__UsingBuilderDestroyer(draftingNoteBuilder1))
    #                                 {
    #                                     draftingNoteBuilder1.Style.LetteringStyle.GeneralTextSize = .125;
    #                                     draftingNoteBuilder1.Commit();
    #                                 }
    #                             }
    #                         }
    #                     }

    #                     letter++;
    #                 }

    #                 IList<string> note = new List<string>();

    #                 foreach (IList<string> t in actualLines)
    #                 {
    #                     string _letter = t[0];
    #                     string drill = t[1];
    #                     string fastenr = t[2];
    #                     string quantity = t[3];
    #                     note.Add($"{_letter}{drill}");
    #                     note.Add($"{fastenr}{quantity}".ToUpper());
    #                     note.Add("");
    #                     string s = t.Aggregate("", (current, k) => current + k);
    #                     note.Add(s);
    #                 }

    #                 return note.ToArray();
    #             }
    #         }
    #     }
    pass


class UFuncAutoSizeComponent:
    #     public class AutoSizeComponent : _UFunc
    # {
    #     private const double Tolerance = .0001;
    #     private static UserDefinedClass _myUdoClass;

    #     public static int Startup()
    #     {
    #         const int retValue = 0;

    #         try
    #         {
    #             initializeUDO(false);
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException();
    #         }

    #         return retValue;
    #     }

    #     public static int initializeUDO(bool alertUser)
    #     {
    #         try
    #         {
    #             if (!(_myUdoClass is null))
    #             {
    #                 print("udo already exists");
    #                 return 0;
    #             }

    #             if (alertUser)
    #                 UI.GetUI()
    #                     .NXMessageBox.Show(
    #                         "UDO",
    #                         NXMessageBox.DialogType.Information,
    #                         "Registering C# UDO Class"
    #                     );

    #             // Define your custom UDO class
    #             _myUdoClass = session_.UserDefinedClassManager.CreateUserDefinedObjectClass(
    #                 "UdoAutoSizeComponent",
    #                 "Update Order Size"
    #             );
    #             // Setup properties on the custom UDO class
    #             _myUdoClass.AllowQueryClassFromName = UserDefinedClass.AllowQueryClass.On;
    #             // Register callbacks for the UDO class
    #             _myUdoClass.AddUpdateHandler(myUpdateCB);
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException();
    #         }

    #         return 0;
    #     }

    #     public static int myUpdateCB(UserDefinedLinkEvent updateEvent)
    #     {
    #         try
    #         {
    #             if (updateEvent.AssociatedObject is null)
    #                 return 0;

    #             int assocObjStatus = ufsession_.Obj.AskStatus(updateEvent.AssociatedObject.Tag);
    #             Tag solidBodyTag = updateEvent.AssociatedObject.Tag;
    #             Body udoBody = (Body)NXObjectManager.Get(solidBodyTag);
    #             Part updatePart = (Part)udoBody.OwningPart;

    #             if (assocObjStatus != 3)
    #                 return 0;

    #             int[] updateFlag = updateEvent.UserDefinedObject.GetIntegers();

    #             if (updateFlag[0] == 1)
    #                 SizeComponent(updatePart);

    #             return 0;
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException();
    #         }

    #         return 0;
    #     }

    #     public static int Main1()
    #     {
    #         const int retValue = 0;
    #         try
    #         {
    #             UserDefinedClass myUdoClass =
    #                 session_.UserDefinedClassManager.GetUserDefinedClassFromClassName(
    #                     "UdoAutoSizeComponent"
    #                 );

    #             if (myUdoClass is null)
    #                 return retValue;

    #             UserDefinedObject[] currentUdo =
    #                 __work_part_.UserDefinedObjectManager.GetUdosOfClass(myUdoClass);

    #             if (currentUdo.Length != 0)
    #                 SizeComponent(__work_part_);
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException();
    #         }

    #         return retValue;
    #     }

    #     public static void SizeComponent(Part updatePartSize)
    #     {
    #         try
    #         {
    #             bool isMetric = false;
    #             BasePart basePart = updatePartSize;

    #             if (basePart.PartUnits == BasePart.Units.Millimeters)
    #                 isMetric = true;

    #             foreach (Feature featDynamic in __work_part_.Features.ToArray())
    #             {
    #                 if (featDynamic.FeatureType != "BLOCK")
    #                     continue;

    #                 if (featDynamic.Name != "DYNAMIC BLOCK")
    #                     continue;

    #                 Block block1 = (Block)featDynamic;
    #                 Body[] sizeBody = block1.GetBodies();
    #                 BlockFeatureBuilder blockFeatureBuilderSize = __work_part_.Features.CreateBlockFeatureBuilder(block1);
    #                 blockFeatureBuilderSize.GetOrientation(out Vector3d xAxis, out Vector3d yAxis);

    #                 double[] initOrigin =
    #                 {
    #                     blockFeatureBuilderSize.Origin.X,
    #                     blockFeatureBuilderSize.Origin.Y,
    #                     blockFeatureBuilderSize.Origin.Z
    #                 };

    #                 double[] xVector = { xAxis.X, xAxis.Y, xAxis.Z };
    #                 double[] yVector = { yAxis.X, yAxis.Y, yAxis.Z };
    #                 double[] initMatrix = new double[9];
    #                 ufsession_.Mtx3.Initialize(xVector, yVector, initMatrix);
    #                 ufsession_.Csys.CreateMatrix(initMatrix, out Tag tempMatrix);
    #                 ufsession_.Csys.CreateTempCsys(initOrigin, tempMatrix, out Tag tempCsys);

    #                 if (tempCsys == Tag.Null)
    #                 {
    #                     UI.GetUI()
    #                         .NXMessageBox.Show(
    #                             "Auto Size Update Error",
    #                             NXMessageBox.DialogType.Error,
    #                             "Description update failed " + updatePartSize.FullPath
    #                         );
    #                     continue;
    #                 }

    #                 // get named expressions

    #                 bool isNamedExpression = false;

    #                 double xValue = 0,
    #                     yValue = 0,
    #                     zValue = 0;

    #                 string burnDirValue = string.Empty;
    #                 string burnoutValue = string.Empty;
    #                 string grindValue = string.Empty;
    #                 string grindTolValue = string.Empty;
    #                 string diesetValue = string.Empty;
    #                 NewMethod7(
    #                     ref isNamedExpression,
    #                     ref xValue,
    #                     ref yValue,
    #                     ref zValue,
    #                     ref burnDirValue,
    #                     ref burnoutValue,
    #                     ref grindValue,
    #                     ref grindTolValue,
    #                     ref diesetValue
    #                 );

    #                 burnDirValue = burnDirValue.Replace("\"", string.Empty);
    #                 burnoutValue = burnoutValue.Replace("\"", string.Empty);
    #                 grindValue = grindValue.Replace("\"", string.Empty);
    #                 grindTolValue = grindTolValue.Replace("\"", string.Empty);
    #                 diesetValue = diesetValue.Replace("\"", string.Empty);

    #                 if (isNamedExpression)
    #                 {
    #                     // get bounding box of solid body

    #                     double[] minCorner = new double[3];
    #                     double[,] directions = new double[3, 3];
    #                     double[] distances = new double[3];
    #                     double[] grindDistances = new double[3];

    #                     ufsession_.Modl.AskBoundingBoxExact(
    #                         sizeBody[0].Tag,
    #                         tempCsys,
    #                         minCorner,
    #                         directions,
    #                         distances
    #                     );
    #                     ufsession_.Modl.AskBoundingBoxExact(
    #                         sizeBody[0].Tag,
    #                         tempCsys,
    #                         minCorner,
    #                         directions,
    #                         grindDistances
    #                     );

    #                     NewMethod6(isMetric, xValue, yValue, zValue, burnoutValue, distances);

    #                     double xDist = distances[0];
    #                     double yDist = distances[1];
    #                     double zDist = distances[2];

    #                     double xGrindDist = grindDistances[0];
    #                     double yGrindDist = grindDistances[1];
    #                     double zGrindDist = grindDistances[2];

    #                     Array.Sort(distances);
    #                     Array.Sort(grindDistances);

    #                     // ReSharper disable once ConvertIfStatementToSwitchStatement
    #                     if (burnoutValue.ToLower() == "no" && grindValue.ToLower() == "no")
    #                     {
    #                         updatePartSize.SetUserAttribute(
    #                             "DESCRIPTION",
    #                             -1,
    #                             $"{distances[0]:f2} X {distances[1]:f2} X {distances[2]:f2}",
    #                             Update.Option.Now
    #                         );
    #                     }
    # 						// sql
    # 						// get this to work
    #                     else if (burnoutValue.ToLower() == "no" && grindValue.ToLower() == "yes")
    #                     {
    #                         // ReSharper disable once ConvertIfStatementToSwitchStatement
    #                         if (burnDirValue.ToLower() == "x")
    #                         {
    #                             NewMethod5(grindTolValue, distances, grindDistances, xGrindDist);
    #                         }

    #                         if (burnDirValue.ToLower() == "y")
    #                         {
    #                             NewMethod4(grindTolValue, distances, grindDistances, yGrindDist);
    #                         }

    #                         if (burnDirValue.ToLower() == "z")
    #                         {
    #                             NewMethod3(grindTolValue, distances, grindDistances, zGrindDist);
    #                         }
    #                     }
    #                     else if (grindValue.ToLower() == "yes")
    #                         NewMethod2(
    #                             burnDirValue,
    #                             grindTolValue,
    #                             xGrindDist,
    #                             yGrindDist,
    #                             zGrindDist
    #                         );
    #                     else
    #                         NewMethod1(burnDirValue, xDist, yDist, zDist);

    #                     if (diesetValue != "yes")
    #                         continue;

    #                     string description = updatePartSize.GetStringUserAttribute(
    #                         "DESCRIPTION",
    #                         -1
    #                     );

    #                     if (description.ToLower().Contains("dieset"))
    #                         continue;

    #                     description += " DIESET";

    #                     updatePartSize.SetUserAttribute(
    #                         "DESCRIPTION",
    #                         -1,
    #                         description,
    #                         Update.Option.Now
    #                     );
    #                 }
    #                 else
    #                 {
    #                     double[] distances = NewMethod(isMetric, sizeBody, tempCsys);
    #                     Array.Sort(distances);

    #                     updatePartSize.SetUserAttribute(
    #                         "DESCRIPTION",
    #                         -1,
    #                         $"{distances[0]:f2} X {distances[1]:f2} X {distances[2]:f2}",
    #                         Update.Option.Now
    #                     );

    #                     if (diesetValue != "yes")
    #                         continue;
    #                     string description = updatePartSize.GetStringUserAttribute(
    #                         "DESCRIPTION",
    #                         -1
    #                     );

    #                     if (description.ToLower().Contains("dieset"))
    #                         continue;
    #                     description += " DIESET";
    #                     updatePartSize.SetUserAttribute(
    #                         "DESCRIPTION",
    #                         -1,
    #                         description,
    #                         Update.Option.Now
    #                     );
    #                 }
    #             }

    #             // If the work part does not have a {"DESCRIPTION"} attribute then we want to return;.
    #             if (!updatePartSize.__HasAttribute("DESCRIPTION"))
    #                 return;

    #             // The string value of the {"DESCRIPTION"} attribute.
    #             string descriptionAtt = updatePartSize.__GetAttribute("DESCRIPTION");

    #             // Checks to see if the {_workPart} contains an expression with value {"yes"} and name of {lwrParallel} or {uprParallel}.
    #             if (
    #                 updatePartSize.Expressions.ToArray().Any(
    #                     exp =>
    #                         (
    #                             exp.Name.ToLower() == "lwrparallel"
    #                             || exp.Name.ToLower() == "uprparallel"
    #                         )
    #                         && exp.StringValue.ToLower() == "yes"
    #                 )
    #             )
    #                 // Appends {"Parallel"} to the end of the {"DESCRIPTION"}
    #                 // attribute string value and then sets the it to be the value of the {"DESCRIPTION"} attribute.
    #                 updatePartSize.SetUserAttribute(
    #                     "DESCRIPTION",
    #                     -1,
    #                     descriptionAtt + " PARALLEL",
    #                     Update.Option.Now
    #                 );
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException();
    #         }
    #     }

    #     private static void NewMethod7(
    #         ref bool isNamedExpression,
    #         ref double xValue,
    #         ref double yValue,
    #         ref double zValue,
    #         ref string burnDirValue,
    #         ref string burnoutValue,
    #         ref string grindValue,
    #         ref string grindTolValue,
    #         ref string diesetValue
    #     )
    #     {
    #         foreach (Expression exp in __work_part_.Expressions.ToArray())
    #         {
    #             if (exp.Name == "AddX")
    #             {
    #                 isNamedExpression = true;
    #                 xValue = exp.Value;
    #             }

    #             if (exp.Name == "AddY")
    #             {
    #                 isNamedExpression = true;
    #                 yValue = exp.Value;
    #             }

    #             if (exp.Name == "AddZ")
    #             {
    #                 isNamedExpression = true;
    #                 zValue = exp.Value;
    #             }

    #             if (exp.Name == "BurnDir")
    #             {
    #                 isNamedExpression = true;
    #                 burnDirValue = exp.RightHandSide;
    #             }

    #             if (exp.Name == "Burnout")
    #             {
    #                 isNamedExpression = true;
    #                 burnoutValue = exp.RightHandSide;
    #             }

    #             if (exp.Name == "Grind")
    #             {
    #                 isNamedExpression = true;
    #                 grindValue = exp.RightHandSide;
    #             }

    #             if (exp.Name == "GrindTolerance")
    #             {
    #                 isNamedExpression = true;
    #                 grindTolValue = exp.RightHandSide;
    #             }

    #             if (exp.Name == "DiesetNote")
    #                 diesetValue = exp.RightHandSide;
    #         }
    #     }

    #     private static void NewMethod6(
    #         bool isMetric,
    #         double xValue,
    #         double yValue,
    #         double zValue,
    #         string burnoutValue,
    #         double[] distances
    #     )
    #     {
    #         // add stock values

    #         distances[0] += xValue;
    #         distances[1] += yValue;
    #         distances[2] += zValue;

    #         if (isMetric)
    #             for (int i = 0; i < distances.Length; i++)
    #                 distances[i] /= 25.4d;

    #         if (burnoutValue.ToLower() == "no")
    #             distances.__RoundTo_125();
    #     }

    #     private static void NewMethod5(
    #         string grindTolValue,
    #         double[] distances,
    #         double[] grindDistances,
    #         double xGrindDist
    #     )
    #     {
    #         if (xGrindDist.__Sub(grindDistances[0]).__Abs() < Tolerance)
    #             __work_part_.__SetAttribute(
    #                 "DESCRIPTION",
    #                 $"{grindDistances[0]:f3} {grindTolValue} X {distances[1]:f2} X {distances[2]:f2}"
    #             );

    #         if (xGrindDist.__Sub(grindDistances[1]).__Abs() < Tolerance)
    #             __work_part_.__SetAttribute(
    #                 "DESCRIPTION",
    #                 $"{distances[0]:f2} X {grindDistances[1]:f3} {grindTolValue} X {distances[2]:f2}"
    #             );

    #         if (xGrindDist.__Sub(grindDistances[2]).__Abs() < Tolerance)
    #             __work_part_.__SetAttribute(
    #                 "DESCRIPTION",
    #                 $"{distances[0]:f2} X {distances[1]:f2} X {grindDistances[2]:f3} {grindTolValue}"
    #             );
    #     }

    #     private static void NewMethod4(
    #         string grindTolValue,
    #         double[] distances,
    #         double[] grindDistances,
    #         double yGrindDist
    #     )
    #     {
    #         if (yGrindDist.__Sub(grindDistances[0]) < Tolerance)
    #             __work_part_.__SetAttribute(
    #                 "DESCRIPTION",
    #                 $"{grindDistances[0]:f3}"
    #                     + " "
    #                     + grindTolValue
    #                     + " X "
    #                     + $"{distances[1]:f2}"
    #                     + " X "
    #                     + $"{distances[2]:f2}"
    #             );

    #         if (yGrindDist.__Sub(grindDistances[1]) < Tolerance)
    #             __work_part_.__SetAttribute(
    #                 "DESCRIPTION",
    #                 $"{distances[0]:f2}"
    #                     + " X "
    #                     + $"{grindDistances[1]:f3}"
    #                     + " "
    #                     + grindTolValue
    #                     + " X "
    #                     + $"{distances[2]:f2}"
    #             );

    #         if (yGrindDist.__Sub(grindDistances[2]) < Tolerance)
    #             __work_part_.__SetAttribute(
    #                 "DESCRIPTION",
    #                 $"{distances[0]:f2}"
    #                     + " X "
    #                     + $"{distances[1]:f2}"
    #                     + " X "
    #                     + $"{grindDistances[2]:f3}"
    #                     + " "
    #                     + grindTolValue
    #             );
    #     }

    #     private static void NewMethod3(
    #         string grindTolValue,
    #         double[] distances,
    #         double[] grindDistances,
    #         double zGrindDist
    #     )
    #     {
    #         if (System.Math.Abs(zGrindDist - grindDistances[0]) < Tolerance)
    #             __work_part_.SetUserAttribute(
    #                 "DESCRIPTION",
    #                 -1,
    #                 $"{grindDistances[0]:f3}"
    #                     + " "
    #                     + grindTolValue
    #                     + " X "
    #                     + $"{distances[1]:f2}"
    #                     + " X "
    #                     + $"{distances[2]:f2}",
    #                 Update.Option.Now
    #             );

    #         if (System.Math.Abs(zGrindDist - grindDistances[1]) < Tolerance)
    #             __work_part_.SetUserAttribute(
    #                 "DESCRIPTION",
    #                 -1,
    #                 $"{distances[0]:f2}"
    #                     + " X "
    #                     + $"{grindDistances[1]:f3}"
    #                     + " "
    #                     + grindTolValue
    #                     + " X "
    #                     + $"{distances[2]:f2}",
    #                 Update.Option.Now
    #             );

    #         if (System.Math.Abs(zGrindDist - grindDistances[2]) < Tolerance)
    #             __work_part_.SetUserAttribute(
    #                 "DESCRIPTION",
    #                 -1,
    #                 $"{distances[0]:f2}"
    #                     + " X "
    #                     + $"{distances[1]:f2}"
    #                     + " X "
    #                     + $"{grindDistances[2]:f3}"
    #                     + " "
    #                     + grindTolValue,
    #                 Update.Option.Now
    #             );
    #     }

    #     private static void NewMethod2(
    #         string burnDirValue,
    #         string grindTolValue,
    #         double xGrindDist,
    #         double yGrindDist,
    #         double zGrindDist
    #     )
    #     {
    #         if (burnDirValue.ToLower() == "x")
    #             __work_part_.SetUserAttribute(
    #                 "DESCRIPTION",
    #                 -1,
    #                 "BURN " + $"{xGrindDist:f3}" + " " + grindTolValue,
    #                 Update.Option.Now
    #             );

    #         if (burnDirValue.ToLower() == "y")
    #             __work_part_.SetUserAttribute(
    #                 "DESCRIPTION",
    #                 -1,
    #                 "BURN " + $"{yGrindDist:f3}" + " " + grindTolValue,
    #                 Update.Option.Now
    #             );

    #         if (burnDirValue.ToLower() == "z")
    #             __work_part_.SetUserAttribute(
    #                 "DESCRIPTION",
    #                 -1,
    #                 "BURN " + $"{zGrindDist:f3}" + " " + grindTolValue,
    #                 Update.Option.Now
    #             );
    #     }

    #     private static void NewMethod1(
    #         string burnDirValue,
    #         double xDist,
    #         double yDist,
    #         double zDist
    #     )
    #     {
    #         double distance;

    #         switch (burnDirValue.ToLower())
    #         {
    #             case "x":
    #                 distance = xDist;
    #                 break;
    #             case "y":
    #                 distance = yDist;
    #                 break;
    #             case "z":
    #                 distance = zDist;
    #                 break;
    #             default:
    #                 return;
    #         }

    #         __work_part_.__SetAttribute(
    #             "DESCRIPTION",
    #             $"BURN {distance:f2}"
    #         );
    #     }

    #     private static double[] NewMethod(bool isMetric, Body[] sizeBody, Tag tempCsys)
    #     {
    #         // get bounding box of solid body

    #         double[] minCorner = new double[3];
    #         double[,] directions = new double[3, 3];
    #         double[] distances = new double[3];

    #         ufsession_.Modl.AskBoundingBoxExact(
    #             sizeBody[0].Tag,
    #             tempCsys,
    #             minCorner,
    #             directions,
    #             distances
    #         );

    #         if (isMetric)
    #             for (int i = 0; i < distances.Length; i++)
    #                 distances[i] /= 25.4d;

    #         distances.__RoundTo_125();
    #         return distances;
    #     }

    #     public override void execute()
    #     {
    #     }

    #     public static void CreateAutoSizeUdo()
    #     {
    #         UserDefinedClass myUdOclass = null;

    #         try
    #         {
    #             myUdOclass = session_.UserDefinedClassManager.GetUserDefinedClassFromClassName(
    #                 "UdoAutoSizeComponent"
    #             );
    #         }
    #         catch (NXException ex) when (ex.ErrorCode == 1535022)
    #         {
    #             AutoSizeComponent.initializeUDO(false);
    #             myUdOclass = session_.UserDefinedClassManager.GetUserDefinedClassFromClassName(
    #                 "UdoAutoSizeComponent"
    #             );
    #         }

    #         if (myUdOclass is null)
    #             return;

    #         UserDefinedObject[] currentUdo = __work_part_.UserDefinedObjectManager.GetUdosOfClass(
    #             myUdOclass
    #         );

    #         if (currentUdo.Length != 0)
    #             return;

    #         BasePart myBasePart = __work_part_;
    #         UserDefinedObjectManager myUdOmanager = myBasePart.UserDefinedObjectManager;
    #         UserDefinedObject myUdo = myUdOmanager.CreateUserDefinedObject(myUdOclass);
    #         UserDefinedObject.LinkDefinition[] myLinks = new UserDefinedObject.LinkDefinition[1];
    #         int numBodies = __work_part_.Bodies.Cast<Body>().Count(body => body.Layer == 1);

    #         if (numBodies != 1)
    #             return;

    #         foreach (Body body in __work_part_.Bodies)
    #         {
    #             if (body.Layer != 1)
    #                 continue;

    #             myLinks[0].AssociatedObject = body;
    #             myLinks[0].Status = UserDefinedObject.LinkStatus.UpToDate;
    #             myUdo.SetLinks(UserDefinedObject.LinkType.Type1, myLinks);
    #             int[] updateOff = { 1 };
    #             myUdo.SetIntegers(updateOff);
    #         }
    #     }
    # }
    pass


class UFuncBlankDataBuilder:
    #      public partial class BlankDataBuilder : _UFuncForm
    #  {
    # 		// sql
    #      private const string dxfCmd = "dxfdwg.cmd /c ";
    #      private const string dxfSettings = "C:\\Program Files\\Siemens\\NX 11.0\\DXFDWG\\dxfdwg.def";
    #      private static Part workPart = session_.Parts.Work;
    #      private static Part displayPart = session_.Parts.Display;
    #      private static readonly string tempDir = Environment.GetEnvironmentVariable("TMP");
    #      private static string nameBuilder = "";
    #      private static string dxfArguments = "";

    #      public BlankDataBuilder()
    #      {
    #          try
    #          {
    #              InitializeComponent();
    #              InitializeFormData();
    #          }
    #          catch (Exception ex)
    #          {
    #              ex.__PrintException();
    #          }
    #      }

    #      private void ComboBoxOperation_SelectedIndexChanged(object sender, EventArgs e)
    #      {
    #          if (comboBoxOperation.Text == "Hot")
    #          {
    #              comboBoxVersion.Enabled = true;

    #              try
    #              {
    #                  List<int> names = new List<int>();

    #                  if (workPart.ComponentAssembly.RootComponent != null)
    #                  {
    #                      foreach (Component comp in workPart.ComponentAssembly.RootComponent.GetChildren())
    #                      {
    #                          int indexOf = comp.DisplayName.LastIndexOf("-V", StringComparison.Ordinal);
    #                          if (indexOf == -1) continue;
    #                          string fullCompName = comp.DisplayName.Substring(indexOf + 1);
    #                          string versionNumber = fullCompName.Substring(1, 2);
    #                          int.TryParse(versionNumber, out int testVersionNumber);
    #                          names.Add(testVersionNumber);
    #                      }

    #                      if (names.Count != 0)
    #                      {
    #                          names.Sort();
    #                          int lastVersionNumber = names[names.Count - 1];
    #                          if ((lastVersionNumber > 0) & (lastVersionNumber < 10))
    #                              comboBoxVersion.Text = "V0" + lastVersionNumber;
    #                          if ((lastVersionNumber > 9) & (lastVersionNumber < 100))
    #                              comboBoxVersion.Text = "V" + lastVersionNumber;
    #                      }
    #                      else
    #                      {
    #                          comboBoxVersion.Text = "";
    #                      }
    #                  }
    #              }

    #              catch (Exception ex)
    #              {
    #                  comboBoxVersion.Text = "";
    #                  ex.__PrintException();
    #              }
    #          }

    #          if (comboBoxOperation.Text != "Cold")
    #              return;

    #          comboBoxVersion.Enabled = true;

    #          try
    #          {
    #              List<int> names = new List<int>();

    #              if (workPart.ComponentAssembly.RootComponent is null)
    #                  return;

    #              foreach (Component comp in workPart.ComponentAssembly.RootComponent.GetChildren())
    #              {
    #                  int indexOf = comp.DisplayName.LastIndexOf("-V", StringComparison.Ordinal);
    #                  if (indexOf == -1) continue;
    #                  string fullCompName = comp.DisplayName.Substring(indexOf + 1);
    #                  string versionNumber = fullCompName.Substring(1, 2);

    #                  int.TryParse(versionNumber, out int testVersionNumber);
    #                  names.Add(testVersionNumber);
    #              }

    #              if (names.Count == 0)
    #              {
    #                  comboBoxVersion.Text = "";
    #                  return;
    #              }

    #              names.Sort();
    #              int lastVersionNumber = names[names.Count - 1] + 1;

    #              if ((lastVersionNumber > 0) & (lastVersionNumber < 10))
    #                  comboBoxVersion.Text = $"V0{lastVersionNumber}";

    #              if ((lastVersionNumber > 9) & (lastVersionNumber < 100))
    #                  comboBoxVersion.Text = $"V{lastVersionNumber}";
    #          }
    #          catch (Exception ex)
    #          {
    #              comboBoxVersion.Text = "";
    #              ex.__PrintException();
    #          }
    #      }

    #      private void ButtonSelect_Click(object sender, EventArgs e)
    #      {
    #          displayPart = session_.Parts.Display;
    #          workPart = session_.Parts.Work;

    #          const string prompt = "Select objects to export";
    #          const string title = "Export data";
    #          IntPtr clientData = IntPtr.Zero;

    #          ufsession_.Ui.LockUgAccess(UF_UI_FROM_CUSTOM);

    #          ufsession_.Ui.SelectWithClassDialog(prompt, title, UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY, null, clientData,
    #              out _, out _, out Tag[] selObjects);

    #          ufsession_.Ui.UnlockUgAccess(UF_UI_FROM_CUSTOM);

    #          foreach (Tag objs in selObjects)
    #              ufsession_.Disp.SetHighlight(objs, 0);

    #          // build export/dxf/component name
    #          // Add Current Date
    #          string currentDate = DateTime.Today.ToString("yyyy-MM-dd");

    #          if (selObjects.Length <= 0)
    #              return;

    #          try
    #          {
    #              if (textBoxJobNumber.Text != string.Empty)
    #                  nameBuilder = textBoxJobNumber.Text;

    #              if (comboBoxVersion.Text != string.Empty)
    #                  nameBuilder += $"-{comboBoxVersion.Text}";

    #              if (comboBoxOperation.Text != string.Empty)
    #              {
    #                  if (comboBoxOperation.Text == "Hot")
    #                      nameBuilder += $"-Hot-Blank-{currentDate}";

    #                  if (comboBoxOperation.Text == "Cold")
    #                      nameBuilder += $"-Cold-Blank-{currentDate}";
    #              }

    #              if (textBoxCustomText.Text != string.Empty)
    #                  nameBuilder += $"-{textBoxCustomText.Text}";

    #              // export temp part for dxf file
    #              string tempPart = $"{tempDir}\\{nameBuilder}";
    #              bool doesExist = false;

    #              if (displayPart.ComponentAssembly.RootComponent != null)
    #                  foreach (Component simComp in displayPart.ComponentAssembly.RootComponent.GetChildren())
    #                      if (simComp.Name == nameBuilder.ToUpper())
    #                          doesExist = true;

    #              if (doesExist)
    #              {
    #                  DialogResult dResult = MessageBox.Show($"Replace file {nameBuilder}?", "File Exist",
    #                      MessageBoxButtons.OKCancel, MessageBoxIcon.Question);

    #                  if (dResult != DialogResult.OK) return;
    #              }

    #              if (!(displayPart.ComponentAssembly.RootComponent is null))
    #                  foreach (Component simComp in displayPart.ComponentAssembly.RootComponent.GetChildren())
    #                  {
    #                      if (simComp.Name != nameBuilder.ToUpper())
    #                          continue;

    #                      Part closeSimPart = (Part)simComp.Prototype;
    #                      closeSimPart.Close(BasePart.CloseWholeTree.False, BasePart.CloseModified.CloseModified, null);
    #                      Session.UndoMarkId markId1 = session_.SetUndoMark(Session.MarkVisibility.Invisible, "");
    #                      NXObject[] objects1 = { simComp };
    #                      session_.UpdateManager.AddObjectsToDeleteList(objects1);
    #                      session_.UpdateManager.DoUpdate(markId1);
    #                  }

    #              BuildFilesExportDxf(tempPart, selObjects);
    #          }
    #          catch (Exception ex)
    #          {
    #              ex.__PrintException();
    #          }

    #          //Set FILENAME Part Attribute to name builder
    #      }

    #      private void ButtonReset_Click(object sender, EventArgs e)
    #      {
    #          try
    #          {
    #              InitializeFormData();
    #          }
    #          catch (Exception ex)
    #          {
    #              ex.__PrintException();
    #          }
    #      }

    #      private void InitializeFormData()
    #      {
    #          if (Session.GetSession().Parts.Display is null)
    #              return;

    #          displayPart = session_.Parts.Display;
    #          workPart = session_.Parts.Work;

    #          textBoxJobNumber.Text = string.Empty;

    #          comboBoxOperation.SelectedIndex = -1;
    #          comboBoxOperation.Items.Clear();

    #          comboBoxVersion.SelectedIndex = -1;
    #          comboBoxVersion.Items.Clear();

    #          textBoxCustomText.Clear();

    #          textBoxRevisionLevel.Clear();

    #          Match match = Regex.Match(workPart.Leaf, RegexSimulation);

    #          textBoxJobNumber.Text = match.Success ? match.Groups["customerNum"].Value : "JOB #";

    #          comboBoxOperation.Items.Add("Hot");
    #          comboBoxOperation.Items.Add("Cold");

    #          comboBoxVersion.Items.Add("V01");
    #          comboBoxVersion.Items.Add("V02");
    #          comboBoxVersion.Items.Add("V03");
    #          comboBoxVersion.Items.Add("V04");
    #          comboBoxVersion.Items.Add("V05");
    #          comboBoxVersion.Items.Add("V06");
    #          comboBoxVersion.Items.Add("V07");
    #          comboBoxVersion.Items.Add("V08");
    #          comboBoxVersion.Items.Add("V09");
    #          comboBoxVersion.Items.Add("V10");
    #          comboBoxVersion.Items.Add("V11");
    #          comboBoxVersion.Items.Add("V12");
    #          comboBoxVersion.Items.Add("V13");
    #          comboBoxVersion.Items.Add("V14");
    #          comboBoxVersion.Items.Add("V15");
    #          comboBoxVersion.Items.Add("V16");
    #          comboBoxVersion.Items.Add("V17");
    #          comboBoxVersion.Items.Add("V18");
    #          comboBoxVersion.Items.Add("V19");
    #          comboBoxVersion.Items.Add("V20");
    #          comboBoxVersion.Items.Add("V21");
    #          comboBoxVersion.Items.Add("V22");
    #          comboBoxVersion.Items.Add("V23");
    #          comboBoxVersion.Items.Add("V24");
    #          comboBoxVersion.Items.Add("V25");
    #      }

    #      private void BuildFilesExportDxf(string partFile, Tag[] tagObjects)
    #      {
    #          try
    #          {
    #              string versionNumber = comboBoxVersion.Text;

    #              if (string.IsNullOrEmpty(versionNumber))
    #                  throw new InvalidOperationException("Invalid version number.");

    #              GFolder folder = GFolder.create_or_null(displayPart)
    #                               ??
    #                               throw new InvalidOperationException(
    #                                   "The current display part does not reside within in a GFolder.");

    #              if (File.Exists(partFile + ".prt"))
    #                  File.Delete(partFile + ".prt");

    #              UFPart.ExportOptions exportOptions = new UFPart.ExportOptions
    #              {
    #                  new_part = true,
    #                  expression_mode = UFPart.ExportExpMode.CopyExpDeeply,
    #                  params_mode = UFPart.ExportParamsMode.RemoveParams
    #              };

    #              ufsession_.Part.ExportWithOptions(partFile, tagObjects.Length, tagObjects, ref exportOptions);

    #              // get path to blank location, check directory structure

    #              string outputDirectory = $"{folder.DirOutgoing}\\{TodaysDate}-Blank-{versionNumber}";

    #              if (!Directory.Exists(outputDirectory))
    #                  Directory.CreateDirectory(outputDirectory);

    #              string compBlanksPath = outputDirectory;

    #              // export part to Blanks directory

    #              if (Directory.Exists(compBlanksPath) == false)
    #                  Directory.CreateDirectory(compBlanksPath);

    #              compBlanksPath += "\\" + nameBuilder + ".prt";

    #              if (File.Exists(compBlanksPath))
    #                  File.Delete(compBlanksPath);

    #              ufsession_.Part.ExportWithOptions(compBlanksPath, tagObjects.Length, tagObjects, ref exportOptions);

    #              // add  component to Blanks file

    #              BasePart basePart1 = session_.Parts.OpenBase(compBlanksPath, out PartLoadStatus basePartLoadStatus);
    #              basePartLoadStatus.Dispose();

    #              Point3d sPartOrigin = new Point3d(0.0, 0.0, 0.0);
    #              Matrix3x3 sPartMatrix = _Matrix3x3Identity;

    #              int layer;

    #              switch (comboBoxOperation.Text)
    #              {
    #                  case "Cold":
    #                      layer = 101;
    #                      break;
    #                  case "Hot":
    #                      layer = 103;
    #                      break;
    #                  default:
    #                      layer = 1;
    #                      break;
    #              }

    #              Part surfacePart = (Part)basePart1;
    #              displayPart.ComponentAssembly.AddComponent(surfacePart, RefsetEntirePart, nameBuilder, sPartOrigin,
    #                  sPartMatrix, layer, out PartLoadStatus sPartLoadStatus);
    #              sPartLoadStatus.Dispose();

    #              displayPart.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);

    #              // export blank dxf data

    #              if (comboBoxOperation.Text != "Hot" && comboBoxOperation.Text != "Cold") return;
    #              string blankDxf =
    #                  Path.ChangeExtension(compBlanksPath,
    #                      "dxf"); //   $"{folder.JobFolder}\\blankDevelopment\\Blanks\\{nameBuilder}.dxf";
    #              string dxfBatch = partFile + ".bat";
    #              dxfArguments = $"{dxfCmd}\"{partFile}.prt\" o=\"{blankDxf}\" d=\"{dxfSettings}\"";

    #              using (FileStream fs = File.Open(dxfBatch, FileMode.Create))
    #              {
    #                  fs.Close();
    #              }

    #              using (StreamWriter writer = new StreamWriter(dxfBatch))
    #              {
    #                  writer.WriteLine("c:");
    #                  writer.WriteLine("cd " + "\"" + "C:\\Program Files\\Siemens\\NX 11.0\\DXFDWG" + "\"");
    #                  writer.WriteLine(dxfArguments);
    #                  writer.WriteLine("");
    #              }

    #              Process.Start(dxfBatch);
    #          }
    #          //Handle this exception somehow - Duane
    #          catch (Exception ex)
    #          {
    #              ex.__PrintException();
    #          }
    #      }

    #      private void ButtonSetAttribute_Click(object sender, EventArgs e)
    #      {
    #          // Add Current Date
    #          string currentDate = DateTime.Today.ToString("yyyy-MM-dd");

    #          if (textBoxJobNumber.Text != string.Empty)
    #              nameBuilder = textBoxJobNumber.Text;

    #          if (comboBoxVersion.Text != string.Empty)
    #              nameBuilder += $"-{comboBoxVersion.Text}";

    #          if (comboBoxOperation.Text != string.Empty)
    #          {
    #              if (comboBoxOperation.Text == "Hot")
    #                  nameBuilder += $"-Hot-Blank-{currentDate}";

    #              if (comboBoxOperation.Text == "Cold")
    #                  nameBuilder += $"-Cold-Blank-{currentDate}";
    #          }

    #          if (textBoxCustomText.Text != string.Empty)
    #              nameBuilder += $"-{textBoxCustomText.Text}";

    #          NXObject.AttributeInformation[] attrInfo = displayPart.GetUserAttributes();

    #          foreach (NXObject.AttributeInformation attr in attrInfo)
    #          {
    #              if (attr.Title != "REVISION TEXT")
    #                  continue;

    #              string attrValue = displayPart.GetStringUserAttribute(attr.Title, -1);

    #              if (attrValue == "")
    #              {
    #                  displayPart.SetUserAttribute("REVISION TEXT", -1, "", NXOpen.Update.Option.Now);
    #                  continue;
    #              }

    #              displayPart.SetUserAttribute("REVISION TEXT", -1, nameBuilder, NXOpen.Update.Option.Now);
    #              Layout layout1 = workPart.Layouts.FindObject("L1");
    #              layout1.ReplaceView(workPart.ModelingViews.WorkView, workPart.ModelingViews.WorkView, true);
    #          }

    #          textBoxRevisionLevel.Text = nameBuilder;
    #      }

    #      private void BlankDataBuilderForm_Load(object sender, EventArgs e)
    #      {
    #          Text = ufunc_rev_name;
    #          Location = Settings.Default.blank_data_builder_form_window_location;
    #      }

    #      private void BlankDataBuilderForm_FormClosed(object sender, FormClosedEventArgs e)
    #      {
    #          Settings.Default.blank_data_builder_form_window_location = Location;
    #          Settings.Default.Save();
    #      }
    #  }
    pass


class UFuncBlankDevelopment:
    #     public class BlankDevelopment : _UFunc
    # {
    #     public override void execute()
    #     {
    #         string message = $"{AssemblyFileVersion} - Blank Development";

    #         session_.SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name);
    #         Curve[] lengthObjs = Selection.SelectCurves(message, message);

    #         if (lengthObjs.Length == 0)
    #             return;

    #         // get total length of selected lines
    #         double addLength = lengthObjs.Select(selTag => (Curve)session_.__GetTaggedObject(selTag.Tag))
    #             .Select(selCurve => selCurve.GetLength())
    #             .Sum();

    #         // get user input for the line to develop
    #         Point3d cursorLocation = new Point3d();
    #         Line developObj = Selection.SelectSingleLine();

    #         if (developObj is null)
    #             return;

    #         // get user selection for which end of the line to extend
    #         double[] cursor = { cursorLocation.X, cursorLocation.Y, cursorLocation.Z };
    #         AskPositionOnObject(developObj.Tag, cursor);
    #         AskCloserToStartOrEnd(developObj.Tag, cursor);
    #         // move closest point distance and direction
    #         Line devLine = (Line)session_.__GetTaggedObject(developObj.Tag);
    #         EditCurveLength(devLine, addLength, cursor);
    #     }

    #     private static void EditCurveLength(Line editLine, double editLength, double[] cursor)
    #     {
    #         Section section1 = __work_part_.Sections.CreateSection(0.0095, 0.01, 0.5);
    #         CurveLengthBuilder builder = __work_part_.Features.CreateCurvelengthBuilder(null);

    #         using (session_.__UsingDoUpdate("Edit Curve Length"))
    #         using (session_.__UsingBuilderDestroyer(builder))
    #         {
    #             builder.Section = section1;
    #             builder.DistanceTolerance = 0.01;
    #             builder.CurveOptions.Associative = false;
    #             builder.CurveOptions.InputCurveOption = CurveOptions.InputCurve.Replace;
    #             builder.CurvelengthData.ExtensionMethod = ExtensionMethod.Incremental;
    #             builder.CurvelengthData.ExtensionSide = ExtensionSide.Symmetric;
    #             builder.CurvelengthData.ExtensionDirection = ExtensionDirection.Natural;
    #             section1.DistanceTolerance = 0.01;
    #             section1.ChainingTolerance = 0.0095;
    #             section1.SetAllowedEntityTypes(Section.AllowTypes.OnlyCurves);
    #             builder.CurvelengthData.ExtensionSide = ExtensionSide.StartEnd;
    #             Curve[] curves1 = new Curve[1];
    #             curves1[0] = editLine;
    #             CurveDumbRule curveDumbRule1 = __work_part_.ScRuleFactory.CreateRuleCurveDumb(curves1);
    #             section1.AllowSelfIntersection(true);
    #             SelectionIntentRule[] rules1 = new SelectionIntentRule[1];
    #             rules1[0] = curveDumbRule1;
    #             Point3d helpPoint1 = new Point3d(cursor[0], cursor[1], cursor[2]);
    #             section1.AddToSection(rules1, editLine, null, null, helpPoint1, Section.Mode.Create, false);
    #             builder.CurvelengthData.SetStartDistance(editLength.ToString());
    #             builder.CurvelengthData.SetEndDistance("0");
    #             builder.CurveOptions.InputCurveOption = CurveOptions.InputCurve.Retain;
    #             builder.Commit();
    #         }
    #     }

    #     private static void AskCloserToStartOrEnd(Tag curve, double[] cursorLocation)
    #     {
    #         double[] limits = new double[2];
    #         double[] startPoint = new double[3];
    #         double[] endPoint = new double[3];
    #         double[] derivatives = new double[3];
    #         double[] closestPoint = new double[3];
    #         ufsession_.Eval.Initialize(curve, out IntPtr evaluator);
    #         ufsession_.Eval.AskLimits(evaluator, limits);
    #         ufsession_.Eval.Evaluate(evaluator, 0, limits[0], startPoint, derivatives);
    #         ufsession_.Eval.Evaluate(evaluator, 0, limits[1], endPoint, derivatives);
    #         ufsession_.Eval.EvaluateClosestPoint(evaluator, cursorLocation, out _, closestPoint);
    #         ufsession_.Eval.Free(evaluator);
    #         ufsession_.Vec3.Distance(closestPoint, startPoint, out _);
    #         ufsession_.Vec3.Distance(closestPoint, endPoint, out _);
    #     }

    #     private static void MapViewToAbsolute(ref double[] cursorLocation)
    #     {
    #         double[] destinationCsys = { 0, 0, 0, 1, 0, 0, 0, 1, 0 };
    #         double[] refViewCsys = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    #         double[] outputMatrix = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    #         ufsession_.Ui.AskLastPickedView(out string viewName);
    #         View lastViewPicked = __work_part_.ModelingViews.FindObject(viewName);
    #         refViewCsys[3] = lastViewPicked.Matrix.Xx;
    #         refViewCsys[4] = lastViewPicked.Matrix.Xy;
    #         refViewCsys[5] = lastViewPicked.Matrix.Xz;
    #         refViewCsys[6] = lastViewPicked.Matrix.Yx;
    #         refViewCsys[7] = lastViewPicked.Matrix.Yy;
    #         refViewCsys[8] = lastViewPicked.Matrix.Yz;
    #         refViewCsys[9] = lastViewPicked.Matrix.Zx;
    #         refViewCsys[10] = lastViewPicked.Matrix.Zy;
    #         refViewCsys[11] = lastViewPicked.Matrix.Zz;
    #         ufsession_.Trns.CreateCsysMappingMatrix(refViewCsys, destinationCsys, outputMatrix, out _);
    #         ufsession_.Trns.MapPosition(cursorLocation, outputMatrix);
    #     }

    #     private static void MapAbsoluteToView(ref double[] cursorLocation)
    #     {
    #         double[] destinationCsys = { 0, 0, 0, 1, 0, 0, 0, 1, 0 };
    #         double[] refViewCsys = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    #         double[] outputMatrix = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    #         ufsession_.Ui.AskLastPickedView(out string viewName);
    #         View lastViewPicked = __work_part_.ModelingViews.FindObject(viewName);
    #         refViewCsys[3] = lastViewPicked.Matrix.Xx;
    #         refViewCsys[4] = lastViewPicked.Matrix.Xy;
    #         refViewCsys[5] = lastViewPicked.Matrix.Xz;
    #         refViewCsys[6] = lastViewPicked.Matrix.Yx;
    #         refViewCsys[7] = lastViewPicked.Matrix.Yy;
    #         refViewCsys[8] = lastViewPicked.Matrix.Yz;
    #         refViewCsys[9] = lastViewPicked.Matrix.Zx;
    #         refViewCsys[10] = lastViewPicked.Matrix.Zy;
    #         refViewCsys[11] = lastViewPicked.Matrix.Zz;
    #         ufsession_.Trns.CreateCsysMappingMatrix(destinationCsys, refViewCsys, outputMatrix, out _);
    #         ufsession_.Trns.MapPosition(cursorLocation, outputMatrix);
    #     }

    #     private static void AskPositionOnObject(Tag obj, double[] cursorLocation)
    #     {
    #         double[] cp = { 0, 0, 0 };
    #         UFCurve.Line lp;
    #         double[] startPoint = new double[3];
    #         double[] endPoint = new double[3];
    #         lp.start_point = startPoint;
    #         lp.end_point = endPoint;
    #         MapAbsoluteToView(ref cursorLocation);
    #         lp.start_point[0] = cursorLocation[0];
    #         lp.start_point[1] = cursorLocation[1];
    #         lp.start_point[2] = cursorLocation[2] + 10000;
    #         lp.end_point[0] = cursorLocation[0];
    #         lp.end_point[1] = cursorLocation[1];
    #         lp.end_point[2] = cursorLocation[2] - 10000;
    #         MapViewToAbsolute(ref lp.start_point);
    #         MapViewToAbsolute(ref lp.end_point);
    #         ufsession_.Curve.CreateLine(ref lp, out Tag aLine);
    #         ufsession_.Modl.AskMinimumDist(obj, aLine, 0, cp, 0, cp, out _, cursorLocation, cp);
    #         ufsession_.Obj.DeleteObject(aLine);
    #     }
    # }
    pass


class UFuncLayoutRefSets:
    #     internal class LayoutRefSets : _UFunc
    # {
    #     public override void execute()
    #     {
    #         print($"{ufunc_rev_name} - {__display_part_.Leaf}");
    #         session_.SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name);

    #         if (__display_part_ is null)
    #         {
    #             print("There is no displayed part loaded");
    #             return;
    #         }

    #         if (!__display_part_.Leaf.ToLower().EndsWith("-layout"))
    #         {
    #             print("Layout Refset can only be used on layouts.");
    #             return;
    #         }

    #         // BODY
    #         // BODY_NO_SLUG
    #         // INCOMING_SLUG
    #         // MATE
    #         string[] excluded_ref_sets = session_.__SqlReadMany(
    #             "tbl_properties",
    #             "LayoutRefSets_excluded_refsets"
    #         ).ToArray();

    #         ReferenceSet[] refsets = __display_part_.GetAllReferenceSets()
    #             .Where(r => r.Name != "BODY"
    #                         && r.Name != "BODY_NO_SLUG"
    #                         && r.Name != "INCOMING_BODY"
    #                         && r.Name != "MATE")
    #             .ToArray();

    #         foreach(var refset in refsets)
    #         {
    #             string refset_name = refset.Name;
    #             __display_part_.DeleteReferenceSet(refset);
    #             print($"Deleted ref set {refset_name}");
    #         }

    #         Body[] solid_bodies_layer_10 = __display_part_.Bodies
    #             .ToArray()
    #             .Where(b => b.IsSolidBody)
    #             .Where(b => b.Layer == 10)
    #             .ToArray();

    #         if (!__display_part_.__TryGetRefset("BODY", out ReferenceSet body_ref_set))
    #         {
    #             body_ref_set = __display_part_.CreateReferenceSet();
    #             body_ref_set.SetName("BODY");
    #             print("Created BODY refset");
    #         }

    #         body_ref_set.AddObjectsToReferenceSet(solid_bodies_layer_10);
    #         print($"Added {solid_bodies_layer_10.Length} body(s) to BODY refset.");

    #         // sql
    #         Body[] solid_bodies_layer_10_161 = solid_bodies_layer_10
    #             .Where(b => b.Color == 13)
    #             .ToArray();

    #         if (solid_bodies_layer_10_161.Length > 0)
    #         {
    #             if (!__display_part_.__TryGetRefset("BODY_NO_SLUG", out ReferenceSet body_no_slug_ref_set))
    #             {
    #                 body_no_slug_ref_set = __display_part_.CreateReferenceSet();
    #                 body_no_slug_ref_set.SetName("BODY_NO_SLUG");
    #                 print("Created BODY_NO_SLUG refset");
    #             }

    #             body_no_slug_ref_set.AddObjectsToReferenceSet(solid_bodies_layer_10_161);
    #             print($"Added {solid_bodies_layer_10_161.Length} body(s) to BODY_NO_SLUG refset.");
    #         }

    #         NXOpen.Layer.Category[] cats = __display_part_.LayerCategories.ToArray();

    #         for (int layer = 12; layer < 20; layer++)
    #             try
    #             {
    #                 Body[] solid_bodies = __display_part_.Bodies
    #                     .ToArray()
    #                     .Where(b => b.IsSolidBody)
    #                     .Where(b => b.Layer == layer)
    #                     .ToArray();

    #                 if (solid_bodies.Length == 0)
    #                     continue;

    #                 NXOpen.Layer.Category cat = cats.Where(c => c.Name != "ALL").FirstOrDefault(c => c.GetMemberLayers().ToHashSet().Contains(layer));

    #                 if (cat is null && solid_bodies.Length > 0)
    #                 {
    #                     print($"Layer {layer} has {solid_bodies.Length} but not layer category name");
    #                     continue;
    #                 }

    #                 string name = cat.Name;

    #                 ReferenceSet refset = null;

    #                 if (!__display_part_.__HasReferenceSet(name))
    #                 {
    #                     refset = __display_part_.CreateReferenceSet();
    #                     refset.SetName(name);
    #                     print($"Created Reference Set: {name}");
    #                 }
    #                 else
    #                     refset = __display_part_.__ReferenceSets(name);

    #                 refset.AddObjectsToReferenceSet(solid_bodies);
    #                 print($"Added {solid_bodies.Length} body(s) to ref set {name}");
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException();
    #             }
    #     }
    # }
    pass


class UFuncStripRefSetter:
    #      public class StripRefSetter : _UFunc
    #  {
    #      public override void execute()
    #      {
    #          print(ufunc_rev_name);

    #          if (__display_part_ is null)
    #          {
    #              print("There is no displayed part loaded");
    #              return;
    #          }

    #          // Need to remove the objects from the reference sets first.
    #          __SetUndoMark(MarkVisibility.Visible, ufunc_rev_name);

    #          if (!__display_part_.Leaf.ToLower().EndsWith("-strip"))
    #          {
    #              print("Strip Refsetter can only be used on a strip.");
    #              return;
    #          }

    #          NXObject[] layer100Components = __display_part_.ComponentAssembly.RootComponent
    #              .GetChildren()
    #              .Where(child => child.Layer == 100)
    #              .Cast<NXObject>()
    #              .ToArray();

    #          NXObject[] layer100Objects = __display_part_.Layers
    #              .GetAllObjectsOnLayer(100)
    #              .Where(obj => obj is Curve || obj is Body)
    #              .Where(obj => !obj.IsOccurrence)
    #              .Concat(layer100Components)
    #              .ToArray();

    #          NXObject[] layer101Components = __display_part_.ComponentAssembly.RootComponent
    #              .GetChildren()
    #              .Where(child => child.Layer == 101)
    #              .Cast<NXObject>()
    #              .ToArray();

    #          NXObject[] layer101Objects = __display_part_
    #              .Layers.GetAllObjectsOnLayer(101)
    #              .Where(obj => obj is Curve || obj is Body)
    #              .Where(obj => !obj.IsOccurrence)
    #              .Concat(layer101Components)
    #              .ToArray();

    #          NXObject[] layer102Components = __display_part_.ComponentAssembly.RootComponent
    #              .GetChildren()
    #              .Where(child => child.Layer == 102)
    #              .Cast<NXObject>()
    #              .ToArray();

    #          NXObject[] layer102Objects = __display_part_.Layers
    #              .GetAllObjectsOnLayer(102)
    #              .Where(obj => obj is Curve || obj is Body)
    #              .Where(obj => !obj.IsOccurrence)
    #              .Concat(layer102Components)
    #              .ToArray();

    #          NXObject[] presses = __display_part_.ComponentAssembly.RootComponent
    #              .GetChildren()
    #              .Where(child => child.Name.ToUpper().Contains("PRESS"))
    #              .Cast<NXObject>()
    #              .ToArray();

    #          __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners(
    #              "BODY_NO_SLUG",
    #              layer101Components
    #                  .Concat(layer102Components)
    #                  .Cast<Component>()
    #                  .ToArray()
    #          );

    #          __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners(
    #              "BODY",
    #              layer100Components
    #                  .Concat(presses)
    #                  .Cast<Component>()
    #                  .ToArray()
    #          );

    #          if (layer100Objects.Length > 0)
    #          {
    #              // WORK_PARTS
    #              const string WORK_PARTS = nameof(WORK_PARTS);
    #              ReferenceSet work_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == WORK_PARTS);

    #              if (work_parts_refset is null)
    #              {
    #                  work_parts_refset = __display_part_.CreateReferenceSet();
    #                  work_parts_refset.SetName(WORK_PARTS);
    #              }

    #              work_parts_refset.AddObjectsToReferenceSet(layer100Objects);
    #          }

    #          if (layer101Objects.Length > 0)
    #          {
    #              // LIFTED_PARTS
    #              const string LIFTED_PARTS = nameof(LIFTED_PARTS);
    #              ReferenceSet lifted_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == LIFTED_PARTS);

    #              if (lifted_parts_refset is null)
    #              {
    #                  lifted_parts_refset = __display_part_.CreateReferenceSet();
    #                  lifted_parts_refset.SetName(LIFTED_PARTS);
    #              }

    #              // set children to body-with-no-slugs reference set before adding
    #              lifted_parts_refset.AddObjectsToReferenceSet(layer101Objects);
    #          }

    #          if (layer100Objects.Length > 0
    #              || layer100Objects.Length > 0
    #              || layer102Objects.Length > 0
    #              || presses.Length > 0)
    #          {
    #              // ALL_WITH_PRESSES
    #              const string ALL_WITH_PRESSES = nameof(ALL_WITH_PRESSES);
    #              ReferenceSet all_with_presses_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == ALL_WITH_PRESSES);

    #              if (all_with_presses_refset is null)
    #              {
    #                  all_with_presses_refset = __display_part_.CreateReferenceSet();
    #                  all_with_presses_refset.SetName(ALL_WITH_PRESSES);
    #              }

    #              // set children to body reference set before adding
    #              all_with_presses_refset.AddObjectsToReferenceSet(layer100Objects);
    #              // set children to body-no-slugs reference set before adding
    #              all_with_presses_refset.AddObjectsToReferenceSet(layer101Objects);
    #              // set children to body-no-slugs reference set before adding
    #              all_with_presses_refset.AddObjectsToReferenceSet(layer102Objects);
    #              // set children to body reference set before adding
    #              all_with_presses_refset.AddObjectsToReferenceSet(presses);

    #              Component[] grippers = __display_part_.ComponentAssembly.RootComponent
    #                  .GetChildren()
    #                  .Where(child => child.Layer == 235)
    #                  .ToArray();

    #              __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners("BODY", grippers);
    #              all_with_presses_refset.AddObjectsToReferenceSet(grippers);
    #          }

    #          if (layer100Objects.Length > 0 || layer100Objects.Length > 0 || layer102Objects.Length > 0)
    #          {
    #              // ALL_PARTS
    #              const string ALL_PARTS = nameof(ALL_PARTS);
    #              ReferenceSet all_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == ALL_PARTS);

    #              if (all_parts_refset is null)
    #              {
    #                  all_parts_refset = __display_part_.CreateReferenceSet();
    #                  all_parts_refset.SetName(ALL_PARTS);
    #              }

    #              // set children to body reference set before adding
    #              all_parts_refset.AddObjectsToReferenceSet(layer100Objects);
    #              // set children to body-no-slugs reference set before adding
    #              all_parts_refset.AddObjectsToReferenceSet(layer101Objects);
    #              // set children to body-no-slugs reference set before adding
    #              all_parts_refset.AddObjectsToReferenceSet(layer102Objects);
    #          }

    #          // TRANSFER_PARTS
    #          if (layer102Components.Length > 0 && __display_part_.Leaf.ToLower().EndsWith("-900-strip"))
    #          {
    #              const string TRANSFER_PARTS = nameof(TRANSFER_PARTS);
    #              ReferenceSet transfer_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == TRANSFER_PARTS);

    #              if (transfer_parts_refset is null)
    #              {
    #                  transfer_parts_refset = __display_part_.CreateReferenceSet();
    #                  transfer_parts_refset.SetName(TRANSFER_PARTS);
    #              }

    #              // set children to body-no-slugs reference set before adding
    #              transfer_parts_refset.AddObjectsToReferenceSet(layer102Components);
    #          }

    #          if (!__display_part_.Leaf.ToLower().EndsWith("-010-strip")
    #              && (layer100Objects.Length > 0
    #              || layer100Objects.Length > 0
    #              || layer102Objects.Length > 0))
    #          {
    #              // PROG_ONLY_WORK
    #              const string PROG_ONLY_WORK = nameof(PROG_ONLY_WORK);
    #              ReferenceSet prog_only_work_refset =__display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == PROG_ONLY_WORK);

    #              if (prog_only_work_refset is null)
    #              {
    #                  prog_only_work_refset = __display_part_.CreateReferenceSet();
    #                  prog_only_work_refset.SetName(PROG_ONLY_WORK);
    #              }

    #              // set children to body reference set before adding
    #              prog_only_work_refset.AddObjectsToReferenceSet(layer100Objects
    #                  .Where(obj => !obj.Name.StartsWith("T"))
    #                  .ToArray());

    #              // set children to body-no-slugs reference set before adding
    #              prog_only_work_refset.AddObjectsToReferenceSet(layer101Objects
    #                  .Where(obj => !obj.Name.StartsWith("T"))
    #                  .ToArray());

    #              // set children to body-no-slugs reference set before adding
    #              prog_only_work_refset.AddObjectsToReferenceSet(layer102Objects
    #                  .Where(obj => !obj.Name.StartsWith("T"))
    #                  .ToArray());
    #          }

    #          prompt("Complete");
    #      }
    #  }
    pass


class UFuncExportStrip:
    #     public partial class ExportStrip : _UFuncForm
    # {
    # 	// sql
    #     public const string Regex_Strip = "^(?<customerNum>\\d+)-(?<opNum>\\d+)-strip$";
    #     public const string DummyPath = "G:\\0Library\\SeedFiles\\Components\\Dummy.prt";
    #     public const string Regex_PressAssembly = "^(?<customerNum>\\d+)-Press-(?<opNum>\\d+)-Assembly$";
    #     public const string Regex_Layout = "^(?<customerNum>\\d+)-(?<opNum>\\d+)-layout$";
    #     public const string Regex_Blank = "^(?<customerNum>\\d+)-(?<opNum>\\d+)-blank$";

    #     public ExportStrip()
    #     {
    #         InitializeComponent();

    #         bool Is010()
    #         {
    # 			// sql
    #             Regex opRegex = new Regex("^[0-9]{4,}-([0-9]{3,})");
    #             Match match = opRegex.Match(__display_part_.Leaf);

    #             if (!match.Success)
    #                 return false;

    #             return match.Groups[1].Value == "010";
    #         }

    #         bool Is900()
    #         {
    # 			// sql
    #             Regex opRegex = new Regex("^[0-9]{4,}-([0-9]{3,})");
    #             Match match = opRegex.Match(__display_part_.Leaf);

    #             if (!match.Success)
    #                 return false;

    #             return match.Groups[1].Value == "900";
    #         }

    #         if (Session.GetSession().Parts.Display is null)
    #             txtInput.Text = $@"{TodaysDate}-";
    #         else if (Is010())
    #             txtInput.Text = $@"{TodaysDate}-Strip";
    #         else if (Is900())
    #             txtInput.Text = $@"{TodaysDate}-FlowChart";

    #         txtInput.Focus();
    #         chkPart.Checked = true;
    #         chkSTP.Checked = true;
    #         chkPDF.Checked = true;
    #         btnAccept.Enabled = true;
    #     }

    #     private void BtnAccept_Click(object sender, EventArgs e)
    #     {
    #         using (session_.__UsingFormShowHide(this))
    #             try
    #             {
    #                 Export(
    #                     chkSTP.Checked,
    #                     (int)numUpDownCopies.Value,
    #                     chkPart.Checked,
    #                     chkPDF.Checked,
    #                     txtInput.Text,
    #                     chkCopy.Checked);
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException();
    #             }
    #             finally
    #             {
    #                 print("Complete");
    #             }
    #     }

    #     public static void CheckAssemblyDummyFiles()
    #     {
    #         if (__display_part_.ComponentAssembly.RootComponent is null)
    #             return;

    #         foreach (Component childOfStrip in __display_part_.ComponentAssembly.RootComponent.GetChildren())
    #         {
    #             if (childOfStrip.IsSuppressed)
    #                 continue;

    #             if (!(childOfStrip.Prototype is Part))
    #                 continue;

    #             if (!Regex.IsMatch(childOfStrip.DisplayName, Regex_PressAssembly, RegexOptions.IgnoreCase))
    #                 continue;

    #             if (childOfStrip.GetChildren().Length == 0)
    #                 throw new Exception($"A press exists in your assembly without any children. {childOfStrip.__AssemblyPathString()}");

    #             if (childOfStrip.GetChildren().Length == 1)
    #                 throw new Exception($"A press exists in your assembly with only one child. Expecting a ram and a bolster. {childOfStrip.__AssemblyPathString()}");

    #             if (childOfStrip.GetChildren().Length != 2)
    #                 continue;

    #             foreach (Component childOfPress in childOfStrip.GetChildren())
    #             {
    #                 if (!(childOfPress.Prototype is Part))
    #                     throw new Exception($"The child of a press must be loaded. {childOfPress.__AssemblyPathString()}");

    #                 if (childOfPress.IsSuppressed)
    #                     throw new Exception($"The child of a press cannot be suppressed. {childOfPress.__AssemblyPathString()}");

    #                 if (childOfPress.GetChildren().Length != 0
    #                     && childOfPress.GetChildren().Any(component => !component.IsSuppressed && component.Prototype is Part))
    #                     continue;

    #                 throw new Exception($"The child of a bolster or ram under a press must be the Dummy file: {DummyPath}{childOfPress.__AssemblyPathString()}");
    #             }

    #             break;
    #         }
    #     }

    #     public static void UpdateForStp()
    #     {
    #         HashSet<Part> partsToSave = new HashSet<Part>();
    #         Part currentD = __display_part_;
    #         Part currentW = session_.Parts.Work;

    #         try
    #         {
    #             foreach (Component child in session_.Parts.Work.ComponentAssembly.RootComponent.GetChildren())
    #             {
    #                 if (child.IsSuppressed)
    #                     continue;

    #                 if (!(child.Prototype is Part))
    #                     continue;

    #                 __display_part_ = child.__Prototype();

    #                 switch (child.ReferenceSet)
    #                 {
    #                     case "Empty":
    #                         continue;

    #                     default:
    #                         {
    #                             Part proto = (Part)child.Prototype;

    #                             ReferenceSet referenceSet = proto.GetAllReferenceSets().FirstOrDefault(refset => refset.Name == child.ReferenceSet);

    #                             if (referenceSet is null)
    #                                 continue;

    #                             NXObject[] objectsInReferenceSet = referenceSet.AskMembersInReferenceSet();

    #                             foreach (NXObject obj in objectsInReferenceSet)
    #                             {
    #                                 if (!(obj is DisplayableObject disp))
    #                                     continue;

    #                                 if (disp.Layer <= 1 || disp.Layer >= 256)
    #                                     continue;

    #                                 if (proto.Layers.GetState(disp.Layer) == State.WorkLayer)
    #                                     continue;

    #                                 proto.Layers.SetState(disp.Layer, State.Selectable);
    #                             }

    #                             session_.DisplayManager.UnblankObjects(objectsInReferenceSet.OfType<DisplayableObject>().ToArray());

    #                             partsToSave.Add(proto);
    #                         }

    #                         continue;
    #                 }
    #             }
    #         }
    #         finally
    #         {
    #             session_.Parts.SetDisplay(currentD, false, false, out _);
    #             session_.Parts.SetWork(currentW);
    #         }

    #         foreach (Part part in partsToSave)
    #             part.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);
    #     }

    #     private static void NewMethod(HashSet<Part> partsToSave, Component child)
    #     {
    #         Part proto = (Part)child.Prototype;
    #         ReferenceSet referenceSet = proto.GetAllReferenceSets().First(refset => refset.Name == child.ReferenceSet);

    #         NXObject[] objectsInReferenceSet = referenceSet.AskMembersInReferenceSet();

    #         foreach (NXObject obj in objectsInReferenceSet)
    #         {
    #             if (!(obj is DisplayableObject disp))
    #                 continue;

    #             if (disp.Layer <= 1 || disp.Layer >= 256)
    #                 continue;

    #             if (proto.Layers.GetState(disp.Layer) == State.WorkLayer)
    #                 continue;

    #             proto.Layers.SetState(disp.Layer, State.Selectable);
    #         }

    #         session_.DisplayManager.UnblankObjects(objectsInReferenceSet.OfType<DisplayableObject>().ToArray());

    #         partsToSave.Add(proto);
    #     }

    # 	// sql , not sql, remove all getcomponentofmany methods
    # 	// convert to descendants
    #     private static void Export(bool chkSTP, int numUpDownCopies, bool chkPart, bool chkPDF, string txtInput,
    #         bool chkCopy)
    #     {
    #         GFolder folder = GFolder.Create(__display_part_.FullPath);

    #         __display_part_.SetUserAttribute("DATE", -1, TodaysDate, NXOpen.Update.Option.Now);

    #         if (folder is null)
    #             throw new Exception("The current displayed part is not in a GFolder.");

    #         if (chkSTP)
    #         {
    #             Part currentD = __display_part_;
    #             Part currentW = session_.Parts.Work;

    #             try
    #             {
    #                 CheckAssemblyDummyFiles();

    #                 Part _currentD = __display_part_;
    #                 Part _currentW = session_.Parts.Work;

    #                 try
    #                 {
    #                     SetLayersInBlanksAndLayoutsAndAddDummies(__display_part_);
    #                 }
    #                 finally
    #                 {
    #                     session_.Parts.SetDisplay(_currentD, false, false, out _);
    #                     session_.Parts.SetWork(_currentW);
    #                 }
    #             }
    #             finally
    #             {
    #                 session_.Parts.SetDisplay(currentD, false, false, out _);
    #                 session_.Parts.SetWork(currentW);
    #             }
    #         }

    #         if (numUpDownCopies > 0)
    #             ExportStripPrintDrawing(numUpDownCopies);

    #         if (!chkPart && !chkPDF && !chkSTP)
    #             return;

    #         if (chkPDF)
    #             UpdateForPdf();

    #         //if (chkSTP)

    #         string outgoingFolderName = folder.CustomerNumber.Length == 6
    #             ? $"{folder.DirLayout}\\{txtInput}"
    #             : $"{folder.DirOutgoing}\\{txtInput}";

    #         if (Directory.Exists(outgoingFolderName))
    #         {
    #             if (MessageBox.Show(
    #                     $@"Folder {outgoingFolderName} already exists, is it okay to overwrite the files in the folder?",
    #                     @"Warning",
    #                     MessageBoxButtons.YesNo) != DialogResult.Yes)
    #                 return;

    #             Directory.Delete(outgoingFolderName, true);
    #         }

    #         Directory.CreateDirectory(outgoingFolderName);

    #         uf_.Ui.SetPrompt($"Export Strip: Setting layers in {__display_part_.Leaf}.");

    #         __work_part_.Layers.SetState(1, State.WorkLayer);

    # 		// sql
    #         for (int i = 2; i <= 256; i++)
    #             __work_part_.Layers.SetState(i, State.Hidden);

    #         new[] { 6, 10, 200, 201, 202, 254 }.ToList()
    #             .ForEach(i => __work_part_.Layers.SetState(i, State.Selectable));

    #         const string regex = "^\\d+-(?<op>\\d+)-.+$";

    #         string op = Regex.Match(session_.Parts.Work.Leaf, regex, RegexOptions.IgnoreCase).Groups["op"].Value;
    #         string commonString = $"{folder.CustomerNumber}-{op}-strip {TodaysDate}";

    #         uf_.Ui.SetPrompt(chkPart
    #             ? "Exporting \".prt\" file."
    #             : "Finding objects to export.");

    #         if (chkPDF)
    #         {
    #             uf_.Ui.SetPrompt("Exporting PDF......");

    #             string outputPath = ExportPDF(outgoingFolderName, commonString);

    #             print(File.Exists(outputPath)
    #                 ? $"Successfully created \"{outputPath}\"."
    #                 : $"Did not successfully create \"{outputPath}\".");
    #         }

    #         if (chkPart)
    #         {
    #             string outputPath = ExportStripPart(outgoingFolderName);

    #             print(File.Exists(outputPath)
    #                 ? $"Successfully created \"{outputPath}\"."
    #                 : $"Did not successfully create \"{outputPath}\".");
    #         }

    #         if (chkSTP)
    #         {
    #             UpdateForStp();

    #             ExportStripStp(outgoingFolderName);
    #             //string outputPath = $"{outgoingFolderName}\\{session_.Parts.Work.Leaf}-{TodaysDate}.stp";
    #             ////session_.Execute(@"C:\Repos\NXJournals\JOURNALS\export_strip.py", "ExportStrip", "export_stp", new object[] { outputPath });
    #             ////NXOpen.UF.UFSession.GetUFSession().Ui.SetPrompt("Exporting Step File.......");

    #             //NXOpen.StepCreator step = session_.DexManager.CreateStepCreator();

    #             //try
    #             //{
    #             //    //step.ExportDestination = NXOpen.BaseCreator.ExportDestinationOption.NativeFileSystem;

    #             //    //step.SettingsFile = "U:\\nxFiles\\Step Translator\\ExternalStep_AllLayers.def";

    #             //    //step.

    #             //    //step.ExportAs = NXOpen.StepCreator.ExportAsOption.Ap214;

    #             //    //step.InputFile = session_.Parts.Work.FullPath;

    #             //    //step.OutputFile = outputPath;

    #             //    //step.ProcessHoldFlag = true;

    #             //    step.Commit();
    #             //}
    #             //finally
    #             //{
    #             //    step.Destroy();
    #             //}

    #             //print_(File.Exists(outputPath)
    #             //    ? $"Successfully created \"{outputPath}\"."
    #             //: $"Did not successfully create \"{outputPath}\".");
    #         }

    #         uf_.Ui.SetPrompt($"Zipping up {outgoingFolderName}.");

    #         string[] filesToZip = Directory.GetFiles($"{outgoingFolderName}");

    #         string zipFileName = $"{folder.CustomerNumber}-{txtInput}.7z";

    #         string zipFile = $"{outgoingFolderName}\\{zipFileName}";

    #         if (filesToZip.Length != 0)
    #         {
    #             Zip7 zip = new Zip7(zipFile, filesToZip);

    #             zip.Start();

    #             zip.WaitForExit();
    #         }

    #         if (chkCopy)
    #         {
    #             if (!Directory.Exists(folder.DirProcessSimDataDesign))
    #                 Directory.CreateDirectory(folder.DirProcessSimDataDesign);

    #             string[] zipFiles = Directory.GetFiles(folder.DirProcessSimDataDesign, "*.7z",
    #                 SearchOption.TopDirectoryOnly);

    #             foreach (string zipFile1 in zipFiles)
    #                 // ReSharper disable once SwitchStatementMissingSomeCases
    #                 switch (MessageBox.Show($@"Delete file ""{zipFile1}""", @"Warning", MessageBoxButtons.YesNo))
    #                 {
    #                     case DialogResult.Yes:
    #                         File.Delete(zipFile1);
    #                         break;
    #                     case DialogResult.No:
    #                         break;
    #                     default:
    #                         throw new ArgumentException();
    #                 }

    #             File.Copy(zipFile, $"{folder.DirProcessSimDataDesign}\\{zipFileName}", true);
    #         }

    #         session_.ApplicationSwitchImmediate("UG_APP_MODELING");

    #         session_.Parts.Work.Drafting.ExitDraftingApplication();
    #     }

    #     public static void UpdateForPdf()
    #     {
    #         DrawingSheet[] sheets = session_.Parts.Work.DrawingSheets.ToArray();

    #         switch (sheets.Length)
    #         {
    #             case 0:
    #                 throw new InvalidOperationException("Current work part doesn't not have a sheet to print.");
    #             case 1:
    #                 session_.ApplicationSwitchImmediate("UG_APP_DRAFTING");
    #                 sheets[0].Open();
    #                 uf_.Draw.IsObjectOutOfDate(sheets[0].Tag, out bool outOfDate);
    #                 if (outOfDate)
    #                     uf_.Draw.UpdOutOfDateViews(sheets[0].Tag);
    #                 sheets[0].OwningPart.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);
    #                 break;
    #             default:
    #                 throw new InvalidOperationException("Current work part contains more than 1 sheet.");
    #         }
    #     }

    #     public static string ExportPDF(string outPutPath, string fileName)
    #     {
    #         DrawingSheet[] sheets = session_.Parts.Work.DrawingSheets.ToArray();

    #         ExportStripPdf(session_.Parts.Work.FullPath, sheets[0].Name, $"{outPutPath}\\{fileName}.pdf");

    #         return $"{outPutPath}\\{fileName}.pdf";
    #     }

    #     private static void AddDummy(Part part, IEnumerable<int> layers)
    #     {
    #         Prompt($"Setting layers in {__display_part_.Leaf}.");

    #         int[] layerArray = layers.ToArray();

    #         __display_part_.Layers.WorkLayer = 1;

    #         for (int i = 2; i < +256; i++)
    #             if (layerArray.Contains(i))
    #                 __display_part_.Layers.SetState(i, State.Selectable);
    #             else
    #                 __display_part_.Layers.SetState(i, State.Hidden);

    #         __display_part_.Layers.SetState(layerArray.Min(), State.WorkLayer);

    #         __display_part_.Layers.SetState(1, State.Hidden);

    #         if (part.ComponentAssembly.RootComponent != null)
    #         {
    #             Component validChild = part.ComponentAssembly.RootComponent
    #                 .GetChildren()
    #                 .Where(component => component.Prototype is Part)
    #                 .FirstOrDefault(component => !component.IsSuppressed);

    #             if (validChild != null)
    #                 return;
    #         }

    #         Part dummyPart = session_.__FindOrOpen(DummyPath);

    #         Prompt($"Adding dummy file to {part.Leaf}.");

    #         session_.Parts.Work.ComponentAssembly.AddComponent(dummyPart, "Entire Part", "DUMMY", _Point3dOrigin,
    #             _Matrix3x3Identity, 1, out PartLoadStatus status);

    #         status.Dispose();
    #     }

    #     public static void Prompt(string message)
    #     {
    #         UFSession.GetUFSession().Ui.SetPrompt(message);
    #     }

    #     private void SetAcceptButtonEnabled()
    #     {
    #         btnAccept.Enabled = chkPart.Checked || chkPDF.Checked || chkSTP.Checked || numUpDownCopies.Value > 0;
    #     }

    #     private void ChkBoxes_CheckedChanged(object sender, EventArgs e)
    #     {
    #         SetAcceptButtonEnabled();
    #     }

    #     private void NumUpDownCopies_ValueChanged(object sender, EventArgs e)
    #     {
    #         SetAcceptButtonEnabled();
    #     }

    #     public static List<Component> Descendants(Component parent)
    #     {
    #         List<Component> _list = new List<Component>
    #         {
    #             parent
    #         };

    #         foreach (Component _child in parent.GetChildren())
    #             _list.AddRange(Descendants(_child));

    #         return _list;
    #     }

    #     public static void SetLayersInBlanksAndLayoutsAndAddDummies(Part snapStrip010)
    #     {
    #         if (!Regex.IsMatch(snapStrip010.Leaf, Regex_Strip, RegexOptions.IgnoreCase))
    #             throw new ArgumentException(@"Must be an op 010 strip.", nameof(snapStrip010));

    #         Part currentD = __display_part_;
    #         Part currentW = session_.Parts.Work;

    #         try
    #         {
    #             Regex blankNameRegex = new Regex("^BLANK-([0-9]{1,})$");

    #             Regex layoutNameRegex = new Regex("^LAYOUT-([0-9]{1,})$");

    #             Part layoutPart = Descendants(__display_part_.ComponentAssembly.RootComponent)
    #                 .Select(component => component.Prototype)
    #                 .OfType<Part>()
    #                 .FirstOrDefault(component => Regex.IsMatch(component.Leaf, Regex_Layout, RegexOptions.IgnoreCase));

    #             //var blankPart = TSG_Library.Extensions.DisplayPart.RootComponent.Children
    #             Part blankPart = Descendants(__display_part_.ComponentAssembly.RootComponent)
    #                 .Select(component => component.Prototype)
    #                 .OfType<Part>()
    #                 .FirstOrDefault(component => Regex.IsMatch(component.Leaf, Regex_Blank, RegexOptions.IgnoreCase));

    #             HashSet<int> layoutLayers = new HashSet<int>();

    #             HashSet<int> blankLayers = new HashSet<int>();

    #             foreach (Component child in Descendants(__display_part_.ComponentAssembly.RootComponent))
    #             {
    #                 if (!(child.Prototype is Part))
    #                     continue;

    #                 if (child.IsSuppressed)
    #                     continue;

    #                 Match blankMatch = blankNameRegex.Match(child.Name);

    #                 Match layoutMatch = layoutNameRegex.Match(child.Name);

    #                 if (blankMatch.Success)
    #                     blankLayers.Add(int.Parse(blankMatch.Groups[1].Value) + 10);

    #                 if (!layoutMatch.Success)
    #                     continue;

    #                 int layer = int.Parse(layoutMatch.Groups[1].Value) * 10;

    #                 layoutLayers.Add(layer);

    #                 layoutLayers.Add(layer + 1);
    #             }

    #             if (blankLayers.Count != 0 && blankPart != null)
    #             {
    #                 session_.Parts.SetDisplay(blankPart, false, false, out _);

    #                 session_.Parts.SetWork(__display_part_);

    #                 AddDummy(blankPart, blankLayers);

    #                 Prompt($"Saving: {blankPart.Leaf}.");

    #                 __display_part_.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False);
    #             }

    #             if (layoutLayers.Count != 0 && layoutPart != null)
    #             {
    #                 session_.Parts.SetDisplay(layoutPart, false, false, out _);

    #                 session_.Parts.SetWork(__display_part_);

    #                 AddDummy(layoutPart, layoutLayers);

    #                 Prompt($"Saving: {layoutPart.Leaf}.");

    #                 __display_part_.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False);
    #             }
    #         }
    #         finally
    #         {
    #             session_.Parts.SetDisplay(currentD, false, false, out _);
    #             session_.Parts.SetWork(currentW);
    #         }

    #         snapStrip010.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);
    #     }

    #     public static void ExportStripStp(string outgoingFolderName)
    #     {
    #         string outputPath = $"{outgoingFolderName}\\{session_.Parts.Work.Leaf}-{TodaysDate}.stp";

    #         StepCreator step = session_.DexManager.CreateStepCreator();

    #         using (session_.__UsingBuilderDestroyer(step))
    #         {
    #             step.ExportDestination = BaseCreator.ExportDestinationOption.NativeFileSystem;

    # 			// sql convert
    # 			// in theory you should just be able to load the settingfile
    # 			// and not set any other step.properties
    #             step.SettingsFile = "U:\\nxFiles\\Step Translator\\ExternalStep_AllLayers.def";

    #             step.ExportAs = StepCreator.ExportAsOption.Ap214;

    #             step.InputFile = session_.Parts.Work.FullPath;

    #             step.OutputFile = outputPath;

    #             step.ProcessHoldFlag = true;

    #             step.Commit();
    #         }

    #         print(File.Exists(outputPath)
    #             ? $"Successfully created \"{outputPath}\"."
    #             : $"Did not successfully create \"{outputPath}\".");
    #     }

    #     public static void ExportStripPdf(string partPath, string drawingSheetName, string filePath)
    #     {
    #         string directory = Path.GetDirectoryName(filePath);

    #         if (!filePath.EndsWith(".pdf"))
    #             throw new Exception("File path for PDF must end with \".pdf\".");

    #         if (File.Exists(filePath))
    #             throw new Exception($"PDF '{filePath}' already exists.");

    #         Part part = session_.__FindOrOpen(partPath);

    #         //We can use SingleOrDefault here because NX will prevent the naming of two drawing sheets the exact same string.
    #         DrawingSheet sheet = part.DrawingSheets
    #                                  .ToArray()
    #                                  .SingleOrDefault(drawingSheet => drawingSheet.Name == drawingSheetName)
    #                              ??
    #                              throw new Exception(
    #                                  $@"Part '{partPath}' does not have a sheet named '{drawingSheetName}'.");

    #         __display_part_ = part;
    #         __work_part_ = __display_part_;

    #         PrintPDFBuilder pdfBuilder = part.PlotManager.CreatePrintPdfbuilder();

    #         using (session_.__UsingBuilderDestroyer(pdfBuilder))
    #         {
    # 			// sql
    #             pdfBuilder.Scale = 1.0;
    #             pdfBuilder.Size = PrintPDFBuilder.SizeOption.ScaleFactor;
    #             pdfBuilder.OutputText = PrintPDFBuilder.OutputTextOption.Polylines;
    #             pdfBuilder.Units = PrintPDFBuilder.UnitsOption.English;
    #             pdfBuilder.XDimension = 8.5;
    #             pdfBuilder.YDimension = 11.0;
    #             pdfBuilder.RasterImages = true;
    #             pdfBuilder.Colors = PrintPDFBuilder.Color.AsDisplayed;
    #             pdfBuilder.Watermark = "";
    #             UFSession.GetUFSession().Draw.IsObjectOutOfDate(sheet.Tag, out bool flag);
    #             if (flag)
    #             {
    #                 UFSession.GetUFSession().Draw.UpdOutOfDateViews(sheet.Tag);
    #                 part.__Save();
    #             }

    #             sheet.Open();
    #             pdfBuilder.SourceBuilder.SetSheets(new NXObject[] { sheet });
    #             pdfBuilder.Filename = filePath;
    #             pdfBuilder.Commit();
    #         }
    #     }

    #     public static string ExportStripPart(string outgoingFolderPath)
    #     {
    #         string[] assemblyPartPaths = __display_part_.ComponentAssembly.RootComponent.__Descendants()
    #             .Where(component => !component.IsSuppressed)
    #             .Select(component => component.Prototype)
    #             .OfType<Part>()
    #             .Distinct()
    #             .Select(part => part.FullPath)
    #             .ToArray();

    #         Zip7 zip = new Zip7($"{outgoingFolderPath}\\NX StripAssembly.7z", assemblyPartPaths);
    #         zip.Start();
    #         zip.WaitForExit();
    #         return $"{outgoingFolderPath}\\NX StripAssembly.7z";
    #     }

    #     public static void ExportStripPrintDrawing(int copies)
    #     {
    #         if (copies == 0)
    #             return;

    #         Part _WorkPart = Session.GetSession().Parts.Work;

    #         UFSession TheUFSession = UFSession.GetUFSession();

    #         //session_.Execute(@"C:\Repos\NXJournals\JOURNALS\export_strip.py", "ExportStrip", "print_drawing_sheet", new object[] { copies });
    #         PrintBuilder printBuilder1 = _WorkPart.PlotManager.CreatePrintBuilder();

    #         try
    #         {
    # 			// sql
    #             printBuilder1.ThinWidth = 1.0;
    #             printBuilder1.NormalWidth = 2.0;
    #             printBuilder1.ThickWidth = 3.0;
    #             printBuilder1.Copies = copies;
    #             printBuilder1.RasterImages = true;
    #             printBuilder1.Output = PrintBuilder.OutputOption.WireframeBlackWhite;
    #             DrawingSheet[] sheets = _WorkPart.DrawingSheets.ToArray();
    #             switch (sheets.Length)
    #             {
    #                 case 0:
    #                     print("Current work part doesn't not have a sheet to print.");
    #                     return;
    #                 case 1:
    #                     session_.ApplicationSwitchImmediate("UG_APP_DRAFTING");
    #                     sheets[0].Open();
    #                     TheUFSession.Draw.IsObjectOutOfDate(sheets[0].Tag, out bool outOfDate);
    #                     if (outOfDate)
    #                         try
    #                         {
    #                             TheUFSession.Draw.UpdOutOfDateViews(sheets[0].Tag);
    #                             sheets[0].OwningPart.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException();
    #                         }

    #                     printBuilder1.SourceBuilder.SetSheets(new NXObject[] { sheets[0] });
    #                     break;
    #                 default:
    #                     print("Current work part contains more than 1 sheet.");
    #                     return;
    #             }

    #             printBuilder1.PrinterText = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC";
    #             printBuilder1.Orientation = PrintBuilder.OrientationOption.Landscape;
    #             printBuilder1.Paper = PrintBuilder.PaperSize.Inch11x17;
    #             printBuilder1.Commit();
    #         }
    #         finally
    #         {
    #             printBuilder1.Destroy();
    #         }
    #     }

    #     private void ExportStripForm_Load(object sender, EventArgs e)
    #     {
    #         Text = AssemblyFileVersion;
    #         Location = Properties.Settings.Default.export_strip_form_window_location;
    #     }

    #     private void ExportStripForm_FormClosed(object sender, FormClosedEventArgs e)
    #     {
    #         Properties.Settings.Default.export_strip_form_window_location = Location;
    #         Properties.Settings.Default.Save();
    #     }

    #     public class Zip7
    #     {
    #         private readonly string[] _filesToZip;

    #         private readonly string _zipArchive;

    #         private Process _process;

    #         private bool _started;

    #         public Zip7(string zipArchive, params string[] filesToZip)
    #         {
    #             _zipArchive = zipArchive;

    #             _filesToZip = filesToZip;
    #         }

    #         public void WaitForExit()
    #         {
    #             if (_process is null)
    #                 throw new ArgumentNullException(nameof(_process));

    #             if (!_started)
    #                 throw new InvalidOperationException("Zip process hasn't been started yet.");

    #             _process.WaitForExit();
    #         }

    #         public void Start()
    #         {
    #             string tempFile = $"{Path.GetTempPath()}zipData{_filesToZip.GetHashCode()}.txt";

    #             using (FileStream fs = File.Open(tempFile, FileMode.Create))
    #             {
    #                 fs.Close();
    #             }

    #             using (StreamWriter writer = new StreamWriter(tempFile))
    #             {
    #                 _filesToZip.ToList().ForEach(writer.WriteLine);
    #             }

    # 			// select
    #             _process = new Process
    #             {
    #                 StartInfo =
    #             {
    #                 CreateNoWindow = false,
    #                 FileName = "C:\\Program Files\\7-Zip\\7z",
    #                 WindowStyle = ProcessWindowStyle.Normal,
    #                 UseShellExecute = true,
    #                 Arguments = $"a -t7z \"{_zipArchive}\" \"@{tempFile}\" -mx9"
    #             }
    #             };

    #             _started = _process.Start();
    #         }
    #     }
    # }
    pass


class UFuncDeleteUnusedCurves:
    #     public class DeleteUnusedCurves : _UFunc
    # {
    #     public override void execute()
    #     {
    #         Curve[] curves = Selection.SelectCurves(
    #             ufunc_rev_name,
    #             ufunc_rev_name,
    #             NXOpen.Selection.SelectionScope.WorkPart
    #         );

    #         if (curves is null || curves.Length == 0)
    #             return;

    #         foreach (Curve delete in curves)
    #         {

    #             ufsession_.Modl.AskObjectFeat(delete.Tag, out Tag featTag);

    #             if (featTag == Tag.Null)
    #                 delete.__Delete();
    #         }
    #     }
    # }
    pass


class CopyToLayer50:
    # public class CopyToLayer50 : _UFunc
    # {
    #     private const int LAYER = 50;

    #     public override void execute()
    #     {
    #         string message = $"{AssemblyFileVersion} - Copy To Layer 50";

    #         Component[] compList = Selection.SelectManyComponents(message);

    #         if (compList.Length == 0)
    #             return;

    #         using (session_.__UsingDisplayPartReset())
    #             foreach (Component comp in compList)
    #             {
    #                 print("/////////////////");
    #                 __work_component_ = comp;

    #                 // if body exists on layer 50, delete body
    #                 Body[] bodies_on_layer_50 = comp.__Prototype().Bodies
    #                     .ToArray()
    #                     .Where(__b => __b.IsSolidBody)
    #                     .Where(__b => __b.Layer == LAYER)
    #                     .ToArray();

    #                 Body[] solid_bodies_layer_1 = comp.__Prototype().Bodies
    #                     .ToArray()
    #                     .Where(__b => __b.IsSolidBody)
    #                     .Where(__b => __b.Layer == 1)
    #                     .ToArray();

    #                 switch (solid_bodies_layer_1.Length)
    #                 {
    #                     case 0:
    #                         print($"Did not a solid body on layer 1 in part {comp.DisplayName}");
    #                         return;
    #                     case 1:
    #                         break;
    #                     default:
    #                         print($"There is more than one solid body on layer 1 in part {comp.DisplayName}");
    #                         return;
    #                 }

    #                 string date = $"{DateTime.Now.Year}-{DateTime.Now.Month}-{DateTime.Now.Day}";

    #                 Body[] layer_50_bodies = comp.__Prototype()
    #                     .Layers
    #                     .GetAllObjectsOnLayer(LAYER).OfType<Body>().ToArray();

    #                 comp.__Prototype()
    #                     .Layers
    #                     .CopyObjects(LAYER, solid_bodies_layer_1);

    #                 List<Body> new_layer_50_bodies = comp.__Prototype()
    #                     .Layers
    #                     .GetAllObjectsOnLayer(LAYER)
    #                     .Except(layer_50_bodies)
    #                     .OfType<Body>()
    #                     .ToList();

    #                 foreach (Body body in new_layer_50_bodies)
    #                 {
    #                     body.OwningPart.Features.GetParentFeatureOfBody(body).SetName(date);
    #                     body.Color = 7;
    #                     body.LineFont = DisplayableObject.ObjectFont.Phantom;
    #                     body.RedisplayObject();
    #                 }

    #                 try
    #                 {
    #                     comp.__Prototype().__ReferenceSets("BODY")
    #                         .RemoveObjectsFromReferenceSet(new_layer_50_bodies.ToArray<NXObject>());
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException();
    #                 }

    #                 comp.__Prototype().Layers.MoveDisplayableObjects(LAYER + 1, layer_50_bodies);

    #                 foreach (Body body in bodies_on_layer_50)
    #                 {
    #                     body.Color = 7;
    #                     body.LineFont = DisplayableObject.ObjectFont.Phantom;
    #                     body.RedisplayObject();

    #                     print($"Copied solid body to " +
    #                         $"{comp.__Prototype().Features.GetAssociatedFeature(body).GetFeatureName()} " +
    #                         $"in part {comp.DisplayName}");
    #                 }

    #                 try
    #                 {
    #                     comp.__Prototype().__ReferenceSets("BODY").RemoveObjectsFromReferenceSet(bodies_on_layer_50);
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException();
    #                 }
    #             }
    #     }
    # }

    pass


class UFuncExtractFreeEdges:
    #     internal class ExtractFreeEdgeCurves : _UFunc
    # {
    #     public override void execute()
    #     {
    #         print(ufunc_rev_name);

    #         if (__display_part_ is null)
    #         {
    #             print("There is no displayed part loaded");
    #             return;
    #         }

    # 		// sql
    # 		// make this is easier to read
    #         session_.SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name);
    #         // Allows the user to select sheet bodies.
    #         Body[] selectedSheetBodies = Selection.SelectManySheetBodies(ufunc_rev_name);
    #         // Gets the edges from the selected sheet bodies.
    #         Edge[] edges = selectedSheetBodies.SelectMany(body => body.GetEdges()).ToArray();
    #         // Gets the free edges, (the edges that are attached to one face).
    #         Edge[] freeEdges = edges.Where(edge => edge.GetFaces().Length == 1).ToArray();
    #         // Gets the curve representation of the {freeEdges}.
    #         Curve[] freeEdgeCurves = freeEdges.Select(edge => edge.__ToCurve()).ToArray();

    #         // Sets all the free edge curves to the current work layer.
    #         foreach (Curve curve in freeEdgeCurves)
    #             curve.__Layer(WorkLayer);

    #         print($"Created {freeEdgeCurves.Length} curves off of free edges.");
    #     }
    # }
    pass
