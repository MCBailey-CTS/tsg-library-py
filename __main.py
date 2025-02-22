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

for x in NXOpen.NXObjectAttributeType.__dict__.items():
    # for x in dir(NXOpen.Features.Block):
    print_(x)

# session().SetUndoMark(NXOpen.)

# convert all Nxopen to a single file
# with classes and sub classes
