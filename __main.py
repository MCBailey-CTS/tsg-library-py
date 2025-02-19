import NXOpen
from NXOpen import Session


def print_(obj: object) -> None:
    session = Session.GetSession()
    listing_window = session.ListingWindow
    listing_window.Open()
    listing_window.WriteLine(str(obj))


# for x in dir(NXOpen.SessionUndoMarkData_Struct):
# UndoMarkData
# for x in dir(Session.UndoMarkId):
#     print_(x)

# o = Session.GetSession().SetUndoMark(NXOpen.Session.MarkVisibility.Visible, 'help')

# print_(type(o))

# UndoToMark
