import traceback
from typing import Sequence
from extensions__ import *


def delete_unused_curves() -> None:
    curves = delete_unused_curves_select_many_curves()
    if len(curves) == 0:
        return
    for delete in curves:
        featTag = ufsession().Modl.AskObjectFeat(delete.Tag)
        if featTag == 0:
            delete_objects([delete])


def export_strip(
    chkSTP: bool,
    numUpDownCopies: int,
    chkPart: bool,
    chkPDF: bool,
    txtInput: str,
    chkCopy: bool,
) -> None:
    # GFolder folder = GFolder.Create(__display_part_.FullPath)
    # __display_part_.SetUserAttribute("DATE", -1, TodaysDate, NXOpen.Update.Option.Now)
    # if (folder is null)
    #     throw new Exception("The current displayed part is not in a GFolder.")
    # if (chkSTP)
    #     Part currentD = __display_part_
    #     Part currentW = session_.Parts.Work
    #     try
    #         CheckAssemblyDummyFiles()
    #         Part _currentD = __display_part_
    #         Part _currentW = session_.Parts.Work
    #         try
    #             SetLayersInBlanksAndLayoutsAndAddDummies(__display_part_)
    #         finally
    #             session_.Parts.SetDisplay(_currentD, false, false, out _)
    #             session_.Parts.SetWork(_currentW)
    #     finally
    #         session_.Parts.SetDisplay(currentD, false, false, out _)
    #         session_.Parts.SetWork(currentW)
    # if (numUpDownCopies > 0)
    #     ExportStripPrintDrawing(numUpDownCopies)
    # if (!chkPart && !chkPDF && !chkSTP)
    #     return
    # if (chkPDF)
    #     UpdateForPdf()
    # string outgoingFolderName = folder.CustomerNumber.Length == 6
    #     ? $"{folder.DirLayout}\\{txtInput}"
    #     : $"{folder.DirOutgoing}\\{txtInput}"
    # if (Directory.Exists(outgoingFolderName))
    #     if (MessageBox.Show(
    #             $@"Folder {outgoingFolderName} already exists, is it okay to overwrite the files in the folder?",
    #             @"Warning",
    #             MessageBoxButtons.YesNo) != DialogResult.Yes)
    #         return
    #     Directory.Delete(outgoingFolderName, true)
    # Directory.CreateDirectory(outgoingFolderName)
    # uf_.Ui.SetPrompt($"Export Strip: Setting layers in {__display_part_.Leaf}.")
    # __work_part_.Layers.SetState(1, State.WorkLayer)
    # for (int i = 2 i <= 256 i++)
    #     __work_part_.Layers.SetState(i, State.Hidden)
    # new[] { 6, 10, 200, 201, 202, 254 }.ToList()
    #     .ForEach(i => __work_part_.Layers.SetState(i, State.Selectable))
    # const string regex = "^\\d+-(?<op>\\d+)-.+$"
    # string op = Regex.Match(session_.Parts.Work.Leaf, regex, RegexOptions.IgnoreCase).Groups["op"].Value
    # string commonString = $"{folder.CustomerNumber}-{op}-strip {TodaysDate}"
    # uf_.Ui.SetPrompt(chkPart
    #     ? "Exporting \".prt\" file."
    #     : "Finding objects to export.")
    # if (chkPDF)
    #     uf_.Ui.SetPrompt("Exporting PDF......")
    #     string outputPath = ExportPDF(outgoingFolderName, commonString)
    #     print(File.Exists(outputPath)
    #         ? $"Successfully created \"{outputPath}\"."
    #         : $"Did not successfully create \"{outputPath}\".")
    # if (chkPart)
    #     string outputPath = ExportStripPart(outgoingFolderName)
    #     print(File.Exists(outputPath)
    #         ? $"Successfully created \"{outputPath}\"."
    #         : $"Did not successfully create \"{outputPath}\".")
    # if (chkSTP)
    #     UpdateForStp()
    #     ExportStripStp(outgoingFolderName)
    #     //string outputPath = $"{outgoingFolderName}\\{session_.Parts.Work.Leaf}-{TodaysDate}.stp"
    #     ////session_.Execute(@"C:\Repos\NXJournals\JOURNALS\export_strip.py", "ExportStrip", "export_stp", new object[] { outputPath })
    #     ////NXOpen.UF.UFSession.GetUFSession().Ui.SetPrompt("Exporting Step File.......")
    #     //NXOpen.StepCreator step = session_.DexManager.CreateStepCreator()
    #     //try
    #     //    //step.ExportDestination = NXOpen.BaseCreator.ExportDestinationOption.NativeFileSystem
    #     //    //step.SettingsFile = "U:\\nxFiles\\Step Translator\\ExternalStep_AllLayers.def"
    #     //    //step.
    #     //    //step.ExportAs = NXOpen.StepCreator.ExportAsOption.Ap214
    #     //    //step.InputFile = session_.Parts.Work.FullPath
    #     //    //step.OutputFile = outputPath
    #     //    //step.ProcessHoldFlag = true
    #     //    step.Commit()
    #     //finally
    #     //    step.Destroy()
    #     //print_(File.Exists(outputPath)
    #     //    ? $"Successfully created \"{outputPath}\"."
    #     //: $"Did not successfully create \"{outputPath}\".")
    # uf_.Ui.SetPrompt($"Zipping up {outgoingFolderName}.")
    # string[] filesToZip = Directory.GetFiles($"{outgoingFolderName}")
    # string zipFileName = $"{folder.CustomerNumber}-{txtInput}.7z"
    # string zipFile = $"{outgoingFolderName}\\{zipFileName}"
    # if (filesToZip.Length != 0)
    #     Zip7 zip = new Zip7(zipFile, filesToZip)
    #     zip.Start()
    #     zip.WaitForExit()
    # session_.ApplicationSwitchImmediate("UG_APP_MODELING")
    # session_.Parts.Work.Drafting.ExitDraftingApplication()
    raise NotImplementedError()


