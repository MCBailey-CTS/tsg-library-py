import traceback
from GMCleanAssembly import delete_objects
from NXOpen import ReferenceSet
from NXOpen.Assemblies import ReplaceComponentBuilder
from NXOpen.Features import BooleanFeature, ExtractFace
import NXOpen.Features
from NXOpen.Layer import State
from extensions__ import *


def strip_wave_out():
    try:
        for feat in work_part().Features.ToArray():
            try:
                if not isinstance(feat, ExtractFace):
                    continue
                if not extract_face_is_linked_body(feat):
                    continue
                is_broken = ufsession().Wave.IsLinkBroken(feat.Tag)
                if is_broken:
                    continue
                xform = ufsession().Wave.AskLinkXform(feat.Tag)
                from_part_occ = ufsession().So.AskAssyCtxtPartOcc(
                    xform, work_part().ComponentAssembly.RootComponent.Tag
                )
                if from_part_occ == NXOpen.Tag.Null:
                    continue
                point = [0.0, 0.0, 0.0]
                ufsession().So.AskPointOfXform(xform, point)
                from_comp = NXOpen.TaggedObjectManager.GetTaggedObject(from_part_occ)

                origin = Point3d()
                corigin = component_origin(from_comp)
                if not point3d_equals_point3d(origin, corigin):
                    continue
                delete_objects(feat)
            except Exception as ex:
                print_(ex)
                traceback.print_exc()
    except:
        traceback.print_exc()


def WaveIn():
    try:
        if not part_has_dynamic_block(work_part()):
            solid_body_layer_1 = work_part().__SingleSolidBodyOnLayer1()
        else:
            work_part().Layers.SetState(96, State.Visible)
            solid_body_layer_1 = part_get_dynamic_block(work_part()).GetBodies()[0]

        if work_part().ComponentAssembly.RootComponent is None:
            return

        for __child in work_part().ComponentAssembly.RootComponent.GetChildren():
            try:
                WaveIn(__child, solid_body_layer_1)
            except Exception as ex:
                print_(ex)
                traceback.print_exc()
    except Exception as ex:
        print_(ex)
        traceback.print_exc()


def CreateLinkedBody(part: Part, descendant: Component) -> ExtractFace:
    raise Exception()


def part_get_reference_set(part: Part, name: str) -> ReferenceSet:
    for ref in part.GetAllReferenceSets():
        if ref.Name == name:
            return ref
    return None


def component_is_loaded(component: Component) -> bool:
    return isinstance(component.Prototype, Part)


def feature_is_broken(feature: Feature) -> bool:
    raise Exception()


def feature_xform(feature: Feature) -> int:
    raise Exception()


def WaveIn1(__child: Component, solid_body_layer_1: Body):
    if not component_is_loaded(__child):
        return
    if __child.IsSuppressed:
        return
    if __child.Layer != 99 and __child.Layer != 98 and __child.Layer != 97:
        return

    is_subtracted = False

    for feature in display_part().Features.ToArray():
        if not isinstance(feature, ExtractFace):
            continue
        extract = feature
        if not extract_face_is_linked_body(extract):
            continue
        if feature_is_broken(extract):
            continue
        xform_tag = feature_xform(extract)
        point = [0.0, 0.0, 0.0]
        ufsession().So.AskPointOfXform(xform_tag, point)
        origin = Point3d()
        if point3d_equals_point3d(origin, component_origin(__child)):
            continue
        is_subtracted = True
        break

    if is_subtracted:
        return
    if not __child.HasInstanceUserAttribute(
        "subtract", NXObject.AttributeType.String, -1
    ):
        return

    subtract_att = __child.__GetAttribute("subtract")
    subtract_ref_set

    match (subtract_att):
        case "HANDLING", "WIRE_TAP":
            subtract_ref_set = "SHORT-TAP"
        case "BLIND_OPP":
            subtract_ref_set = "CBORE_BLIND_OPP"
        case "CLR_DRILL":
            subtract_ref_set = "CLR_HOLE"
        case _:
            subtract_ref_set = subtract_att

    current = __child.ReferenceSet
    __child.__ReferenceSet(subtract_ref_set)

    linked_body = CreateLinkedBody(work_part(), __child)
    linked_body.OwningPart.Layers.MoveDisplayableObjects(96, linked_body.GetBodies())
    linked_body.SetName(f"{__child.DisplayName}, {subtract_att}")

    try:
        SubtractLinkedBody(work_part(), solid_body_layer_1, linked_body)
    except Exception as ex:
        # catch (NXException ex) when (ex.ErrorCode == 670030)
        print(
            f"Could not subtract {__child.DisplayName} with reference set {subtract_ref_set}"
        )
        traceback.print_exc()

    match (subtract_att):
        case "HANDLING", "WIRE_TAP":
            __child.Layer = 98
            __child.RedisplayObject()
        case "TOOLING":
            __child.Layer = 97
            __child.RedisplayObject()
    if __child.Layer != 99 or subtract_att == "HANDLING" or subtract_att == "WIRE_TAP":
        __child.__ReferenceSet("Empty")
        work_part().__FindReferenceSet("BODY").RemoveObjectsFromReferenceSet([__child])
        return

    __child.__ReferenceSet("BODY")
    part_get_reference_set(work_part(), "BODY").AddObjectsToReferenceSet([__child])


