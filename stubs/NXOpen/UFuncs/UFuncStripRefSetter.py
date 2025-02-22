class UFuncStripRefSetter:
    #      public class StripRefSetter : _UFunc
    #  {
    #      public override void execute()
    #      {
    #          print(ufunc_rev_name);

    #          if (__display_part_ is null)
    #          {
    #              print("There is no displayed part loaded");
    #              return;
    #          }

    #          // Need to remove the objects from the reference sets first.
    #          __SetUndoMark(MarkVisibility.Visible, ufunc_rev_name);

    #          if (!__display_part_.Leaf.ToLower().EndsWith("-strip"))
    #          {
    #              print("Strip Refsetter can only be used on a strip.");
    #              return;
    #          }

    #          NXObject[] layer100Components = __display_part_.ComponentAssembly.RootComponent
    #              .GetChildren()
    #              .Where(child => child.Layer == 100)
    #              .Cast<NXObject>()
    #              .ToArray();

    #          NXObject[] layer100Objects = __display_part_.Layers
    #              .GetAllObjectsOnLayer(100)
    #              .Where(obj => obj is Curve || obj is Body)
    #              .Where(obj => !obj.IsOccurrence)
    #              .Concat(layer100Components)
    #              .ToArray();

    #          NXObject[] layer101Components = __display_part_.ComponentAssembly.RootComponent
    #              .GetChildren()
    #              .Where(child => child.Layer == 101)
    #              .Cast<NXObject>()
    #              .ToArray();

    #          NXObject[] layer101Objects = __display_part_
    #              .Layers.GetAllObjectsOnLayer(101)
    #              .Where(obj => obj is Curve || obj is Body)
    #              .Where(obj => !obj.IsOccurrence)
    #              .Concat(layer101Components)
    #              .ToArray();

    #          NXObject[] layer102Components = __display_part_.ComponentAssembly.RootComponent
    #              .GetChildren()
    #              .Where(child => child.Layer == 102)
    #              .Cast<NXObject>()
    #              .ToArray();

    #          NXObject[] layer102Objects = __display_part_.Layers
    #              .GetAllObjectsOnLayer(102)
    #              .Where(obj => obj is Curve || obj is Body)
    #              .Where(obj => !obj.IsOccurrence)
    #              .Concat(layer102Components)
    #              .ToArray();

    #          NXObject[] presses = __display_part_.ComponentAssembly.RootComponent
    #              .GetChildren()
    #              .Where(child => child.Name.ToUpper().Contains("PRESS"))
    #              .Cast<NXObject>()
    #              .ToArray();

    #          __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners(
    #              "BODY_NO_SLUG",
    #              layer101Components
    #                  .Concat(layer102Components)
    #                  .Cast<Component>()
    #                  .ToArray()
    #          );

    #          __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners(
    #              "BODY",
    #              layer100Components
    #                  .Concat(presses)
    #                  .Cast<Component>()
    #                  .ToArray()
    #          );

    #          if (layer100Objects.Length > 0)
    #          {
    #              // WORK_PARTS
    #              const string WORK_PARTS = nameof(WORK_PARTS);
    #              ReferenceSet work_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == WORK_PARTS);

    #              if (work_parts_refset is null)
    #              {
    #                  work_parts_refset = __display_part_.CreateReferenceSet();
    #                  work_parts_refset.SetName(WORK_PARTS);
    #              }

    #              work_parts_refset.AddObjectsToReferenceSet(layer100Objects);
    #          }

    #          if (layer101Objects.Length > 0)
    #          {
    #              // LIFTED_PARTS
    #              const string LIFTED_PARTS = nameof(LIFTED_PARTS);
    #              ReferenceSet lifted_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == LIFTED_PARTS);

    #              if (lifted_parts_refset is null)
    #              {
    #                  lifted_parts_refset = __display_part_.CreateReferenceSet();
    #                  lifted_parts_refset.SetName(LIFTED_PARTS);
    #              }

    #              // set children to body-with-no-slugs reference set before adding
    #              lifted_parts_refset.AddObjectsToReferenceSet(layer101Objects);
    #          }

    #          if (layer100Objects.Length > 0
    #              || layer100Objects.Length > 0
    #              || layer102Objects.Length > 0
    #              || presses.Length > 0)
    #          {
    #              // ALL_WITH_PRESSES
    #              const string ALL_WITH_PRESSES = nameof(ALL_WITH_PRESSES);
    #              ReferenceSet all_with_presses_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == ALL_WITH_PRESSES);

    #              if (all_with_presses_refset is null)
    #              {
    #                  all_with_presses_refset = __display_part_.CreateReferenceSet();
    #                  all_with_presses_refset.SetName(ALL_WITH_PRESSES);
    #              }

    #              // set children to body reference set before adding
    #              all_with_presses_refset.AddObjectsToReferenceSet(layer100Objects);
    #              // set children to body-no-slugs reference set before adding
    #              all_with_presses_refset.AddObjectsToReferenceSet(layer101Objects);
    #              // set children to body-no-slugs reference set before adding
    #              all_with_presses_refset.AddObjectsToReferenceSet(layer102Objects);
    #              // set children to body reference set before adding
    #              all_with_presses_refset.AddObjectsToReferenceSet(presses);

    #              Component[] grippers = __display_part_.ComponentAssembly.RootComponent
    #                  .GetChildren()
    #                  .Where(child => child.Layer == 235)
    #                  .ToArray();

    #              __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners("BODY", grippers);
    #              all_with_presses_refset.AddObjectsToReferenceSet(grippers);
    #          }

    #          if (layer100Objects.Length > 0 || layer100Objects.Length > 0 || layer102Objects.Length > 0)
    #          {
    #              // ALL_PARTS
    #              const string ALL_PARTS = nameof(ALL_PARTS);
    #              ReferenceSet all_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == ALL_PARTS);

    #              if (all_parts_refset is null)
    #              {
    #                  all_parts_refset = __display_part_.CreateReferenceSet();
    #                  all_parts_refset.SetName(ALL_PARTS);
    #              }

    #              // set children to body reference set before adding
    #              all_parts_refset.AddObjectsToReferenceSet(layer100Objects);
    #              // set children to body-no-slugs reference set before adding
    #              all_parts_refset.AddObjectsToReferenceSet(layer101Objects);
    #              // set children to body-no-slugs reference set before adding
    #              all_parts_refset.AddObjectsToReferenceSet(layer102Objects);
    #          }

    #          // TRANSFER_PARTS
    #          if (layer102Components.Length > 0 && __display_part_.Leaf.ToLower().EndsWith("-900-strip"))
    #          {
    #              const string TRANSFER_PARTS = nameof(TRANSFER_PARTS);
    #              ReferenceSet transfer_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == TRANSFER_PARTS);

    #              if (transfer_parts_refset is null)
    #              {
    #                  transfer_parts_refset = __display_part_.CreateReferenceSet();
    #                  transfer_parts_refset.SetName(TRANSFER_PARTS);
    #              }

    #              // set children to body-no-slugs reference set before adding
    #              transfer_parts_refset.AddObjectsToReferenceSet(layer102Components);
    #          }

    #          if (!__display_part_.Leaf.ToLower().EndsWith("-010-strip")
    #              && (layer100Objects.Length > 0
    #              || layer100Objects.Length > 0
    #              || layer102Objects.Length > 0))
    #          {
    #              // PROG_ONLY_WORK
    #              const string PROG_ONLY_WORK = nameof(PROG_ONLY_WORK);
    #              ReferenceSet prog_only_work_refset =__display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == PROG_ONLY_WORK);

    #              if (prog_only_work_refset is null)
    #              {
    #                  prog_only_work_refset = __display_part_.CreateReferenceSet();
    #                  prog_only_work_refset.SetName(PROG_ONLY_WORK);
    #              }

    #              // set children to body reference set before adding
    #              prog_only_work_refset.AddObjectsToReferenceSet(layer100Objects
    #                  .Where(obj => !obj.Name.StartsWith("T"))
    #                  .ToArray());

    #              // set children to body-no-slugs reference set before adding
    #              prog_only_work_refset.AddObjectsToReferenceSet(layer101Objects
    #                  .Where(obj => !obj.Name.StartsWith("T"))
    #                  .ToArray());

    #              // set children to body-no-slugs reference set before adding
    #              prog_only_work_refset.AddObjectsToReferenceSet(layer102Objects
    #                  .Where(obj => !obj.Name.StartsWith("T"))
    #                  .ToArray());
    #          }

    #          prompt("Complete");
    #      }
    #  }
    pass