def strip_ref_setter() -> None:
    # print(ufunc_rev_name);

    # if (__display_part_ is null)
    # {
    #     print("There is no displayed part loaded");
    #     return;
    # }

    # // Need to remove the objects from the reference sets first.
    # __SetUndoMark(MarkVisibility.Visible, ufunc_rev_name);

    # if (!__display_part_.Leaf.ToLower().EndsWith("-strip"))
    # {
    #     print("Strip Refsetter can only be used on a strip.");
    #     return;
    # }

    # NXObject[] layer100Components = __display_part_.ComponentAssembly.RootComponent
    #     .GetChildren()
    #     .Where(child => child.Layer == 100)
    #     .Cast<NXObject>()
    #     .ToArray();

    # NXObject[] layer100Objects = __display_part_.Layers
    #     .GetAllObjectsOnLayer(100)
    #     .Where(obj => obj is Curve || obj is Body)
    #     .Where(obj => !obj.IsOccurrence)
    #     .Concat(layer100Components)
    #     .ToArray();

    # NXObject[] layer101Components = __display_part_.ComponentAssembly.RootComponent
    #     .GetChildren()
    #     .Where(child => child.Layer == 101)
    #     .Cast<NXObject>()
    #     .ToArray();

    # NXObject[] layer101Objects = __display_part_
    #     .Layers.GetAllObjectsOnLayer(101)
    #     .Where(obj => obj is Curve || obj is Body)
    #     .Where(obj => !obj.IsOccurrence)
    #     .Concat(layer101Components)
    #     .ToArray();

    # NXObject[] layer102Components = __display_part_.ComponentAssembly.RootComponent
    #     .GetChildren()
    #     .Where(child => child.Layer == 102)
    #     .Cast<NXObject>()
    #     .ToArray();

    # NXObject[] layer102Objects = __display_part_.Layers
    #     .GetAllObjectsOnLayer(102)
    #     .Where(obj => obj is Curve || obj is Body)
    #     .Where(obj => !obj.IsOccurrence)
    #     .Concat(layer102Components)
    #     .ToArray();

    # NXObject[] presses = __display_part_.ComponentAssembly.RootComponent
    #     .GetChildren()
    #     .Where(child => child.Name.ToUpper().Contains("PRESS"))
    #     .Cast<NXObject>()
    #     .ToArray();

    # __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners(
    #     "BODY_NO_SLUG",
    #     layer101Components
    #         .Concat(layer102Components)
    #         .Cast<Component>()
    #         .ToArray()
    # );

    # __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners(
    #     "BODY",
    #     layer100Components
    #         .Concat(presses)
    #         .Cast<Component>()
    #         .ToArray()
    # );

    # if (layer100Objects.Length > 0)
    # {
    #     // WORK_PARTS
    #     const string WORK_PARTS = nameof(WORK_PARTS);
    #     ReferenceSet work_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == WORK_PARTS);

    #     if (work_parts_refset is null)
    #     {
    #         work_parts_refset = __display_part_.CreateReferenceSet();
    #         work_parts_refset.SetName(WORK_PARTS);
    #     }

    #     work_parts_refset.AddObjectsToReferenceSet(layer100Objects);
    # }

    # if (layer101Objects.Length > 0)
    # {
    #     // LIFTED_PARTS
    #     const string LIFTED_PARTS = nameof(LIFTED_PARTS);
    #     ReferenceSet lifted_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == LIFTED_PARTS);

    #     if (lifted_parts_refset is null)
    #     {
    #         lifted_parts_refset = __display_part_.CreateReferenceSet();
    #         lifted_parts_refset.SetName(LIFTED_PARTS);
    #     }

    #     // set children to body-with-no-slugs reference set before adding
    #     lifted_parts_refset.AddObjectsToReferenceSet(layer101Objects);
    # }

    # if (layer100Objects.Length > 0
    #     || layer100Objects.Length > 0
    #     || layer102Objects.Length > 0
    #     || presses.Length > 0)
    # {
    #     // ALL_WITH_PRESSES
    #     const string ALL_WITH_PRESSES = nameof(ALL_WITH_PRESSES);
    #     ReferenceSet all_with_presses_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == ALL_WITH_PRESSES);

    #     if (all_with_presses_refset is null)
    #     {
    #         all_with_presses_refset = __display_part_.CreateReferenceSet();
    #         all_with_presses_refset.SetName(ALL_WITH_PRESSES);
    #     }

    #     // set children to body reference set before adding
    #     all_with_presses_refset.AddObjectsToReferenceSet(layer100Objects);
    #     // set children to body-no-slugs reference set before adding
    #     all_with_presses_refset.AddObjectsToReferenceSet(layer101Objects);
    #     // set children to body-no-slugs reference set before adding
    #     all_with_presses_refset.AddObjectsToReferenceSet(layer102Objects);
    #     // set children to body reference set before adding
    #     all_with_presses_refset.AddObjectsToReferenceSet(presses);

    #     Component[] grippers = __display_part_.ComponentAssembly.RootComponent
    #         .GetChildren()
    #         .Where(child => child.Layer == 235)
    #         .ToArray();

    #     __display_part_.ComponentAssembly.ReplaceReferenceSetInOwners("BODY", grippers);
    #     all_with_presses_refset.AddObjectsToReferenceSet(grippers);
    # }

    # if (layer100Objects.Length > 0 || layer100Objects.Length > 0 || layer102Objects.Length > 0)
    # {
    #     // ALL_PARTS
    #     const string ALL_PARTS = nameof(ALL_PARTS);
    #     ReferenceSet all_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == ALL_PARTS);

    #     if (all_parts_refset is null)
    #     {
    #         all_parts_refset = __display_part_.CreateReferenceSet();
    #         all_parts_refset.SetName(ALL_PARTS);
    #     }

    #     // set children to body reference set before adding
    #     all_parts_refset.AddObjectsToReferenceSet(layer100Objects);
    #     // set children to body-no-slugs reference set before adding
    #     all_parts_refset.AddObjectsToReferenceSet(layer101Objects);
    #     // set children to body-no-slugs reference set before adding
    #     all_parts_refset.AddObjectsToReferenceSet(layer102Objects);
    # }

    # // TRANSFER_PARTS
    # if (layer102Components.Length > 0 && __display_part_.Leaf.ToLower().EndsWith("-900-strip"))
    # {
    #     const string TRANSFER_PARTS = nameof(TRANSFER_PARTS);
    #     ReferenceSet transfer_parts_refset = __display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == TRANSFER_PARTS);

    #     if (transfer_parts_refset is null)
    #     {
    #         transfer_parts_refset = __display_part_.CreateReferenceSet();
    #         transfer_parts_refset.SetName(TRANSFER_PARTS);
    #     }

    #     // set children to body-no-slugs reference set before adding
    #     transfer_parts_refset.AddObjectsToReferenceSet(layer102Components);
    # }

    # if (!__display_part_.Leaf.ToLower().EndsWith("-010-strip")
    #     && (layer100Objects.Length > 0
    #     || layer100Objects.Length > 0
    #     || layer102Objects.Length > 0))
    # {
    #     // PROG_ONLY_WORK
    #     const string PROG_ONLY_WORK = nameof(PROG_ONLY_WORK);
    #     ReferenceSet prog_only_work_refset =__display_part_.GetAllReferenceSets().SingleOrDefault(set => set.Name == PROG_ONLY_WORK);

    #     if (prog_only_work_refset is null)
    #     {
    #         prog_only_work_refset = __display_part_.CreateReferenceSet();
    #         prog_only_work_refset.SetName(PROG_ONLY_WORK);
    #     }

    #     // set children to body reference set before adding
    #     prog_only_work_refset.AddObjectsToReferenceSet(layer100Objects
    #         .Where(obj => !obj.Name.StartsWith("T"))
    #         .ToArray());

    #     // set children to body-no-slugs reference set before adding
    #     prog_only_work_refset.AddObjectsToReferenceSet(layer101Objects
    #         .Where(obj => !obj.Name.StartsWith("T"))
    #         .ToArray());

    #     // set children to body-no-slugs reference set before adding
    #     prog_only_work_refset.AddObjectsToReferenceSet(layer102Objects
    #         .Where(obj => !obj.Name.StartsWith("T"))
    #         .ToArray());
    # }

    # prompt("Complete");
    raise NotImplementedError()


