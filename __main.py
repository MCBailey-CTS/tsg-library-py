from typing import Union
import NXOpen
import NXOpen.Annotations
import NXOpen.Annotations
import NXOpen.UF
import NXOpen.Features
import NXOpen.Annotations
from NXOpen.Positioning import DisplayedConstraint, DisplayedConstraintCollection
from NXOpen import Session, TaggedObject
from __extensions__ import *
import NXOpen.Drawings


# print_()

# print_(NXOpen.Features.Feature)
# print_(NXOpen.Features.Feature.__bases__)
# print_(NXOpen.Annotations.BaseNote.__bases__)
# print_(NXOpen.SelectNXObjectList)
# print_(NXOpen.Positioning.DisplayedConstraint)
# print_(NXOpen.UF.UFSession.GetUFSession().Disp)
# set_display_part()

# obj=NXOpen.Utilities.NXObjectManager.Get(objectTag)

# ufsession().Vec3.Scale(scale, vector3d.__ToArray(), scaled_vec)

print_(ufsession().Vec3)

# ufsession().Vec3.Scale()


for x in dir(ufsession().Vec3):
    print_(x)

# temp = cycle_by_name("005")
# components = cast_components(temp)
# selected = select_components()
# print_(len(selected))
# trimmed_components = hash_

# for x in temp:
#     print_(component_ancestors(x))

# print_(len(temp))


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