def _GetProtoPartOcc(owningPart: Part, partOcc: Component) -> Component:
    instance = ufsession().Assem.AskInstOfPartOcc(partOcc.Tag)
    prototypeChildPartOcc = ufsession().Assem.AskPartOccOfInst(
        owningPart.ComponentAssembly.RootComponent.Tag, instance
    )
    return cast_tagged_object(prototypeChildPartOcc)


def SubtractLinkedBody(
    owningPart: Part, subtractBody: Body, linkedBody: ExtractFace
) -> BooleanFeature:
    booleanBuilder = owningPart.Features.CreateBooleanBuilderUsingCollector(
        Feature.Null
    )
    try:
        booleanBuilder.Target = subtractBody
        collector = owningPart.ScCollectors.CreateCollector()
        rules = [owningPart.ScRuleFactory.CreateRuleBodyDumb(linkedBody.GetBodies())]
        collector.ReplaceRules(rules, False)
        booleanBuilder.ToolBodyCollector = collector
        booleanBuilder.Operation = Feature.BooleanType.Subtract
        return booleanBuilder.Commit()
    finally:
        booleanBuilder.Destroy()


def component_members(component: Component) -> Sequence[NXObject]:
    raise NotImplementedError()


def CreateLinkedBody(owningPart: Part, child: Component) -> ExtractFace:
    toolBodies = [
        obj
        for obj in component_members(child)
        if isinstance(obj, Body) and obj.IsSolidBody
    ]
    linkedBodyBuilder = owningPart.Features.CreateExtractFaceBuilder(
        NXOpen.Features.Feature.Null
    )
    try:
        linkedBodyBuilder.Associative = True
        linkedBodyBuilder.FeatureOption = (
            NXOpen.Features.ExtractFaceBuilder.FeatureOptionType.OneFeatureForAllBodies
        )
        linkedBodyBuilder.FixAtCurrentTimestamp = False
        linkedBodyBuilder.ParentPart = (
            NXOpen.Features.ExtractFaceBuilder.ParentPartType.OtherPart
        )
        linkedBodyBuilder.Type = NXOpen.Features.ExtractFaceBuilder.ExtractType.Body
        linkedBodyBuilder.ExtractBodyCollector.ReplaceRules(
            [owningPart.ScRuleFactory.CreateRuleBodyDumb(toolBodies)], False
        )
        return linkedBodyBuilder.Commit()
    finally:
        linkedBodyBuilder.Destroy()


