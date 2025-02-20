import NXOpen
import NXOpen.Annotations
import NXOpen.Annotations
import NXOpen.UF
import NXOpen.Features
import NXOpen.Annotations
from NXOpen.Positioning import DisplayedConstraint, DisplayedConstraintCollection
from NXOpen import Session
from __extensions__ import *
import NXOpen.Drawings


# print_()

# print_(NXOpen.Features.Feature)
# print_(NXOpen.Features.Feature.__bases__)
# print_(NXOpen.Annotations.BaseNote.__bases__)
# print_(NXOpen.SelectNXObjectList)
# print_(NXOpen.Positioning.DisplayedConstraint)
print_(NXOpen.UF.UFSession.GetUFSession().Disp)
# for x in dir(NXOpen.Drawings.DrawingSheet):
#     print_(x)

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
