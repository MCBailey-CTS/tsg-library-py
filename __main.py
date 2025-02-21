import enum
from typing import Dict, Union
import NXOpen
import NXOpen.Annotations
import NXOpen.Annotations
import NXOpen.UF
import NXOpen.Features
import NXOpen.Annotations
import NXOpen.Layer
from NXOpen.Positioning import DisplayedConstraint, DisplayedConstraintCollection
from NXOpen import Session, TaggedObject
from extensions__ import *
import NXOpen.Drawings

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

def part_descendant_parts(part: Part) -> List[Part]:
    __parts = {}
    __parts[part.Leaf] = part
    for component in component_descendants(part.ComponentAssembly.RootComponent):
        if isinstance(component.Prototype, Part):
            if component.DisplayName not in __parts.keys():
                __parts[component.DisplayName] = component.Prototype
    return list(__parts.values())

def component_assembly_struct(components:List[Component])->Dict[str,Tuple[Part, List[Component]]]:
    dict_:Dict[str,Tuple[Part, List[Component]]] = {}

    for comp in components:
        parent = comp.Parent
        while parent is not None:
            parent_part = parent.Prototype
            part_occs:Tuple[List[int], int] = ufsession().Assem.AskOccsOfPart(parent_part.Tag, comp.Prototype.Tag)
            descendants = []
            for t in part_occs[0]:
                descendants.append(cast_tagged_object(t))
            if parent_part.Leaf not in dict_    :
                dict_[parent_part.Leaf] = (parent_part, descendants)
            parent = parent.Parent




temp = cycle_by_name("041")
components = cast_components(temp)


dict_ = component_assembly_struct(components)


original = display_part()

try:

    for key in dict_:
        pair = dict_[key]
        session().Parts.SetDisplay(pair[0], False, False)
        print_(display_part().Leaf)
        for c in pair[1]:
            c.Layer = 10
            c.SetLayerOption(-1)
            c.RedisplayObject()


finally:
    session().Parts.SetDisplay(original, False, False)



# print_(dict_)

#       }
#   }

#   foreach(var key in  dict.Keys)
#   {
#       print(key.Leaf);
#       print(dict[key].Length);



#   }


# k = display_part().Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)

# print_(k)

# k.Destory()

# for x in dir(NXOpen.NXObjectAttributeType):
#     print_(x)

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
