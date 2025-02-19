import inspect
import NXOpen
from NXOpen.Assemblies import Component
import NXOpen.UF
from __extensions__ import *

# for x in

# exit()


def select_components() -> List[Component]:
    # Set up the selection criteria
    # Select the components in the current work part
    # displayableObjectType = NXOpen.Selection.Filter.Component

    # Use SelectTaggedObjects to allow the user to select components
    selected_objects: tuple[
        object, list[Component]
    ] = NXOpen.UI.GetUI().SelectionManager.SelectTaggedObjects(
        "Select components",
        "Select components",
        # NXOpen.SelectionResponseMemberType
        NXOpen.SelectionSelectionScope.AnyInAssembly,
        NXOpen.SelectionSelectionAction.ClearAndEnableSpecific,
        False,
        False,
        [NXOpen.Selection.MaskTriple(63, 0, 0)],
    )
    print_(NXOpen.UI)
    print_(selected_objects)
    return selected_objects[1]


# print_(inspect.signature())

# NXOpen.UF.UFSession.GetUFSession().Ui.GetInputIntegers()
# for x in dir(NXOpen.Session):
#     print_(x)

# for x in dir(NXOpen.UF.UFSession.GetUFSession().Ui.GetInputIntegers):
# comp = display_part().ComponentAssembly.RootComponent.GetChildren()[0]

# # print_(comp.DisplayName)
# # print_(comp.Tag)
# # print_(comp)
# xxx = NXOpen.TaggedObjectManager.GetTaggedObject(comp.Tag)
# # print_(repr(xxx))
# ggg = NXOpen.Selection.MaskTriple(63, 0, 0)

# print_(ggg)

# print_(session_)


# theSession = NXOpen.Session.GetSession()
# ui = theSession.UI

# Prompt the user for a string input (default "0")
# result = NXOpen.UI.GetUI().InputBox("Please enter a number", "Input Required", "0")

# print_(result)


# comp = display_part().ComponentAssembly.RootComponent


# k


def __main__(layer: int, color: int) -> None:
    components = select_components()
    # NXOpen.UF.UFSession.GetUFSession().Ui.SetStatus(str(components))

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
