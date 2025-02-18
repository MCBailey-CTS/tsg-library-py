import NXOpen
import NXOpen.UF


def session() -> NXOpen.Session:
    return NXOpen.Session.GetSession()


def display_part() -> NXOpen.Part:
    return session().Parts.Display



def print_(obj: object) -> None:
    session = NXOpen.Session.GetSession()
    listing_window = session.ListingWindow
    listing_window.Open()
    listing_window.WriteLine(str(obj))




def select_components():
    # Get the current session and part
    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work

    # Set up the selection criteria
    # Select the components in the current work part
    # displayableObjectType = NXOpen.Selection.Filter.Component

    # "message", 
    # "tite", 
    # , 

    # Use SelectTaggedObjects to allow the user to select components
    selected_objects = NXOpen.UI.GetUI().SelectionManager.SelectTaggedObjects(
        "Select components",     
        "Select components",     
        NXOpen.  Selection.SelectionScope.AnyInAssembly,  
        NXOpen.Selection.SelectionAction.ClearAndEnableSpecific, 
        False, 
        False, 
        [ NXOpen.Selection. MaskTriple(63,0,0) ]
    )
    return selected_objects[1]
    
components = select_components()
NXOpen.UF.UFSession.GetUFSession().Ui.SetStatus(str(components))

# the color to change the body
color = 186
# the layer to set the first and last solid body on layer 1 in a detail
layer = 42

original = display_part()

try:

    theSession = NXOpen.Session.GetSession()
    # need to convert {components} to a set of parts incase they pick the user picks two components with the same prototype
    for comp in components:
        # need to set the {comp} to the {layer} first before you change displayed part

        session().Parts.SetDisplay(comp.Prototype, False, False)
        solid_body_layer_1 = list(filter(lambda b:b.Layer == 1, list(session().Parts.Display.Bodies)))
        if len(solid_body_layer_1) != 1:
            raise Exception(f'There were {len(solid_body_layer_1)} solid bodies in part {comp.DisplayName}')
        solid_body_layer_1 = solid_body_layer_1[0]

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
        displayModification1.Apply([solid_body_layer_1])
        theSession.UpdateManager.DoUpdate(session().SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "m" ))
        displayModification1.Dispose()

        feature = display_part().Features.GetParentFeatureOfBody(solid_body_layer_1)
        feature.MakeCurrentFeature()

        displayModification1 = theSession.DisplayManager.NewDisplayModification()
        displayModification1.ApplyToAllFaces = True
        displayModification1.ApplyToOwningParts = False
        displayModification1.NewColor = color
        displayModification1.NewLayer = layer
        displayModification1.Apply([solid_body_layer_1])
        theSession.UpdateManager.DoUpdate(session().SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "m" ))
        displayModification1.Dispose()

        features = list(display_part().Features)

        features[len(features) - 1].MakeCurrentFeature()

        


finally:
    session().Parts.SetDisplay(original,False,False)
    pass

    
