import traceback
from GMCleanAssembly import delete_objects
from extensions__ import *


class UFuncAddFasteners:
    
    #     //public const string AddFastenersSizeFile2 = @"U:\nxFiles\UfuncFiles\AddFastenerSizes.txt"
    #     private static BasePart.Units _unit = BasePart.Units.Millimeters
    #     private int WorkPartChangedRegister
    #     public static int _translucency = -1
    #     private int _1x_2x = 2

    @staticmethod
    def point3d_equals_point3d(pnt0:Point3d, pnt1:Point3d)->bool:
        raise Exception()
    
    @staticmethod
    def strip_wave_out():
        try:
            for feat in work_part().Features.ToArray():
                try:
                    if   not isinstance(feat, ExtractFace):continue
                    if not extract_face_is_linked_body(feat):continue
                    is_broken=ufsession().Wave.IsLinkBroken(feat.Tag)
                    if is_broken :continue
                    xform = ufsession().Wave.AskLinkXform(feat.Tag)
                    from_part_occ =ufsession().So.AskAssyCtxtPartOcc(xform, work_part().ComponentAssembly.RootComponent.Tag)
                    if from_part_occ == NXOpen.Tag.Null:continue
                    point = [0.0,0.0,0.0]
                    ufsession().So.AskPointOfXform(xform, point)
                    from_comp = NXOpen.TaggedObjectManager.GetTaggedObject(from_part_occ)

                    origin =Point3d()
                    corigin = component_origin(from_comp)
                    if not UFuncAddFasteners.point3d_equals_point3d(origin, corigin):continue
                    delete_objects(feat)
                except Exception as ex:
                    print_(ex)
                    traceback.print_exc()
        finally:
            WorkPartChanged()

    

    #     private void BtnViewWcs_Click(object sender, EventArgs e)
    #     {
    #         Matrix3x3 coordSystem = display_part().WCS.CoordinateSystem.Orientation.Element
    #         display_part().Views.WorkView.Orient(coordSystem)
    #     }

    #     private void CmbGridSpacing_SelectedIndexChanged(object sender, EventArgs e)
    #     {
    #         if (display_part() is null)
    #             return

    #         double _grid_spacing = (double)cmbGridSpacing.SelectedValue

    # 		// sql - tolerance
    #         if (_grid_spacing.__Abs() < .001)
    #         {
    #             display_part().Preferences.Workplane.ShowGrid = false
    #             display_part().Preferences.Workplane.SnapToGrid = false
    #             return
    #         }

    #         display_part().Preferences.Workplane.SnapToGrid = true

    #         WorkPlane.GridSize grid = new WorkPlane.GridSize
    #         {
    #             MajorGridSpacing = _grid_spacing,
    #             MinorLinesPerMajor = 1,
    #             SnapPointsPerMinor = 1
    #         }

    #         display_part().Preferences.Workplane.SetRectangularUniformGridSize(grid)
    #     }

    #     private void ButtonSelectComponent_Click(object sender, EventArgs e)
    #     {
    #         // we want to hide the other forms here
    #         // var session_control_part = session_.Parts.ToArray().First(p => p.Leaf.StartsWith("session-control"))

    #         // session_control_part.SetUserAttribute("show", -1, "false", NXOpen.Update.Option.Now)

    #         // session_control_part.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False)

    #         try
    #         {
    #             Properties.Settings.Default.tsg_library_hide_forms = true
    #             Settings.Default.Save()

    #             using (session_.__UsingFormShowHide(this))
    #             {
    #                 try
    #                 {
    #                     SelectTarget()
    #                     listBoxSelection.Enabled = true
    #                     btnWireTaps.Enabled = true
    #                     chkCycleAdd.Enabled = true
    #                     chkReverseCycleAdd.Enabled = true
    #                     btnPlanView.Enabled = true
    #                     btnOrigin.Enabled = true
    #                     btnWireTaps.Enabled = true
    #                     menuItemUnits.Enabled = true
    #                     btnSelectComponent.Enabled = false
    #                     toolStripMenuItem1.Enabled = true
    #                     btnChangeRefSet.Enabled = true
    #                 }
    #                 catch (NothingSelectedException)
    #                 {
    #                     btnSelectComponent.Enabled = true
    #                     Reset()
    #                 }
    #                 catch (NoDynamicBlockException)
    #                 {
    #                     print(@"No dynamic block in current Work Part. You will have to move the WCS manually.")
    #                     Reset()
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException()
    #                 }
    #             }
    #         }
    #         finally
    #         {
    #             // session_control_part.SetUserAttribute("show", -1, "true", NXOpen.Update.Option.Now)

    #             // session_control_part.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False)

    #             Show()
    #         //catch (Exception ex)
    #         //{
    #         //}

    #             Properties.Settings.Default.tsg_library_hide_forms = false
    #             Settings.Default.Save()
    #         }
    #     }

    #     private void LoadShcs()
    #     {
    #         string unit_dir = IsFormMetric ? "Metric" : "English"
    #         listBoxSelection.SelectedIndexChanged -= ListBoxSelection_SelectedIndexChanged
    #         listBoxSelection.DataSource = null
    #         string suffix

    #         switch (_1x_2x)
    #         {
    #             case 1:
    #                 suffix = ""
    #                 break
    #             case 2:
    #                 suffix = "-2x"
    #                 break
    #             default:
    #                 print("Cannot determine which fastener to use")
    #                 return
    #         }

    #         FastenerListItem[] shcss = Directory
    #             .GetDirectories($@"G:\0Library\Fasteners\{unit_dir}\SocketHeadCapScrews{suffix}")
    #             .Select(__f => new FastenerListItem(Path.GetFileNameWithoutExtension(__f), __f))
    #             .ToArray()
    # 		// sql
    #         const string preferred_diameters_path = @"U:\nxFiles\UfuncFiles\AddFastenersPreferredDiameters.txt"
    #         const string preferred_gm_diameters_path = @"U:\nxFiles\UfuncFiles\AddFastenersPreferredDiametersGm.txt"

    #         if (cmbPreferred.SelectedIndex == 1)
    #         {
    #             HashSet<string> shcs_preferred_dirs = File.ReadAllLines(preferred_diameters_path)
    #                 .Where(__s => !string.IsNullOrEmpty(__s))
    #                 .Where(__s => !string.IsNullOrWhiteSpace(__s))
    #                 .Select(Path.GetDirectoryName)
    #                 .ToHashSet()

    #             shcss = shcss.Where(item => shcs_preferred_dirs.Contains(item.Value)).ToArray()
    #         }
    #         else if (cmbPreferred.SelectedIndex == 2)
    #         {
    #             HashSet<string> shcs_preferred_dirs = File.ReadAllLines(preferred_gm_diameters_path)
    #                 .Where(__s => !string.IsNullOrEmpty(__s))
    #                 .Where(__s => !string.IsNullOrWhiteSpace(__s))
    #                 .Select(Path.GetDirectoryName)
    #                 .ToHashSet()

    #             shcss = shcss.Where(item => shcs_preferred_dirs.Contains(item.Value)).ToArray()
    #         }

    #         listBoxSelection.DisplayMember = nameof(FastenerListItem.Text)
    #         listBoxSelection.ValueMember = nameof(FastenerListItem.Value)
    #         listBoxSelection.DataSource = shcss
    #         listBoxSelection.SelectedIndex = -1
    #         listBoxSelection.SelectedIndexChanged += ListBoxSelection_SelectedIndexChanged
    #     }

    #     private void LoadDowel()
    #     {
    #         string unit_dir = IsFormMetric ? "Metric" : "English"
    #         listBoxSelection.SelectedIndexChanged -= ListBoxSelection_SelectedIndexChanged
    #         listBoxSelection.DataSource = null

    #         chkCycleAdd.Checked = false
    #         chkReverseCycleAdd.Checked = false

    #         FastenerListItem[] dowels = Directory.GetFiles($@"G:\0Library\Fasteners\{unit_dir}\Dowels", "*.prt",
    #                 SearchOption.TopDirectoryOnly)
    #             .Select(__f => new FastenerListItem(Path.GetFileNameWithoutExtension(__f), __f))
    #             .ToArray()

    #         listBoxSelection.DisplayMember = nameof(FastenerListItem.Text)
    #         listBoxSelection.ValueMember = nameof(FastenerListItem.Value)
    #         listBoxSelection.DataSource = dowels
    #         listBoxSelection.SelectedIndex = -1
    #         listBoxSelection.SelectedIndexChanged += ListBoxSelection_SelectedIndexChanged
    #     }

    #     private void LoadJack()
    #     {
    #         string unit_dir = IsFormMetric ? "Metric" : "English"
    #         listBoxSelection.SelectedIndexChanged -= ListBoxSelection_SelectedIndexChanged
    #         listBoxSelection.DataSource = null
    #         chkCycleAdd.Checked = false
    #         chkReverseCycleAdd.Checked = false

    #         FastenerListItem[] jackScrewsTsg = Directory.GetFiles($@"G:\0Library\Fasteners\{unit_dir}\JackScrews",
    #                 "*-tsg.prt",
    #                 SearchOption.TopDirectoryOnly)
    #             .Select(__f => new FastenerListItem(__f.__LeafF(), __f))
    #             .OrderBy(__s =>
    #             {
    #                 Match match = Regex.Match(__s.Text, "^_?(?<diameter>\\d+)(mm)?-jck-screw-tsg$")

    #                 if (!match.Success)
    #                     throw new Exception($"{__s.Text} didn't match regex")

    #                 return int.Parse(match.Groups["diameter"].Value)
    #             })
    #             .ToArray()

    #         FastenerListItem[] jackScrews = Directory.GetFiles($@"G:\0Library\Fasteners\{unit_dir}\JackScrews",
    #                 "*-screw.prt",
    #                 SearchOption.TopDirectoryOnly)
    #             .Select(__f => new FastenerListItem(Path.GetFileNameWithoutExtension(__f), __f))
    #             .ToArray()

    #         jackScrewsTsg = jackScrewsTsg.Concat(jackScrews).ToArray()
    #         listBoxSelection.DisplayMember = nameof(FastenerListItem.Text)
    #         listBoxSelection.ValueMember = nameof(FastenerListItem.Value)
    #         listBoxSelection.DataSource = jackScrewsTsg
    #         listBoxSelection.SelectedIndex = -1
    #         listBoxSelection.SelectedIndexChanged += ListBoxSelection_SelectedIndexChanged
    #     }

    #     private void Reset()
    #     {
    #         try
    #         {
    #             if (work_part() is null)
    #                 return

    #             btnChangeRefSet.Enabled = false
    #             toolStripMenuItem1.Enabled = false
    #             chkSubstitute.Checked = false
    #             listBoxSelection.SelectedIndex = -1
    #             __work_component_?.__Translucency(0)

    #             if (work_part().__HasDynamicBlock())
    #             {
    #                 work_part().__DynamicBlock().GetBodies()[0].__Translucency(0)
    #                 toolStripMenuItem1.Enabled = true
    #             }
    #             else if (!work_part().__HasDynamicBlock())
    #             {
    #                 Body[] bodies = work_part().Bodies.ToArray()
    #                     .Where(__b => __b.IsSolidBody)
    #                     .Where(__b => __b.Layer == 1)
    #                     .ToArray()

    #                 if (bodies.Length == 1)
    #                     work_part().__SingleSolidBodyOnLayer1().__Translucency(0)

    #                 toolStripMenuItem1.Enabled = true
    #             }
    #             else
    #             {
    #                 btnOrigin.Enabled = false
    #                 btnPlanView.Enabled = false
    #                 btnWireTaps.Enabled = false
    #                 btnChangeRefSet.Enabled = true
    #             }

    #             if (work_part().Tag != display_part().Tag)
    #                 ufsession_.Assem.SetWorkPart(NXOpen.Tag.Null)
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException()
    #         }
    #         finally
    #         {
    #             btnSelectComponent.Enabled = true
    #             btnReset.Enabled = true
    #         }
    #     }

    #     private void BtnOtherOk_Click(object sender, EventArgs e)
    #     {
    #         using (session_.__UsingFormShowHide(this))
    #         {
    #             try
    #             {
    #                 session_.SetUndoMark(Session.MarkVisibility.Visible, "AddFasteners")

    #                 if (__work_component_ is null)
    #                 {
    #                     // Working at the displayed part
    #                     WaveIn()
    #                     MakePlanView(display_part().WCS.Save())
    #                     return
    #                 }

    #                 // Working at the assembly level.
    #                 Component originalWorkComponent = __work_component_

    #                 using (new DisplayPartReset())
    #                 {
    #                     display_part() = work_part()
    #                     WaveIn()
    #                     MakePlanView(display_part().WCS.Save())
    #                 }

    #                 foreach (Component child in originalWorkComponent.GetChildren())
    #                 {
    #                     if (!child.__IsLoaded())
    #                     {
    #                         print($"Child {child.Name} is not loaded")
    #                         continue
    #                     }
    #                     Component protoPartOcc = _GetProtoPartOcc(originalWorkComponent.__Prototype(), child)

    #                     switch (protoPartOcc.Layer)
    #                     {
    #                         case LayerDwlTooling:
    #                         case LayerShcsHandlingWireTap:
    #                             break
    #                         default:
    #                             child.__ReferenceSet(protoPartOcc.ReferenceSet)
    #                             break
    #                     }
    #                 }
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException()
    #             }
    #             finally
    #             {
    #                 Reset()
    #                 btnReset.Enabled = true
    #                 btnSelectComponent.Enabled = true
    #             }
    #         }
    #     }

    #     public static void WaveIn()
    #     {
    #         try
    #         {
    #             Body solid_body_layer_1

    #             if (!work_part().__HasDynamicBlock())
    #             {
    #                 solid_body_layer_1 = work_part().__SingleSolidBodyOnLayer1()
    #             }
    #             else
    #             {
    #                 work_part().Layers.SetState(96, State.Visible)
    #                 solid_body_layer_1 = work_part().__DynamicBlock().GetBodies()[0]
    #             }

    #             if (work_part().ComponentAssembly.RootComponent is null)
    #                 return

    #             foreach (Component __child in work_part().ComponentAssembly.RootComponent.GetChildren())
    #                 try
    #                 {
    #                     WaveIn(__child, solid_body_layer_1)
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException()
    #                 }
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException()
    #         }
    #     }

    #     public static void WaveIn(Component __child, Body solid_body_layer_1)
    #     {
    #         if (!__child.__IsLoaded())
    #             return

    #         if (__child.IsSuppressed)
    #             return

    #         if (__child.Layer != 99 && __child.Layer != 98 && __child.Layer != 97)
    #             return

    #         bool is_subtracted = false

    #         foreach (var feature in display_part().Features.ToArray())
    #         {
    #             if (!(feature is ExtractFace extract))
    #                 continue

    #             if (!extract.__IsLinkedBody())
    #                 continue

    #             if (extract.__IsBroken())
    #             {
    #                 ufsession_.Wave.AskBrokenLinkSourcePart(extract.Tag, out var part_name, out var t)
    #                 print(part_name)
    #                 print(t)
    #                 continue
    #             }

    #             var xform_tag = extract.__XFormTag()
    #             var point = new double[3]
    #             ufsession_.So.AskPointOfXform(xform_tag, point)
    #             var origin = point.__ToPoint3d()

    #             if (!origin.__IsEqualTo(__child.__Origin()))
    #                 continue

    #             is_subtracted = true
    #             break
    #         }

    #         if (is_subtracted)
    #             return

    #         if (!__child.HasInstanceUserAttribute("subtract", NXObject.AttributeType.String, -1))
    #             return

    #         string subtract_att = __child.__GetAttribute("subtract")
    #         string subtract_ref_set

    #         switch (subtract_att)
    #         {
    #             case "HANDLING":
    #             case "WIRE_TAP":
    #                 subtract_ref_set = "SHORT-TAP"
    #                 break
    #             case "BLIND_OPP":
    #                 subtract_ref_set = "CBORE_BLIND_OPP"
    #                 break
    #             case "CLR_DRILL":
    #                 subtract_ref_set = "CLR_HOLE"
    #                 break
    #             default:
    #                 subtract_ref_set = subtract_att
    #                 break
    #         }

    #         string current = __child.ReferenceSet
    #         __child.__ReferenceSet(subtract_ref_set)

    #         ExtractFace linked_body = CreateLinkedBody(work_part(), __child)
    #         linked_body.OwningPart.Layers.MoveDisplayableObjects(96, linked_body.GetBodies())
    #         linked_body.SetName($"{__child.DisplayName}, {subtract_att}")

    #         try
    #         {
    #             SubtractLinkedBody(work_part(), solid_body_layer_1, linked_body)
    #         }
    #         catch (NXException ex) when (ex.ErrorCode == 670030)
    #         {
    #             print($"Could not subtract {__child.DisplayName} with reference set {subtract_ref_set}")
    #         }

    #         switch (subtract_att)
    #         {
    #             case "HANDLING":
    #             case "WIRE_TAP":
    #                 __child.__Layer(98)
    #                 break
    #             case "TOOLING":
    #                 __child.__Layer(97)
    #                 break
    #         }

    #         if (__child.Layer != 99 || subtract_att == "HANDLING" || subtract_att == "WIRE_TAP")
    #         {
    #             __child.__ReferenceSet("Empty")
    #             work_part().__FindReferenceSet("BODY").RemoveObjectsFromReferenceSet(new NXObject[] { __child })
    #             return
    #         }

    #         __child.__ReferenceSet("BODY")

    #         work_part().GetAllReferenceSets()
    #             .Single(__r => __r.Name == "BODY")
    #             .AddObjectsToReferenceSet(new[] { __child })
    #     }

    #     private static Component _GetProtoPartOcc(Part owningPart, Component partOcc)
    #     {
    #         Tag instance = ufsession_.Assem.AskInstOfPartOcc(partOcc.Tag)

    #         Tag prototypeChildPartOcc =
    #             ufsession_.Assem.AskPartOccOfInst(owningPart.ComponentAssembly.RootComponent.Tag, instance)

    #         return (Component)prototypeChildPartOcc.__ToTaggedObject()
    #     }

    #     private static BooleanFeature SubtractLinkedBody(Part owningPart, Body subtractBody, ExtractFace linkedBody)
    #     {
    #         BooleanBuilder booleanBuilder = owningPart.Features.CreateBooleanBuilderUsingCollector(null)

    #         using (new Destroyer(booleanBuilder))
    #         {
    #             booleanBuilder.Target = subtractBody
    #             ScCollector collector = owningPart.ScCollectors.CreateCollector()

    #             SelectionIntentRule[] rules =
    #             {
    #                 owningPart.ScRuleFactory.CreateRuleBodyDumb(linkedBody.GetBodies())
    #             }

    #             collector.ReplaceRules(rules, false)
    #             booleanBuilder.ToolBodyCollector = collector
    #             booleanBuilder.Operation = Feature.BooleanType.Subtract
    #             return (BooleanFeature)booleanBuilder.Commit()
    #         }
    #     }

    #     private static ExtractFace CreateLinkedBody(Part owningPart, Component child)
    #     {
    #         Body[] toolBodies = child.__Members()
    #             .OfType<Body>()
    #             .Where(body => body.IsSolidBody)
    #             .ToArray()

    #         ExtractFaceBuilder linkedBodyBuilder = owningPart.Features.CreateExtractFaceBuilder(null)

    #         using (new Destroyer(linkedBodyBuilder))
    #         {
    #             linkedBodyBuilder.Associative = true
    #             linkedBodyBuilder.FeatureOption = ExtractFaceBuilder.FeatureOptionType.OneFeatureForAllBodies
    #             linkedBodyBuilder.FixAtCurrentTimestamp = false
    #             linkedBodyBuilder.ParentPart = ExtractFaceBuilder.ParentPartType.OtherPart
    #             linkedBodyBuilder.Type = ExtractFaceBuilder.ExtractType.Body

    #             SelectionIntentRule[] rules =
    #             {
    #                 owningPart.ScRuleFactory.CreateRuleBodyDumb(toolBodies)
    #             }

    #             linkedBodyBuilder.ExtractBodyCollector.ReplaceRules(rules, false)
    #             return (ExtractFace)linkedBodyBuilder.Commit()
    #         }
    #     }

   

    #     public static void InsertWireTaps()
    #     {
    #         session_.SetUndoMark(Session.MarkVisibility.Visible, "WIRE_TAP")

    #         if (display_part().Tag == work_part().Tag)
    #             new[] { 99, 98, 97 }.ToList().ForEach(i => display_part().Layers.SetState(i, State.Selectable))

    #         Part wireTapScrew =
    #             session_.__FindOrOpen(@"G:\0Library\Fasteners\Metric\SocketHeadCapScrews\008\8mm-shcs-020.prt")
    #         display_part().WCS.Rotate(WCS.Axis.XAxis, 90.0)
    #         CartesianCoordinateSystem savedCsys = display_part().WCS.Save()
    #         Matrix3x3 rotateOrientation = savedCsys.Orientation.Element
    #         double x = display_part().PartUnits == BasePart.Units.Inches ? 1 : 25.4
    #         double[] offset1 = { 1.00 * x, .875 * x, 0.00 }
    #         double[] offset2 = { 3.00 * x, .875 * x, 0.00 }
    #         double[] mappedOffset1 = new double[3]
    #         ufsession_.Csys.MapPoint(UF_CSYS_ROOT_WCS_COORDS, offset1, UF_CSYS_ROOT_COORDS, mappedOffset1)
    #         double[] mappedOffset2 = new double[3]
    #         ufsession_.Csys.MapPoint(UF_CSYS_ROOT_WCS_COORDS, offset2, UF_CSYS_ROOT_COORDS, mappedOffset2)
    #         double[] mappedToWork1 = new double[3]
    #         ufsession_.Csys.MapPoint(UF_CSYS_ROOT_COORDS, mappedOffset1, UF_CSYS_WORK_COORDS, mappedToWork1)
    #         double[] mappedToWork2 = new double[3]
    #         ufsession_.Csys.MapPoint(UF_CSYS_ROOT_COORDS, mappedOffset2, UF_CSYS_WORK_COORDS, mappedToWork2)
    #         Point3d basePoint1 = new Point3d(mappedToWork1[0], mappedToWork1[1], mappedToWork1[2])
    #         Point3d basePoint2 = new Point3d(mappedToWork2[0], mappedToWork2[1], mappedToWork2[2])

    #         Component component1 = work_part().ComponentAssembly.AddComponent(
    #             wireTapScrew,
    #             "SHORT-TAP",
    #             "8mm-shcs-020",
    #             basePoint1,
    #             rotateOrientation,
    #             98,
    #             out _)

    #         Component component2 = work_part().ComponentAssembly.AddComponent(
    #             wireTapScrew,
    #             "SHORT-TAP",
    #             "8mm-shcs-020",
    #             basePoint2,
    #             rotateOrientation,
    #             98,
    #             out _)

    #         display_part().WCS.Rotate(WCS.Axis.XAxis, -90.0)
    #         const string subtract = "subtract"
    #         component1.SetInstanceUserAttribute(subtract, -1, "WIRE_TAP", NXOpen.Update.Option.Now)
    #         component2.SetInstanceUserAttribute(subtract, -1, "WIRE_TAP", NXOpen.Update.Option.Now)
    #         session_.__DeleteObjects(savedCsys)
    #     }



    #     private void PlaceFastenersJigJacks(Part fastener_part)
    #     {
    #         try
    #         {
    #             btnOk.Enabled = false
    #             listBoxSelection.SelectedIndex = -1
    #             listBoxSelection.Enabled = false
    #             btnChangeRefSet.Enabled = false
    #             btnReset.Enabled = false
    #             btnPlanView.Enabled = false
    #             btnWireTaps.Enabled = false
    #             btnOrigin.Enabled = false

    #             cmbGridSpacing.SelectedValue = display_part().Preferences
    #                 .Workplane
    #                 .GetRectangularUniformGridSize()
    #                 .MajorGridSpacing

    #             chkGrid.Checked = display_part().Preferences.Workplane.ShowGrid

    #             if (display_part().Tag == work_part().Tag)
    #             {
    #                 display_part().Layers.SetState(1, State.WorkLayer)

    #                 new[] { 99, 98, 97, 97 }
    #                     .ToList()
    #                     .ForEach(i => display_part().Layers.SetState(i, State.Selectable))
    #             }

    #             cmbReferenceSet.Items.Clear()
    #             HashSet<string> refsets = fastener_part.GetAllReferenceSets().Select(__r => __r.Name).ToHashSet()
    #             refsets.Remove("BODY")
    #             refsets.Remove("BODY_EDGE")
    #             refsets.Remove("MODEL")
    #             cmbReferenceSet.Items.AddRange(refsets.ToArray())
    #             cmbReferenceSet.SelectedIndex = 0
    #             CartesianCoordinateSystem csys = display_part().WCS.Save()

    #             Component addedFastener = work_part().ComponentAssembly.AddComponent(
    #                 fastener_part,
    #                 "GRID",
    #                 fastener_part.Leaf,
    #                 csys.Origin,
    #                 csys.Orientation.Element,
    #                 99,
    #                 out _)

    #             session_.__DeleteObjects(csys)

    #             if (MoveComponentWithMouse(addedFastener) != UF_UI_PICK_RESPONSE)
    #             {
    #                 session_.__DeleteObjects(addedFastener)
    #                 return
    #             }

    #             CartesianCoordinateSystem proto_csys = work_part().CoordinateSystems.CreateCoordinateSystem(
    #                 addedFastener.__Origin(),
    #                 addedFastener.__Orientation(), false)

    #             if (__work_component_ is null)
    #             {
    #                 proto_csys.GetDirections(out Vector3d xDir, out Vector3d yDir)
    #                 display_part().WCS.SetOriginAndMatrix(proto_csys.Origin, xDir.__ToMatrix3x3(yDir))
    #                 session_.__DeleteObjects(proto_csys)
    #             }
    #             else
    #             {
    #                 CartesianCoordinateSystem occ_csys =
    #                     (CartesianCoordinateSystem)__work_component_.FindOccurrence(proto_csys)
    #                 occ_csys.GetDirections(out Vector3d xDir, out Vector3d yDir)
    #                 display_part().WCS.SetOriginAndMatrix(occ_csys.Origin, xDir.__ToMatrix3x3(yDir))
    #                 session_.__DeleteObjects(proto_csys)
    #             }

    #             string reference_set = cmbReferenceSet.Text
    #             addedFastener.SetInstanceUserAttribute("subtract", -1, reference_set, NXOpen.Update.Option.Now)
    #             cmbGridSpacing.SelectedValue = 1.000
    #             PlaceFasteners(addedFastener.__Prototype(), false)
    #             cmbGridSpacing.SelectedValue = 0.125

    #             if (__work_component_ is null)
    #             {
    #                 addedFastener.__ReferenceSet("BODY_EDGE")
    #                 return
    #             }

    #             Tag instance = ufsession_.Assem.AskInstOfPartOcc(addedFastener.Tag)
    #             Tag other = ufsession_.Assem.AskPartOccOfInst(__work_component_.Tag, instance)
    #             Component comp = (Component)session_.GetObjectManager().GetTaggedObject(other)
    #             comp.__ReferenceSet("BODY_EDGE")
    #         }
    #         finally
    #         {
    #             btnOk.Enabled = true
    #         }
    #     }

    #     public void PlaceFasteners(Part fastener_part, bool reset_ref_sets = true)
    #     {
    #         try
    #         {
    #             listBoxSelection.SelectedIndexChanged -= ListBoxSelection_SelectedIndexChanged
    #             listBoxSelection.SelectedIndex = -1
    #             listBoxSelection.Enabled = false
    #             btnOk.Enabled = false
    #             grpFastenerType.Enabled = false
    #             mnuStrMainMenu.Enabled = false
    #             btnChangeRefSet.Enabled = false
    #             btnPlanView.Enabled = false
    #             btnReset.Enabled = false
    #             btnWireTaps.Enabled = false
    #             chkCycleAdd.Enabled = false
    #             chkReverseCycleAdd.Enabled = false
    #             chkSubstitute.Enabled = false
    #             btnOrigin.Enabled = false

    #             try
    #             {
    #                 double value = (double)cmbGridSpacing.SelectedValue

    #                 if (value > 0.0)
    #                     display_part().Preferences.Workplane.SetRectangularUniformGridSize(
    #                         new WorkPlane.GridSize
    #                         {
    #                             MajorGridSpacing = value,
    #                             MinorLinesPerMajor = 1,
    #                             SnapPointsPerMinor = 1
    #                         }
    #                     )
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException()
    #             }

    #             chkGrid.Checked = display_part().Preferences.Workplane.ShowGrid

    #             if (display_part().Tag == work_part().Tag)
    #             {
    #                 display_part().Layers.SetState(1, State.WorkLayer)

    #                 new[] { 99, 98, 97, 96 }
    #                     .ToList()
    #                     .ForEach(i => display_part().Layers.SetState(i, State.Selectable))
    #             }

    #             if (reset_ref_sets)
    #             {
    #                 cmbReferenceSet.Items.Clear()
    #                 HashSet<string> refsets = fastener_part.GetAllReferenceSets().Select(__r => __r.Name).ToHashSet()
    #                 refsets.Remove("BODY")
    #                 refsets.Remove("MODEL")
    #                 cmbReferenceSet.Items.AddRange(refsets.ToArray())
    #                 cmbReferenceSet.SelectedIndex = 0

    #                 if (fastener_part.__IsShcs())
    #                     cmbReferenceSet.Items.Add("HANDLING")
    #             }

    #             CartesianCoordinateSystem csys = display_part().WCS.Save()
    #             Component addedFastener = null

    #             Face bottomFace = null

    #             if (chkManual.Checked)
    #             {
    #                 bottomFace = Ui.Selection.SelectSingleFace(x => x.SolidFaceType == Face.FaceType.Planar)

    #                 if (bottomFace is null)
    #                     return
    #             }

    #             try
    #             {
    #                 while (true)
    #                 {
    #                     display_part().WCS.CoordinateSystem.GetDirections(out Vector3d xDir, out Vector3d yDir)
    #                     Matrix3x3 ori = xDir.__ToMatrix3x3(yDir)

    #                     if (!chkManual.Checked)
    #                         addedFastener = work_part().ComponentAssembly.AddComponent(
    #                             fastener_part,
    #                             "BODY_EDGE",
    #                             fastener_part.Leaf,
    #                             csys.Origin,
    #                             csys.Orientation.Element,
    #                             99,
    #                             out _)

    #                     if (chkManual.Checked)
    #                     {
    #                         string message = "Select Origin"
    #                         UFUi.PointBaseMethod pbMethod = UFUi.PointBaseMethod.PointInferred
    #                         Tag selection = NXOpen.Tag.Null
    #                         double[] basePoint = new double[3]
    #                         int response

    #                         using (session_.__UsingLockUiFromCustom())
    #                             ufsession_.Ui.PointConstruct(
    #                                 message,
    #                                 ref pbMethod,
    #                                 out selection,
    #                                 basePoint,
    #                                 out response
    #                             )

    #                         switch (response)
    #                         {
    #                             case UF_UI_OK:
    #                                 break
    #                             case UF_UI_BACK:
    #                             case UF_UI_CANCEL:
    #                                 return
    #                             default:
    #                                 throw NXException.Create(response)
    #                         }

    #                         var orientation = bottomFace.__NormalVector().__Negate().__ToMatrix3x3()
    #                         var origin = basePoint.__ToPoint3d()

    #                         addedFastener = work_part().ComponentAssembly.AddComponent(
    #                             fastener_part,
    #                             "BODY_EDGE",
    #                             fastener_part.Leaf,
    #                             origin,
    #                             orientation,
    #                             99,
    #                             out _)
    #                     }
    #                     else if (MoveComponentWithMouse(addedFastener) != UF_UI_PICK_RESPONSE)
    #                     {
    #                         session_.__DeleteObjects(addedFastener)
    #                         break
    #                     }

    #                     if (!(addedFastener is null))
    #                     {

    #                         string reference_set = cmbReferenceSet.Text
    #                         addedFastener.SetInstanceUserAttribute("subtract", -1, reference_set, NXOpen.Update.Option.Now)

    #                         switch (reference_set)
    #                         {
    #                             case "HANDLING":
    #                             case "WIRE_TAP":
    #                                 addedFastener.__Layer(98)
    #                                 break
    #                             case "TOOLING":
    #                                 addedFastener.__Layer(97)
    #                                 break
    #                             default:
    #                                 addedFastener.__Layer(99)
    #                                 break
    #                         }
    #                     }
    #                 }
    #             }
    #             finally
    #             {
    #                 session_.__DeleteObjects(csys)
    #             }
    #         }
    #         finally
    #         {
    #             listBoxSelection.Enabled = true
    #             grpFastenerType.Enabled = true
    #             mnuStrMainMenu.Enabled = true
    #             btnChangeRefSet.Enabled = true
    #             btnPlanView.Enabled = true
    #             btnReset.Enabled = true
    #             btnWireTaps.Enabled = true
    #             chkCycleAdd.Enabled = true
    #             chkReverseCycleAdd.Enabled = true
    #             chkSubstitute.Enabled = true
    #             btnOrigin.Enabled = true
    #             btnOk.Enabled = true
    #             listBoxSelection.SelectedIndex = -1
    #             listBoxSelection.SelectedIndexChanged += ListBoxSelection_SelectedIndexChanged
    #         }
    #     }

    #     public void PlaceFastenersCycle(Part fastener_part)
    #     {
    #         try
    #         {
    #             string dir = Path.GetDirectoryName(fastener_part.FullPath)
    #             string leaf = fastener_part.Leaf
    #             string[] cycles = CycleAdd1.MetricCyclePair[dir]
    #             string small_dwl = cycles[0]
    #             string large_dwl = cycles[1]
    #             string jack = cycles[2]
    #             Match match = Regex.Match(leaf, "-shcs-(?<length>\\d+)")
    #             string actual_dwl = small_dwl

    #             if (match.Success)
    #             {
    #                 int length = int.Parse(match.Groups["length"].Value)

    #                 if (length >= CycleAdd1.MetricDelimeter)
    #                     actual_dwl = large_dwl
    #             }

    #             string shcs = fastener_part.FullPath
    #             string dowel = actual_dwl
    #             Part shcs_part = session_.__FindOrOpen(shcs)
    #             Part dowel_part = session_.__FindOrOpen(dowel)
    #             Part jigjack_part = session_.__FindOrOpen(jack)

    #             if (chkCycleAdd.Checked)
    #                 PlaceFasteners(shcs_part)
    #             else
    #                 PlaceFastenersJigJacks(jigjack_part)

    #             PlaceFasteners(dowel_part)

    #             if (chkCycleAdd.Checked)
    #                 PlaceFastenersJigJacks(jigjack_part)
    #             else
    #                 PlaceFasteners(shcs_part)
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException()
    #         }
    #     }

    #     public static void SubstituteFasteners(Part nxPart)
    #     {
    #         using (new LockUpdates())
    #         {
    #             Component[] fasteners_to_substitue = new Component[0]

    #             if (nxPart.__IsShcs())
    #                 fasteners_to_substitue = work_part().__RootComponent()
    #                     .GetChildren()
    #                     .Where(__c => __c._IsShcs_())
    #                     .ToArray()
    #             else if (nxPart.__IsDwl())
    #                 fasteners_to_substitue = work_part().__RootComponent()
    #                     .GetChildren()
    #                     .Where(__c => __c._IsDwl_())
    #                     .ToArray()
    #             else if (nxPart.__IsJckScrew())
    #                 fasteners_to_substitue = work_part().__RootComponent()
    #                     .GetChildren()
    #                     .Where(__c => __c._IsJckScrew_())
    #                     .ToArray()
    #             else if (nxPart.__IsJckScrewTsg())
    #                 fasteners_to_substitue = work_part().__RootComponent()
    #                     .GetChildren()
    #                     .Where(__c => __c._IsJckScrewTsg_())
    #                     .ToArray()

    #             if (fasteners_to_substitue.Length == 0)
    #             {
    #                 print($"Couldn't find any fasteners to substitue with {nxPart.Leaf}")
    #                 return
    #             }

    #             string original_display_name = fasteners_to_substitue[0].DisplayName
    #             ReplaceComponentBuilder replaceBuilder = work_part().AssemblyManager.CreateReplaceComponentBuilder()

    #             using (new Destroyer(replaceBuilder))
    #             {
    #                 replaceBuilder.ReplacementPart = nxPart.FullPath
    #                 replaceBuilder.MaintainRelationships = true
    #                 replaceBuilder.ReplaceAllOccurrences = false
    #                 replaceBuilder.ComponentNameType = ReplaceComponentBuilder.ComponentNameOption.AsSpecified
    #                 replaceBuilder.ComponentsToReplace.Add(fasteners_to_substitue)
    #                 replaceBuilder.Commit()
    #             }

    #             print($"Substituted fasteners {original_display_name} -> {nxPart.Leaf}")
    #         }
    #     }

    #     private static void MotionCallback(double[] positionArray, ref UFUi.MotionCbData mtnCbData, IntPtr clientData)
    #     {
    #         GCHandle _handle = (GCHandle)clientData
    #         Component component1 = (Component)_handle.Target
    #         Session theSession = session_
    #         Part workPart = theSession.Parts.Work
    #         ComponentPositioner componentPositioner1
    #         componentPositioner1 = workPart.ComponentAssembly.Positioner
    #         componentPositioner1.ClearNetwork()
    #         componentPositioner1.BeginMoveComponent()
    #         _ = theSession.Preferences.Assemblies.InterpartPositioning
    #         Network network1
    #         network1 = componentPositioner1.EstablishNetwork()
    #         ComponentNetwork componentNetwork1 = (ComponentNetwork)network1
    #         componentNetwork1.MoveObjectsState = true
    #         Component nullNXOpen_Assemblies_Component = null
    #         componentNetwork1.DisplayComponent = nullNXOpen_Assemblies_Component
    #         componentNetwork1.NetworkArrangementsMode = ComponentNetwork.ArrangementsMode.Existing
    #         componentNetwork1.RemoveAllConstraints()
    #         NXObject[] movableObjects1 = new NXObject[1]
    #         movableObjects1[0] = component1
    #         componentNetwork1.SetMovingGroup(movableObjects1)
    #         componentNetwork1.Solve()
    #         componentNetwork1.MoveObjectsState = true
    #         componentNetwork1.NetworkArrangementsMode = ComponentNetwork.ArrangementsMode.Existing
    #         componentNetwork1.BeginDrag()
    #         component1.GetPosition(out Point3d position, out _)

    #         Vector3d translation1 = new Vector3d(
    #             positionArray[0] - position.X,
    #             positionArray[1] - position.Y,
    #             positionArray[2] - position.Z)

    #         componentNetwork1.DragByTranslation(translation1)
    #         componentNetwork1.EndDrag()
    #         componentNetwork1.ResetDisplay()
    #         componentNetwork1.ApplyToModel()
    #         componentNetwork1.Solve()
    #         componentPositioner1.ClearNetwork()
    #         theSession.UpdateManager.AddToDeleteList(componentNetwork1)
    #         componentPositioner1.DeleteNonPersistentConstraints()
    #         componentPositioner1.EndMoveComponent()
    #         ufsession_.Modl.Update()
    #     }

    #     public static int MoveComponentWithMouse(Component snapComponent)
    #     {
    #         GCHandle __handle = GCHandle.Alloc(snapComponent)

    #         using (session_.__UsingGCHandle(__handle))
    #         using (session_.__UsingLockUiFromCustom())
    #         {
    #             double[] screenPos = new double[3]

    #             ufsession_.Ui.SpecifyScreenPosition(
    #                 "Move Object",
    #                 MotionCallback,
    #                 (IntPtr)__handle,
    #                 screenPos,
    #                 out Tag _,
    #                 out int response)

    #             return response
    #         }
    #     }

    #     private void BtnChangeRefSet_Click(object sender, EventArgs e)
    #     {
    #         using (session_.__UsingFormShowHide(this))
    #             try
    #             {
    #                 SelectChangeReferenceSet()
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException()
    #             }
    #     }

    #     public void SelectChangeReferenceSet()
    #     {
    #         try
    #         {
    #             Component[] fasteners = Selection.SelectManyComponents()

    #             if (fasteners.Length == 0)
    #                 return

    #             if (fasteners.Any(__fast => __fast.OwningComponent.Tag != fasteners[0].OwningComponent.Tag))
    #             {
    #                 print("All fasteners must be under the same component")
    #                 return
    #             }

    #             // remove BODY, GRID, BODY_EDGE, MODEL
    #             List<string> reference_set_names = fasteners.Select(__fast => __fast.Prototype)
    #                 .OfType<Part>()
    #                 .SelectMany(__part => __part.GetAllReferenceSets())
    #                 .Select(__ref => __ref.Name)
    #                 .Distinct()
    #                 .ToList()

    #             reference_set_names.Remove("BODY")
    #             reference_set_names.Remove("BODY_EDGE")
    #             reference_set_names.Remove("GRID")
    #             reference_set_names.Remove("MODEL")

    #             // all shcs metric
    #             if (fasteners.All(__fast => __fast._IsShcs_()) &&
    #                 fasteners.All(__fast => __fast.Name.ToLower().Contains("mm")))
    #                 reference_set_names.Add("HANDLING")
    #             // all shcs english
    #             else if (fasteners.All(__fast => __fast._IsShcs_()) &&
    #                      fasteners.All(__fast => !__fast.Name.ToLower().Contains("mm")))
    #                 reference_set_names.Add("HANDLING")
    #             // all dwl metric
    #             else if (fasteners.All(__fast => __fast._IsDwl_()) &&
    #                      fasteners.All(__fast => __fast.Name.ToLower().Contains("mm")))
    #                 reference_set_names.Add("TOOLING")
    #             // all dwl english
    #             else if (fasteners.All(__fast => __fast._IsDwl_()) &&
    #                      fasteners.All(__fast => !__fast.Name.ToLower().Contains("mm")))
    #                 reference_set_names.Add("TOOLING")
    #             // all jack screw
    #             else if (fasteners.All(__fast => __fast._IsJckScrew_()))
    #             {
    #             }
    #             // all jack screw tsg
    #             else if (fasteners.All(__fast => __fast._IsJckScrewTsg_()))
    #             {
    #             }
    #             else
    #             {
    #                 print("You cannot select different type of fasteners in the same selection")
    #                 return
    #             }

    #             string selected_ref_set =
    #                 session_.__SelectMenuItem14gt("Select Reference Set", reference_set_names.ToArray())

    #             foreach (Component selected_fastener in fasteners)
    #                 using (session_.__UsingDisplayPartReset())
    #                 {
    #                     Component actual_fastener

    #                     if (!(__work_component_ is null)
    #                         || selected_fastener.Parent.Tag != display_part().ComponentAssembly.RootComponent.Tag)
    #                     {
    #                         Tag instance = ufsession_.Assem.AskInstOfPartOcc(selected_fastener.Tag)
    #                         Tag actual_tag = ufsession_.Assem.AskPartOccOfInst(
    #                             __work_component_.__Prototype().ComponentAssembly.RootComponent.Tag, instance)
    #                         actual_fastener = (Component)session_.__GetTaggedObject(actual_tag)
    #                         display_part() = actual_fastener.Parent.__Prototype()
    #                     }
    #                     else
    #                         actual_fastener = selected_fastener

    #                     display_part()
    #                         .Features
    #                         .ToArray()
    #                         .OfType<ExtractFace>()
    #                         .Where(__f => __f.FeatureType == "LINKED_BODY")
    #                         .ToList()
    #                         .ForEach(__k =>
    #                         {
    #                             ufsession_.Wave.IsLinkBroken(__k.Tag, out bool is_broken)

    #                             if (is_broken)
    #                                 return

    #                             ufsession_.Wave.AskLinkXform(__k.Tag, out Tag xform)

    #                             ufsession_.So.AskAssyCtxtPartOcc(
    #                                 xform,
    #                                 display_part().ComponentAssembly.RootComponent.Tag,
    #                                 out Tag from_part_occ)

    #                             if (from_part_occ == NXOpen.Tag.Null)
    #                                 return

    #                             double[] point = new double[3]
    #                             ufsession_.So.AskPointOfXform(xform, point)
    #                             Component from_comp = (Component)from_part_occ.__ToTaggedObject()

    #                             if (!from_comp.__Origin().__IsEqualTo(point))
    #                                 return

    #                             if (from_part_occ != actual_fastener.Tag)
    #                                 return

    #                             session_.__DeleteObjects(__k)

    #                             actual_fastener.SetInstanceUserAttribute("subtract", -1, selected_ref_set,
    #                                 NXOpen.Update.Option.Now)

    #                             WaveIn(actual_fastener, display_part().__SingleSolidBodyOnLayer1())
    #                         })
    #                 }
    #         }
    #         catch (NothingSelectedException)
    #         {
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException()
    #         }
    #     }

    #     private void BtnPlanView_Click(object sender, EventArgs e)
    #     {
    #         const string createPlanView = "Create Plan View?"
    #         const string areYouSure = "Are you sure?"
    #         DialogResult result = MessageBox.Show(createPlanView, areYouSure, MessageBoxButtons.YesNo)

    #         if (result == DialogResult.Yes)
    #             MakePlanView(display_part().WCS.Save())
    #     }

    #     private void ChkGrid_CheckedChanged(object sender, EventArgs e)
    #     {
    #         display_part().Preferences.Workplane.ShowGrid = chkGrid.Checked
    #     }

    #     private void ForceButtonsOnToolStripMenuItem_Click(object sender, EventArgs e)
    #     {
    #         ChangeAllButtonsEnabled(true)
    #     }

    #     public void ChangeAllButtonsEnabled(bool flag)
    #     {
    #         ChangEnabled(flag, listBoxSelection, btnSelectComponent, grpFastenerType, chkGrid, cmbGridSpacing,
    #             btnPlanView, btnOk, btnOrigin, btnWireTaps, btnChangeRefSet, chkSubstitute,
    #             chkSubstitute, chkCycleAdd, chkReverseCycleAdd)
    #         mnu2x.Enabled = flag
    #         menuItemUnits.Enabled = flag
    #     }

    #     private void CloseAllFastenersMenuItem_Click(object sender, EventArgs e)
    #     {
    #         try
    #         {
    #             const string oLibraryFasteners = "G:\\0Library\\Fasteners"

    #             if (display_part().FullPath.StartsWith(oLibraryFasteners))
    #             {
    #                 print("You cannot run this command with a fastener as your display part.")
    #                 return
    #             }

    #             List<BasePart> partsToClose = session_.Parts
    #                 .ToArray()
    #                 .Where(part => part.FullPath.StartsWith(oLibraryFasteners))
    #                 .ToList()

    #             partsToClose.ForEach(part => part.__Close(true, true))
    #             print($"Closed {partsToClose.Count} fastener files.")
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException()
    #         }
    #     }




    @staticmethod
    def MakePlanView(csys)->None:
        l1 = "L1"
        top = "Top"
        plan = "PLAN"
        set_display_part(work_part())
        planView = part_get_modeling_view(work_part(),'PLAN')
        if planView is not None:
            layout = work_part().Layouts.FindObject(l1)
            modelingView1 = work_part().ModelingViews.WorkView
            modelingView2 = work_part().ModelingViews.FindObject(top)
            layout.ReplaceView(modelingView1, modelingView2, True)
            tempView = work_part().ModelingViews.FindObject(plan)
            delete_objects([tempView])
        ufsession().View.SetViewMatrix("", 3, csys.Tag, None)
        modelingView1 =display_part().Views.SaveAs(display_part().ModelingViews.WorkView, plan, False, False)
        modelingView2 = display_part().ModelingViews.FindObject(top)
        display_part().Layouts.FindObject(l1).ReplaceView(modelingView1, modelingView2, True)
        delete_objects([csys])

    @staticmethod
    def GetLinkedBody(owning_part:Part, child:Component):
        for  feature in list(owning_part.Features):
            if feature.FeatureType != "LINKED_BODY":continue
            xform = ufsession().Wave.AskLinkXform(feature.Tag)
            if xform == NXOpen.Tag.Null:continue
            fromPartOcc = ufsession().So.AskAssyCtxtPartOcc(xform, owning_part.ComponentAssembly.RootComponent.Tag)
            if fromPartOcc == child.Tag:
                return feature
        return None

    #     public static void WaveOut(Component child)
    #     {
    #         Part owningPart = (Part)child.OwningPart

    #         if (child.Parent.Tag != owningPart.ComponentAssembly.RootComponent.Tag)
    #             throw new ArgumentException("Can only wave out immediate children.")

    #         ExtractFace linkedBody = GetLinkedBody(owningPart, child)
    #         session_.__DeleteObjects(linkedBody)
    #     }

    #     public static void WaveOut()
    #     {
    #         if (work_part().Tag == display_part().Tag)
    #         {
    #             foreach (Component __child in work_part().ComponentAssembly.RootComponent.GetChildren())
    #                 try
    #                 {
    #                     if (__child.Layer != 99 && __child.Layer != 98 && __child.Layer != 97)
    #                         continue

    #                     if (__child.IsSuppressed)
    #                         continue

    #                     if (!__child.__IsFastener())
    #                         continue

    #                     ExtractFace link = GetLinkedBody(work_part(), __child)
    #                     WaveOut(__child)
    #                     session_.__DeleteObjects(link)
    #                 }
    #                 catch (Exception ex)
    #                 {
    #                     ex.__PrintException()
    #                 }

    #             return
    #         }

    #         foreach (Component child in __work_component_.GetChildren())
    #         {
    #             if (child.IsSuppressed)
    #                 continue

    #             if (!child.__IsFastener())
    #                 continue

    #             Component protoPartOcc = _GetProtoPartOcc(work_part(), child)
    #             WaveOut(protoPartOcc)
    #         }
    #     }

    #     private static void BlockOrigin()
    #     {
    #         try
    #         {
    #             SetWcsToWorkPart()
    #         }
    #         catch (Exception ex)
    #         {
    #             ex.__PrintException()
    #         }
    #     }

    #     public static void SelectTarget()
    #     {
    #         NXOpen.Selection.Response response = UI.GetUI().SelectionManager.SelectTaggedObject(
    #             "Select A Target Body",
    #             "Select A Target Body",
    #             NXOpen.Selection.SelectionScope.AnyInAssembly,
    #             NXOpen.Selection.SelectionAction.ClearAndEnableSpecific,
    #             false,
    #             false,
    #             new[] { Selection.SolidBodyMask },
    #             out TaggedObject _object,
    #             out _)

    #         switch (response)
    #         {
    #             case NXOpen.Selection.Response.Back:
    #             case NXOpen.Selection.Response.Cancel:
    #                 throw new NothingSelectedException()
    #             case NXOpen.Selection.Response.Ok:
    #                 if (!work_part().__HasDynamicBlock())
    #                 {
    #                     display_part().WCS.SetOriginAndMatrix(_Point3dOrigin, _Matrix3x3Identity)

    #                     // if(!work_part().__TrySingleSolidBodyLayer1(out Body solid_body))
    #                     // throw new NoSolidBodyOnLayer1Exception()

    #                     Body solid_body = work_part().__SingleSolidBodyOnLayer1()
    #                     solid_body.__Translucency(75)
    #                     print("Part does not have a dynamic block. You will need to move the csys manually.")
    #                     return
    #                 }

    #                 work_part().__DynamicBlock().GetBodies()[0].__Translucency(75)
    #                 display_part().WCS.SetOriginAndMatrix(work_part().__DynamicBlock().__Origin(),
    #                     work_part().__DynamicBlock().__Orientation())
    #                 return
    #             case NXOpen.Selection.Response.ObjectSelectedByName:
    #                 throw new InvalidOperationException("Cannot select an object by name")
    #             case NXOpen.Selection.Response.ObjectSelected:
    #                 Body selected = (Body)_object

    #                 if (selected.IsOccurrence)
    #                 {
    #                     Body proto_selected = selected.__Prototype()
    #                     Part part = selected.OwningComponent.__Prototype()

    #                     if (!part.__HasDynamicBlock())
    #                     {
    #                         __work_component_ = selected.OwningComponent
    #                         __work_component_.__Translucency(75)
    #                         display_part().WCS.SetOriginAndMatrix(__work_component_.__Origin(),
    #                             __work_component_.__Orientation())
    #                         print("Part does not have a dynamic block. You will need to move the csys manually.")
    #                         return
    #                     }

    #                     Point3d origin = part.__DynamicBlock().__Origin()
    #                     Matrix3x3 orientation = part.__DynamicBlock().__Orientation()
    #                     CartesianCoordinateSystem csys =
    #                         part.CoordinateSystems.CreateCoordinateSystem(origin, orientation, false)
    #                     selected.OwningComponent.__Prototype().__FindReferenceSet("BODY")
    #                         .AddObjectsToReferenceSet(new[] { csys })
    #                     CartesianCoordinateSystem occ_csys =
    #                         (CartesianCoordinateSystem)selected.OwningComponent.FindOccurrence(csys)
    #                     display_part().WCS.SetCoordinateSystemCartesianAtCsys(occ_csys)
    #                     __work_component_ = selected.OwningComponent
    #                     __work_component_.__Translucency(75)
    #                     session_.__DeleteObjects(occ_csys, csys)
    #                 }
    #                 else if (work_part().__HasDynamicBlock())
    #                 {
    #                     if (work_part().__DynamicBlock().GetBodies()[0].Tag != selected.Tag)
    #                         throw new InvalidOperationException("Selected body that wasn't the dynamic block")

    #                     work_part().__DynamicBlock().GetBodies()[0].__Translucency(75)
    #                     display_part().WCS.SetOriginAndMatrix(work_part().__DynamicBlock().__Origin(),
    #                         work_part().__DynamicBlock().__Orientation())
    #                 }
    #                 else
    #                 {
    #                     Body[] bodies = work_part().Bodies.ToArray()
    #                         .Where(__b => __b.IsSolidBody)
    #                         .Where(__b => __b.Layer == 1)
    #                         .ToArray()

    #                     if (bodies.Length == 1)
    #                     {
    #                         work_part().__SingleSolidBodyOnLayer1().__Translucency(75)
    #                         display_part().WCS.SetOriginAndMatrix(_Point3dOrigin, _Matrix3x3Identity)
    #                         print("Part does not have a dynamic block. You will need to move the csys manually.")
    #                     }
    #                 }

    #                 break
    #         }
    #     }
    @staticmethod
    def SetWcsToWorkPart()->None:
        Block dynamicBlock = work_part().__DynamicBlock()
        Point3d origin = dynamicBlock.__Origin()
        Matrix3x3 orientation = dynamicBlock.__Orientation()

        if work_part().Tag == display_part().Tag:
            display_part().WCS.SetOriginAndMatrix(origin, orientation)
            return

        absCsys =display_part().CoordinateSystems.CreateCoordinateSystem(_Point3dOrigin, _Matrix3x3Identity, true)

        CartesianCoordinateSystem compCsys = display_part().CoordinateSystems.CreateCoordinateSystem(
            __work_component_.__Origin(),
            __work_component_.__Orientation(),
            true)

        Point3d newOrigin = origin.__MapCsysToCsys(compCsys, absCsys)
        Vector3d newXVec = __work_component_.__Orientation().__AxisX().__MapCsysToCsys(compCsys, absCsys)
        Vector3d newYVec = __work_component_.__Orientation().__AxisY().__MapCsysToCsys(compCsys, absCsys)
        Matrix3x3 newOrientation = newXVec.__ToMatrix3x3(newYVec)
        display_part().WCS.SetOriginAndMatrix(newOrigin, newOrientation)
    }

    #     private void mnu2x_Click(object sender, EventArgs e)
    #     {
    #         switch (_1x_2x)
    #         {
    #             case 1:
    #                 mnu2x.Text = "2x"
    #                 _1x_2x = 2
    #                 break
    #             case 2:
    #                 mnu2x.Text = "1x"
    #                 _1x_2x = 1
    #                 break
    #             default:
    #                 print("Couldn't determine 1x or 2x")
    #                 break
    #         }

    #         if (rdoTypeScrew.Checked)
    #             LoadShcs()
    #     }

    #     private void RdoFastener_CheckedChanged(object sender, EventArgs e)
    #     {
    #         if (rdoTypeScrew.Checked)
    #             LoadShcs()

    #         if (rdoTypeDowel.Checked)
    #             LoadDowel()

    #         if (rdoTypeJack.Checked)
    #             LoadJack()
    #     }


    pass