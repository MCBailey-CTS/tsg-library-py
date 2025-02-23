import traceback
from GMCleanAssembly import delete_objects
from NXOpen import WCSAxis
from NXOpen.Assemblies import ReplaceComponentBuilder
from NXOpen.Features import ExtractFace
import NXOpen.Features
from NXOpen.Layer import State
from extensions__ import *
import NXOpen.UF
from typing import Sequence


def strip_wave_out() -> None:
    try:
        for feat in list(work_part().Features):
            try:
                if not isinstance(feat, ExtractFace):
                    continue
                if not extract_face_is_linked_body(feat):
                    continue
                is_broken = ufsession().Wave.IsLinkBroken(feat.Tag)  # type: ignore
                if is_broken:
                    continue
                xform = ufsession().Wave.AskLinkXform(feat.Tag)  # type: ignore
                from_part_occ = ufsession().So.AskAssyCtxtPartOcc(  # type: ignore
                    xform, work_part().ComponentAssembly.RootComponent.Tag
                )
                if from_part_occ == 0:
                    continue
                point = [0.0, 0.0, 0.0]
                ufsession().So.AskPointOfXform(xform, point)  # type: ignore
                from_comp = NXOpen.TaggedObjectManager.GetTaggedObject(  # type: ignore
                    from_part_occ
                )  # type: Component
                origin = Point3d()
                corigin = component_origin(from_comp)
                if not point3d_equals_point3d(origin, corigin):
                    continue
                delete_objects([feat])
            except Exception as ex:
                print_(ex)
                traceback.print_exc()
    except:
        traceback.print_exc()


def WaveIn() -> None:
    try:
        if not part_has_dynamic_block(work_part()):
            k = [
                body
                for body in list(work_part().Bodies)
                if body.IsSolidBody() and body.Layer == 1
            ]
            assert len(k) == 1
            solid_body_layer_1 = k[0]
        else:
            work_part().Layers.SetState(96, State.Visible)
            solid_body_layer_1 = part_get_dynamic_block(work_part()).GetBodies()[0]

        if work_part().ComponentAssembly.RootComponent is None:
            return

        for __child in work_part().ComponentAssembly.RootComponent.GetChildren():
            try:
                WaveIn(__child, solid_body_layer_1)  # type: ignore
            except Exception as ex:
                print_(ex)
                traceback.print_exc()
    except Exception as ex:
        print_(ex)
        traceback.print_exc()


def WaveIn1(__child: Component, solid_body_layer_1: Body) -> None:
    if not component_is_loaded(__child):
        return
    if __child.IsSuppressed:
        return
    if __child.Layer != 99 and __child.Layer != 98 and __child.Layer != 97:
        return

    is_subtracted = False

    for feature in list(display_part().Features):
        if not isinstance(feature, ExtractFace):
            continue
        extract = feature
        if not extract_face_is_linked_body(extract):
            continue
        if feature_is_broken(extract):
            continue
        xform_tag = feature_xform(extract)
        point = [0.0, 0.0, 0.0]
        ufsession().So.AskPointOfXform(xform_tag, point)  # type: ignore
        origin = Point3d()
        if point3d_equals_point3d(origin, component_origin(__child)):
            continue
        is_subtracted = True
        break

    if is_subtracted:
        return
    if not __child.HasInstanceUserAttribute(
        "subtract", NXObjectAttributeType.String, -1
    ):
        return

    subtract_att = nxobject_get_attribute(__child, "subtract")

    if subtract_att == "HANDLING" or subtract_att == "SHORT-TAP":
        subtract_ref_set = "SHORT-TAP"
    elif subtract_att == "BLIND_OPP":
        subtract_ref_set = "CBORE_BLIND_OPP"
    elif subtract_att == "CLR_DRILL":
        subtract_ref_set = "CLR_HOLE"
    else:
        subtract_ref_set = subtract_att

    component_set_reference_set(__child, subtract_ref_set)

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

    if subtract_att == "HANDLING" or subtract_att == "WIRE_TAP":
        __child.Layer = 98
        __child.RedisplayObject()
    elif subtract_att == "TOOLING":
        __child.Layer = 97
        __child.RedisplayObject()

    if __child.Layer != 99 or subtract_att == "HANDLING" or subtract_att == "WIRE_TAP":
        component_set_reference_set(__child, "Empty")
        part_get_reference_set(work_part(), "BODY").RemoveObjectsFromReferenceSet(
            [__child]
        )
        return
    component_set_reference_set(__child, "BODY")
    part_get_reference_set(work_part(), "BODY").AddObjectsToReferenceSet([__child])


