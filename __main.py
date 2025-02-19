import NXOpen
import NXOpen.UF
from NXOpen import Session


def print_(obj: object) -> None:
    session = Session.GetSession()
    listing_window = session.ListingWindow
    listing_window.Open()
    listing_window.WriteLine(str(obj))


session_ = Session.GetSession()
display = session_.Parts.Display
comps = list(filter(lambda x:'101' in x.Name, display.ComponentAssembly.RootComponent.GetChildren()))
result = NXOpen.UF.UFSession.GetUFSession().Assem.AskOccsOfPart(0,comps[0].Prototype.Tag )

print_(len(comps))
print_(len(result))
# for k in comps:
#     k.Highlight()

# for x in dir(NXOpen.SessionUndoMarkData_Struct):
# UndoMarkData
# for x in dir(NXOpen.UF.UFSession.GetUFSession().Assem):
#     print_(x)

# o = Session.GetSession().SetUndoMark(NXOpen.Session.MarkVisibility.Visible, 'help')

# print_(type(o))




# comp = NXOpen.Session.GetSession().Parts.WorkComponent

# comp.SetLayerOption()

# UndoToMark
