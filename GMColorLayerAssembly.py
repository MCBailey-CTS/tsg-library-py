from NXOpen import Part
from NXOpen.Assemblies import Component
from NXOpen.Layer import State
import NXOpen.UF
from extensions__ import *
from typing import Dict, List, Tuple


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


def __main__(layer: int, color: int) -> None:
    components = select_components()
    if len(components) == 0:
        return
    parts = hash_components_to_parts(components)
    with WithResetDisplayPart():
        for part in parts:
            try:
                color_layer_solid_body_1(part, layer, color)
            except Exception as ex:
                print_(ex)
    with WithResetDisplayPart():
        ancestors: Dict[str, Part] = {}
        for part in parts:
            part_occs = ufsession().Assem.AskOccsOfPart(display_part().Tag, part.Tag)
            for t in part_occs[0]:
                j = cast_component(t)
                for ancestor in component_ancestors(j):
                    if ancestor.DisplayName not in ancestors:
                        ancestors[ancestor.DisplayName] = ancestor.Prototype  # type: ignore
                with WithResetDisplayPart():
                    for ancest in ancestors.keys():
                        session().Parts.SetDisplay(ancestors[ancest], False, False)
                        display_part().Layers.SetState(layer, State.Selectable)
                        part_occs1 = ufsession().Assem.AskOccsOfPart(
                            ancestors[ancest].Tag, part.Tag
                        )

                        for h in part_occs1[0]:
                            cmp = cast_component(h)
                            cmp.Layer = layer
                            cmp.SetLayerOption(-1)
                            cmp.DirectOwner.ReplaceReferenceSet(cmp, "PART")
                            cmp.RedisplayObject()
