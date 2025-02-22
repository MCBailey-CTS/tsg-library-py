class UFuncExtractFreeEdges:
    #     internal class ExtractFreeEdgeCurves : _UFunc
    # {
    #     public override void execute()
    #     {
    #         print(ufunc_rev_name);

    #         if (__display_part_ is null)
    #         {
    #             print("There is no displayed part loaded");
    #             return;
    #         }

    # 		// sql
    # 		// make this is easier to read
    #         session_.SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name);
    #         // Allows the user to select sheet bodies.
    #         Body[] selectedSheetBodies = Selection.SelectManySheetBodies(ufunc_rev_name);
    #         // Gets the edges from the selected sheet bodies.
    #         Edge[] edges = selectedSheetBodies.SelectMany(body => body.GetEdges()).ToArray();
    #         // Gets the free edges, (the edges that are attached to one face).
    #         Edge[] freeEdges = edges.Where(edge => edge.GetFaces().Length == 1).ToArray();
    #         // Gets the curve representation of the {freeEdges}.
    #         Curve[] freeEdgeCurves = freeEdges.Select(edge => edge.__ToCurve()).ToArray();

    #         // Sets all the free edge curves to the current work layer.
    #         foreach (Curve curve in freeEdgeCurves)
    #             curve.__Layer(WorkLayer);

    #         print($"Created {freeEdgeCurves.Length} curves off of free edges.");
    #     }
    # }
    pass
