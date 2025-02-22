class UFuncLayoutRefSets:
    #     internal class LayoutRefSets : _UFunc
    # {
    #     public override void execute()
    #     {
    #         print($"{ufunc_rev_name} - {__display_part_.Leaf}");
    #         session_.SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name);

    #         if (__display_part_ is null)
    #         {
    #             print("There is no displayed part loaded");
    #             return;
    #         }

    #         if (!__display_part_.Leaf.ToLower().EndsWith("-layout"))
    #         {
    #             print("Layout Refset can only be used on layouts.");
    #             return;
    #         }

    #         // BODY
    #         // BODY_NO_SLUG
    #         // INCOMING_SLUG
    #         // MATE
    #         string[] excluded_ref_sets = session_.__SqlReadMany(
    #             "tbl_properties",
    #             "LayoutRefSets_excluded_refsets"
    #         ).ToArray();

    #         ReferenceSet[] refsets = __display_part_.GetAllReferenceSets()
    #             .Where(r => r.Name != "BODY"
    #                         && r.Name != "BODY_NO_SLUG"
    #                         && r.Name != "INCOMING_BODY"
    #                         && r.Name != "MATE")
    #             .ToArray();

    #         foreach(var refset in refsets)
    #         {
    #             string refset_name = refset.Name;
    #             __display_part_.DeleteReferenceSet(refset);
    #             print($"Deleted ref set {refset_name}");
    #         }

    #         Body[] solid_bodies_layer_10 = __display_part_.Bodies
    #             .ToArray()
    #             .Where(b => b.IsSolidBody)
    #             .Where(b => b.Layer == 10)
    #             .ToArray();

    #         if (!__display_part_.__TryGetRefset("BODY", out ReferenceSet body_ref_set))
    #         {
    #             body_ref_set = __display_part_.CreateReferenceSet();
    #             body_ref_set.SetName("BODY");
    #             print("Created BODY refset");
    #         }

    #         body_ref_set.AddObjectsToReferenceSet(solid_bodies_layer_10);
    #         print($"Added {solid_bodies_layer_10.Length} body(s) to BODY refset.");

    #         // sql
    #         Body[] solid_bodies_layer_10_161 = solid_bodies_layer_10
    #             .Where(b => b.Color == 13)
    #             .ToArray();

    #         if (solid_bodies_layer_10_161.Length > 0)
    #         {
    #             if (!__display_part_.__TryGetRefset("BODY_NO_SLUG", out ReferenceSet body_no_slug_ref_set))
    #             {
    #                 body_no_slug_ref_set = __display_part_.CreateReferenceSet();
    #                 body_no_slug_ref_set.SetName("BODY_NO_SLUG");
    #                 print("Created BODY_NO_SLUG refset");
    #             }

    #             body_no_slug_ref_set.AddObjectsToReferenceSet(solid_bodies_layer_10_161);
    #             print($"Added {solid_bodies_layer_10_161.Length} body(s) to BODY_NO_SLUG refset.");
    #         }

    #         NXOpen.Layer.Category[] cats = __display_part_.LayerCategories.ToArray();

    #         for (int layer = 12; layer < 20; layer++)
    #             try
    #             {
    #                 Body[] solid_bodies = __display_part_.Bodies
    #                     .ToArray()
    #                     .Where(b => b.IsSolidBody)
    #                     .Where(b => b.Layer == layer)
    #                     .ToArray();

    #                 if (solid_bodies.Length == 0)
    #                     continue;

    #                 NXOpen.Layer.Category cat = cats.Where(c => c.Name != "ALL").FirstOrDefault(c => c.GetMemberLayers().ToHashSet().Contains(layer));

    #                 if (cat is null && solid_bodies.Length > 0)
    #                 {
    #                     print($"Layer {layer} has {solid_bodies.Length} but not layer category name");
    #                     continue;
    #                 }

    #                 string name = cat.Name;

    #                 ReferenceSet refset = null;

    #                 if (!__display_part_.__HasReferenceSet(name))
    #                 {
    #                     refset = __display_part_.CreateReferenceSet();
    #                     refset.SetName(name);
    #                     print($"Created Reference Set: {name}");
    #                 }
    #                 else
    #                     refset = __display_part_.__ReferenceSets(name);

    #                 refset.AddObjectsToReferenceSet(solid_bodies);
    #                 print($"Added {solid_bodies.Length} body(s) to ref set {name}");
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException();
    #             }
    #     }
    # }
    pass
