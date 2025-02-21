from NXOpen import Part
from NXOpen.Assemblies import Component
from NXOpen.Layer import State
import NXOpen.UF
from extensions__ import *
from typing import Dict, List


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


def __main___old(layer: int, color: int) -> None:
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
        comp.Layer = layer
        comp.SetLayerOption(-1)
        comp.RedisplayObject()

    if display_part().Layers.WorkLayer != layer:
        display_part().Layers.SetState(layer, State.Selectable)


def hash_components_to_parts(components:List[Component])->List[Part]:
    dict_:Dict[str, Part] ={}
    for comp in components:
        if comp.DisplayName in dict_: continue
        dict_[comp.DisplayName] = comp.Prototype
    return dict_.values()

def color_layer_solid_body_1(part:Part, layer:int, color:int)->None:
    session().Parts.SetDisplay(part, False, False)
    display_part().Layers.SetState(layer, State.Selectable)

    solid_body_layer_1 = list(
        filter(lambda b: b.Layer == 1, list(display_part().Bodies))
    )

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
                color_layer_solid_body_1(part,layer,color)
            except Exception as ex:
                print_(ex)
    finally:
         session().Parts.SetDisplay(original, False, False)

    try:
        ancestors:Dict[str,Part] = {}
        for part in parts:
            part_occs:Tuple[List[int], int] = ufsession().Assem.AskOccsOfPart(display_part().Tag, part.Tag)

            descendants = []
            for t in part_occs[0]:
                # set layer of component
                j = cast_tagged_object(t)
                # print_(j.DisplayName)
                # print_(j.Parent.DisplayName)

                for ancest in  component_ancestors(j):
                    if ancest.DisplayName not in ancestors:
                        ancestors[ancest.DisplayName] = ancest.Prototype
                try:
                    for ancest in ancestors:
                        session().Parts.SetDisplay(ancestors[ancest], False, False)
                        display_part().Layers.SetState(layer, State.Selectable)
                        part_occs1:Tuple[List[int], int] = ufsession().Assem.AskOccsOfPart(ancestors[ancest].Tag, part.Tag)

                        for h in part_occs1[0]:
                            cast_tagged_object(h).Layer = layer
                            cast_tagged_object(h).SetLayerOption(-1)
                            cast_tagged_object(h).RedisplayObject()
                    # print_(ancest)
                finally:
                    session().Parts.SetDisplay(original, False, False)

                


                # session().Parts.SetDisplay(j.Parent.Prototype, False, False)


    finally:
        session().Parts.SetDisplay(original, False, False)



            # if j.DisplayName not in parents:
            #     parents[j.DisplayName] = j.Prototype

            # print_(j.Parent.DisplayName)
            # descendants.append()

    # print_(parents)

        

    # descendants = comp


    # for part in parts:





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
        comp.Layer = layer
        comp.SetLayerOption(-1)
        comp.RedisplayObject()

    if display_part().Layers.WorkLayer != layer:
        display_part().Layers.SetState(layer, State.Selectable)

__main__(10, 186)