def layout_ref_sets() -> None:
    if display_part() is None:
        print_("There is no displayed part loaded")
        return

    if not display_part().Leaf.lower().endswith("-layout"):
        print_("Layout Refset can only be used on layouts.")
        return

    # BODY
    # BODY_NO_SLUG
    # INCOMING_SLUG
    # MATE
    # string[] excluded_ref_sets = session_.__SqlReadMany(
    #     "tbl_properties",
    #     "LayoutRefSets_excluded_refsets"
    # ).ToArray()

    for refset in list(display_part().GetAllReferenceSets()):
        if (
            refset.Name == "BODY"
            or refset.Name == "INCOMING_BODY"
            or refset.Name == "BODY_NO_SLUG"
            or refset.Name == "MATE"
        ):
            refset_name = refset.Name
            display_part().DeleteReferenceSet(refset)
            print_(f"Deleted ref set {refset_name}")

    solid_bodies_layer_10 = part_solid_bodies_on_layer(display_part(), 10)

    # if (!display_part().__TryGetRefset("BODY", out ReferenceSet body_ref_set))
    # {
    #     body_ref_set = display_part().CreateReferenceSet()
    #     body_ref_set.SetName("BODY")
    #     print_("Created BODY refset")
    # }

    # body_ref_set.AddObjectsToReferenceSet(solid_bodies_layer_10)
    # print_(f"Added {solid_bodies_layer_10.Length} body(s) to BODY refset.")

    # Body[] solid_bodies_layer_10_161 = solid_bodies_layer_10
    #     .Where(b => b.Color == 13)
    #     .ToArray()

    # if (solid_bodies_layer_10_161.Length > 0)
    # {
    #     if (!display_part().__TryGetRefset("BODY_NO_SLUG", out ReferenceSet body_no_slug_ref_set))
    #     {
    #         body_no_slug_ref_set = display_part().CreateReferenceSet()
    #         body_no_slug_ref_set.SetName("BODY_NO_SLUG")
    #         print_("Created BODY_NO_SLUG refset")
    #     }

    #     body_no_slug_ref_set.AddObjectsToReferenceSet(solid_bodies_layer_10_161)
    #     print_(f"Added {solid_bodies_layer_10_161.Length} body(s) to BODY_NO_SLUG refset.")
    # }

    # NXOpen.Layer.Category[] cats = display_part().LayerCategories.ToArray()

    for layer in range(12, 20):
        solid_bodies = part_solid_bodies_on_layer(display_part(), layer)

        if len(solid_bodies) == 0:
            continue

        # NXOpen.Layer.Category cat = cats.Where(c => c.Name != "ALL").FirstOrDefault(c => c.GetMemberLayers().ToHashSet().Contains(layer))

        # if (cat is null && solid_bodies.Length > 0)
        # {
        #     print_(f"Layer {layer} has {solid_bodies.Length} but not layer category name")
        #     continue
        # }

        # string name = cat.Name

        # ReferenceSet refset = null

        # if (!display_part().__HasReferenceSet(name))
        # {
        #     refset = display_part().CreateReferenceSet()
        #     refset.SetName(name)
        #     print_(f"Created Reference Set: {name}")
        # }
        # else
        #     refset = display_part().__ReferenceSets(name)

        # refset.AddObjectsToReferenceSet(solid_bodies)
        # print_(f"Added {solid_bodies.Length} body(s) to ref set {name}")
    raise NotImplementedError()


def assembly_wavelink_WavelinkSubtool() -> None:
    # session().SetUndoMark(Session.MarkVisibility.Visible, f"{ufunc_rev_name} - {nameof(WavelinkSubtool)}")
    target = assemby_wavelink_select_single_solid_body()
    if target is None:
        return
    tools = assemby_wavelink_select_many_component1()
    if len(tools) == 0:
        return
    with WithResetDisplayPart():
        with WithSuppressDisplay():
            try:
                current = display_part().Layers.WorkLayer

                try:
                    # work_component() = target.OwningComponent
                    display_part().Layers.SetState(96, NXOpen.Layer.State.WorkLayer)
                    for tool in tools:
                        with WithReferenceSetReset():
                            try:
                                # ReferenceSet reference_set = tool.__Prototype()
                                #     .GetAllReferenceSets()
                                #     .SingleOrDefault(refset => refset.Name == "SUB_TOOL" || refset.Name == "SUB-TOOL" || refset.Name == "SUBTOOL")

                                # if reference_set is None:
                                #     print_(f"Didn't find any sub tool reference sets for {tool.DisplayName} - {tool.Name} - {tool.Tag}")
                                #     continue

                                # tool.__ReferenceSet(reference_set.Name)
                                # ExtractFace linked_body = tool.__CreateLinkedBody()
                                # print_("//////////////////")
                                # print_($"Created {linked_body.GetFeatureName()} in {linked_body.OwningPart.Leaf}")
                                # BooleanFeature boolean_feature = target.__Subtract(linked_body.GetBodies())
                                # print_($"Created {boolean_feature.GetFeatureName()} in {linked_body.OwningPart.Leaf}")
                                pass

                                # }
                                # catch (NXException ex) when (ex.ErrorCode == 670030)
                                # {
                                #     print_($"Error occurred when trying to subtract {tool.DisplayName}, no interference.")
                                # }
                                # catch (InvalidOperationException)
                                # {
                                #     print_($"Found more than one sub tool reference set for {tool.DisplayName} - {tool.Name} - {tool.Tag}")
                                # }
                            except Exception as ex:
                                print_(ex)
                                traceback.print_exc()
                finally:
                    display_part().Layers.SetState(
                        current, NXOpen.Layer.State.WorkLayer
                    )
            except Exception as ex:
                print_(ex)
                traceback.print_exc()

    pass


def assembly_wavelink_WaveLinkFasteners(
    blank_tools: bool, shcs_ref_set: str, dwl_ref_set: str, jck_ref_set: str
) -> None:
    # session_.SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name)
    # using (session_.__UsingDisplayPartReset())
    try:
        targets = assembly_wavelink_select_multiple_solid_bodies()
        if len(targets) == 0:
            return
        tools = assembly_wavelink_select_multiple_components()
        if len(tools) == 0:
            return
        # using (session_.__UsingSuppressDisplay())
        for target in targets:
            for tool in tools:
                # using (session_.__UsingDisplayPartReset())
                # using (session_.__UsingResetWorkLayer())
                try:
                    # work_component() = target.OwningComponent
                    display_part().Layers.SetState(96, NXOpen.Layer.State.WorkLayer)
                    for child in tool.GetChildren():
                        try:
                            # if (!child.__IsLoaded())
                            #     print_(f"Child fastener {child.DisplayName} was not loaded.")
                            #     continue

                            if child.IsSuppressed:
                                continue
                            # todo
                            # using (child.__UsingReferenceSetReset())
                            # {
                            # string original_ref_set = child.ReferenceSet
                            # Component proto_child_fastener = child.__ProtoChildComp()

                            # if proto_child_fastener.Layer != LayerFastener:
                            #     continue

                            try:
                                # string[] ref_sets = new[] { shcs_ref_set, dwl_ref_set, jck_ref_set }
                                #     .Where(__r => !string.IsNullOrEmpty(__r))
                                #     .ToArray()

                                # string[] fastener_ref_set_names = proto_child_fastener.__Prototype()
                                #     .GetAllReferenceSets()
                                #     .Select(__r => __r.Name)
                                #     .Intersect(ref_sets)
                                #     .ToArray()

                                # switch (fastener_ref_set_names.Length)
                                # {
                                #     case 0:
                                #         if ((!(shcs_ref_set is null)&& child._IsShcs_())
                                #             || (!(dwl_ref_set is null) && child._IsDwl_())
                                #             || (!(jck_ref_set is null) && child._IsJckScrewTsg_() || child._IsJckScrew_()))
                                #             print_(
                                #                 $"Coulnd't find any valid ref sets for {child.DisplayName}")
                                #         continue
                                #     case 1:
                                #         child.__ReferenceSet(fastener_ref_set_names[0])
                                #         break
                                #     default:
                                #         print_(
                                #             $"Found more than one valid ref set for {child.DisplayName}")
                                #         continue
                                # }

                                # if (!target.__InterferesWith(child))
                                # {
                                #     print_(
                                #         $"Could not subtract fastener {child.DisplayName}, no interference.")
                                #     continue
                                # }

                                # ExtractFace ext = child.__CreateLinkedBody()
                                # //ext.__Layer(96)
                                # print_("//////////////////")
                                # print_($"Created {ext.GetFeatureName()} in {ext.OwningPart.Leaf}")
                                # BooleanFeature boolean_feature = target.__Subtract(ext.GetBodies())
                                # print_($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}")
                                ...
                            except:
                                raise NotImplementedError()
                            # }
                        except:
                            raise NotImplementedError()

                    if blank_tools:
                        tool.Blank()
                except:
                    raise NotImplementedError()
    except:
        raise NotImplementedError()


