import NXOpen


def print_(obj: object) -> None:
    session = NXOpen.Session.GetSession()
    listing_window = session.ListingWindow
    listing_window.Open()
    listing_window.WriteLine(str(obj))


session = NXOpen.Session.GetSession()
listing_window = session.ListingWindow
listing_window.Open()


# %freebeerRocks96^

# listing_window.WriteLine(str(NXOpen.Assemblies.Component))


# for comp in session.Parts.Display.ComponentAssembly.RootComponent.GetChildren():
#     t : NXOpen.Assemblies.Component = comp
#     listing_window.WriteLine(str(comp.DisplayName))


# for x in dir(session.Parts.Display):
for x in dir(NXOpen.Direction):
    print_(x)

# work_comp = session.Parts.WorkComponent


# print_(f'DisplayName: {work_comp.DisplayName}')

# print_(f'Name       : {work_comp.Name}')

# listing_window.WriteLine(f'Children    : {work_comp.GetChildren()}')

# for att in dir(work_comp):
#     print_(att)


# print_(work_comp)

# listing_window.WriteLine(str(dir(NXOpen.Curve.Curve)))


# v = str(NXOpen.Assemblies.Component.GetPosition.__doc__)

# listing_window.WriteLine(v)

# listing_window.WriteLine("in hwew")

# listing_window.WriteLine(str(dir(NXOpen.TaggedObject.Null)))
# listing_window.WriteLine()
# listing_window.WriteLine("This is a line of text.")
# listing_window.Close()
