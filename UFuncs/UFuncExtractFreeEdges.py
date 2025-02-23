from extensions__ import *

ufunc_rev_name = "ExtractFreeEdges"


def __main__():
    if display_part() is None:
        print_("No Display Part")
        return
    session().SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name)
    selectedSheetBodies = select_many_sheet_bodies(ufunc_rev_name)
    edges = map(lambda b: b.GetEdges(), selectedSheetBodies)
    faces = map(lambda e: e.GetFaces(), edges)
    freeEdgeCurves = map(lambda f: edge_to_curve(f), faces)
    for curve in freeEdgeCurves:
        curve.Layer = display_part().Layers.WorkLayer
        curve.RedisplayObject()
    print(f"Created {len(freeEdgeCurves)} curves off of free edges.")