def assembly_wavelink_WaveLinkBoolean(
    blank_tools: bool, booleanType: Feature.BooleanType
) -> None:
    # session_.SetUndoMark(Session.MarkVisibility.Visible, "Assembly Wavelink")
    # using (session_.__UsingDisplayPartReset())
    try:
        # {
        targets = assembly_wavelink_select_multiple_solid_bodies()

        if len(targets) == 0:
            return

        tools = select_components()
        # SelectManyComponents1(c =>
        # {
        #     if (!(c is Component comp))
        #         return false

        #     return targets.All(b => b.OwningComponent.Tag != c.Tag)
        #     && !comp.DisplayName.__IsAssemblyHolder()
        # })

        if len(tools) == 0:
            return

        # var referenceSets = tools.Select(snapComponent => new { snapComponent, snapComponent.ReferenceSet }).ToList()
        # RefSetForm formCts = new RefSetForm(tools)

        # if (booleanType != Feature.BooleanType.Create)
        #     formCts.RemoveReferenceSet("BODY")

        # formCts.ShowDialog()

        # if (!formCts.IsSelected)
        #     return
        for target in targets:
            for tool in tools:
                # using (session_.__UsingDisplayPartReset())
                # using (child.__UsingReferenceSetReset())
                # using (session_.__UsingResetWorkLayer())
                # {
                current = display_part().Layers.WorkLayer

                try:
                    # {
                    # work_component() = target.OwningComponent

                    # display_part().Layers.SetState(96, NXOpen.Layer.State.WorkLayer)

                    # child.__ReferenceSet(formCts.SelectedReferenceSetName)

                    # foreach (var ext in child.__CreateLinkedBodies())
                    try:
                        # print_("//////////////////")

                        # print_($"Created {ext.GetFeatureName()} in {ext.OwningPart.Leaf}")

                        # switch (booleanType)
                        # {
                        #     case Feature.BooleanType.Subtract:
                        #         {
                        #             BooleanFeature boolean_feature = target.__Subtract(ext.GetBodies())
                        #             print_($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}")
                        #         }
                        #         break

                        #     case Feature.BooleanType.Unite:
                        #         {
                        #             BooleanFeature boolean_feature = target.__Unite(ext.GetBodies())
                        #             print_($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}")
                        #         }
                        #         break

                        #     case Feature.BooleanType.Intersect:
                        #         {
                        #             BooleanFeature boolean_feature = target.__Intersect(ext.GetBodies())
                        #             print_($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}")
                        #         }
                        #         break
                        # }
                        # }
                        # catch (NXException ex) when (ex.ErrorCode == 670030)
                        # {
                        #     print_($"Error occurred when trying to subtract {child.DisplayName}, no interference.")
                        # }
                        # catch (Exception ex)
                        # {
                        #     ex.__print_Exception()
                        # }
                        ...
                    except:
                        NotImplementedError()
                # }
                finally:
                    # {
                    # display_part().Layers.SetState(current, NXOpen.Layer.State.WorkLayer)
                    raise NotImplementedError()
                # }
            # }

        if blank_tools:
            for tool in tools:
                tool.Blank()
    except:
        raise NotImplementedError()
    raise NotImplementedError()


def extract_free_edges():
    if display_part() is None:
        print_("No Display Part")
        return
    session().SetUndoMark(Session.MarkVisibility.Visible, "extract_free_edges")
    selectedSheetBodies = select_many_sheet_bodies("extract_free_edges")
    edges = map(lambda b: b.GetEdges(), selectedSheetBodies)
    faces = map(lambda e: e.GetFaces(), edges)
    freeEdgeCurves = map(lambda f: edge_to_curve(f), faces)
    for curve in freeEdgeCurves:
        curve.Layer = display_part().Layers.WorkLayer
        curve.RedisplayObject()
    print(f"Created {len(freeEdgeCurves)} curves off of free edges.")


def copy_to_layer_50() -> None:
    # private const int LAYER = 50;
    # string message = $"{AssemblyFileVersion} - Copy To Layer 50";
    # Component[] compList = Selection.SelectManyComponents(message);
    # if (compList.Length == 0)
    #     return;
    # using (session_.__UsingDisplayPartReset())
    #     foreach (Component comp in compList)
    #         print("/////////////////");
    #         __work_component_ = comp;
    #         // if body exists on layer 50, delete body
    #         Body[] bodies_on_layer_50 = comp.__Prototype().Bodies
    #             .ToArray()
    #             .Where(__b => __b.IsSolidBody)
    #             .Where(__b => __b.Layer == LAYER)
    #             .ToArray();
    #         Body[] solid_bodies_layer_1 = comp.__Prototype().Bodies
    #             .ToArray()
    #             .Where(__b => __b.IsSolidBody)
    #             .Where(__b => __b.Layer == 1)
    #             .ToArray();
    #         switch (solid_bodies_layer_1.Length)
    #         {
    #             case 0:
    #                 print($"Did not a solid body on layer 1 in part {comp.DisplayName}");
    #                 return;
    #             case 1:
    #                 break;
    #             default:
    #                 print($"There is more than one solid body on layer 1 in part {comp.DisplayName}");
    #                 return;
    #         }
    #         string date = $"{DateTime.Now.Year}-{DateTime.Now.Month}-{DateTime.Now.Day}";
    #         Body[] layer_50_bodies = comp.__Prototype()
    #             .Layers
    #             .GetAllObjectsOnLayer(LAYER).OfType<Body>().ToArray();
    #         comp.__Prototype()
    #             .Layers
    #             .CopyObjects(LAYER, solid_bodies_layer_1);
    #         List<Body> new_layer_50_bodies = comp.__Prototype()
    #             .Layers
    #             .GetAllObjectsOnLayer(LAYER)
    #             .Except(layer_50_bodies)
    #             .OfType<Body>()
    #             .ToList();
    #         foreach (Body body in new_layer_50_bodies)
    #             body.OwningPart.Features.GetParentFeatureOfBody(body).SetName(date);
    #             body.Color = 7;
    #             body.LineFont = DisplayableObject.ObjectFont.Phantom;
    #             body.RedisplayObject();
    #         try
    #             comp.__Prototype().__ReferenceSets("BODY")
    #                 .RemoveObjectsFromReferenceSet(new_layer_50_bodies.ToArray<NXObject>());
    #         catch (Exception ex)
    #             ex.__PrintException();
    #         comp.__Prototype().Layers.MoveDisplayableObjects(LAYER + 1, layer_50_bodies);
    #         foreach (Body body in bodies_on_layer_50)
    #             body.Color = 7;
    #             body.LineFont = DisplayableObject.ObjectFont.Phantom;
    #             body.RedisplayObject();
    #             print($"Copied solid body to " +
    #                 $"{comp.__Prototype().Features.GetAssociatedFeature(body).GetFeatureName()} " +
    #                 $"in part {comp.DisplayName}");
    #         try
    #             comp.__Prototype().__ReferenceSets("BODY").RemoveObjectsFromReferenceSet(bodies_on_layer_50);
    #         catch (Exception ex)
    #             ex.__PrintException();

    raise NotImplementedError()


