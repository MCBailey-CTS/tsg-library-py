class UFuncExportStrip:
    #     public partial class ExportStrip : _UFuncForm
    # {
    # 	// sql
    #     public const string Regex_Strip = "^(?<customerNum>\\d+)-(?<opNum>\\d+)-strip$";
    #     public const string DummyPath = "G:\\0Library\\SeedFiles\\Components\\Dummy.prt";
    #     public const string Regex_PressAssembly = "^(?<customerNum>\\d+)-Press-(?<opNum>\\d+)-Assembly$";
    #     public const string Regex_Layout = "^(?<customerNum>\\d+)-(?<opNum>\\d+)-layout$";
    #     public const string Regex_Blank = "^(?<customerNum>\\d+)-(?<opNum>\\d+)-blank$";

    #     public ExportStrip()
    #     {
    #         InitializeComponent();

    #         bool Is010()
    #         {
    # 			// sql
    #             Regex opRegex = new Regex("^[0-9]{4,}-([0-9]{3,})");
    #             Match match = opRegex.Match(__display_part_.Leaf);

    #             if (!match.Success)
    #                 return false;

    #             return match.Groups[1].Value == "010";
    #         }

    #         bool Is900()
    #         {
    # 			// sql
    #             Regex opRegex = new Regex("^[0-9]{4,}-([0-9]{3,})");
    #             Match match = opRegex.Match(__display_part_.Leaf);

    #             if (!match.Success)
    #                 return false;

    #             return match.Groups[1].Value == "900";
    #         }

    #         if (Session.GetSession().Parts.Display is null)
    #             txtInput.Text = $@"{TodaysDate}-";
    #         else if (Is010())
    #             txtInput.Text = $@"{TodaysDate}-Strip";
    #         else if (Is900())
    #             txtInput.Text = $@"{TodaysDate}-FlowChart";

    #         txtInput.Focus();
    #         chkPart.Checked = true;
    #         chkSTP.Checked = true;
    #         chkPDF.Checked = true;
    #         btnAccept.Enabled = true;
    #     }

    #     private void BtnAccept_Click(object sender, EventArgs e)
    #     {
    #         using (session_.__UsingFormShowHide(this))
    #             try
    #             {
    #                 Export(
    #                     chkSTP.Checked,
    #                     (int)numUpDownCopies.Value,
    #                     chkPart.Checked,
    #                     chkPDF.Checked,
    #                     txtInput.Text,
    #                     chkCopy.Checked);
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException();
    #             }
    #             finally
    #             {
    #                 print("Complete");
    #             }
    #     }

    #     public static void CheckAssemblyDummyFiles()
    #     {
    #         if (__display_part_.ComponentAssembly.RootComponent is null)
    #             return;

    #         foreach (Component childOfStrip in __display_part_.ComponentAssembly.RootComponent.GetChildren())
    #         {
    #             if (childOfStrip.IsSuppressed)
    #                 continue;

    #             if (!(childOfStrip.Prototype is Part))
    #                 continue;

    #             if (!Regex.IsMatch(childOfStrip.DisplayName, Regex_PressAssembly, RegexOptions.IgnoreCase))
    #                 continue;

    #             if (childOfStrip.GetChildren().Length == 0)
    #                 throw new Exception($"A press exists in your assembly without any children. {childOfStrip.__AssemblyPathString()}");

    #             if (childOfStrip.GetChildren().Length == 1)
    #                 throw new Exception($"A press exists in your assembly with only one child. Expecting a ram and a bolster. {childOfStrip.__AssemblyPathString()}");

    #             if (childOfStrip.GetChildren().Length != 2)
    #                 continue;

    #             foreach (Component childOfPress in childOfStrip.GetChildren())
    #             {
    #                 if (!(childOfPress.Prototype is Part))
    #                     throw new Exception($"The child of a press must be loaded. {childOfPress.__AssemblyPathString()}");

    #                 if (childOfPress.IsSuppressed)
    #                     throw new Exception($"The child of a press cannot be suppressed. {childOfPress.__AssemblyPathString()}");

    #                 if (childOfPress.GetChildren().Length != 0
    #                     && childOfPress.GetChildren().Any(component => !component.IsSuppressed && component.Prototype is Part))
    #                     continue;

    #                 throw new Exception($"The child of a bolster or ram under a press must be the Dummy file: {DummyPath}{childOfPress.__AssemblyPathString()}");
    #             }

    #             break;
    #         }
    #     }

    #     public static void UpdateForStp()
    #     {
    #         HashSet<Part> partsToSave = new HashSet<Part>();
    #         Part currentD = __display_part_;
    #         Part currentW = session_.Parts.Work;

    #         try
    #         {
    #             foreach (Component child in session_.Parts.Work.ComponentAssembly.RootComponent.GetChildren())
    #             {
    #                 if (child.IsSuppressed)
    #                     continue;

    #                 if (!(child.Prototype is Part))
    #                     continue;

    #                 __display_part_ = child.__Prototype();

    #                 switch (child.ReferenceSet)
    #                 {
    #                     case "Empty":
    #                         continue;

    #                     default:
    #                         {
    #                             Part proto = (Part)child.Prototype;

    #                             ReferenceSet referenceSet = proto.GetAllReferenceSets().FirstOrDefault(refset => refset.Name == child.ReferenceSet);

    #                             if (referenceSet is null)
    #                                 continue;

    #                             NXObject[] objectsInReferenceSet = referenceSet.AskMembersInReferenceSet();

    #                             foreach (NXObject obj in objectsInReferenceSet)
    #                             {
    #                                 if (!(obj is DisplayableObject disp))
    #                                     continue;

    #                                 if (disp.Layer <= 1 || disp.Layer >= 256)
    #                                     continue;

    #                                 if (proto.Layers.GetState(disp.Layer) == State.WorkLayer)
    #                                     continue;

    #                                 proto.Layers.SetState(disp.Layer, State.Selectable);
    #                             }

    #                             session_.DisplayManager.UnblankObjects(objectsInReferenceSet.OfType<DisplayableObject>().ToArray());

    #                             partsToSave.Add(proto);
    #                         }

    #                         continue;
    #                 }
    #             }
    #         }
    #         finally
    #         {
    #             session_.Parts.SetDisplay(currentD, false, false, out _);
    #             session_.Parts.SetWork(currentW);
    #         }

    #         foreach (Part part in partsToSave)
    #             part.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);
    #     }

    #     private static void NewMethod(HashSet<Part> partsToSave, Component child)
    #     {
    #         Part proto = (Part)child.Prototype;
    #         ReferenceSet referenceSet = proto.GetAllReferenceSets().First(refset => refset.Name == child.ReferenceSet);

    #         NXObject[] objectsInReferenceSet = referenceSet.AskMembersInReferenceSet();

    #         foreach (NXObject obj in objectsInReferenceSet)
    #         {
    #             if (!(obj is DisplayableObject disp))
    #                 continue;

    #             if (disp.Layer <= 1 || disp.Layer >= 256)
    #                 continue;

    #             if (proto.Layers.GetState(disp.Layer) == State.WorkLayer)
    #                 continue;

    #             proto.Layers.SetState(disp.Layer, State.Selectable);
    #         }

    #         session_.DisplayManager.UnblankObjects(objectsInReferenceSet.OfType<DisplayableObject>().ToArray());

    #         partsToSave.Add(proto);
    #     }

    # 	// sql , not sql, remove all getcomponentofmany methods
    # 	// convert to descendants
    #     private static void Export(bool chkSTP, int numUpDownCopies, bool chkPart, bool chkPDF, string txtInput,
    #         bool chkCopy)
    #     {
    #         GFolder folder = GFolder.Create(__display_part_.FullPath);

    #         __display_part_.SetUserAttribute("DATE", -1, TodaysDate, NXOpen.Update.Option.Now);

    #         if (folder is null)
    #             throw new Exception("The current displayed part is not in a GFolder.");

    #         if (chkSTP)
    #         {
    #             Part currentD = __display_part_;
    #             Part currentW = session_.Parts.Work;

    #             try
    #             {
    #                 CheckAssemblyDummyFiles();

    #                 Part _currentD = __display_part_;
    #                 Part _currentW = session_.Parts.Work;

    #                 try
    #                 {
    #                     SetLayersInBlanksAndLayoutsAndAddDummies(__display_part_);
    #                 }
    #                 finally
    #                 {
    #                     session_.Parts.SetDisplay(_currentD, false, false, out _);
    #                     session_.Parts.SetWork(_currentW);
    #                 }
    #             }
    #             finally
    #             {
    #                 session_.Parts.SetDisplay(currentD, false, false, out _);
    #                 session_.Parts.SetWork(currentW);
    #             }
    #         }

    #         if (numUpDownCopies > 0)
    #             ExportStripPrintDrawing(numUpDownCopies);

    #         if (!chkPart && !chkPDF && !chkSTP)
    #             return;

    #         if (chkPDF)
    #             UpdateForPdf();

    #         //if (chkSTP)

    #         string outgoingFolderName = folder.CustomerNumber.Length == 6
    #             ? $"{folder.DirLayout}\\{txtInput}"
    #             : $"{folder.DirOutgoing}\\{txtInput}";

    #         if (Directory.Exists(outgoingFolderName))
    #         {
    #             if (MessageBox.Show(
    #                     $@"Folder {outgoingFolderName} already exists, is it okay to overwrite the files in the folder?",
    #                     @"Warning",
    #                     MessageBoxButtons.YesNo) != DialogResult.Yes)
    #                 return;

    #             Directory.Delete(outgoingFolderName, true);
    #         }

    #         Directory.CreateDirectory(outgoingFolderName);

    #         uf_.Ui.SetPrompt($"Export Strip: Setting layers in {__display_part_.Leaf}.");

    #         __work_part_.Layers.SetState(1, State.WorkLayer);

    # 		// sql
    #         for (int i = 2; i <= 256; i++)
    #             __work_part_.Layers.SetState(i, State.Hidden);

    #         new[] { 6, 10, 200, 201, 202, 254 }.ToList()
    #             .ForEach(i => __work_part_.Layers.SetState(i, State.Selectable));

    #         const string regex = "^\\d+-(?<op>\\d+)-.+$";

    #         string op = Regex.Match(session_.Parts.Work.Leaf, regex, RegexOptions.IgnoreCase).Groups["op"].Value;
    #         string commonString = $"{folder.CustomerNumber}-{op}-strip {TodaysDate}";

    #         uf_.Ui.SetPrompt(chkPart
    #             ? "Exporting \".prt\" file."
    #             : "Finding objects to export.");

    #         if (chkPDF)
    #         {
    #             uf_.Ui.SetPrompt("Exporting PDF......");

    #             string outputPath = ExportPDF(outgoingFolderName, commonString);

    #             print(File.Exists(outputPath)
    #                 ? $"Successfully created \"{outputPath}\"."
    #                 : $"Did not successfully create \"{outputPath}\".");
    #         }

    #         if (chkPart)
    #         {
    #             string outputPath = ExportStripPart(outgoingFolderName);

    #             print(File.Exists(outputPath)
    #                 ? $"Successfully created \"{outputPath}\"."
    #                 : $"Did not successfully create \"{outputPath}\".");
    #         }

    #         if (chkSTP)
    #         {
    #             UpdateForStp();

    #             ExportStripStp(outgoingFolderName);
    #             //string outputPath = $"{outgoingFolderName}\\{session_.Parts.Work.Leaf}-{TodaysDate}.stp";
    #             ////session_.Execute(@"C:\Repos\NXJournals\JOURNALS\export_strip.py", "ExportStrip", "export_stp", new object[] { outputPath });
    #             ////NXOpen.UF.UFSession.GetUFSession().Ui.SetPrompt("Exporting Step File.......");

    #             //NXOpen.StepCreator step = session_.DexManager.CreateStepCreator();

    #             //try
    #             //{
    #             //    //step.ExportDestination = NXOpen.BaseCreator.ExportDestinationOption.NativeFileSystem;

    #             //    //step.SettingsFile = "U:\\nxFiles\\Step Translator\\ExternalStep_AllLayers.def";

    #             //    //step.

    #             //    //step.ExportAs = NXOpen.StepCreator.ExportAsOption.Ap214;

    #             //    //step.InputFile = session_.Parts.Work.FullPath;

    #             //    //step.OutputFile = outputPath;

    #             //    //step.ProcessHoldFlag = true;

    #             //    step.Commit();
    #             //}
    #             //finally
    #             //{
    #             //    step.Destroy();
    #             //}

    #             //print_(File.Exists(outputPath)
    #             //    ? $"Successfully created \"{outputPath}\"."
    #             //: $"Did not successfully create \"{outputPath}\".");
    #         }

    #         uf_.Ui.SetPrompt($"Zipping up {outgoingFolderName}.");

    #         string[] filesToZip = Directory.GetFiles($"{outgoingFolderName}");

    #         string zipFileName = $"{folder.CustomerNumber}-{txtInput}.7z";

    #         string zipFile = $"{outgoingFolderName}\\{zipFileName}";

    #         if (filesToZip.Length != 0)
    #         {
    #             Zip7 zip = new Zip7(zipFile, filesToZip);

    #             zip.Start();

    #             zip.WaitForExit();
    #         }

    #         if (chkCopy)
    #         {
    #             if (!Directory.Exists(folder.DirProcessSimDataDesign))
    #                 Directory.CreateDirectory(folder.DirProcessSimDataDesign);

    #             string[] zipFiles = Directory.GetFiles(folder.DirProcessSimDataDesign, "*.7z",
    #                 SearchOption.TopDirectoryOnly);

    #             foreach (string zipFile1 in zipFiles)
    #                 // ReSharper disable once SwitchStatementMissingSomeCases
    #                 switch (MessageBox.Show($@"Delete file ""{zipFile1}""", @"Warning", MessageBoxButtons.YesNo))
    #                 {
    #                     case DialogResult.Yes:
    #                         File.Delete(zipFile1);
    #                         break;
    #                     case DialogResult.No:
    #                         break;
    #                     default:
    #                         throw new ArgumentException();
    #                 }

    #             File.Copy(zipFile, $"{folder.DirProcessSimDataDesign}\\{zipFileName}", true);
    #         }

    #         session_.ApplicationSwitchImmediate("UG_APP_MODELING");

    #         session_.Parts.Work.Drafting.ExitDraftingApplication();
    #     }

    #     public static void UpdateForPdf()
    #     {
    #         DrawingSheet[] sheets = session_.Parts.Work.DrawingSheets.ToArray();

    #         switch (sheets.Length)
    #         {
    #             case 0:
    #                 throw new InvalidOperationException("Current work part doesn't not have a sheet to print.");
    #             case 1:
    #                 session_.ApplicationSwitchImmediate("UG_APP_DRAFTING");
    #                 sheets[0].Open();
    #                 uf_.Draw.IsObjectOutOfDate(sheets[0].Tag, out bool outOfDate);
    #                 if (outOfDate)
    #                     uf_.Draw.UpdOutOfDateViews(sheets[0].Tag);
    #                 sheets[0].OwningPart.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);
    #                 break;
    #             default:
    #                 throw new InvalidOperationException("Current work part contains more than 1 sheet.");
    #         }
    #     }

    #     public static string ExportPDF(string outPutPath, string fileName)
    #     {
    #         DrawingSheet[] sheets = session_.Parts.Work.DrawingSheets.ToArray();

    #         ExportStripPdf(session_.Parts.Work.FullPath, sheets[0].Name, $"{outPutPath}\\{fileName}.pdf");

    #         return $"{outPutPath}\\{fileName}.pdf";
    #     }

    #     private static void AddDummy(Part part, IEnumerable<int> layers)
    #     {
    #         Prompt($"Setting layers in {__display_part_.Leaf}.");

    #         int[] layerArray = layers.ToArray();

    #         __display_part_.Layers.WorkLayer = 1;

    #         for (int i = 2; i < +256; i++)
    #             if (layerArray.Contains(i))
    #                 __display_part_.Layers.SetState(i, State.Selectable);
    #             else
    #                 __display_part_.Layers.SetState(i, State.Hidden);

    #         __display_part_.Layers.SetState(layerArray.Min(), State.WorkLayer);

    #         __display_part_.Layers.SetState(1, State.Hidden);

    #         if (part.ComponentAssembly.RootComponent != null)
    #         {
    #             Component validChild = part.ComponentAssembly.RootComponent
    #                 .GetChildren()
    #                 .Where(component => component.Prototype is Part)
    #                 .FirstOrDefault(component => !component.IsSuppressed);

    #             if (validChild != null)
    #                 return;
    #         }

    #         Part dummyPart = session_.__FindOrOpen(DummyPath);

    #         Prompt($"Adding dummy file to {part.Leaf}.");

    #         session_.Parts.Work.ComponentAssembly.AddComponent(dummyPart, "Entire Part", "DUMMY", _Point3dOrigin,
    #             _Matrix3x3Identity, 1, out PartLoadStatus status);

    #         status.Dispose();
    #     }

    #     public static void Prompt(string message)
    #     {
    #         UFSession.GetUFSession().Ui.SetPrompt(message);
    #     }

    #     private void SetAcceptButtonEnabled()
    #     {
    #         btnAccept.Enabled = chkPart.Checked || chkPDF.Checked || chkSTP.Checked || numUpDownCopies.Value > 0;
    #     }

    #     private void ChkBoxes_CheckedChanged(object sender, EventArgs e)
    #     {
    #         SetAcceptButtonEnabled();
    #     }

    #     private void NumUpDownCopies_ValueChanged(object sender, EventArgs e)
    #     {
    #         SetAcceptButtonEnabled();
    #     }

    #     public static List<Component> Descendants(Component parent)
    #     {
    #         List<Component> _list = new List<Component>
    #         {
    #             parent
    #         };

    #         foreach (Component _child in parent.GetChildren())
    #             _list.AddRange(Descendants(_child));

    #         return _list;
    #     }

    #     public static void SetLayersInBlanksAndLayoutsAndAddDummies(Part snapStrip010)
    #     {
    #         if (!Regex.IsMatch(snapStrip010.Leaf, Regex_Strip, RegexOptions.IgnoreCase))
    #             throw new ArgumentException(@"Must be an op 010 strip.", nameof(snapStrip010));

    #         Part currentD = __display_part_;
    #         Part currentW = session_.Parts.Work;

    #         try
    #         {
    #             Regex blankNameRegex = new Regex("^BLANK-([0-9]{1,})$");

    #             Regex layoutNameRegex = new Regex("^LAYOUT-([0-9]{1,})$");

    #             Part layoutPart = Descendants(__display_part_.ComponentAssembly.RootComponent)
    #                 .Select(component => component.Prototype)
    #                 .OfType<Part>()
    #                 .FirstOrDefault(component => Regex.IsMatch(component.Leaf, Regex_Layout, RegexOptions.IgnoreCase));

    #             //var blankPart = TSG_Library.Extensions.DisplayPart.RootComponent.Children
    #             Part blankPart = Descendants(__display_part_.ComponentAssembly.RootComponent)
    #                 .Select(component => component.Prototype)
    #                 .OfType<Part>()
    #                 .FirstOrDefault(component => Regex.IsMatch(component.Leaf, Regex_Blank, RegexOptions.IgnoreCase));

    #             HashSet<int> layoutLayers = new HashSet<int>();

    #             HashSet<int> blankLayers = new HashSet<int>();

    #             foreach (Component child in Descendants(__display_part_.ComponentAssembly.RootComponent))
    #             {
    #                 if (!(child.Prototype is Part))
    #                     continue;

    #                 if (child.IsSuppressed)
    #                     continue;

    #                 Match blankMatch = blankNameRegex.Match(child.Name);

    #                 Match layoutMatch = layoutNameRegex.Match(child.Name);

    #                 if (blankMatch.Success)
    #                     blankLayers.Add(int.Parse(blankMatch.Groups[1].Value) + 10);

    #                 if (!layoutMatch.Success)
    #                     continue;

    #                 int layer = int.Parse(layoutMatch.Groups[1].Value) * 10;

    #                 layoutLayers.Add(layer);

    #                 layoutLayers.Add(layer + 1);
    #             }

    #             if (blankLayers.Count != 0 && blankPart != null)
    #             {
    #                 session_.Parts.SetDisplay(blankPart, false, false, out _);

    #                 session_.Parts.SetWork(__display_part_);

    #                 AddDummy(blankPart, blankLayers);

    #                 Prompt($"Saving: {blankPart.Leaf}.");

    #                 __display_part_.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False);
    #             }

    #             if (layoutLayers.Count != 0 && layoutPart != null)
    #             {
    #                 session_.Parts.SetDisplay(layoutPart, false, false, out _);

    #                 session_.Parts.SetWork(__display_part_);

    #                 AddDummy(layoutPart, layoutLayers);

    #                 Prompt($"Saving: {layoutPart.Leaf}.");

    #                 __display_part_.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False);
    #             }
    #         }
    #         finally
    #         {
    #             session_.Parts.SetDisplay(currentD, false, false, out _);
    #             session_.Parts.SetWork(currentW);
    #         }

    #         snapStrip010.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);
    #     }

    #     public static void ExportStripStp(string outgoingFolderName)
    #     {
    #         string outputPath = $"{outgoingFolderName}\\{session_.Parts.Work.Leaf}-{TodaysDate}.stp";

    #         StepCreator step = session_.DexManager.CreateStepCreator();

    #         using (session_.__UsingBuilderDestroyer(step))
    #         {
    #             step.ExportDestination = BaseCreator.ExportDestinationOption.NativeFileSystem;

    # 			// sql convert
    # 			// in theory you should just be able to load the settingfile
    # 			// and not set any other step.properties
    #             step.SettingsFile = "U:\\nxFiles\\Step Translator\\ExternalStep_AllLayers.def";

    #             step.ExportAs = StepCreator.ExportAsOption.Ap214;

    #             step.InputFile = session_.Parts.Work.FullPath;

    #             step.OutputFile = outputPath;

    #             step.ProcessHoldFlag = true;

    #             step.Commit();
    #         }

    #         print(File.Exists(outputPath)
    #             ? $"Successfully created \"{outputPath}\"."
    #             : $"Did not successfully create \"{outputPath}\".");
    #     }

    #     public static void ExportStripPdf(string partPath, string drawingSheetName, string filePath)
    #     {
    #         string directory = Path.GetDirectoryName(filePath);

    #         if (!filePath.EndsWith(".pdf"))
    #             throw new Exception("File path for PDF must end with \".pdf\".");

    #         if (File.Exists(filePath))
    #             throw new Exception($"PDF '{filePath}' already exists.");

    #         Part part = session_.__FindOrOpen(partPath);

    #         //We can use SingleOrDefault here because NX will prevent the naming of two drawing sheets the exact same string.
    #         DrawingSheet sheet = part.DrawingSheets
    #                                  .ToArray()
    #                                  .SingleOrDefault(drawingSheet => drawingSheet.Name == drawingSheetName)
    #                              ??
    #                              throw new Exception(
    #                                  $@"Part '{partPath}' does not have a sheet named '{drawingSheetName}'.");

    #         __display_part_ = part;
    #         __work_part_ = __display_part_;

    #         PrintPDFBuilder pdfBuilder = part.PlotManager.CreatePrintPdfbuilder();

    #         using (session_.__UsingBuilderDestroyer(pdfBuilder))
    #         {
    # 			// sql
    #             pdfBuilder.Scale = 1.0;
    #             pdfBuilder.Size = PrintPDFBuilder.SizeOption.ScaleFactor;
    #             pdfBuilder.OutputText = PrintPDFBuilder.OutputTextOption.Polylines;
    #             pdfBuilder.Units = PrintPDFBuilder.UnitsOption.English;
    #             pdfBuilder.XDimension = 8.5;
    #             pdfBuilder.YDimension = 11.0;
    #             pdfBuilder.RasterImages = true;
    #             pdfBuilder.Colors = PrintPDFBuilder.Color.AsDisplayed;
    #             pdfBuilder.Watermark = "";
    #             UFSession.GetUFSession().Draw.IsObjectOutOfDate(sheet.Tag, out bool flag);
    #             if (flag)
    #             {
    #                 UFSession.GetUFSession().Draw.UpdOutOfDateViews(sheet.Tag);
    #                 part.__Save();
    #             }

    #             sheet.Open();
    #             pdfBuilder.SourceBuilder.SetSheets(new NXObject[] { sheet });
    #             pdfBuilder.Filename = filePath;
    #             pdfBuilder.Commit();
    #         }
    #     }

    #     public static string ExportStripPart(string outgoingFolderPath)
    #     {
    #         string[] assemblyPartPaths = __display_part_.ComponentAssembly.RootComponent.__Descendants()
    #             .Where(component => !component.IsSuppressed)
    #             .Select(component => component.Prototype)
    #             .OfType<Part>()
    #             .Distinct()
    #             .Select(part => part.FullPath)
    #             .ToArray();

    #         Zip7 zip = new Zip7($"{outgoingFolderPath}\\NX StripAssembly.7z", assemblyPartPaths);
    #         zip.Start();
    #         zip.WaitForExit();
    #         return $"{outgoingFolderPath}\\NX StripAssembly.7z";
    #     }

    #     public static void ExportStripPrintDrawing(int copies)
    #     {
    #         if (copies == 0)
    #             return;

    #         Part _WorkPart = Session.GetSession().Parts.Work;

    #         UFSession TheUFSession = UFSession.GetUFSession();

    #         //session_.Execute(@"C:\Repos\NXJournals\JOURNALS\export_strip.py", "ExportStrip", "print_drawing_sheet", new object[] { copies });
    #         PrintBuilder printBuilder1 = _WorkPart.PlotManager.CreatePrintBuilder();

    #         try
    #         {
    # 			// sql
    #             printBuilder1.ThinWidth = 1.0;
    #             printBuilder1.NormalWidth = 2.0;
    #             printBuilder1.ThickWidth = 3.0;
    #             printBuilder1.Copies = copies;
    #             printBuilder1.RasterImages = true;
    #             printBuilder1.Output = PrintBuilder.OutputOption.WireframeBlackWhite;
    #             DrawingSheet[] sheets = _WorkPart.DrawingSheets.ToArray();
    #             switch (sheets.Length)
    #             {
    #                 case 0:
    #                     print("Current work part doesn't not have a sheet to print.");
    #                     return;
    #                 case 1:
    #                     session_.ApplicationSwitchImmediate("UG_APP_DRAFTING");
    #                     sheets[0].Open();
    #                     TheUFSession.Draw.IsObjectOutOfDate(sheets[0].Tag, out bool outOfDate);
    #                     if (outOfDate)
    #                         try
    #                         {
    #                             TheUFSession.Draw.UpdOutOfDateViews(sheets[0].Tag);
    #                             sheets[0].OwningPart.Save(BasePart.SaveComponents.True, BasePart.CloseAfterSave.False);
    #                         }
    #                         catch (Exception ex)
    #                         {
    #                             ex.__PrintException();
    #                         }

    #                     printBuilder1.SourceBuilder.SetSheets(new NXObject[] { sheets[0] });
    #                     break;
    #                 default:
    #                     print("Current work part contains more than 1 sheet.");
    #                     return;
    #             }

    #             printBuilder1.PrinterText = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC";
    #             printBuilder1.Orientation = PrintBuilder.OrientationOption.Landscape;
    #             printBuilder1.Paper = PrintBuilder.PaperSize.Inch11x17;
    #             printBuilder1.Commit();
    #         }
    #         finally
    #         {
    #             printBuilder1.Destroy();
    #         }
    #     }

    #     private void ExportStripForm_Load(object sender, EventArgs e)
    #     {
    #         Text = AssemblyFileVersion;
    #         Location = Properties.Settings.Default.export_strip_form_window_location;
    #     }

    #     private void ExportStripForm_FormClosed(object sender, FormClosedEventArgs e)
    #     {
    #         Properties.Settings.Default.export_strip_form_window_location = Location;
    #         Properties.Settings.Default.Save();
    #     }

    #     public class Zip7
    #     {
    #         private readonly string[] _filesToZip;

    #         private readonly string _zipArchive;

    #         private Process _process;

    #         private bool _started;

    #         public Zip7(string zipArchive, params string[] filesToZip)
    #         {
    #             _zipArchive = zipArchive;

    #             _filesToZip = filesToZip;
    #         }

    #         public void WaitForExit()
    #         {
    #             if (_process is null)
    #                 throw new ArgumentNullException(nameof(_process));

    #             if (!_started)
    #                 throw new InvalidOperationException("Zip process hasn't been started yet.");

    #             _process.WaitForExit();
    #         }

    #         public void Start()
    #         {
    #             string tempFile = $"{Path.GetTempPath()}zipData{_filesToZip.GetHashCode()}.txt";

    #             using (FileStream fs = File.Open(tempFile, FileMode.Create))
    #             {
    #                 fs.Close();
    #             }

    #             using (StreamWriter writer = new StreamWriter(tempFile))
    #             {
    #                 _filesToZip.ToList().ForEach(writer.WriteLine);
    #             }

    # 			// select
    #             _process = new Process
    #             {
    #                 StartInfo =
    #             {
    #                 CreateNoWindow = false,
    #                 FileName = "C:\\Program Files\\7-Zip\\7z",
    #                 WindowStyle = ProcessWindowStyle.Normal,
    #                 UseShellExecute = true,
    #                 Arguments = $"a -t7z \"{_zipArchive}\" \"@{tempFile}\" -mx9"
    #             }
    #             };

    #             _started = _process.Start();
    #         }
    #     }
    # }
    pass
