import NXOpen
from NXOpen.Assemblies import Component
import NXOpen.UF
from __extensions__ import *
from typing import List

def select_components() -> List[Component]:
    selected_objects = NXOpen.UI.GetUI().SelectionManager.SelectTaggedObjects(
        "Select components",
        "Select components",
        # NXOpen.SelectionResponseMemberType
        NXOpen.SelectionSelectionScope.AnyInAssembly,
        NXOpen.SelectionSelectionAction.ClearAndEnableSpecific,
        False,
        False,
        [NXOpen.Selection.MaskTriple(63, 0, 0)],
    )
    return selected_objects[1] # type: ignore

def __main__(layer: int, color: int) -> None:
    components = select_components()
    # the color to change the body
    # the layer to set the first and last solid body on layer 1 in a detail
    original = display_part()

    try:
        theSession = NXOpen.Session.GetSession()
        # need to convert {components} to a set of parts incase they pick the user picks two components with the same prototype
        for comp in components:
            # need to set the {comp} to the {layer} first before you change displayed part
            # foreach selected component, need to prompt the user for a layer, and color
            # comp.SetLayerOption(-1)
            prototype = comp.Prototype

            if not isinstance(prototype, NXOpen.Part):
                print_(f"Component {comp.DisplayName} is not opened")
                continue

            session_.Parts.SetDisplay(comp.Prototype, False, False)
            solid_body_layer_1 = list(
                filter(lambda b: b.Layer == 1, list(session_.Parts.Display.Bodies))
            )
            if len(solid_body_layer_1) != 1:
                raise Exception(
                    f"There were {len(solid_body_layer_1)} solid bodies in part {comp.DisplayName}"
                )

            displayModification1 = theSession.DisplayManager.NewDisplayModification()
            displayModification1.ApplyToAllFaces = True
            # look at this.
            # if set to true you can probably change the color of the
            # prototype body and layer from the component level
            # without ever changing the displayed part.
            # that way you can always stay at the top level assembly.
            displayModification1.ApplyToOwningParts = False
            displayModification1.NewColor = color
            displayModification1.NewLayer = layer
            displayModification1.Apply([solid_body_layer_1[0]])
            # theSession.UpdateManager.DoUpdate(
            #     session_.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "m")
            # )
            displayModification1.Dispose()
            print_(solid_body_layer_1[0].Layer)
            # bbai0@icloud.com
            feature = display_part().Features.GetParentFeatureOfBody(
                solid_body_layer_1[0]
            )
            feature.MakeCurrentFeature()

            displayModification1 = theSession.DisplayManager.NewDisplayModification()
            displayModification1.ApplyToAllFaces = True
            displayModification1.ApplyToOwningParts = False
            displayModification1.NewColor = color
            displayModification1.NewLayer = layer
            displayModification1.Apply([solid_body_layer_1[0]])
            # theSession.UpdateManager.DoUpdate(
            #     session_.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "m")
            # )
            displayModification1.Dispose()
            features = list(display_part().Features)
            features[len(features) - 1].MakeCurrentFeature()

    except Exception as ex:
        print_(ex)

    finally:
        session_.Parts.SetDisplay(original, False, False)

    for comp in components:
        # need to set the {comp} to the {layer} first before you change displayed part

        # foreach selected component, need to prompt the user for a layer, and color
        comp.Layer = layer
        comp.RedisplayObject()

        comp.SetLayerOption(-1)
        comp.RedisplayObject()
        print_(f"{comp.Name}-{comp.Tag}-{comp.Color}-{comp.Layer}")
    NXOpen.UF.UFSession.GetUFSession().Disp.RegenerateDisplay()


__main__(10, 10)