def gm_color_layer_color_layer_solid_body_1(part: Part, layer: int, color: int) -> None:
    session().Parts.SetDisplay(part, False, False)
    display_part().Layers.SetState(layer, State.Selectable)

    solid_body_layer_1 = list(
        filter(lambda b: b.Layer == 1, list(display_part().Bodies))
    )

    if not part_has_reference_set(display_part(), "PART"):
        if part_has_reference_set(display_part(), "BODY"):
            refset = part_get_reference_set(display_part(), "BODY")
            refset.SetName("PART")
        else:
            refset = part_crt_reference_set(display_part(), "PART")
            refset.AddObjectsToReferenceSet(solid_body_layer_1)

    assert (
        len(solid_body_layer_1) == 1
    ), f"There were {len(solid_body_layer_1)} solid bodies in part {part.Leaf}"

    display_part().Features.GetParentFeatureOfBody(
        solid_body_layer_1[0]
    ).MakeCurrentFeature()

    displayModification1 = session().DisplayManager.NewDisplayModification()
    displayModification1.ApplyToAllFaces = True
    displayModification1.ApplyToOwningParts = True
    displayModification1.NewColor = color
    displayModification1.NewLayer = layer
    displayModification1.Apply([solid_body_layer_1[0]])
    displayModification1.Dispose()
    features = list(display_part().Features)
    features[len(features) - 1].MakeCurrentFeature()


def gm_color_layer(layer: int, color: int) -> None:
    components = select_components()
    if len(components) == 0:
        return
    parts = hash_components_to_parts(components)
    with WithResetDisplayPart():
        for part in parts:
            try:
                gm_color_layer_color_layer_solid_body_1(part, layer, color)
            except Exception as ex:
                print_(ex)
    with WithResetDisplayPart():
        ancestors: Dict[str, Part] = {}
        for part in parts:
            part_occs = ufsession().Assem.AskOccsOfPart(display_part().Tag, part.Tag)
            for t in part_occs[0]:
                j = cast_component(t)
                for ancestor in component_ancestors(j):
                    if ancestor.DisplayName not in ancestors:
                        ancestors[ancestor.DisplayName] = ancestor.Prototype  # type: ignore
                with WithResetDisplayPart():
                    for ancest in ancestors.keys():
                        session().Parts.SetDisplay(ancestors[ancest], False, False)
                        display_part().Layers.SetState(layer, State.Selectable)
                        part_occs1 = ufsession().Assem.AskOccsOfPart(
                            ancestors[ancest].Tag, part.Tag
                        )

                        for h in part_occs1[0]:
                            cmp = cast_component(h)
                            cmp.Layer = layer
                            cmp.SetLayerOption(-1)
                            cmp.DirectOwner.ReplaceReferenceSet(cmp, "PART")
                            cmp.RedisplayObject()


def add_fasteners_strip_wave_out() -> None:
    try:
        for feat in list(work_part().Features):
            try:
                if not isinstance(feat, ExtractFace):
                    continue
                if not extract_face_is_linked_body(feat):
                    continue
                is_broken = ufsession().Wave.IsLinkBroken(feat.Tag)  # type: ignore
                if is_broken:
                    continue
                xform = ufsession().Wave.AskLinkXform(feat.Tag)  # type: ignore
                from_part_occ = ufsession().So.AskAssyCtxtPartOcc(  # type: ignore
                    xform, work_part().ComponentAssembly.RootComponent.Tag
                )
                if from_part_occ == 0:
                    continue
                point = [0.0, 0.0, 0.0]
                ufsession().So.AskPointOfXform(xform, point)  # type: ignore
                from_comp = cast_component(from_part_occ)
                origin = Point3d()
                corigin = component_origin(from_comp)
                if not point3d_equals_point3d(origin, corigin):
                    continue
                delete_objects([feat])
            except Exception as ex:
                print_(ex)
                traceback.print_exc()
    except:
        traceback.print_exc()


def add_fasteners_WaveIn() -> None:
    try:
        if not part_has_dynamic_block(work_part()):
            k = [
                body
                for body in list(work_part().Bodies)
                if body.IsSolidBody() and body.Layer == 1
            ]
            assert len(k) == 1
            solid_body_layer_1 = k[0]
        else:
            work_part().Layers.SetState(96, State.Visible)
            solid_body_layer_1 = part_get_dynamic_block(work_part()).GetBodies()[0]

        if work_part().ComponentAssembly.RootComponent is None:
            return

        for __child in work_part().ComponentAssembly.RootComponent.GetChildren():
            try:
                add_fasteners_WaveIn1(__child, solid_body_layer_1)
            except Exception as ex:
                print_("///////////////////")
                print_(ex)
                print_(traceback.format_exc())
                print_("///////////////////")
    except Exception as ex:
        print_(ex)
        traceback.print_exc()


def add_fasteners_WaveIn1(__child: Component, solid_body_layer_1: Body) -> None:
    if not component_is_loaded(__child):
        return
    if __child.IsSuppressed:
        return
    if __child.Layer != 99 and __child.Layer != 98 and __child.Layer != 97:
        return

    is_subtracted = False

    for feature in list(display_part().Features):
        if not isinstance(feature, ExtractFace):
            continue
        extract = feature
        if not extract_face_is_linked_body(extract):
            continue
        if feature_is_broken(extract):
            continue
        xform_tag = feature_xform(extract)
        point = ufsession().So.AskPointOfXform(xform_tag)
        origin = Point3d(point[0], point[1], point[2])
        if point3d_equals_point3d(origin, component_origin(__child)):
            continue
        is_subtracted = True
        break

    if is_subtracted:
        return
    if not __child.HasInstanceUserAttribute(
        "subtract", NXObjectAttributeType.String, -1
    ):
        return

    subtract_att = nxobject_get_attribute(__child, "subtract")

    if subtract_att == "HANDLING" or subtract_att == "SHORT-TAP":
        subtract_ref_set = "SHORT-TAP"
    elif subtract_att == "BLIND_OPP":
        subtract_ref_set = "CBORE_BLIND_OPP"
    elif subtract_att == "CLR_DRILL":
        subtract_ref_set = "CLR_HOLE"
    else:
        subtract_ref_set = subtract_att

    component_set_reference_set(__child, subtract_ref_set)

    linked_body = CreateLinkedBody(work_part(), __child)
    linked_body.OwningPart.Layers.MoveDisplayableObjects(96, linked_body.GetBodies())
    linked_body.SetName(f"{__child.DisplayName}, {subtract_att}")

    try:
        SubtractLinkedBody(work_part(), solid_body_layer_1, linked_body)
    except:
        # catch (NXException ex) when (ex.ErrorCode == 670030)
        print_("//////////////////////////////////////")
        print_(traceback.format_exc())
        print(
            f"Could not subtract {__child.DisplayName} with reference set {subtract_ref_set}"
        )
        print_("//////////////////////////////////////")

    if subtract_att == "HANDLING" or subtract_att == "WIRE_TAP":
        __child.Layer = 98
        __child.RedisplayObject()
    elif subtract_att == "TOOLING":
        __child.Layer = 97
        __child.RedisplayObject()

    if __child.Layer != 99 or subtract_att == "HANDLING" or subtract_att == "WIRE_TAP":
        component_set_reference_set(__child, "Empty")
        part_get_reference_set(work_part(), "BODY").RemoveObjectsFromReferenceSet(
            [__child]
        )
        return
    component_set_reference_set(__child, "BODY")
    part_get_reference_set(work_part(), "BODY").AddObjectsToReferenceSet([__child])


