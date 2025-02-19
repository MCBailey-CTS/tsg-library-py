import NXOpen
import NXOpen.UF
import NXOpen.Features
import NXOpen.Annotations
from NXOpen.Positioning import DisplayedConstraint, DisplayedConstraintCollection
from NXOpen import Session
from __extensions__ import *



# print_()

print_(NXOpen.Features.FeatureCollection.__base__)

# print_(NXOpen.Positioning.DisplayedConstraint)
for x in dir(DisplayedConstraintCollection):
    #  .CleanupParts.Components
    #  ):
    print_(x)

# selected_objects = NXOpen.UI.GetUI().SelectionManager.SelectTaggedObjects(
#         "Select components",
#         "Select components",
#         # NXOpen.SelectionResponseMemberType
#         NXOpen.SelectionSelectionScope.AnyInAssembly,
#         NXOpen.SelectionSelectionAction.ClearAndEnableSpecific,
#         False,
#         False,
#         [NXOpen.Selection.MaskTriple(63, 0, 0)],
#     )

# o = Session.GetSession().SetUndoMark(NXOpen.Session.MarkVisibility.Visible, 'help')

# print_(type(o))


# comp = NXOpen.Session.GetSession().Parts.WorkComponent

# comp.SetLayerOption()

# UndoToMark