def InsertWireTaps() -> None:
    session().SetUndoMark(NXOpen.SessionMarkVisibility.Visible, "WIRE_TAP")
    if display_part().Tag == work_part().Tag:
        for i in [99, 98, 97]:
            display_part().Layers.SetState(i, State.Selectable)
    wireTapScrew = session().__FindOrOpen(
        "G:\\0Library\\Fasteners\\Metric\\SocketHeadCapScrews\\008\\8mm-shcs-020.prt"
    )
    display_part().WCS.Rotate(WCS.Axis.XAxis, 90.0)
    savedCsys = display_part().WCS.Save()
    rotateOrientation = savedCsys.Orientation.Element
    x = 1 if display_part().PartUnits == NXOpen.BasePart.Units.Inches else 25.4
    offset2 = [3.00 * x, 0.875 * x, 0.00]
    mappedOffset1 = ufsession().Csys.MapPoint(
        NXOpen.UFConstants.UF_CSYS_ROOT_WCS_COORDS,
        [1.00 * x, 0.875 * x, 0.00],
        NXOpen.UFConstants.UF_CSYS_ROOT_COORDS,
    )
    mappedOffset2 = ufsession().Csys.MapPoint(
        NXOpen.UFConstants.UF_CSYS_ROOT_WCS_COORDS,
        offset2,
        NXOpen.UFConstants.UF_CSYS_ROOT_COORDS,
    )
    mappedToWork1 = ufsession().Csys.MapPoint(
        NXOpen.UFConstants.UF_CSYS_ROOT_COORDS,
        mappedOffset1,
        NXOpen.UFConstants.UF_CSYS_WORK_COORDS,
    )
    mappedToWork2 = ufsession().Csys.MapPoint(
        NXOpen.UFConstants.UF_CSYS_ROOT_COORDS,
        mappedOffset2,
        NXOpen.UFConstants.UF_CSYS_WORK_COORDS,
    )
    basePoint1 = Point3d(mappedToWork1[0], mappedToWork1[1], mappedToWork1[2])
    basePoint2 = Point3d(mappedToWork2[0], mappedToWork2[1], mappedToWork2[2])
    component1 = work_part().ComponentAssembly.AddComponent(
        wireTapScrew, "SHORT-TAP", "8mm-shcs-020", basePoint1, rotateOrientation, 98
    )
    component2 = work_part().ComponentAssembly.AddComponent(
        wireTapScrew, "SHORT-TAP", "8mm-shcs-020", basePoint2, rotateOrientation, 98
    )

    display_part().WCS.Rotate(WCS.Axis.XAxis, -90.0)
    component1.SetInstanceUserAttribute(
        "subtract", -1, "WIRE_TAP", NXOpen.Update.Option.Now
    )
    component2.SetInstanceUserAttribute(
        "subtract", -1, "WIRE_TAP", NXOpen.Update.Option.Now
    )
    delete_objects([savedCsys])


def SubstituteFasteners(nxPart: Part) -> None:
    with WithLockUpdates():
        fasteners_to_substitue: Sequence[Component] = []
        func = None
        if is_shcs(nxPart):
            func = is_shcs
        elif is_dwl(nxPart):
            func = is_dwl
        elif is_jck_screw(nxPart):
            func = is_jck_screw
        elif is_jck_screw_tsg(nxPart):
            func = is_jck_screw_tsg

        if func is None:
            raise Exception()

        fasteners_to_substitue = [
            c
            for c in work_part().ComponentAssembly.RootComponent.GetChildren()
            if func(c)
        ]

        if len(fasteners_to_substitue) == 0:
            print(f"Couldn't find any fasteners to substitue with {nxPart.Leaf}")
            return

        original_display_name = fasteners_to_substitue[0].DisplayName
        replaceBuilder = work_part().AssemblyManager.CreateReplaceComponentBuilder()

        try:
            replaceBuilder.ReplacementPart = nxPart.FullPath
            replaceBuilder.MaintainRelationships = True
            replaceBuilder.ReplaceAllOccurrences = False
            replaceBuilder.ComponentNameType = (
                ReplaceComponentBuilder.ComponentNameOption.AsSpecified
            )
            replaceBuilder.ComponentsToReplace.Add(fasteners_to_substitue)
            replaceBuilder.Commit()
        finally:
            replaceBuilder.Destroy()
        print(f"Substituted fasteners {original_display_name} -> {nxPart.Leaf}")


