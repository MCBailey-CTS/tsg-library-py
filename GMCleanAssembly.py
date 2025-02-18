from pathlib import Path
import NXOpen
import os


def print_(obj: object) -> None:
    session = NXOpen.Session.GetSession()
    listing_window = session.ListingWindow
    listing_window.Open()
    listing_window.WriteLine(str(obj))


def session() -> NXOpen.Session:
    return NXOpen.Session.GetSession()


def display_part() -> NXOpen.Part:
    return session().Parts.Display


# Stopwatch stopwatch = Stopwatch.StartNew();

def get_all_descendants(component):
    descendants = []
    # print_('hdhdhdh')

    if component is None:
        # print_('none')
        return descendants
    
    # Get children of the current component
    children = component.GetChildren()

    # Iterate through children and collect them recursively
    for child in children:
        descendants.append(child)
        # Recursively get descendants of the child component
        descendants.extend(get_all_descendants(child))

    return descendants


def DescendantParts(part):
    __parts = {}
    __parts[part.Leaf] =part
    for component in get_all_descendants(part.ComponentAssembly.RootComponent):
        if isinstance(component.Prototype, NXOpen.Part):
            if component.DisplayName not in __parts.keys():
                __parts[component.DisplayName] = component.Prototype
    return list(__parts.values())

def delete_objects(objects)->None:
    session().UpdateManager.ClearDeleteList()
    undo = session().SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "DELETE")
    session().UpdateManager.AddObjectsToDeleteList(objects)
    session().UpdateManager.DoUpdate(undo)




# def main():
print_("in here")
session().SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "GMCleanAssembly" )

original_display = session().Parts.Display
# print_('helllo world')
fasteners = {}

for root, dirs, files in os.walk("G:\\0Library\\Fasteners"):
    for file in files:
        path = os.path.join(root, file)
        temp = Path(path).stem
        fasteners[temp] = temp


parts = DescendantParts(display_part())



parts = list(filter(lambda p: p.Leaf not in fasteners, parts))
parts = list(filter(lambda p: 'layout'not in p.Leaf.lower()  , parts))
parts = list(filter(lambda p: 'strip'not in p.Leaf.lower()  , parts))

#     using (session_.__UsingDisplayPartReset())
#     using (session_.__UsingSuppressDisplay())
#         for (int i = 0; i < parts.Length; i++)

# print_(len(parts))

for index, value in enumerate(parts):

#             try
#             {
#                 Part part = parts[i];
#                 prompt($"({i + 1} - {parts.Length}) -> {part.Leaf}");


    session().Parts.SetDisplay(value, False, False)

    suppresed_features = list(filter(lambda f:not f.Suppressed, display_part().Features))

    if len(suppresed_features) > 0:
        # session_.__DeleteObjects(suppresed_features);
        pass

    # display = session.Parts.Display
    removeBuilder = display_part().Features.CreateRemoveParametersBuilder()
    removeBuilder.Objects.Add(list(display_part().Bodies))
    removeBuilder.Objects.Add(list(display_part().Curves))
    removeBuilder.Objects.Add(list(display_part().Points))
    removeBuilder.Objects.Add(list(display_part().Datums))
    removeBuilder.Objects.Add(list(display_part().CoordinateSystems))
    if removeBuilder.Objects.Size > 0:
        removeBuilder.Commit()
    removeBuilder.Destroy()

    non_layer_1_bodies = list(filter(lambda b:b.Layer != 1, list(display_part().Bodies)))

    if len(non_layer_1_bodies) > 0:
        delete_objects(non_layer_1_bodies)

    Curves = list(display_part().Curves)

    if len(Curves)> 0:
        delete_objects(Curves)

    Datums = list(display_part().Datums)

    if len(Datums)> 0:
        delete_objects(Datums)

    Notes = list(display_part().Notes)

    if len(Notes)> 0:
        delete_objects(Notes)

    if display_part().ComponentAssembly.RootComponent is not None:
        for child in list(display_part().ComponentAssembly.RootComponent.GetChildren()):
            if child.DisplayName in fasteners or child.IsSuppressed:
                delete_objects([child])

    contraints = list(display_part().DisplayedConstraints)

    if len(contraints)> 0:
        delete_objects(contraints)

    drawings = list(display_part().DrawingSheets)

    if len(drawings)> 0:
        delete_objects(drawings)

session().Parts.SetDisplay(original_display, False, False)
part_cleanup = session().NewPartCleanup()

#         using (part_cleanup)
#         {

# for k in dir(NXOpen.PartCleanup.CleanupParts):
#     print_(k)



# change this to Components.
# that way when the program gets here,
# we should be at the first display part.
# it will prevent them from cleaning up all open parts
# and fasteners that might not pertain to this assembly any more
part_cleanup.PartsToCleanup = NXOpen.PartCleanup.CleanupParts.Components
part_cleanup.CleanupAssemblyConstraints = True
part_cleanup.CleanupCAMObjects = True
part_cleanup.CleanupDraftingObjects = True
part_cleanup.CleanupFeatureData = True
part_cleanup.CleanupMatingData = True
part_cleanup.CleanupMotionData = True
part_cleanup.CleanupPartFamilyData = True
part_cleanup.CleanupRoutingData = True
part_cleanup.DeleteBrokenInterpartLinks = True
part_cleanup.DeleteDuplicateLights = True
part_cleanup.DeleteInvalidAttributes = True
part_cleanup.DeleteMaterials = True
part_cleanup.DeleteSpreadSheetData = True
part_cleanup.DeleteUnusedExpressions = True
part_cleanup.DeleteUnusedExtractReferences = True
part_cleanup.DeleteUnusedFonts = True
part_cleanup.DeleteUnusedObjects = True
part_cleanup.DeleteUnusedUnits = True
part_cleanup.DeleteVisualEditorData = True
part_cleanup.FixOffplaneSketchCurves = True
part_cleanup.GroupsToDelete = NXOpen.PartCleanup.DeleteGroups.All
part_cleanup.ResetComponentDisplay = NXOpen.PartCleanup.ResetComponentDisplayAction.RemoveAllChanges
part_cleanup.TurnOffHighlighting = True
part_cleanup.DoCleanup()


# def scale_part(part, scale_factor):
#     # Get the work part's bodies and scale them
#     bodies = part.Bodies
#     for body in bodies:
#         # Scale each body in the part by the scale factor
#         body.Transform(NXOpen.Matrix3x3.Identity(), NXOpen.Vector3d.Zero(), scale_factor)
#         print(f"Scaled body: {body.Name} by factor {scale_factor}")