def add_fasteners_InsertWireTaps() -> None:
    session().SetUndoMark(NXOpen.SessionMarkVisibility.Visible, "WIRE_TAP")
    if display_part().Tag == work_part().Tag:
        for i in [99, 98, 97]:
            display_part().Layers.SetState(i, State.Selectable)
    wireTapScrew = session_get_or_open_part(
        "G:\\0Library\\Fasteners\\Metric\\SocketHeadCapScrews\\008\\8mm-shcs-020.prt"
    )

    display_part().WCS.Rotate(WCSAxis.XAxis, 90.0)
    savedCsys = display_part().WCS.Save()  # type: ignore
    rotateOrientation = savedCsys.Orientation.Element
    x = 1 if display_part().PartUnits == NXOpen.BasePartUnits.Inches else 25.4
    offset2 = [3.00 * x, 0.875 * x, 0.00]
    mappedOffset1 = ufsession().Csys.MapPoint(
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_WCS_COORDS,
        [1.00 * x, 0.875 * x, 0.00],
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_COORDS,
    )
    mappedOffset2 = ufsession().Csys.MapPoint(
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_WCS_COORDS,
        offset2,
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_COORDS,
    )
    mappedToWork1 = ufsession().Csys.MapPoint(
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_COORDS,
        mappedOffset1,
        NXOpen.UF.UFConstants.UF_CSYS_WORK_COORDS,
    )
    mappedToWork2 = ufsession().Csys.MapPoint(
        NXOpen.UF.UFConstants.UF_CSYS_ROOT_COORDS,
        mappedOffset2,
        NXOpen.UF.UFConstants.UF_CSYS_WORK_COORDS,
    )
    basePoint1 = Point3d(mappedToWork1[0], mappedToWork1[1], mappedToWork1[2])
    basePoint2 = Point3d(mappedToWork2[0], mappedToWork2[1], mappedToWork2[2])
    component1 = work_part().ComponentAssembly.AddComponent(
        wireTapScrew, "SHORT-TAP", "8mm-shcs-020", basePoint1, rotateOrientation, 98
    )
    component2 = work_part().ComponentAssembly.AddComponent(
        wireTapScrew, "SHORT-TAP", "8mm-shcs-020", basePoint2, rotateOrientation, 98
    )

    display_part().WCS.Rotate(WCSAxis.XAxis, -90.0)
    component1.SetInstanceUserAttribute("subtract", -1, "WIRE_TAP", UpdateOption.Now)
    component2.SetInstanceUserAttribute("subtract", -1, "WIRE_TAP", UpdateOption.Now)
    delete_objects([savedCsys])


def add_fasteners_SubstituteFasteners(nxPart: Part) -> None:
    with WithLockUpdates():
        fasteners_to_substitue: Sequence[Component] = []
        func = None
        if is_shcs(nxPart):
            func = is_shcs
        elif is_dwl(nxPart):
            func = is_dwl
        elif is_jck_screw(nxPart):
            func = is_jck_screw
        elif is_jck_screw_tsg(nxPart):
            func = is_jck_screw_tsg

        if func is None:
            raise Exception()

        fasteners_to_substitue = [
            c
            for c in work_part().ComponentAssembly.RootComponent.GetChildren()
            if func(c)
        ]

        if len(fasteners_to_substitue) == 0:
            print(f"Couldn't find any fasteners to substitue with {nxPart.Leaf}")
            return

        original_display_name = fasteners_to_substitue[0].DisplayName
        replaceBuilder = work_part().AssemblyManager.CreateReplaceComponentBuilder()  # type: ignore

        try:
            replaceBuilder.ReplacementPart = nxPart.FullPath
            replaceBuilder.MaintainRelationships = True
            replaceBuilder.ReplaceAllOccurrences = False
            replaceBuilder.ComponentNameType = ReplaceComponentBuilder.ComponentNameOption.AsSpecified  # type: ignore
            replaceBuilder.ComponentsToReplace.Add(fasteners_to_substitue)
            replaceBuilder.Commit()
        finally:
            replaceBuilder.Destroy()
        print(f"Substituted fasteners {original_display_name} -> {nxPart.Leaf}")


def add_fasteners_WaveOut1(child: Component) -> None:
    if child.Parent.Tag != child.OwningPart.ComponentAssembly.RootComponent.Tag:
        raise Exception("Can only wave out immediate children.")
    linkedBody = AddFastenersGetLinkedBody(child.OwningPart, child)
    delete_objects([linkedBody])


def add_fasteners_WaveOut() -> None:
    try:
        if work_part().Tag == display_part().Tag:
            for __child in work_part().ComponentAssembly.RootComponent.GetChildren():
                try:
                    if (
                        __child.Layer != 99
                        and __child.Layer != 98
                        and __child.Layer != 97
                    ):
                        continue
                    if __child.IsSuppressed:
                        continue
                    if not is_fastener(__child):
                        continue
                    add_fasteners_WaveOut1(__child)
                except:
                    print_("//////////////////")
                    print_(traceback.format_exc())
                    print_("//////////////////")
            return

        for child in work_component().GetChildren():
            if child.IsSuppressed:
                continue
            if not is_fastener(child):
                continue
            protoPartOcc = GetProtoPartOcc(work_part(), child)
            add_fasteners_WaveOut1(protoPartOcc)  # type: ignore
    except Exception as ex:
        print_(ex)


def add_fasteners_SetWcsToWorkPart() -> None:
    # dynamicBlock = part_get_dynamic_block(work_part())
    # origin = block_get_origin(dynamicBlock)
    # orientation = block_get_orientation(dynamicBlock)
    # if work_part().Tag == display_part().Tag:
    #     display_part().WCS.SetOriginAndMatrix(origin, orientation)
    #     return
    # absCsys = display_part().CoordinateSystems.CreateCoordinateSystem(
    #     Point3d(), matrix3x3_identity(), True
    # )
    # compCsys = display_part().CoordinateSystems.CreateCoordinateSystem(
    #     component_origin(work_component()),
    #     component_orientation(work_component()),
    #     True,
    # )
    # newOrigin = map_point_csys_to_csys(origin, compCsys, absCsys)
    # newXVec = map_point_csys_to_csys(
    #     axisx(component_orientation(work_component())), compCsys, absCsys
    # )
    # newYVec = map_vector_csys_to_csys(
    #     axisy(component_orientation(work_component())), compCsys, absCsys
    # )
    # newOrientation = to_matrix3x3(newXVec, newYVec)
    # display_part().WCS.SetOriginAndMatrix(newOrigin, newOrientation)
    raise NotImplementedError()