def InsertWireTaps() -> None:
    session().SetUndoMark(NXOpen.SessionMarkVisibility.Visible, "WIRE_TAP")
    if display_part().Tag == work_part().Tag:
        for i in [99, 98, 97]:
            display_part().Layers.SetState(i, State.Selectable)
    wireTapScrew = session_get_or_open_part(
        "G:\\0Library\\Fasteners\\Metric\\SocketHeadCapScrews\\008\\8mm-shcs-020.prt"
    )

    display_part().WCS.Rotate(WCSAxis.XAxis, 90.0)
    savedCsys = display_part().WCS.Save()  # type: ignore
    rotateOrientation = savedCsys.Orientation.Element
    x = 1 if display_part().PartUnits == NXOpen.BasePartUnits.Inches else 25.4
    offset2 = [3.00 * x, 0.875 * x, 0.00]
    mappedOffset1 = ufsession().Csys.MapPoint(
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_WCS_COORDS,
        [1.00 * x, 0.875 * x, 0.00],
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_COORDS,
    )
    mappedOffset2 = ufsession().Csys.MapPoint(
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_WCS_COORDS,
        offset2,
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_COORDS,
    )
    mappedToWork1 = ufsession().Csys.MapPoint(
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_COORDS,
        mappedOffset1,
        NXOpen.UF.UFConstants.UF_CSYS_WORK_COORDS,
    )
    mappedToWork2 = ufsession().Csys.MapPoint(
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_COORDS,
        mappedOffset2,
        NXOpen.UF.UFConstants.UF_CSYS_WORK_COORDS,
    )
    basePoint1 = Point3d(mappedToWork1[0], mappedToWork1[1], mappedToWork1[2])
    basePoint2 = Point3d(mappedToWork2[0], mappedToWork2[1], mappedToWork2[2])
    component1 = work_part().ComponentAssembly.AddComponent(
        wireTapScrew, "SHORT-TAP", "8mm-shcs-020", basePoint1, rotateOrientation, 98
    )
    component2 = work_part().ComponentAssembly.AddComponent(
        wireTapScrew, "SHORT-TAP", "8mm-shcs-020", basePoint2, rotateOrientation, 98
    )

    display_part().WCS.Rotate(WCSAxis.XAxis, -90.0)
    component1.SetInstanceUserAttribute("subtract", -1, "WIRE_TAP", UpdateOption.Now)
    component2.SetInstanceUserAttribute("subtract", -1, "WIRE_TAP", UpdateOption.Now)
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
        replaceBuilder = work_part().AssemblyManager.CreateReplaceComponentBuilder()  # type: ignore

        try:
            replaceBuilder.ReplacementPart = nxPart.FullPath
            replaceBuilder.MaintainRelationships = True
            replaceBuilder.ReplaceAllOccurrences = False
            replaceBuilder.ComponentNameType = ReplaceComponentBuilder.ComponentNameOption.AsSpecified  # type: ignore

            replaceBuilder.ComponentsToReplace.Add(fasteners_to_substitue)
            replaceBuilder.Commit()
        finally:
            replaceBuilder.Destroy()
        print(f"Substituted fasteners {original_display_name} -> {nxPart.Leaf}")


def WaveOut1(child: Component) -> None:
    if child.Parent.Tag != child.OwningPart.ComponentAssembly.RootComponent.Tag:
        raise Exception("Can only wave out immediate children.")
    linkedBody = AddFastenersGetLinkedBody(child.OwningPart, child)
    delete_objects([linkedBody])


def WaveOut() -> None:
    if work_part().Tag == display_part().Tag:
        for __child in work_part().ComponentAssembly.RootComponent.GetChildren():
            try:
                if __child.Layer != 99 and __child.Layer != 98 and __child.Layer != 97:
                    continue
                if __child.IsSuppressed:
                    continue
                if not is_fastener(__child):
                    continue

                link = AddFastenersGetLinkedBody(work_part(), __child)
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
        protoPartOcc = GetProtoPartOcc(work_part(), child)
        WaveOut(protoPartOcc)  # type: ignore


def SetWcsToWorkPart() -> None:
    # dynamicBlock = part_get_dynamic_block(work_part())
    # origin = block_get_origin(dynamicBlock)
    # orientation = block_get_orientation(dynamicBlock)
    # if work_part().Tag == display_part().Tag:
    #     display_part().WCS.SetOriginAndMatrix(origin, orientation)
    #     return
    # absCsys = display_part().CoordinateSystems.CreateCoordinateSystem(
    #     Point3d(), matrix3x3_identity(), True
    # )
    # compCsys = display_part().CoordinateSystems.CreateCoordinateSystem(
    #     component_origin(work_component()),
    #     component_orientation(work_component()),
    #     True,
    # )
    # newOrigin = map_point_csys_to_csys(origin, compCsys, absCsys)
    # newXVec = map_point_csys_to_csys(
    #     axisx(component_orientation(work_component())), compCsys, absCsys
    # )
    # newYVec = map_vector_csys_to_csys(
    #     axisy(component_orientation(work_component())), compCsys, absCsys
    # )
    # newOrientation = to_matrix3x3(newXVec, newYVec)
    # display_part().WCS.SetOriginAndMatrix(newOrigin, newOrientation)
    raise NotImplementedError()