def MakePlanView(csys) -> None:
    l1 = "L1"
    top = "Top"
    plan = "PLAN"
    set_display_part(work_part())
    planView = part_get_modeling_view(work_part(), "PLAN")
    if planView is not None:
        layout = work_part().Layouts.FindObject(l1)
        modelingView1 = work_part().ModelingViews.WorkView
        modelingView2 = work_part().ModelingViews.FindObject(top)
        layout.ReplaceView(modelingView1, modelingView2, True)
        tempView = work_part().ModelingViews.FindObject(plan)
        delete_objects([tempView])
    ufsession().View.SetViewMatrix("", 3, csys.Tag, None)
    modelingView1 = display_part().Views.SaveAs(
        display_part().ModelingViews.WorkView, plan, False, False
    )
    modelingView2 = display_part().ModelingViews.FindObject(top)
    display_part().Layouts.FindObject(l1).ReplaceView(
        modelingView1, modelingView2, True
    )
    delete_objects([csys])


def GetLinkedBody(owning_part: Part, child: Component):
    for feature in list(owning_part.Features):
        if feature.FeatureType != "LINKED_BODY":
            continue
        xform = ufsession().Wave.AskLinkXform(feature.Tag)
        if xform == NXOpen.Tag.Null:
            continue
        fromPartOcc = ufsession().So.AskAssyCtxtPartOcc(
            xform, owning_part.ComponentAssembly.RootComponent.Tag
        )
        if fromPartOcc == child.Tag:
            return feature
    return None


def WaveOut1(child: Component):
    if child.Parent.Tag != child.OwningPart.ComponentAssembly.RootComponent.Tag:
        raise Exception("Can only wave out immediate children.")
    linkedBody = GetLinkedBody(child.OwningPart, child)
    delete_objects([linkedBody])


def WaveOut():
    if work_part().Tag == display_part().Tag:
        for __child in work_part().ComponentAssembly.RootComponent.GetChildren():
            try:
                if __child.Layer != 99 and __child.Layer != 98 and __child.Layer != 97:
                    continue
                if __child.IsSuppressed:
                    continue
                if not is_fastener(__child):
                    continue

                link = GetLinkedBody(work_part(), __child)
                WaveOut1(__child)
                delete_objects(link)
            except:
                traceback.print_exc()
        return

    for child in work_component().GetChildren():
        if child.IsSuppressed:
            continue
        if not is_fastener(child):
            continue
        protoPartOcc = _GetProtoPartOcc(work_part(), child)
        WaveOut(protoPartOcc)


def to_matrix3x3(xvec: Vector3d, yvec: Vector3d) -> Matrix3x3:
    raise Exception()


def axisx(matrix: Matrix3x3) -> Vector3d:
    raise NotImplementedError()


def axisy(matrix: Matrix3x3) -> Vector3d:
    raise NotImplementedError()


def SetWcsToWorkPart() -> None:
    dynamicBlock = part_get_dynamic_block(work_part())
    origin = block_get_origin(dynamicBlock)
    orientation = block_get_orientation(dynamicBlock)
    if work_part().Tag == display_part().Tag:
        display_part().WCS.SetOriginAndMatrix(origin, orientation)
        return
    absCsys = display_part().CoordinateSystems.CreateCoordinateSystem(
        Point3d(), matrix3x3_identity(), True
    )
    compCsys = display_part().CoordinateSystems.CreateCoordinateSystem(
        component_origin(work_component()),
        component_orientation(work_component()),
        True,
    )
    newOrigin = map_csys_to_csys(origin, compCsys, absCsys)
    newXVec = map_csys_to_csys(
        axisx(component_orientation(work_component())), compCsys, absCsys
    )
    newYVec = map_csys_to_csys(
        axisy(component_orientation(work_component())), compCsys, absCsys
    )
    newOrientation = to_matrix3x3(newXVec, newYVec)
    display_part().WCS.SetOriginAndMatrix(newOrigin, newOrientation)