def export_design() -> None:
    #     Part topLevelAssembly,
    #     Component[] __components,
    #     string outgoingDirectoryName = null,
    #     bool isRto = false,
    #     bool zipAssembly = false,
    #     bool pdf4Views = false,
    #     bool stp999 = false,
    #     bool stpDetails = false,
    #     bool stpSee3DData = false,
    #     bool dwgBurnout = false,
    #     bool parasolid = false,
    #     bool paraCasting = false,
    #     bool print4Views = false,
    #     bool isChange = false)
    # {
    #     using (session_.__UsingDisplayPartReset())
    #     {
    #         //using (session_.__UsingSuppressDisplay())
    #         {
    #             ufsession_.Ui.SetPrompt("Filtering components to export.")
    #             GFolder folder = GFolder.Create(topLevelAssembly.FullPath)

    #             if (!__components.All(comp => comp.OwningPart.Tag == topLevelAssembly.Tag))
    #                 throw new InvalidOperationException(
    #                     "All valid components must be under the top level display part.")

    #             bool isSixDigit = folder.CustomerNumber.Length == 6
    #             HashSet<Part> hashedParts = new HashSet<Part>()

    #             foreach (Component comp in __components)
    #             {
    #                 if (!(comp.Prototype is Part part))
    #                     continue

    #                 hashedParts.Add(part)
    #             }

    #             Part[] validParts = hashedParts.ToArray()

    #             // sql
    #             const string sevenZip = @"C:\Program Files\7-Zip\7z.exe"

    #             if (!File.Exists(sevenZip))
    #                 throw new FileNotFoundException($"Could not find \"{sevenZip}\".")

    #             string parentFolder = isSixDigit
    #                 ? folder.DirDesignInformation
    #                 : folder.DirOutgoing

    #             string exportDirectory = string.IsNullOrEmpty(outgoingDirectoryName)
    #                 ? null
    #                 : $"{parentFolder}\\{outgoingDirectoryName}"

    #             if (!(isRto && isSixDigit) && zipAssembly && exportDirectory != null && Directory.Exists(exportDirectory))
    #                 switch (MessageBox.Show($@"{exportDirectory} already exisits, would you like to overwrite it?",
    #                             @"Warning", MessageBoxButtons.YesNo))
    #                 {
    #                     case DialogResult.Yes:
    #                         Directory.Delete(exportDirectory, true)
    #                         break
    #                     default:
    #                         return
    #                 }

    #             if (!(isRto && isSixDigit))
    #                 if (!string.IsNullOrEmpty(outgoingDirectoryName))
    #                     Directory.CreateDirectory(exportDirectory)

    #             // If this is an RTO, then we need to delete the data files in the appropriate op folders.
    #             if (isRto && !isChange)
    #                 try
    #                 {
    #                     DeleteOpFolders(__display_part_, folder)
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException()
    #                 }

    #             if (exportDirectory != null)
    #                 Directory.CreateDirectory(exportDirectory)

    #             Regex detailRegex = new Regex(RegexDetail, RegexOptions.IgnoreCase)
    #             validParts = validParts.Distinct(new EqualityLeaf()).ToArray()

    #             IDictionary<string, ISet<Part>> exportDict = SortPartsForExport(validParts)

    #             //#pragma warning disable CS0612 // Type or member is obsolete
    #             //                        if (!CheckSizeDescriptions(exportDict["PDF_4-VIEW"]))
    #             //                            switch (MessageBox.Show(
    #             //                                        "At least one block did not match its' description. Would you like to continue?",
    #             //                                        "Warning", MessageBoxButtons.YesNo))
    #             //                            {
    #             //                                case DialogResult.Yes:
    #             //                                    break
    #             //                                default:
    #             //                                    return
    #             //                            }
    #             //#pragma warning restore CS0612 // Type or member is obsolete

    #             __display_part_.__Save()

    #             Stopwatch stop_watch = new Stopwatch()

    #             stop_watch.Start()

    #             try
    #             {
    #                 /////////////////////
    #                 Process assemblyProcess = null

    #                 // Sets up the strip.
    #                 if (isRto || stpDetails || zipAssembly)
    #                     using (session_.__UsingDisplayPartReset())
    #                         SetUpStrip(folder)

    #                 UpdateParts(
    #                     isRto,
    #                     pdf4Views, stpDetails, exportDict["PDF_4-VIEW"],
    #                     print4Views, exportDict["PDF_4-VIEW"],
    #                     dwgBurnout, exportDict["DWG_BURNOUT"],
    #                     stp999, exportDict["STP_999"],
    #                     stpSee3DData, exportDict["STP_SEE3D"],
    #                     paraCasting, exportDict["X_T_CASTING"],
    #                     __components)

    #                 Dictionary<string, Process> dict = new Dictionary<string, Process>()

    #                 if (isRto && detailRegex.IsMatch(topLevelAssembly.Leaf))
    #                 {
    #                     string stpPath = CreatePath(folder, topLevelAssembly, "-Step-Assembly", ".stp")

    #                     string dir = Path.GetDirectoryName(stpPath)

    #                     if (!Directory.Exists(dir))
    #                         Directory.CreateDirectory(dir)

    #                     AssemblyExportDesignDataStp(topLevelAssembly.FullPath, stpPath, FilePathExternalStepAssemblyDef)
    #                 }

    #                 // Prints the parts with 4-Views.
    #                 if (print4Views)
    #                     using (session_.__UsingDisplayPartReset())
    #                     {
    #                         PrintPdfs(exportDict["PDF_4-VIEW"])
    #                     }

    #                 // Gets the processes that will create the pdf 4-Views.
    #                 if (isRto || pdf4Views)
    #                     foreach (Part part in exportDict["PDF_4-VIEW"])
    #                         try
    #                         {
    #                             if (part.Leaf.EndsWith("000"))
    #                                 continue

    #                             string pdfPath = CreatePath(folder, part, "-Pdf-4-Views", ".pdf")

    #                             string dir = Path.GetDirectoryName(pdfPath)

    #                             if (!Directory.Exists(dir))
    #                                 Directory.CreateDirectory(dir)

    #                             if (File.Exists(pdfPath))
    #                                 File.Delete(pdfPath)

    #                             print($"PDF 4-VIEW -> {pdfPath}")
    #                             AssemblyExportDesignDataPdf(part, "4-VIEW", pdfPath)
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException()
    #                         }

    #                 // If this is a RTO then
    #                 if (isRto || stpDetails)
    #                     foreach (Part part in exportDict["PDF_4-VIEW"])
    #                     {
    #                         string stpPath = CreatePath(folder, part, "-Step-Details", ".stp")

    #                         string dir = Path.GetDirectoryName(stpPath)

    #                         if (!Directory.Exists(dir))
    #                             Directory.CreateDirectory(dir)

    #                         if (File.Exists(stpPath))
    #                             File.Delete(stpPath)

    #                         print($"Step Details -> {part.FullPath}")
    #                         AssemblyExportDesignDataStp(part.FullPath, stpPath, FilePathExternalStepDetailDef)
    #                     }

    #                 if (zipAssembly && !(isRto || stpDetails))
    #                     try
    #                     {
    #                         string path = $"{exportDirectory}\\{topLevelAssembly.Leaf}.stp"

    #                         string dir = Path.GetDirectoryName(path)

    #                         if (!Directory.Exists(dir))
    #                             Directory.CreateDirectory(dir)

    #                         print($"{nameof(AssemblyExportDesignDataStp)} - {topLevelAssembly}")

    #                         AssemblyExportDesignDataStp(topLevelAssembly.FullPath, path, FilePathExternalStepDetailDef)
    #                     }
    #                     catch (Exception ex)
    #                     {
    #                         ex.__PrintException()
    #                     }

    #                 // Gets the processes that create stp see 3d data.
    #                 if (isRto || stpSee3DData)
    #                     foreach (Part part in exportDict["STP_SEE3D"])
    #                         try
    #                         {
    #                             string output = CreatePath(folder, part, "-Step-See-3D-Data", ".stp")

    #                             string dir = Path.GetDirectoryName(output)

    #                             if (!Directory.Exists(dir))
    #                                 Directory.CreateDirectory(dir)

    #                             print($"STEP See 3d - {part.FullPath}")

    #                             AssemblyExportDesignDataStp(part.FullPath, output, @"U:\nxFiles\Step Translator\ExternalStep_Detail.def")
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException()
    #                         }

    #                 // Gets the processes that create stp 999 details.
    #                 if (isRto || stp999)
    #                     foreach (Part part in exportDict["STP_999"])
    #                         try
    #                         {
    #                             string output = CreatePath(folder, part, "-Step-999", ".stp")

    #                             string dir = Path.GetDirectoryName(output)

    #                             if (!Directory.Exists(dir))
    #                                 Directory.CreateDirectory(dir)

    #                             print($"999 - {part.FullPath}")
    #                             AssemblyExportDesignDataStp(part.FullPath, output, @"U:\nxFiles\Step Translator\ExternalStep_Detail.def")
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException()
    #                         }

    #                 // Gets the processes that create burnout dwgs.
    #                 if (isRto || dwgBurnout)
    #                     foreach (Part part in exportDict["DWG_BURNOUT"])
    #                         try
    #                         {
    #                             string output = CreatePath(folder, part, "-Dwg-Burnouts", ".dwg")

    #                             string dir = Path.GetDirectoryName(output)

    #                             if (!Directory.Exists(dir))
    #                                 Directory.CreateDirectory(dir)

    #                             print($"BURNOUT - {part.FullPath}")

    #                             AssemblyExportDesignDataDwg(part.FullPath, "BURNOUT", output)
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException()
    #                         }

    #                 //if (dwg4Views)
    #                 //    foreach (Part part in hashedParts)
    #                 //        try
    #                 //        {
    #                 //            string output = CreatePath(folder, part, "-Dwg-4-Views", ".dwg")

    #                 //            string dir = Path.GetDirectoryName(output)

    #                 //            if (!Directory.Exists(dir))
    #                 //                Directory.CreateDirectory(dir)

    #                 //            //print($"BURNOUT - {part.FullPath}")

    #                 //            Dwg(part.FullPath, "4-VIEW", output)
    #                 //        }
    #                 //        catch (Exception ex)
    #                 //        {
    #                 //            ex.__PrintException()
    #                 //        }

    #                 // Creates casting parasolids.
    #                 if (isRto || paraCasting)
    #                     foreach (Part castingPart in exportDict["X_T_CASTING"])
    #                         try
    #                         {
    #                             print($"{nameof(CreateCasting)} - {castingPart.FullPath}")
    #                             CreateCasting(castingPart, folder)
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException()
    #                         }

    #                 HashSet<string> expectedFiles = new HashSet<string>(dict.Keys)

    #                 HashSet<string> directoriesToExport = new HashSet<string>(expectedFiles.Select(Path.GetDirectoryName))

    #                 CreateDirectoriesDeleteFiles(expectedFiles)

    #                 string zipPath = $"{exportDirectory}\\{topLevelAssembly.Leaf}_NX.7z"

    #                 if ((isRto && !isSixDigit) || (zipAssembly && !isRto))
    #                 {
    #                     print(nameof(Assembly))
    #                     assemblyProcess = Assembly(topLevelAssembly, false, zipPath)
    #                     assemblyProcess.Start()
    #                 }

    #                 prompt("Validating Stp Files.")

    #                 print(nameof(WriteStpCyanFiles))
    #                 WriteStpCyanFiles(expectedFiles)

    #                 prompt("Zipping up data folders.")

    #                 // Gets all the data folders that were created and zips them up and places them in the proper outgoingData folderWithCtsNumber if this is an RTO.
    #                 if (isRto && !isSixDigit)
    #                 {
    #                     print(nameof(ZipUpDataFolders))
    #                     ZipUpDataFolders(directoriesToExport, exportDirectory)
    #                 }

    #                 if (isRto && !isSixDigit)
    #                 {
    #                     print(nameof(ZipupDirectories))
    #                     ZipupDirectories(sevenZip, directoriesToExport, zipPath)
    #                 }

    #                 foreach (string file_key in dict.Keys)
    #                     try
    #                     {
    #                         Process process = dict[file_key]

    #                         if (File.Exists(file_key))
    #                             continue

    #                         print($"Recreating: {file_key}")
    #                         prompt($"Recreating: {file_key}")

    #                         process.Start()

    #                         process.WaitForExit()
    #                     }
    #                     catch (Exception ex)
    #                     {
    #                         ex.__PrintException()
    #                     }

    #                 // Checks to make sure that any expected data files were actually created.
    #                 if (expectedFiles.Count > 0)
    #                 {
    #                     print(nameof(ErrorCheck))
    #                     ErrorCheck(isRto, zipAssembly, expectedFiles)
    #                 }

    #                 // Moves the sim report to the out going folderWithCtsNumber if one exists.
    #                 if (isRto && !isSixDigit && !(exportDirectory is null))
    #                 {
    #                     print(nameof(MoveSimReport))
    #                     MoveSimReport(folder, exportDirectory)
    #                 }

    #                 // Moves the stock list to the outgoing folderWithCtsNumber if one exists.
    #                 if (isRto && !isSixDigit && !(exportDirectory is null))
    #                 {
    #                     print(nameof(MoveStocklist))
    #                     MoveStocklist(folder, topLevelAssembly.Leaf, exportDirectory)
    #                 }

    #                 if (!(exportDirectory is null))
    #                 {
    #                     print(nameof(ZipupDataDirectories))
    #                     ZipupDataDirectories(exportDirectory, assemblyProcess)
    #                 }

    #                 /////////////////////////
    #             }
    #             finally
    #             {
    #                 stop_watch.Stop()

    #                 print($"{stop_watch.Elapsed.Minutes}:{stop_watch.Elapsed.Seconds}")
    #             }
    #         }
    #     }
    # }
    raise NotImplementedError()
