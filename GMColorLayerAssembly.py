from NXOpen import Part
from NXOpen.Assemblies import Component
from NXOpen.Layer import State
import NXOpen.UF
from __extensions__ import *
from typing import List

# set_layer_status(layer:int, )


def main_component(component: Component, layer: int, color: int) -> None:
    # need to set the {comp} to the {layer} first before you change displayed part
    # foreach selected component, need to prompt the user for a layer, and color
    # comp.SetLayerOption(-1)
    prototype = component.Prototype

    assert isinstance(
        prototype, Part
    ), f"Component {component.DisplayName} is not opened"

    session().Parts.SetDisplay(component.Prototype, False, False)
    display_part().Layers.SetState(layer, State.Selectable)

    solid_body_layer_1 = list(
        filter(lambda b: b.Layer == 1, list(display_part().Bodies))
    )

    assert (
        len(solid_body_layer_1) == 1
    ), f"There were {len(solid_body_layer_1)} solid bodies in part {component.DisplayName}"

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
    # return
    # the color to change the body
    # the layer to set the first and last solid body on layer 1 in a detail
    original = display_part()
    try:
        # need to convert {components} to a set of parts incase they pick the user picks two components with the same prototype
        for comp in components:
            try:
                main_component(comp, layer, color)
            except Exception as ex:
                print_(ex)

    finally:
        session().Parts.SetDisplay(original, False, False)

    for comp in components:
        # need to set the {comp} to the {layer} first before you change displayed part
        # foreach selected component, need to prompt the user for a layer, and color
        comp.Layer = layer
        comp.RedisplayObject()
        comp.SetLayerOption(-1)
        comp.RedisplayObject()

    if display_part().Layers.WorkLayer != layer:
        display_part().Layers.SetState(layer, State.Selectable)
        # print_(f"{comp.Name}-{comp.Tag}-{comp.Color}-{comp.Layer}")
    # NXOpen.UF.UFSession.GetUFSession().Disp.RegenerateDisplay()


__main__(10, 10)
