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

# try
# {
#     // remove castings first
#     // MATERIAL == '2500, 3500'
#     // whack parameters
#     // remove fasteners
#     // all lines
#     // notes
#     // drawings
#     // all suppressed components
#     // in theory there should only be one body solid body on layer 1.
#     // assembly needs to be fully loaded, try to load, else tell the user they need to fully load. Show them the assembly path to the unloaded components.
#     // alert if part has more than one solid body on layer 1 at the end


#     // need to delete the udo
#     // also need to delete the all groups you can find, expressions and stuff
#     // part cleanup the whole assembly.
#     session_.SetUndoMark(Session.MarkVisibility.Visible, "GMSeal");
# session = NXOpen.Session.GetSession()


# def list_files_recursive(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             print(os.path.join(root, file))


def get_all_descendants(component):
    descendants = []

    # Get children of the current component
    children = component.GetChildren()

    # Iterate through children and collect them recursively
    for child in children:
        descendants.append(child)
        # Recursively get descendants of the child component
        descendants.extend(get_all_descendants(child))

    return descendants


def DescendantParts(part):
    parts = {}
    for component in get_all_descendants(part.ComponentAssembly.RootComponent):
        if isinstance(component.Prototype, NXOpen.Part):
            if component.DisplayName not in parts.keys():
                parts[component.DisplayName] = component.Prototype
    return list(parts.values())


# undo = session.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "DELETE")
# session.UpdateManager.AddObjectsToDeleteList(session.Parts.Display.ComponentAssembly.RootComponent.GetChildren())

# session.UpdateManager.DoUpdate(undo)


# def main():
session().SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "GMCleanAssembly" )
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



# for index, value in enumerate(parts):



#             try
#             {
#                 Part part = parts[i];
#                 prompt($"({i + 1} - {parts.Length}) -> {part.Leaf}");



    # session().Parts.SetDisplay(value, False, False)
    



suppresed_features = list(filter(lambda f:not f.Suppressed, display_part().Features))
print_(len(suppresed_features))
                    

#                 if (suppresed_features.Length > 0)
#                     session_.__DeleteObjects(suppresed_features);


# display = session.Parts.Display
# removeBuilder = display.Features.CreateRemoveParametersBuilder()
# removeBuilder.Objects.Add(display.Bodies.ToArray())
# removeBuilder.Objects.Add(display.Curves.ToArray())
# removeBuilder.Objects.Add(display.Points.ToArray())
# removeBuilder.Objects.Add(display.Datums.ToArray())
# removeBuilder.Objects.Add(display.CoordinateSystems.ToArray())

#     if len(removeBuilder.Objects) > 0:
#         removeBuilder.Commit()
# removeBuilder.Destory()

#                 Body[] non_layer_1_bodies = __display_part_.Bodies
#                     .ToArray()
#                     .Where(body => body.Layer != 1)
#                     .ToArray();

#                 if (non_layer_1_bodies.Length > 0)
#                     session_.__DeleteObjects(non_layer_1_bodies);


#                 session_.__DeleteObjects(__display_part_.Curves.ToArray());
#                 session_.__DeleteObjects(__display_part_.Datums.ToArray());
#                 session_.__DeleteObjects(__display_part_.Notes.ToArray());

#                 foreach (NXOpen.Assemblies.Component comp in __display_part_.__Children())
#                     if (fasteners.Contains(comp.DisplayName) || comp.IsSuppressed)
#                         comp.__Delete();

#                 NXOpen.Positioning.DisplayedConstraint[] contraints = __display_part_.DisplayedConstraints.ToArray();

#                 if (contraints.Length > 0)
#                     session_.__DeleteObjects(contraints);

#                 NXOpen.Drawings.DrawingSheet[] drawings = __display_part_.DrawingSheets.ToArray();

#                 if (drawings.Length > 0)
#                     session_.__DeleteObjects(drawings);


#                 __display_part_.ComponentGroups
#                     .ToArray()
#                     .ToList()
#                     .ForEach(g => g.__Delete());
#             }
#             catch (Exception ex)
#             {
#                 ex.__PrintException(parts[i].Leaf);
#             }
#     prompt("Performing Part Cleanup");
#     try
#     {
#         PartCleanup part_cleanup = session_.NewPartCleanup();

#         using (part_cleanup)
#         {

#             part_cleanup.PartsToCleanup = CleanupParts.All;
#             part_cleanup.CleanupAssemblyConstraints = true;
#             part_cleanup.CleanupCAMObjects = true;
#             part_cleanup.CleanupDraftingObjects = true;
#             part_cleanup.CleanupFeatureData = true;
#             part_cleanup.CleanupMatingData = true;
#             part_cleanup.CleanupMotionData = true;
#             part_cleanup.CleanupPartFamilyData = true;
#             part_cleanup.CleanupRoutingData = true;
#             part_cleanup.DeleteBrokenInterpartLinks = true;
#             part_cleanup.DeleteDuplicateLights = true;
#             part_cleanup.DeleteInvalidAttributes = true;
#             part_cleanup.DeleteMaterials = true;
#             part_cleanup.DeleteSpreadSheetData = true;
#             part_cleanup.DeleteUnusedExpressions = true;
#             part_cleanup.DeleteUnusedExtractReferences = true;
#             part_cleanup.DeleteUnusedFonts = true;
#             part_cleanup.DeleteUnusedObjects = true;
#             part_cleanup.DeleteUnusedUnits = true;
#             part_cleanup.DeleteVisualEditorData = true;
#             part_cleanup.FixOffplaneSketchCurves = true;
#             part_cleanup.GroupsToDelete = PartCleanup.DeleteGroups.All;
#             part_cleanup.ResetComponentDisplay = ResetComponentDisplayAction.RemoveAllChanges;
#             part_cleanup.TurnOffHighlighting = true;
#             part_cleanup.DoCleanup();
#         }
#     }
#     catch (Exception ex)
#     {
#         ex.__PrintException();
#     }
# }
# catch (Exception ex)
# {
#     ex.__PrintException();
# }

# stopwatch.Stop();

# print(stopwatch.Elapsed);
# class Main_:
#     @staticmethod

# print()
# list_files_recursive('G:\\0Library\\Fasteners')
# print_(os.listdir(,))

#     print_("madr it in here")

# if __name__ == '__main__':
#     main()
