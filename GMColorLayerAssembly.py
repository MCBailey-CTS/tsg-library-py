from NXOpen import Part
from NXOpen.Assemblies import Component
from NXOpen.Layer import State
import NXOpen.UF
from extensions__ import *
from typing import Dict, List, Tuple


def part_has_reference_set(part: Part, name: str) -> bool:
    return any(r.Name == name for r in part.GetAllReferenceSets())


def part_get_reference_set(part: Part, name: str):  # ->ReferenceSet:
    for r in part.GetAllReferenceSets():
        if r.Name == name:
            return r
    raise Exception()


def part_crt_reference_set(part: Part, name: str):  # ->ReferenceSet:
    refset = part.CreateReferenceSet()
    refset.SetName(name)
    return refset


def hash_components_to_parts(components: List[Component]) -> List[Part]:
    dict_: Dict[str, Part] = {}
    for comp in components:
        if comp.DisplayName in dict_:
            continue
        dict_[comp.DisplayName] = comp.Prototype
    return dict_.values()


def color_layer_solid_body_1(part: Part, layer: int, color: int) -> None:
    session().Parts.SetDisplay(part, False, False)
    display_part().Layers.SetState(layer, State.Selectable)

    solid_body_layer_1 = list(
        filter(lambda b: b.Layer == 1, list(display_part().Bodies))
    )

    if not part_has_reference_set(display_part(), "PART"):
        if part_has_reference_set(display_part(), "BODY"):
            refset = part_get_reference_set(display_part(), "BODY")
            refset.SetName("PART")
        else:
            refset = part_crt_reference_set(display_part(), "PART")
            refset.AddObjectsToReferenceSet(solid_body_layer_1)

    # do_
    # ufsession.Modeling.Update()

    assert (
        len(solid_body_layer_1) == 1
    ), f"There were {len(solid_body_layer_1)} solid bodies in part {part.Leaf}"

    display_part().Features.GetParentFeatureOfBody(
        solid_body_layer_1[0]
    ).MakeCurrentFeature()

    displayModification1 = session().DisplayManager.NewDisplayModification()
    displayModification1.ApplyToAllFaces = True
    displayModification1.ApplyToOwningParts = True
    displayModification1.NewColor = color
    displayModification1.NewLayer = layer
    displayModification1.Apply([solid_body_layer_1[0]])
    displayModification1.Dispose()
    features = list(display_part().Features)
    features[len(features) - 1].MakeCurrentFeature()


def component_descendants(component: Component) -> List[Component]:
    descendants = []
    if component is None:
        return descendants
    # Get children of the current component
    children = component.GetChildren()
    # Iterate through children and collect them recursively
    for child in children:
        descendants.append(child)
        # Recursively get descendants of the child component
        descendants.extend(component_descendants(child))
    return descendants


def __main__(layer: int, color: int) -> None:
    components = select_components()
    if len(components) == 0:
        return
    parts = hash_components_to_parts(components)
    original = display_part()
    try:
        for part in parts:
            try:
                color_layer_solid_body_1(part, layer, color)
            except Exception as ex:
                print_(ex)
    finally:
        session().Parts.SetDisplay(original, False, False)

    try:
        ancestors: Dict[str, Part] = {}
        for part in parts:
            part_occs: Tuple[List[int], int] = ufsession().Assem.AskOccsOfPart(
                display_part().Tag, part.Tag
            )

            descendants = []
            for t in part_occs[0]:
                # set layer of component
                j = cast_tagged_object(t)
                # print_(j.DisplayName)
                # print_(j.Parent.DisplayName)

                for ancest in component_ancestors(j):
                    if ancest.DisplayName not in ancestors:
                        ancestors[ancest.DisplayName] = ancest.Prototype
                try:
                    for ancest in ancestors:
                        session().Parts.SetDisplay(ancestors[ancest], False, False)
                        display_part().Layers.SetState(layer, State.Selectable)
                        part_occs1: Tuple[
                            List[int], int
                        ] = ufsession().Assem.AskOccsOfPart(
                            ancestors[ancest].Tag, part.Tag
                        )

                        for h in part_occs1[0]:
                            cmp = cast_component(h)
                            cmp.Layer = layer
                            cmp.SetLayerOption(-1)
                            cmp.DirectOwner.ReplaceReferenceSet(cmp, "PART")
                            cmp.RedisplayObject()

                    # print_(ancest)
                finally:
                    session().Parts.SetDisplay(original, False, False)

                # session().Parts.SetDisplay(j.Parent.Prototype, False, False)

    finally:
        session().Parts.SetDisplay(original, False, False)


# __main__(10, 186)
