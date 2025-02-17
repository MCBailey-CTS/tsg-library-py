
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features

session = NXOpen.Session.GetSession()
listing_window = session.ListingWindow
listing_window.Open()


# listing_window.WriteLine(str(NXOpen.Assemblies.Component))



# for comp in session.Parts.Display.ComponentAssembly.RootComponent.GetChildren():
#     t : NXOpen.Assemblies.Component = comp
#     listing_window.WriteLine(str(comp.DisplayName))



# for x in dir(session.Parts.Display):
for x in dir(NXOpen.Features):
    listing_window.WriteLine(str(x))

# listing_window.WriteLine(str(dir(NXOpen.TaggedObject.Null)))
# listing_window.WriteLine()
# listing_window.WriteLine("This is a line of text.")
listing_window.Close()