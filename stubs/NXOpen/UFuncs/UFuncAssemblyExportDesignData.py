class UFuncAssemblyExportDesignData:
    #  public partial class AssemblyExportDesignData : _UFuncForm
    #  {
    #      public AssemblyExportDesignData()
    #      {
    #          InitializeComponent();
    #      }

    #      public static Part _WorkPart => Session.GetSession().Parts.Work;

    #      private void ResetForm()
    #      {
    #          if (__display_part_ is null)
    #          {
    #              Enabled = false;
    #              return;
    #          }

    #          Enabled = true;

    #          if (!rdoChange.Checked && !rdoRto.Checked && !rdoReview50.Checked && !rdoReview90.Checked &&
    #              !rdoReview100.Checked && !rdoOther.Checked)
    #              rdoReview50.Checked = true;

    #          GFolder folder = GFolder.create_or_null(_WorkPart);

    #          if (folder is null)
    #              return;

    #          if (folder.CustomerNumber.Length == 6)
    #          {
    #              if (rdoRto.Checked || rdoChange.Checked)
    #              {
    #                  txtFolderName.Text = "";
    #                  txtFolderName.Enabled = false;
    #                  return;
    #              }

    #              txtFolderName.Enabled = true;

    #              return;
    #          }

    #          txtFolderName.Enabled = true;
    #      }

    #      private void BtnData_Clicked(object sender, EventArgs e)
    #      {
    #          Hide();

    #          try
    #          {
    #              if (sender == btnDesignAccept)
    #                  Export_Design();
    #              else if (sender == btnSelectComponents)
    #                  ManualExport(false);
    #              else if (sender == btnSelectAll)
    #                  ManualExport(true);
    #          }
    #          catch (Exception ex)
    #          {
    #              ex.__PrintException();
    #          }
    #          finally
    #          {
    #              print("Complete");
    #              Show();
    #          }

    #          //stopwatch.Stop();

    #          //print_($"Time: {stopwatch.Elapsed.TotalMinutes:f2}");
    #      }

    #      private void ManualExport(bool selectAll)
    #      {
    #          Part __display_part_ = Session.GetSession().Parts.Display;

    #          List<Component> components = selectAll
    #              ? __display_part_.ComponentAssembly.RootComponent.__Descendants().ToList()
    #              : Selection.SelectManyComponents().ToList();

    #          if (components.Count == 0)
    #              return;

    #          components.Add(__display_part_.ComponentAssembly.RootComponent);

    #          if (chk4ViewDwg.Checked)
    #              try
    #              {
    #                  ExportDwg4Views(components);
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }

    #          Export1.Design(
    #              __display_part_,
    #              components.ToArray(),
    #              null,
    #              false,
    #              false,
    #              chk4ViewPDF.Checked,
    #              false,
    #              chkDetailStep.Checked,
    #              chkSee3DData.Checked,
    #              chkBurnout.Checked,
    #              chkParasolids.Checked,
    #              chkCastings.Checked,
    #              chkPrintData.Checked,
    #              rdoChange.Checked);
    #      }

    #      private void ExportDwg4Views(List<Component> components)
    #      {
    #          GFolder folder = GFolder.Create(__display_part_.FullPath);

    #          Part[] parts = components.Select(c => c.Prototype)
    #              .OfType<Part>()
    #              .Where(p => p.__HasDrawingSheet("4-VIEW"))
    #              .Distinct()
    #              .ToArray();

    #          var parts_to_export = from part in parts
    #                                where part.__IsPartDetail()
    #                                let op = part.__AskDetailOp()
    #                                let match = Regex.Match(part.Leaf, "^(\\d+-\\d+)-\\d+$")
    #                                where match.Success
    #                                let dir = $"{folder.dir_op(op)}\\{match.Groups[1].Value}-dwg-4-views"
    #                                let output = $"{dir}\\{part.Leaf}.dwg"
    #                                select new
    #                                {
    #                                    input_part = part.FullPath,
    #                                    output_part = output,
    #                                };

    #          foreach (var p in parts_to_export)
    #              try
    #              {
    #                  string dir = Path.GetDirectoryName(p.output_part);

    #                  if (!Directory.Exists(dir))
    #                      Directory.CreateDirectory(dir);

    #                  DxfdwgCreator dwgCreator = session_.DexManager.CreateDxfdwgCreator();

    #                  using (session_.__UsingBuilderDestroyer(dwgCreator))
    #                  {
    #                      dwgCreator.ExportData = DxfdwgCreator.ExportDataOption.Drawing;
    #                      dwgCreator.SettingsFile = "C:\\Program Files\\Siemens\\NX1899\\dxfdwg\\dxfdwg.def";
    #                      dwgCreator.OutputFileType = DxfdwgCreator.OutputFileTypeOption.Dwg;
    #                      dwgCreator.InputFile = p.input_part;
    #                      dwgCreator.OutputFile = p.output_part;
    #                      dwgCreator.DrawingList = "4-VIEW";
    #                      dwgCreator.ProcessHoldFlag = true;
    #                      dwgCreator.Commit();

    #                  }
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #      }

    #      private void Export_Design()
    #      {
    #          Component[] components;

    #          bool isRto = false;

    #          if (rdoRto.Checked)
    #          {
    #              isRto = true;
    #              components = __display_part_.ComponentAssembly.RootComponent.__Descendants().ToArray();
    #          }
    #          else if (rdoChange.Checked)
    #          {
    #              isRto = true;
    #              components = Selection.SelectManyComponents();
    #          }
    #          else if (rdoReview50.Checked || rdoReview90.Checked || rdoReview100.Checked || rdoOther.Checked)
    #          {
    #              isRto = false;
    #              components = __display_part_.ComponentAssembly.RootComponent.__Descendants().ToArray();
    #          }
    #          else
    #          {
    #              throw new ArgumentException();
    #          }

    #          if (components.Length == 0)
    #              return;

    #          Export1.Design(
    #              __display_part_,
    #              components,
    #              txtFolderName.Text,
    #              isRto || rdoChange.Checked,
    #              true,
    #              print4Views: isRto && chkPrintDesign.Checked,
    #              isChange: rdoChange.Checked);
    #      }

    #      private void Rdo_CheckedChanged(object sender, EventArgs e)
    #      {
    #          try
    #          {
    #              chkPrintDesign.Enabled = rdoRto.Checked || rdoChange.Checked;

    #              btnDesignAccept.Text = rdoChange.Checked
    #                  ? "Select"
    #                  : "Execute";

    #              if (__display_part_ is null)
    #                  return;

    #              GFolder folder = GFolder.create_or_null(_WorkPart);

    #              if (folder is null)
    #                  return;

    #              switch (folder.CustomerNumber.Length)
    #              {
    #                  case 6:
    #                      txtFolderName.Enabled = !rdoChange.Checked && !rdoRto.Checked;
    #                      break;
    #                  default:
    #                      txtFolderName.Enabled = true;
    #                      break;
    #              }

    #              string folderName = $"{TodaysDate}-----{__display_part_.Leaf}-----";

    #              if (sender == rdoReview50)
    #                  txtFolderName.Text = folderName + @"50% Review";

    #              else if (sender == rdoReview90)
    #                  txtFolderName.Text = folderName + @"90% Review";

    #              else if (sender == rdoReview100)
    #                  txtFolderName.Text = folderName + @"100% Review";

    #              else if (sender == rdoRto)
    #                  txtFolderName.Text = folderName + @"RTO";

    #              else if (sender == rdoOther)
    #                  txtFolderName.Text = folderName + @"-----";

    #              else if (sender == rdoChange)
    #                  txtFolderName.Text = folderName + @"-----";
    #          }
    #          catch (Exception ex)
    #          {
    #              ex.__PrintException();
    #          }
    #      }

    #      private void TabControl_Selected(object sender, TabControlEventArgs e)
    #      {
    #          if (tabControl.SelectedTab == tabDesign)
    #              Size = new Size(275, 249);
    #          else if (tabControl.SelectedTab == tabData)
    #              Size = new Size(182, 385);
    #      }

    #      private void AssemblyExportDesignDataForm_Load(object sender, EventArgs e)
    #      {
    #          Text = $"{AssemblyFileVersion} - Assembly Export";
    #          ResetForm();
    #          Location = Settings.Default.assembly_export_design_data_form_window_location;
    #      }

    #      private void AssemblyExportDesignDataForm_FormClosed(object sender, FormClosedEventArgs e)
    #      {
    #          Settings.Default.assembly_export_design_data_form_window_location = Location;
    #          Settings.Default.Save();
    #      }

    #      public class Export1
    #      {
    #          private const string ExportImportExe =
    #              @"U:\NX110\Concept\NX110library\Ufunc\ExportImportData\ExportImportData.exe";

    #          private const string Step214Ug = @"C:\Program Files\Siemens\NX 11.0\STEP214UG\step214ug.exe";

    #          public const string _printerCts = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC";

    #          // sql
    #          public static readonly int[] Layers = { 1, 94, 100, 111, 200, 230 };

    #          public static void Design(
    #              Part topLevelAssembly,
    #              Component[] __components,
    #              string outgoingDirectoryName = null,
    #              bool isRto = false,
    #              bool zipAssembly = false,
    #              bool pdf4Views = false,
    #              bool stp999 = false,
    #              bool stpDetails = false,
    #              bool stpSee3DData = false,
    #              bool dwgBurnout = false,
    #              bool parasolid = false,
    #              bool paraCasting = false,
    #              bool print4Views = false,
    #              bool isChange = false)
    #          {
    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  //using (session_.__UsingSuppressDisplay())
    #                  {
    #                      ufsession_.Ui.SetPrompt("Filtering components to export.");
    #                      GFolder folder = GFolder.Create(topLevelAssembly.FullPath);

    #                      if (!__components.All(comp => comp.OwningPart.Tag == topLevelAssembly.Tag))
    #                          throw new InvalidOperationException(
    #                              "All valid components must be under the top level display part.");

    #                      bool isSixDigit = folder.CustomerNumber.Length == 6;
    #                      HashSet<Part> hashedParts = new HashSet<Part>();

    #                      foreach (Component comp in __components)
    #                      {
    #                          if (!(comp.Prototype is Part part))
    #                              continue;

    #                          hashedParts.Add(part);
    #                      }

    #                      Part[] validParts = hashedParts.ToArray();

    #                      // sql
    #                      const string sevenZip = @"C:\Program Files\7-Zip\7z.exe";

    #                      if (!File.Exists(sevenZip))
    #                          throw new FileNotFoundException($"Could not find \"{sevenZip}\".");

    #                      string parentFolder = isSixDigit
    #                          ? folder.DirDesignInformation
    #                          : folder.DirOutgoing;

    #                      string exportDirectory = string.IsNullOrEmpty(outgoingDirectoryName)
    #                          ? null
    #                          : $"{parentFolder}\\{outgoingDirectoryName}";

    #                      if (!(isRto && isSixDigit) && zipAssembly && exportDirectory != null && Directory.Exists(exportDirectory))
    #                          switch (MessageBox.Show($@"{exportDirectory} already exisits, would you like to overwrite it?",
    #                                      @"Warning", MessageBoxButtons.YesNo))
    #                          {
    #                              case DialogResult.Yes:
    #                                  Directory.Delete(exportDirectory, true);
    #                                  break;
    #                              default:
    #                                  return;
    #                          }

    #                      if (!(isRto && isSixDigit))
    #                          if (!string.IsNullOrEmpty(outgoingDirectoryName))
    #                              Directory.CreateDirectory(exportDirectory);

    #                      // If this is an RTO, then we need to delete the data files in the appropriate op folders.
    #                      if (isRto && !isChange)
    #                          try
    #                          {
    #                              DeleteOpFolders(__display_part_, folder);
    #                          }
    #                          catch (Exception ex)
    #                          {
    #                              ex.__PrintException();
    #                          }

    #                      if (exportDirectory != null)
    #                          Directory.CreateDirectory(exportDirectory);

    #                      Regex detailRegex = new Regex(RegexDetail, RegexOptions.IgnoreCase);
    #                      validParts = validParts.Distinct(new EqualityLeaf()).ToArray();

    #                      IDictionary<string, ISet<Part>> exportDict = SortPartsForExport(validParts);

    #                      //#pragma warning disable CS0612 // Type or member is obsolete
    #                      //                        if (!CheckSizeDescriptions(exportDict["PDF_4-VIEW"]))
    #                      //                            switch (MessageBox.Show(
    #                      //                                        "At least one block did not match its' description. Would you like to continue?",
    #                      //                                        "Warning", MessageBoxButtons.YesNo))
    #                      //                            {
    #                      //                                case DialogResult.Yes:
    #                      //                                    break;
    #                      //                                default:
    #                      //                                    return;
    #                      //                            }
    #                      //#pragma warning restore CS0612 // Type or member is obsolete

    #                      __display_part_.__Save();

    #                      Stopwatch stop_watch = new Stopwatch();

    #                      stop_watch.Start();

    #                      try
    #                      {
    #                          /////////////////////
    #                          Process assemblyProcess = null;

    #                          // Sets up the strip.
    #                          if (isRto || stpDetails || zipAssembly)
    #                              using (session_.__UsingDisplayPartReset())
    #                                  SetUpStrip(folder);

    #                          UpdateParts(
    #                              isRto,
    #                              pdf4Views, stpDetails, exportDict["PDF_4-VIEW"],
    #                              print4Views, exportDict["PDF_4-VIEW"],
    #                              dwgBurnout, exportDict["DWG_BURNOUT"],
    #                              stp999, exportDict["STP_999"],
    #                              stpSee3DData, exportDict["STP_SEE3D"],
    #                              paraCasting, exportDict["X_T_CASTING"],
    #                              __components);

    #                          Dictionary<string, Process> dict = new Dictionary<string, Process>();

    #                          if (isRto && detailRegex.IsMatch(topLevelAssembly.Leaf))
    #                          {
    #                              string stpPath = CreatePath(folder, topLevelAssembly, "-Step-Assembly", ".stp");

    #                              string dir = Path.GetDirectoryName(stpPath);

    #                              if (!Directory.Exists(dir))
    #                                  Directory.CreateDirectory(dir);

    #                              AssemblyExportDesignDataStp(topLevelAssembly.FullPath, stpPath, FilePathExternalStepAssemblyDef);
    #                          }

    #                          // Prints the parts with 4-Views.
    #                          if (print4Views)
    #                              using (session_.__UsingDisplayPartReset())
    #                              {
    #                                  PrintPdfs(exportDict["PDF_4-VIEW"]);
    #                              }

    #                          // Gets the processes that will create the pdf 4-Views.
    #                          if (isRto || pdf4Views)
    #                              foreach (Part part in exportDict["PDF_4-VIEW"])
    #                                  try
    #                                  {
    #                                      if (part.Leaf.EndsWith("000"))
    #                                          continue;

    #                                      string pdfPath = CreatePath(folder, part, "-Pdf-4-Views", ".pdf");

    #                                      string dir = Path.GetDirectoryName(pdfPath);

    #                                      if (!Directory.Exists(dir))
    #                                          Directory.CreateDirectory(dir);

    #                                      if (File.Exists(pdfPath))
    #                                          File.Delete(pdfPath);

    #                                      print($"PDF 4-VIEW -> {pdfPath}");
    #                                      AssemblyExportDesignDataPdf(part, "4-VIEW", pdfPath);
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          // If this is a RTO then
    #                          if (isRto || stpDetails)
    #                              foreach (Part part in exportDict["PDF_4-VIEW"])
    #                              {
    #                                  string stpPath = CreatePath(folder, part, "-Step-Details", ".stp");

    #                                  string dir = Path.GetDirectoryName(stpPath);

    #                                  if (!Directory.Exists(dir))
    #                                      Directory.CreateDirectory(dir);

    #                                  if (File.Exists(stpPath))
    #                                      File.Delete(stpPath);

    #                                  print($"Step Details -> {part.FullPath}");
    #                                  AssemblyExportDesignDataStp(part.FullPath, stpPath, FilePathExternalStepDetailDef);
    #                              }

    #                          if (zipAssembly && !(isRto || stpDetails))
    #                              try
    #                              {
    #                                  string path = $"{exportDirectory}\\{topLevelAssembly.Leaf}.stp";

    #                                  string dir = Path.GetDirectoryName(path);

    #                                  if (!Directory.Exists(dir))
    #                                      Directory.CreateDirectory(dir);

    #                                  print($"{nameof(AssemblyExportDesignDataStp)} - {topLevelAssembly}");

    #                                  AssemblyExportDesignDataStp(topLevelAssembly.FullPath, path, FilePathExternalStepDetailDef);
    #                              }
    #                              catch (Exception ex)
    #                              {
    #                                  ex.__PrintException();
    #                              }

    #                          // Gets the processes that create stp see 3d data.
    #                          if (isRto || stpSee3DData)
    #                              foreach (Part part in exportDict["STP_SEE3D"])
    #                                  try
    #                                  {
    #                                      string output = CreatePath(folder, part, "-Step-See-3D-Data", ".stp");

    #                                      string dir = Path.GetDirectoryName(output);

    #                                      if (!Directory.Exists(dir))
    #                                          Directory.CreateDirectory(dir);

    #                                      print($"STEP See 3d - {part.FullPath}");

    #                                      AssemblyExportDesignDataStp(part.FullPath, output, @"U:\nxFiles\Step Translator\ExternalStep_Detail.def");
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          // Gets the processes that create stp 999 details.
    #                          if (isRto || stp999)
    #                              foreach (Part part in exportDict["STP_999"])
    #                                  try
    #                                  {
    #                                      string output = CreatePath(folder, part, "-Step-999", ".stp");

    #                                      string dir = Path.GetDirectoryName(output);

    #                                      if (!Directory.Exists(dir))
    #                                          Directory.CreateDirectory(dir);

    #                                      print($"999 - {part.FullPath}");
    #                                      AssemblyExportDesignDataStp(part.FullPath, output, @"U:\nxFiles\Step Translator\ExternalStep_Detail.def");
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          // Gets the processes that create burnout dwgs.
    #                          if (isRto || dwgBurnout)
    #                              foreach (Part part in exportDict["DWG_BURNOUT"])
    #                                  try
    #                                  {
    #                                      string output = CreatePath(folder, part, "-Dwg-Burnouts", ".dwg");

    #                                      string dir = Path.GetDirectoryName(output);

    #                                      if (!Directory.Exists(dir))
    #                                          Directory.CreateDirectory(dir);

    #                                      print($"BURNOUT - {part.FullPath}");

    #                                      AssemblyExportDesignDataDwg(part.FullPath, "BURNOUT", output);
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          //if (dwg4Views)
    #                          //    foreach (Part part in hashedParts)
    #                          //        try
    #                          //        {
    #                          //            string output = CreatePath(folder, part, "-Dwg-4-Views", ".dwg");

    #                          //            string dir = Path.GetDirectoryName(output);

    #                          //            if (!Directory.Exists(dir))
    #                          //                Directory.CreateDirectory(dir);

    #                          //            //print($"BURNOUT - {part.FullPath}");

    #                          //            Dwg(part.FullPath, "4-VIEW", output);
    #                          //        }
    #                          //        catch (Exception ex)
    #                          //        {
    #                          //            ex.__PrintException();
    #                          //        }

    #                          // Creates casting parasolids.
    #                          if (isRto || paraCasting)
    #                              foreach (Part castingPart in exportDict["X_T_CASTING"])
    #                                  try
    #                                  {
    #                                      print($"{nameof(CreateCasting)} - {castingPart.FullPath}");
    #                                      CreateCasting(castingPart, folder);
    #                                  }
    #                                  catch (Exception ex)
    #                                  {
    #                                      ex.__PrintException();
    #                                  }

    #                          HashSet<string> expectedFiles = new HashSet<string>(dict.Keys);

    #                          HashSet<string> directoriesToExport = new HashSet<string>(expectedFiles.Select(Path.GetDirectoryName));

    #                          CreateDirectoriesDeleteFiles(expectedFiles);

    #                          string zipPath = $"{exportDirectory}\\{topLevelAssembly.Leaf}_NX.7z";

    #                          if ((isRto && !isSixDigit) || (zipAssembly && !isRto))
    #                          {
    #                              print(nameof(Assembly));
    #                              assemblyProcess = Assembly(topLevelAssembly, false, zipPath);
    #                              assemblyProcess.Start();
    #                          }

    #                          prompt("Validating Stp Files.");

    #                          print(nameof(WriteStpCyanFiles));
    #                          WriteStpCyanFiles(expectedFiles);

    #                          prompt("Zipping up data folders.");

    #                          // Gets all the data folders that were created and zips them up and places them in the proper outgoingData folderWithCtsNumber if this is an RTO.
    #                          if (isRto && !isSixDigit)
    #                          {
    #                              print(nameof(ZipUpDataFolders));
    #                              ZipUpDataFolders(directoriesToExport, exportDirectory);
    #                          }

    #                          if (isRto && !isSixDigit)
    #                          {
    #                              print(nameof(ZipupDirectories));
    #                              ZipupDirectories(sevenZip, directoriesToExport, zipPath);
    #                          }

    #                          foreach (string file_key in dict.Keys)
    #                              try
    #                              {
    #                                  Process process = dict[file_key];

    #                                  if (File.Exists(file_key))
    #                                      continue;

    #                                  print($"Recreating: {file_key}");
    #                                  prompt($"Recreating: {file_key}");

    #                                  process.Start();

    #                                  process.WaitForExit();
    #                              }
    #                              catch (Exception ex)
    #                              {
    #                                  ex.__PrintException();
    #                              }

    #                          // Checks to make sure that any expected data files were actually created.
    #                          if (expectedFiles.Count > 0)
    #                          {
    #                              print(nameof(ErrorCheck));
    #                              ErrorCheck(isRto, zipAssembly, expectedFiles);
    #                          }

    #                          // Moves the sim report to the out going folderWithCtsNumber if one exists.
    #                          if (isRto && !isSixDigit && !(exportDirectory is null))
    #                          {
    #                              print(nameof(MoveSimReport));
    #                              MoveSimReport(folder, exportDirectory);
    #                          }

    #                          // Moves the stock list to the outgoing folderWithCtsNumber if one exists.
    #                          if (isRto && !isSixDigit && !(exportDirectory is null))
    #                          {
    #                              print(nameof(MoveStocklist));
    #                              MoveStocklist(folder, topLevelAssembly.Leaf, exportDirectory);
    #                          }

    #                          if (!(exportDirectory is null))
    #                          {
    #                              print(nameof(ZipupDataDirectories));
    #                              ZipupDataDirectories(exportDirectory, assemblyProcess);
    #                          }

    #                          /////////////////////////
    #                      }
    #                      finally
    #                      {
    #                          stop_watch.Stop();

    #                          print($"{stop_watch.Elapsed.Minutes}:{stop_watch.Elapsed.Seconds}");
    #                      }
    #                  }
    #              }
    #          }

    #          public static void DeleteOpFolders(Part part, GFolder folder)
    #          {
    #              if (folder is null)
    #                  throw new ArgumentException();

    #              // Matches the {part.Leaf} to 000 regex.
    #              Match top_match = Regex.Match(part.Leaf, RegexOp000Holder, RegexOptions.IgnoreCase);

    #              // If the {match} is not a success, then {part} is not a "000".
    #              if (!top_match.Success)
    #                  throw new Exception($"Part \"{part.FullPath}\" is not a 000.");

    #              // Gets the op of the {part}.
    #              string op = top_match.Groups["opNum"].Value;

    #              // The set that holds the data directories to delete.
    #              HashSet<string> directoriesToDelete = new HashSet<string>();

    #              switch (op)
    #              {
    #                  // Matches the 900 000's.
    #                  case "900":
    #                      {
    #                          directoriesToDelete.Add($"{folder.dir_op("900")}\\{folder.CustomerNumber}-900-Step-Assembly");

    #                          foreach (Component component in part.ComponentAssembly.RootComponent.GetChildren())
    #                          {
    #                              Match match = Regex.Match(component.DisplayName, RegexLwr);

    #                              if (!match.Success)
    #                                  continue;

    #                              string assembly_op = match.Groups["opNum"].Value;

    #                              if (assembly_op.Length % 2 != 0)
    #                                  continue;

    #                              for (int i = 0; i < assembly_op.Length - 1; i += 2)
    #                              {
    #                                  string temp_op = assembly_op[i] + "" + assembly_op[i + 1] + "0";

    #                                  string directory = folder.dir_op(temp_op);

    #                                  directoriesToDelete.Add(
    #                                      $"{directory}\\{folder.CustomerNumber}-{temp_op}-Parasolids-Castings");
    #                                  directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Pdf-4-Views");
    #                                  directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-Details");
    #                                  directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-Assembly");
    #                                  directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Dwg-Burnouts");
    #                                  directoriesToDelete.Add(
    #                                      $"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-See-3D-Data");
    #                              }
    #                          }
    #                      }
    #                      break;

    #                  // This matches all the regular op 010, 020, 030 and so 000's.
    #                  case var _ when op.Length == 3:
    #                      {
    #                          // Gets the assembly folderWithCtsNumber correpsonding to the {assemblyOp000}.
    #                          string assemblyFolder = folder.dir_op(op);

    #                          // If the directory {assemblyFolder} doesn't exist, then we want to throw.
    #                          if (!Directory.Exists(assemblyFolder))
    #                              throw new DirectoryNotFoundException($"Could not find directory \"{assemblyFolder}\".");

    #                          foreach (string directory in Directory.GetDirectories(assemblyFolder))
    #                          {
    #                              string dirName = Path.GetFileName(directory);

    #                              if (dirName == null)
    #                                  continue;

    #                              if (!dirName.StartsWith($"{folder.CustomerNumber}-{op}"))
    #                                  continue;

    #                              // Adds the {directory} to the {directoriesToDelete}.
    #                              directoriesToDelete.Add(directory);
    #                          }
    #                      }
    #                      break;

    #                  // Matches the assembly holder by ensuring that the op has an even amount of characters.
    #                  case var _ when op.Length % 2 == 0:
    #                      {
    #                          // A list to hold the ops.
    #                          List<string> opList = new List<string>();

    #                          // Gets the character array of the {assemblyHolder}.
    #                          char[] charArray = op.ToCharArray();

    #                          // Grab the op characters two at a time.
    #                          for (int i = 0; i < charArray.Length; i += 2)
    #                              opList.Add(charArray[i] + "" + charArray[i + 1] + "0");

    #                          foreach (string assemblyOp in opList)
    #                          {
    #                              // Gets the assembly folderWithCtsNumber correpsonding to the {assemblyOp000}.
    #                              string assemblyFolder = folder.dir_op(assemblyOp);

    #                              // If the directory {assemblyFolder} doesn't exist, then we want to throw.
    #                              if (!Directory.Exists(assemblyFolder))
    #                                  throw new DirectoryNotFoundException($"Could not find directory \"{assemblyFolder}\".");

    #                              foreach (string directory in Directory.GetDirectories(assemblyFolder))
    #                              {
    #                                  string dirName = Path.GetFileName(directory);

    #                                  if (dirName == null)
    #                                      continue;

    #                                  if (!dirName.StartsWith($"{folder.CustomerNumber}-{assemblyOp}"))
    #                                      continue;

    #                                  // Adds the {directory} to the {directoriesToDelete}.
    #                                  directoriesToDelete.Add(directory);
    #                              }
    #                          }
    #                      }
    #                      break;
    #              }

    #              foreach (string dir in directoriesToDelete)
    #                  if (Directory.Exists(dir))
    #                      Directory.Delete(dir, true);
    #          }

    #          public static void WriteStpCyanFiles(IEnumerable<string> expectedFiles)
    #          {
    #              foreach (string expected in expectedFiles)
    #              {
    #                  if (!expected.EndsWith(".stp") || !File.Exists(expected))
    #                      continue;

    #                  string fileText = File.ReadAllText(expected);

    #                  if (!fileText.Contains("Cyan"))
    #                      continue;

    #                  File.WriteAllText(expected, fileText.Replace("Cyan", "cyan"));
    #              }
    #          }

    #          public static void CreateDirectoriesDeleteFiles(IEnumerable<string> expectedFiles)
    #          {
    #              foreach (string file in expectedFiles)
    #                  try
    #                  {
    #                      string directory = Path.GetDirectoryName(file);
    #                      Directory.CreateDirectory(directory ?? throw new Exception());
    #                      File.Delete(file);
    #                  }
    #                  catch (Exception ex)
    #                  {
    #                      ex.__PrintException();
    #                  }
    #          }

    #          [Obsolete]
    #          public static bool CheckSizeDescriptions(IEnumerable<Part> partsInBom)
    #          {
    #              //bool allPassed = true;
    #              //foreach (Part part in partsInBom)
    #              //    try
    #              //    {
    #              //        if (!SizeDescription1.Validate(part, out string message))
    #              //        {
    #              //            if (message == "Part does not contain a Dynamic Block.")
    #              //                continue;
    #              //            allPassed = false;
    #              //            print_($"{part.Leaf}:\n{message}\n");
    #              //        }
    #              //    }
    #              //    catch (Exception ex)
    #              //    {
    #              //        ex.__PrintException();
    #              //    }

    #              //return allPassed;

    #              throw new NotImplementedException();
    #          }

    #          public static string CreatePath(GFolder folder, Part part, string directoryTag, string extension)
    #          {
    #              string directory =
    #                  $"{folder.DirJob}\\{folder.CustomerNumber}-{part.__AskDetailOp()}\\{folder.CustomerNumber}-{part.__AskDetailOp()}{directoryTag}";
    #              string stpPath = $"{directory}\\{part.Leaf}{extension}";
    #              return stpPath;
    #          }

    #          public static void SetLayers()
    #          {
    #              __display_part_.Layers.SetState(1, NXOpen.Layer.State.WorkLayer);

    #              for (int i = 2; i <= 256; i++)
    #                  if (Layers.Contains(i))
    #                      __display_part_.Layers.SetState(i, NXOpen.Layer.State.Selectable);
    #                  else
    #                      __display_part_.Layers.SetState(i, NXOpen.Layer.State.Hidden);
    #          }

    #          public static void CreateCasting(Part part, GFolder folder)
    #          {
    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  __display_part_ = part;

    #                  string op = part.__AskDetailOp();

    #                  string castingDirectory =
    #                      $"{folder.DirJob}\\{folder.CustomerNumber}-{op}\\{folder.CustomerNumber}-{op}-Parasolids-Castings";

    #                  if (!Directory.Exists(castingDirectory))
    #                      Directory.CreateDirectory(castingDirectory);

    #                  print($"Casting Step - {part.FullPath}");
    #                  CreateCastingStep(part, castingDirectory);

    #                  string castingPath = $"{castingDirectory}\\{part.Leaf}.x_t";

    #                  if (File.Exists(castingPath))
    #                      File.Delete(castingPath);

    #                  List<Tag> tagBodies = part.Bodies
    #                      .ToArray()
    #                      .OfType<Body>()
    #                      .Where(body => body.Layer == 1)
    #                      .Select(body => body.Tag)
    #                      .ToList();

    #                  if (tagBodies.Count == 0)
    #                  {
    #                      print($"Did not find any solid bodies on layer 1 in part {part.Leaf}");

    #                      return;
    #                  }

    #                  if (!(part.ComponentAssembly.RootComponent is null))
    #                      foreach (Component child in part.ComponentAssembly.RootComponent.GetChildren())
    #                      {
    #                          if (child.IsSuppressed)
    #                              continue;

    #                          if (child.Layer != 96)
    #                              continue;

    #                          if (child.ReferenceSet == "Empty")
    #                              continue;

    #                          foreach (Body __body in child.__Members().OfType<Body>().Where(__b => __b.IsSolidBody))
    #                              tagBodies.Add(__body.Tag);
    #                      }

    #                  string castingFile =
    #                      $"{folder.DirJob}\\{folder.CustomerNumber}-{op}\\{folder.CustomerNumber}-{op}-Parasolids-Castings\\{part.Leaf}.x_t";

    #                  ufsession_.Ps.ExportData(tagBodies.ToArray(), castingFile);
    #              }

    #              string FullPath = part.FullPath;

    #              part.Close(BasePart.CloseWholeTree.False, BasePart.CloseModified.CloseModified, null);

    #              session_.__FindOrOpen(FullPath);
    #          }

    #          private static void CreateCastingStep(Part part, string castingDirectory)
    #          {
    #              try
    #              {
    #                  string step_path = $"{castingDirectory}\\{part.Leaf}.stp";

    #                  if (File.Exists(step_path))
    #                      File.Delete(step_path);

    #                  using (session_.__UsingLockUgUpdates())

    #                  {
    #                      foreach (Component child in __display_part_.ComponentAssembly.RootComponent.GetChildren())
    #                      {
    #                          // sql
    #                          if (child.Layer == 96)
    #                              continue;

    #                          if (child.IsSuppressed)
    #                              continue;

    #                          child.Suppress();
    #                      }
    #                  }

    #                  Session theSession = Session.GetSession();
    #                  Part workPart = theSession.Parts.Work;
    #                  Part displayPart = theSession.Parts.Display;
    #                  // ----------------------------------------------
    #                  //   Menu: File->Export->STEP...
    #                  // ----------------------------------------------
    #                  Session.UndoMarkId markId1;
    #                  markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start");

    #                  StepCreator stepCreator1;
    #                  stepCreator1 = theSession.DexManager.CreateStepCreator();

    #                  // sql
    #                  stepCreator1.ExportAs = StepCreator.ExportAsOption.Ap214;

    #                  stepCreator1.BsplineTol = 0.001;

    #                  stepCreator1.SettingsFile = "C:\\Program Files\\Siemens\\NX1899\\step214ug\\ugstep214.def";

    #                  stepCreator1.BsplineTol = 0.001;

    #                  stepCreator1.InputFile = part.FullPath;

    #                  theSession.SetUndoMarkName(markId1, "Export STEP File Dialog");

    #                  Session.UndoMarkId markId2;
    #                  markId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Export STEP File");

    #                  theSession.DeleteUndoMark(markId2, null);

    #                  Session.UndoMarkId markId3;
    #                  markId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Export STEP File");

    #                  stepCreator1.OutputFile = step_path;

    #                  stepCreator1.FileSaveFlag = false;

    #                  stepCreator1.LayerMask = "1,96";

    #                  stepCreator1.ProcessHoldFlag = true;

    #                  NXObject nXObject1;
    #                  nXObject1 = stepCreator1.Commit();

    #                  theSession.DeleteUndoMark(markId3, null);

    #                  theSession.SetUndoMarkName(markId1, "Export STEP File");

    #                  stepCreator1.Destroy();
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void SetLayersInBlanksAndLayoutsAndAddDummies(Part snapStrip010)
    #          {
    #              if (!Regex.IsMatch(snapStrip010.Leaf, RegexStrip, RegexOptions.IgnoreCase))
    #                  throw new ArgumentException(@"Must be an op 010 strip.", nameof(snapStrip010));

    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  // sql
    #                  Regex blankNameRegex = new Regex("^BLANK-([0-9]{1,})$");

    #                  Regex layoutNameRegex = new Regex("^LAYOUT-([0-9]{1,})$");

    #                  Part layoutPart = __display_part_.ComponentAssembly.RootComponent.__Descendants()
    #                      .Select(component => component.Prototype)
    #                      .OfType<Part>()
    #                      .FirstOrDefault(component => Regex.IsMatch(component.Leaf, RegexLayout, RegexOptions.IgnoreCase));

    #                  Part blankPart = __display_part_.ComponentAssembly.RootComponent.__Descendants()
    #                      .Select(component => component.Prototype)
    #                      .OfType<Part>()
    #                      .FirstOrDefault(component => Regex.IsMatch(component.Leaf, RegexBlank, RegexOptions.IgnoreCase));

    #                  HashSet<int> layoutLayers = new HashSet<int>();

    #                  HashSet<int> blankLayers = new HashSet<int>();

    #                  foreach (Component child in __display_part_.ComponentAssembly.RootComponent.__Descendants())
    #                  {
    #                      if (!(child.Prototype is Part))
    #                          continue;

    #                      if (child.IsSuppressed)
    #                          continue;

    #                      Match blankMatch = blankNameRegex.Match(child.Name);
    #                      Match layoutMatch = layoutNameRegex.Match(child.Name);

    #                      if (blankMatch.Success)
    #                      {
    #                          int layer = int.Parse(blankMatch.Groups[1].Value) + 10;
    #                          blankLayers.Add(layer);
    #                      }

    #                      if (!layoutMatch.Success) continue;
    #                      {
    #                          int layer = int.Parse(layoutMatch.Groups[1].Value) * 10;
    #                          layoutLayers.Add(layer);
    #                          layoutLayers.Add(layer + 1);
    #                      }
    #                  }

    #                  if (blankLayers.Count != 0 && blankPart != null)
    #                  {
    #                      __display_part_ = blankPart;
    #                      __work_part_ = __display_part_;
    #                      AddDummy(blankPart, blankLayers);
    #                      ufsession_.Ui.SetPrompt($"Saving: {blankPart.Leaf}.");
    #                      Session.GetSession().Parts.Display
    #                          .Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False);
    #                  }

    #                  if (layoutLayers.Count != 0 && layoutPart != null)
    #                  {
    #                      __display_part_ = layoutPart;
    #                      __work_part_ = __display_part_;
    #                      AddDummy(layoutPart, layoutLayers);
    #                      ufsession_.Ui.SetPrompt($"Saving: {layoutPart.Leaf}.");
    #                      session_.Parts.Display.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False);
    #                  }
    #              }

    #              snapStrip010.__Save();
    #          }

    #          private static void AddDummy(Part part, IEnumerable<int> layers)
    #          {
    #              ufsession_.Ui.SetPrompt($"Setting layers in {__display_part_.Leaf}.");
    #              int[] layerArray = layers.ToArray();
    #              __display_part_.Layers.SetState(1, NXOpen.Layer.State.WorkLayer);

    #              for (int i = 2; i < +256; i++)
    #                  __display_part_.Layers.SetState(i, layerArray.Contains(i)
    #                      ? NXOpen.Layer.State.Selectable
    #                      : NXOpen.Layer.State.Hidden);

    #              __display_part_.Layers.SetState(layerArray.Min(), NXOpen.Layer.State.WorkLayer);
    #              __display_part_.Layers.SetState(1, NXOpen.Layer.State.Hidden);

    #              if (!(part.ComponentAssembly.RootComponent is null))
    #              {
    #                  Component validChild = part.ComponentAssembly.RootComponent
    #                      .GetChildren()
    #                      .Where(component => component.__IsLoaded())
    #                      .FirstOrDefault(component => !component.IsSuppressed);

    #                  if (validChild != null)
    #                      return;
    #              }

    #              Part dummyPart = session_.__FindOrOpen(DummyPath);
    #              ufsession_.Ui.SetPrompt($"Adding dummy file to {part.Leaf}.");
    #              __work_part_.ComponentAssembly.AddComponent(dummyPart, "Entire Part", "DUMMY", _Point3dOrigin,
    #                  _Matrix3x3Identity, 1, out _);
    #          }

    #          public static void CheckAssemblyDummyFiles()
    #          {
    #              ufsession_.Ui.SetPrompt("Checking Dummy files exist.");

    #              if (__display_part_.ComponentAssembly.RootComponent == null)
    #                  return;

    #              foreach (Component childOfStrip in __display_part_.ComponentAssembly.RootComponent.GetChildren())
    #              {
    #                  if (childOfStrip.IsSuppressed)
    #                      continue;

    #                  if (!childOfStrip.__IsLoaded())
    #                      continue;

    #                  if (!Regex.IsMatch(childOfStrip.DisplayName, RegexPressAssembly, RegexOptions.IgnoreCase))
    #                      continue;

    #                  if (childOfStrip.GetChildren().Length == 0)
    #                      throw new InvalidOperationException(
    #                          $"A press exists in your assembly without any children. {childOfStrip.__AssemblyPathString()}");

    #                  switch (childOfStrip.GetChildren().Length)
    #                  {
    #                      case 1:
    #                          throw new InvalidOperationException(
    #                              $"A press exists in your assembly with only one child. Expecting a ram and a bolster. {childOfStrip.__AssemblyPathString()}");
    #                      case 2:
    #                          foreach (Component childOfPress in childOfStrip.GetChildren())
    #                          {
    #                              if (!childOfPress.__IsLoaded())
    #                                  throw new InvalidOperationException(
    #                                      $"The child of a press must be loaded. {childOfPress.__AssemblyPathString()}");

    #                              if (childOfPress.IsSuppressed)
    #                                  throw new InvalidOperationException(
    #                                      $"The child of a press cannot be suppressed. {childOfPress.__AssemblyPathString()}");

    #                              if (childOfPress.GetChildren().Length != 0 && childOfPress.GetChildren()
    #                                      .Select(component => component)
    #                                      .Any(component => !component.IsSuppressed && component.Prototype is Part))
    #                                  continue;

    #                              throw new InvalidOperationException(
    #                                  $"The child of a bolster or ram under a press must be the Dummy file: {DummyPath}. {childOfPress.__AssemblyPathString()}");
    #                          }

    #                          break;
    #                  }
    #              }
    #          }

    #          public static void ZipupDataDirectories(string exportDirectory, Process assemblyProcess)
    #          {
    #              try
    #              {
    #                  string[] stpFilesInOutGoingFolder =
    #                      Directory.GetFiles(exportDirectory, "*.stp", SearchOption.TopDirectoryOnly);

    #                  if (stpFilesInOutGoingFolder.Length != 0)
    #                  {
    #                      string displayName = Path.GetFileNameWithoutExtension(stpFilesInOutGoingFolder.First());

    #                      Process stpZipProcess = AssemblyExportDesignDataCreate7ZipProcess($"{exportDirectory}\\{displayName}_STP.7z",
    #                          stpFilesInOutGoingFolder);

    #                      stpZipProcess.Start();

    #                      stpZipProcess.WaitForExit();

    #                      foreach (string file in stpFilesInOutGoingFolder)
    #                          try
    #                          {
    #                              if (File.Exists(file)) File.Delete(file);
    #                          }
    #                          catch (Exception ex)
    #                          {
    #                              ex.__PrintException();
    #                          }
    #                  }

    #                  assemblyProcess?.WaitForExit();
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          /// <summary>
    #          ///     Gets the file paths of all Sim Reports with the specified <paramref name="ctsJobNumber" />.
    #          /// </summary>
    #          /// <param name="ctsJobNumber">The job number.</param>
    #          /// <returns>An array of SimReport file paths.</returns>
    #          public static string[] GetReports(string ctsJobNumber)
    #          {
    #              return (from directory in Directory.GetDirectories("X:\\")
    #                      let directoryName = Path.GetFileName(directory)
    #                      where directoryName != null
    #                      // sql
    #                      let match = new Regex("^Reports-([0-9]{4})-([0-9]{4})$").Match(directoryName)
    #                      where match.Success
    #                      let startRange = int.Parse(match.Groups[1].Value)
    #                      let endRange = int.Parse(match.Groups[2].Value)
    #                      let jobNumber = int.Parse(ctsJobNumber)
    #                      where startRange <= jobNumber && jobNumber <= endRange
    #                      from report in Directory.GetFiles(directory, "*.7z")
    #                      let fileName = Path.GetFileNameWithoutExtension(report)
    #                      where fileName.StartsWith(ctsJobNumber)
    #                      select report).ToArray();
    #          }

    #          public static IDictionary<string, ISet<Part>> SortPartsForExport(IEnumerable<Part> validParts)
    #          {
    #              Regex detailRegex = new Regex(RegexDetail, RegexOptions.IgnoreCase);

    #              IDictionary<string, ISet<Part>> exportDict = new Dictionary<string, ISet<Part>>
    #          {
    #              { "PDF_4-VIEW", new HashSet<Part>() },
    #              { "STP_DETAIL", new HashSet<Part>() },
    #              { "DWG_BURNOUT", new HashSet<Part>() },
    #              { "STP_999", new HashSet<Part>() },
    #              { "STP_SEE3D", new HashSet<Part>() },
    #              { "X_T_CASTING", new HashSet<Part>() },
    #              { "X_T", new HashSet<Part>() }
    #          };

    #              foreach (Part part in validParts)
    #              {
    #                  Match match = detailRegex.Match(part.Leaf);

    #                  if (!match.Success)
    #                      continue;

    #                  if (part.Leaf.__IsAssemblyHolder())
    #                      continue;

    #                  if (part.Leaf.EndsWith("000"))
    #                      continue;

    #                  if (part.__HasDrawingSheet("4-VIEW"))
    #                      exportDict["PDF_4-VIEW"].Add(part);

    #                  if (part.__HasDrawingSheet("BURNOUT"))
    #                      exportDict["DWG_BURNOUT"].Add(part);

    #                  if (part.__IsSee3DData())
    #                      exportDict["STP_SEE3D"].Add(part);

    #                  if (part.__Is999())
    #                      exportDict["STP_999"].Add(part);

    #                  if (part.__IsCasting())
    #                      exportDict["X_T_CASTING"].Add(part);

    #                  if (part.__HasReferenceSet("BODY"))
    #                      exportDict["X_T"].Add(part);
    #              }

    #              return exportDict;
    #          }

    #          public static void UpdateParts(
    #              bool isRto,
    #              bool pdf4Views, bool stpDetails, IEnumerable<Part> partsWith4ViewsNoAssemblyHolders,
    #              bool print4Views, IEnumerable<Part> partsWith4Views,
    #              bool dwgBurnout, IEnumerable<Part> burnoutParts,
    #              bool stp999, IEnumerable<Part> nine99Parts,
    #              bool stpSee3DData, IEnumerable<Part> see3DDataParts,
    #              bool paraCasting, IEnumerable<Part> castingParts,
    #              Component[] selected_components)
    #          {
    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  ISet<Part> selected_parts =
    #                      new HashSet<Part>(selected_components.Select(__c => __c.Prototype).OfType<Part>());

    #                  ISet<Part> partsToUpdate = new HashSet<Part>();

    #                  if (isRto || pdf4Views || stpDetails)
    #                      foreach (Part part in partsWith4ViewsNoAssemblyHolders)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || dwgBurnout)
    #                      foreach (Part part in burnoutParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || print4Views)
    #                      foreach (Part part in partsWith4Views)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || paraCasting)
    #                      foreach (Part part in castingParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || stp999)
    #                      foreach (Part part in nine99Parts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (isRto || stpSee3DData)
    #                      foreach (Part part in see3DDataParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part);

    #                  if (partsToUpdate.Count > 0)
    #                      UpdateParts(partsToUpdate.ToArray());
    #              }
    #          }

    #          public static void ZipupDirectories(string sevenZip, IEnumerable<string> directoriesToExport, string zipPath)
    #          {
    #              try
    #              {
    #                  // Constructs the arguments that deletes the sub data folders in the newly created assembly zip folderWithCtsNumber.
    #                  string arguments = $"d \"{zipPath}\" -r {directoriesToExport.Select(Path.GetFileName).Where(dir => dir != null).Aggregate("", (s1, s2) => $"{s1} \"{s2}\"")}";

    #                  // Starts the actual delete process.
    #                  Process deleteProcess = Process.Start(sevenZip, arguments);

    #                  // Waits for the {deleteProcess} to finish.
    #                  deleteProcess?.WaitForExit();
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void MoveSimReport(GFolder folder, string exportDirectory)
    #          {
    #              try
    #              {
    #                  if (!folder.is_cts_job())
    #                      return;

    #                  if (GetReports(folder.CtsNumber).Length != 0)
    #                      foreach (string report in GetReports(folder.CtsNumber))
    #                      {
    #                          string reportName = Path.GetFileName(report);

    #                          if (reportName == null)
    #                              continue;

    #                          string exportedReportPath = $"{exportDirectory}\\{reportName}";

    #                          if (File.Exists(exportedReportPath))
    #                          {
    #                              print($"Sim report \"{exportedReportPath}\" already exists.");
    #                              continue;
    #                          }

    #                          File.Copy(report, exportedReportPath);
    #                      }
    #                  else
    #                      print("Unable to find a sim report to transfer.");
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void LaunchProcesses(int numberOfProcesses, params Process[] processes)
    #          {
    #              int processesCompleted = 0;

    #              try
    #              {
    #                  int length = numberOfProcesses > processes.Length
    #                      ? processes.Length
    #                      : numberOfProcesses;
    #                  HashSet<Process> hashProcesses = new HashSet<Process>();
    #                  for (int i = 0; i < length; i++)
    #                  {
    #                      processes[i].Start();
    #                      hashProcesses.Add(processes[i]);
    #                      prompt($"{processesCompleted} of {processes.Length}");
    #                  }

    #                  for (int i = length; processesCompleted < processes.Length; i++)
    #                  {
    #                      Process first = hashProcesses.FirstOrDefault(process => process != null && process.HasExited);
    #                      if (first == null)
    #                      {
    #                          i--;
    #                          continue;
    #                      }

    #                      hashProcesses.Remove(first);
    #                      processesCompleted++;
    #                      if (i < processes.Length)
    #                      {
    #                          Process nextProcess = processes[i];
    #                          nextProcess.Start();
    #                          hashProcesses.Add(nextProcess);
    #                      }

    #                      prompt($"{processesCompleted} of {processes.Length}");
    #                  }

    #                  processes.ToList().ForEach(proc => proc.WaitForExit());
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }

    #              ufsession_.Ui.SetPrompt("All processes have finished.");
    #          }

    #          public static void UpdateParts(params Part[] parts)
    #          {
    #              Part[] validParts = parts.Where(part => !part.Leaf.__IsAssemblyHolder()).Distinct(new EqualityLeaf())
    #                  .ToArray();

    #              for (int i = 0; i < validParts.Length; i++)
    #                  try
    #                  {
    #                      string report = $"Updating: {i + 1} of {validParts.Length}. ";
    #                      Part part = validParts[i];
    #                      ufsession_.Ui.SetPrompt($"{report}Setting Display Part to {part.Leaf}. ");
    #                      __display_part_ = part;
    #                      __work_part_ = __display_part_;

    #                      if (part.__IsCasting() && !(part.ComponentAssembly.RootComponent is null))
    #                          // If it is a casting then it cannot contain a child that is a lift lug and set to entire part.
    #                          if ((from child in part.ComponentAssembly.RootComponent.GetChildren()
    #                               where child.Prototype is Part
    #                               where child.__Prototype().FullPath.Contains("LiftLugs")
    #                               where child.ReferenceSet != RefsetEmpty
    #                               select child)
    #                              .Any(child => child.ReferenceSet == RefsetEntirePart))
    #                              print(
    #                                  $"Casting part {__display_part_.Leaf} contains a Lift Lug that is set to Entire Part. Casting Part cannot be made.");

    #                      ufsession_.Ui.SetPrompt($"{report}Setting layers in {part.Leaf}.");
    #                      SetLayers();
    #                      ufsession_.Ui.SetPrompt($"{report}Finding DisplayableObjects in {part.Leaf}.");
    #                      List<DisplayableObject> objects = new List<DisplayableObject>();

    #                      foreach (int layer in Layers)
    #                          objects.AddRange(__display_part_.Layers.GetAllObjectsOnLayer(layer)
    #                              .OfType<DisplayableObject>());

    #                      ufsession_.Ui.SetPrompt($"{report}Unblanking objects in {part.Leaf}.");
    #                      session_.DisplayManager.UnblankObjects(objects.ToArray());

    #                      foreach (DraftingView view in __display_part_.DraftingViews)
    #                          view.Update();

    #                      ufsession_.Ui.SetPrompt($"{report}Switching back to modeling in {part.Leaf}.");
    #                      session_.ApplicationSwitchImmediate("UG_APP_MODELING");
    #                      __work_part_.Drafting.ExitDraftingApplication();
    #                      ufsession_.Ui.SetPrompt($"{report}Saving {part.Leaf}.");
    #                      part.__Save();
    #                  }
    #                  catch (Exception ex)
    #                  {
    #                      ex.__PrintException(validParts[i].Leaf);
    #                  }
    #          }

    #          public static void SetUpStrip(GFolder folder)
    #          {
    #              try
    #              {
    #                  string strip_010 = folder.file_strip("010");

    #                  if (!File.Exists(strip_010))
    #                      return;

    #                  Part op010Strip = session_.__FindOrOpen(strip_010);

    #                  SetLayersInBlanksAndLayoutsAndAddDummies(op010Strip);

    #                  CheckAssemblyDummyFiles();

    #                  op010Strip.__Save();
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static Process Assembly(Part snapPart, bool waitForProcess, string zipPath)
    #          {
    #              HashSet<string> filePaths = new HashSet<string>();

    #              foreach (Component component in GetAssembly(snapPart.ComponentAssembly.RootComponent))
    #                  filePaths.Add(component.__Prototype().FullPath);

    #              return AssemblyExportDesignDataCreate7ZipProcess(zipPath, filePaths.ToArray());
    #          }

    #          /// <summary>Gets all the components under the given <paramref name="snapComponent" />.</summary>
    #          /// <remarks>The program will not go past components that are suppressed or end with "simulation"</remarks>
    #          /// <param name="snapComponent">The component to get the descendants from.</param>
    #          private static IEnumerable<Component> GetAssembly(Component snapComponent)
    #          {
    #              if (!snapComponent.__IsLoaded())
    #                  yield break;

    #              if (snapComponent.DisplayName.ToLower().EndsWith("-simulation"))
    #                  yield break;

    #              if (snapComponent.IsSuppressed)
    #                  yield break;

    #              yield return snapComponent;

    #              foreach (Component child in snapComponent.GetChildren())
    #                  foreach (Component comp in GetAssembly(child))
    #                      yield return comp;
    #          }

    #          public static void PrintPdfs(IEnumerable<Part> partsWith4Views)
    #          {
    #              using (session_.__UsingSuppressDisplay())
    #              {
    #                  try
    #                  {
    #                      UFSession.GetUFSession().Disp.SetDisplay(UFConstants.UF_DISP_UNSUPPRESS_DISPLAY);
    #                      UFSession.GetUFSession().Disp.RegenerateDisplay();
    #                      Print4Views(partsWith4Views);
    #                  }
    #                  catch (Exception ex)
    #                  {
    #                      ex.__PrintException();
    #                  }
    #              }
    #          }

    #          public static void ErrorCheck(bool isRto, bool zipAssembly, IEnumerable<string> expectedFiles)
    #          {
    #              string[] enumerable = expectedFiles as string[] ?? expectedFiles.ToArray();

    #              int fileCreatedCount = enumerable.Where(File.Exists).Count();

    #              print($"Created {fileCreatedCount} file(s).");

    #              if (!isRto && !zipAssembly)
    #                  print(
    #                      "Created files will have to be manually moved to outgoingData folderWithCtsNumber if that is desired. (Example: RTO)");

    #              List<string> filesThatWereNotCreated = enumerable.Where(s => !File.Exists(s)).ToList();

    #              List<Tuple<string, string>> errorList = new List<Tuple<string, string>>();

    #              foreach (string file in filesThatWereNotCreated)
    #              {
    #                  string extension = Path.GetExtension(file);

    #                  if (extension == null)
    #                      continue;

    #                  string errorFilePath = file.Replace(extension, ".err");

    #                  if (File.Exists(errorFilePath))
    #                  {
    #                      string[] fileContents = File.ReadAllLines(errorFilePath);

    #                      errorList.Add(new Tuple<string, string>(file, fileContents[0]));

    #                      File.Delete(errorFilePath);
    #                  }
    #                  else
    #                  {
    #                      errorList.Add(new Tuple<string, string>(file, "Unknown error."));
    #                  }
    #              }

    #              if (errorList.Count <= 0)
    #                  return;

    #              print("Files that were not created.");

    #              errorList.ForEach(print);
    #          }

    #          public static void ZipUpDataFolders(IEnumerable<string> directoriesToExport, string exportDirectory)
    #          {
    #              LaunchProcesses(10, (
    #                  from directory in directoriesToExport
    #                  let directoryName = Path.GetFileName(directory)
    #                  select AssemblyExportDesignDataCreate7ZipProcess($"{exportDirectory}\\{directoryName}.7z", directory)
    #              ).ToArray());
    #          }

    #          public static void Print4Views(IEnumerable<Part> allParts)
    #          {
    #              try
    #              {
    #                  bool IsNotAssembly(Part part)
    #                  {
    #                      string name = Path.GetFileNameWithoutExtension(part.FullPath);

    #                      if (name == null)
    #                          return false;

    #                      name = name.ToLower();

    #                      if (name.EndsWith("000") || name.EndsWith("lsh") || name.EndsWith("ush") || name.EndsWith("lwr") ||
    #                          name.EndsWith("upr"))
    #                          return false;

    #                      return !name.Contains("lsp") && !name.Contains("usp");
    #                  }

    #                  List<Part> parts = allParts
    #                      .Where(part => Regex.IsMatch(part.Leaf, RegexDetail, RegexOptions.IgnoreCase))
    #                      .Where(IsNotAssembly)
    #                      .Where(part => part.DraftingDrawingSheets.ToArray().Any(__d => __d.Name.ToUpper() == "4-VIEW"))
    #                      .ToList();

    #                  parts.Sort((part1, part2) => string.Compare(part1.Leaf, part2.Leaf, StringComparison.Ordinal));

    #                  for (int i = 0; i < parts.Count; i++)
    #                  {
    #                      Part part = parts[i];

    #                      ufsession_.Ui.SetPrompt($"{i + 1} of {parts.Count}. Printing 4-VIEW of {part.Leaf}.");

    #                      __display_part_ = part;

    #                      __work_part_ = __display_part_;

    #                      PrintBuilder printBuilder = __work_part_.PlotManager.CreatePrintBuilder();

    #                      using (new Destroyer(printBuilder))
    #                      {
    #                          // sql
    #                          printBuilder.Copies = 1;

    #                          printBuilder.ThinWidth = 1.0;

    #                          printBuilder.NormalWidth = 2.0;

    #                          printBuilder.ThickWidth = 3.0;

    #                          printBuilder.Output = PrintBuilder.OutputOption.WireframeBlackWhite;

    #                          printBuilder.ShadedGeometry = true;

    #                          DrawingSheet drawingSheet = __work_part_.DraftingDrawingSheets.FindObject("4-VIEW");

    #                          drawingSheet.Open();

    #                          printBuilder.SourceBuilder.SetSheets(new NXObject[] { drawingSheet });

    #                          printBuilder.PrinterText = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC";

    #                          printBuilder.Orientation = PrintBuilder.OrientationOption.Landscape;

    #                          printBuilder.Paper = PrintBuilder.PaperSize.Letter;

    #                          printBuilder.Commit();
    #                      }
    #                  }
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void MoveStocklist(GFolder folder, string topDisplayName, string exportDirectory)
    #          {
    #              try
    #              {
    #                  string stocklist = (from file in Directory.GetFiles(folder.DirStocklist)
    #                                      let name = Path.GetFileNameWithoutExtension(file)
    #                                      where name != null
    #                                      where name.EndsWith($"{topDisplayName}-stocklist")
    #                                      select file).SingleOrDefault();

    #                  if (stocklist is null)
    #                  {
    #                      print($"Could not find a stocklist named: {topDisplayName}-stocklist");
    #                      return;
    #                  }

    #                  File.Copy(stocklist, $"{exportDirectory}\\{Path.GetFileName(stocklist)}");
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static Process AssemblyExportDesignDataCreate7ZipProcess(string zipPath, params string[] filesToZip)
    #          {
    #              string tempFile = $"{Path.GetTempPath()}zipData{filesToZip.GetHashCode()}.txt";

    #              using (FileStream fs = File.Open(tempFile, FileMode.Create))
    #              {
    #                  fs.Close();
    #              }

    #              using (StreamWriter writer = new StreamWriter(tempFile))
    #              {
    #                  filesToZip.ToList().ForEach(writer.WriteLine);
    #              }

    #              return new Process
    #              {
    #                  EnableRaisingEvents = false,
    #                  StartInfo =
    #              {
    #                  CreateNoWindow = false,
    #                  FileName = "C:\\Program Files\\7-Zip\\7z",
    #                  WindowStyle = ProcessWindowStyle.Normal,
    #                  UseShellExecute = true,
    #                  Arguments = $"a -t7z \"{zipPath}\" \"@{tempFile}\" -mx9"
    #              }
    #              };
    #          }

    #          public static void AssemblyExportDesignDataSevenZip(string path, bool wait, params string[] fileNames)
    #          {
    #              string directory = Path.GetDirectoryName(path);

    #              string str = directory + "\\" + "zipData.txt";

    #              try
    #              {
    #                  using (FileStream fileStream = File.Open(str, FileMode.Create))
    #                  {
    #                      fileStream.Close();
    #                  }

    #                  using (StreamWriter streamWriter = new StreamWriter(str))
    #                  {
    #                      foreach (string fileName in fileNames)
    #                          streamWriter.WriteLine(fileName);
    #                  }

    #                  AssemblyExportDesignDataSevenZip(path, wait, str);
    #              }
    #              finally
    #              {
    #                  File.Delete(str);
    #              }
    #          }

    #          public static void AssemblyExportDesignDataSevenZip(string path, bool wait, string textFileToRead)
    #          {
    #              if (string.IsNullOrEmpty(path))
    #                  throw new ArgumentException(@"Invalid path.", nameof(path));

    #              if (File.Exists(path))
    #                  throw new IOException("The specified output_path already exists.");

    #              if (!File.Exists(textFileToRead))
    #                  throw new FileNotFoundException();

    #              // sql
    #              string fileToRead = "a -t7z \"" + path + "\" \"@" + textFileToRead + "\" -mx9";

    #              Process process = new Process
    #              {
    #                  EnableRaisingEvents = false,
    #                  StartInfo =
    #              {
    #                  FileName = "C:\\Program Files\\7-Zip\\7z",
    #                  Arguments = fileToRead
    #              }
    #              };

    #              process.Start();

    #              if (!wait)
    #                  return;

    #              process.WaitForExit();

    #              print(File.Exists(path)
    #                  ? $"Successfully created \"{path}\"."
    #                  : $"Unsuccessfully created \"{path}\".");
    #          }

    #          public static void AssemblyExportDesignDataPdf(Part part, string drawingSheetName, string filePath)
    #          {
    #              string directory = Path.GetDirectoryName(filePath);

    #              if (!filePath.EndsWith(".pdf"))
    #                  throw new InvalidOperationException("File path for PDF must end with \".pdf\".");

    #              if (File.Exists(filePath))
    #                  throw new ArgumentOutOfRangeException("output_path", "PDF \"" + filePath + "\" already exists.");

    #              //We can use SingleOrDefault here because NX will prevent the naming of two drawing sheets the exact same string.
    #              DrawingSheet sheet = part.DrawingSheets
    #                                       .ToArray()
    #                                       .SingleOrDefault(drawingSheet => drawingSheet.Name == drawingSheetName)
    #                                   ??
    #                                   throw new ArgumentException(
    #                                       $@"Part ""{part.Leaf}"" does not have a sheet named ""{drawingSheetName}"".",
    #                                       "drawingSheetName");

    #              __display_part_ = part;
    #              session_.__SetDisplayToWork();
    #              SetLayers();

    #              PrintPDFBuilder pdfBuilder = part.PlotManager.CreatePrintPdfbuilder();

    #              using (session_.__UsingBuilderDestroyer(pdfBuilder))
    #              {
    #                  // sql
    #                  pdfBuilder.Scale = 1.0;
    #                  pdfBuilder.Size = PrintPDFBuilder.SizeOption.ScaleFactor;
    #                  pdfBuilder.OutputText = PrintPDFBuilder.OutputTextOption.Polylines;
    #                  pdfBuilder.Units = PrintPDFBuilder.UnitsOption.English;
    #                  pdfBuilder.XDimension = 8.5;
    #                  pdfBuilder.YDimension = 11.0;
    #                  pdfBuilder.RasterImages = true;
    #                  pdfBuilder.Colors = PrintPDFBuilder.Color.BlackOnWhite;
    #                  pdfBuilder.Watermark = "";
    #                  UFSession.GetUFSession().Draw.IsObjectOutOfDate(sheet.Tag, out bool flag);

    #                  if (flag)
    #                  {
    #                      UFSession.GetUFSession().Draw.UpdOutOfDateViews(sheet.Tag);
    #                      part.__Save();
    #                  }

    #                  sheet.Open();
    #                  pdfBuilder.SourceBuilder.SetSheets(new NXObject[] { sheet });
    #                  pdfBuilder.Filename = filePath;
    #                  pdfBuilder.Commit();
    #              }
    #          }

    #          public static void AssemblyExportDesignDataStp(string partPath, string output_path, string settings_file)
    #          {
    #              try
    #              {
    #                  if (!output_path.EndsWith(".stp"))
    #                      throw new InvalidOperationException("File path for STP must end with \".stp\".");

    #                  if (File.Exists(output_path))
    #                      throw new ArgumentOutOfRangeException("output_path", "STP \"" + output_path + "\" already exists.");

    #                  if (!File.Exists(partPath))
    #                      throw new FileNotFoundException("Could not find file location \"" + partPath + "\".");

    #                  session_.__FindOrOpen(partPath);

    #                  StepCreator stepCreator = Session.GetSession().DexManager.CreateStepCreator();

    #                  using (session_.__UsingBuilderDestroyer(stepCreator))
    #                  {
    #                      // sql
    #                      stepCreator.ExportAs = StepCreator.ExportAsOption.Ap214;
    #                      stepCreator.SettingsFile = settings_file;
    #                      stepCreator.ObjectTypes.Solids = true;
    #                      stepCreator.OutputFile = output_path;
    #                      stepCreator.BsplineTol = 0.0254;
    #                      stepCreator.ObjectTypes.Annotations = true;
    #                      stepCreator.ExportFrom = StepCreator.ExportFromOption.ExistingPart;
    #                      stepCreator.InputFile = partPath;
    #                      stepCreator.FileSaveFlag = false;
    #                      stepCreator.LayerMask = "1, 96";
    #                      stepCreator.ProcessHoldFlag = true;
    #                      stepCreator.Commit();
    #                  }

    #                  string switchFilePath = output_path.Replace(".stp", ".log");

    #                  if (File.Exists(switchFilePath))
    #                      File.Delete(switchFilePath);
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException();
    #              }
    #          }

    #          public static void AssemblyExportDesignDataDwg(string partPath, string drawingSheetName, string filePath)
    #          {
    #              string directory = Path.GetDirectoryName(filePath);

    #              if (File.Exists(filePath))
    #                  throw new ArgumentOutOfRangeException("output_path", "DWG \"" + filePath + "\" already exists.");

    #              Part part = session_.__FindOrOpen(partPath);

    #              DrawingSheet sheet = part.DrawingSheets
    #                                       .ToArray()
    #                                       .SingleOrDefault(drawingSheet => drawingSheet.Name == drawingSheetName)
    #                                   ??
    #                                   throw new ArgumentException(
    #                                       $"Part \"{part.Leaf}\" does not have a sheet named \"{drawingSheetName}\".",
    #                                       "drawingSheetName");

    #              UFSession.GetUFSession().Draw.IsObjectOutOfDate(sheet.Tag, out bool flag);

    #              if (flag)
    #              {
    #                  SetLayers();
    #                  UFSession.GetUFSession().Draw.UpdOutOfDateViews(sheet.Tag);
    #                  part.__Save();
    #              }

    #              DxfdwgCreator dxfdwgCreator1 = session_.DexManager.CreateDxfdwgCreator();
    #              using (session_.__UsingBuilderDestroyer(dxfdwgCreator1))
    #              {
    #                  // sql
    #                  dxfdwgCreator1.ExportData = DxfdwgCreator.ExportDataOption.Drawing;
    #                  dxfdwgCreator1.AutoCADRevision = DxfdwgCreator.AutoCADRevisionOptions.R2004;
    #                  dxfdwgCreator1.ViewEditMode = true;
    #                  dxfdwgCreator1.FlattenAssembly = true;
    #                  dxfdwgCreator1.SettingsFile = "C:\\Program Files\\Siemens\\NX 11.0\\dxfdwg\\dxfdwg.def";
    #                  dxfdwgCreator1.ExportFrom = DxfdwgCreator.ExportFromOption.ExistingPart;
    #                  dxfdwgCreator1.OutputFileType = DxfdwgCreator.OutputFileTypeOption.Dwg;
    #                  dxfdwgCreator1.ObjectTypes.Curves = true;
    #                  dxfdwgCreator1.ObjectTypes.Annotations = true;
    #                  dxfdwgCreator1.ObjectTypes.Structures = true;
    #                  dxfdwgCreator1.FlattenAssembly = false;
    #                  dxfdwgCreator1.ExportData = DxfdwgCreator.ExportDataOption.Drawing;
    #                  dxfdwgCreator1.InputFile = part.FullPath;
    #                  dxfdwgCreator1.ProcessHoldFlag = true;
    #                  dxfdwgCreator1.OutputFile = filePath;
    #                  dxfdwgCreator1.WidthFactorMode = DxfdwgCreator.WidthfactorMethodOptions.AutomaticCalculation;
    #                  dxfdwgCreator1.LayerMask = "1-256";
    #                  dxfdwgCreator1.DrawingList = drawingSheetName;
    #                  dxfdwgCreator1.Commit();
    #              }

    #              string switchFilePath = filePath.Replace(".dwg", ".log");

    #              if (File.Exists(switchFilePath))
    #                  File.Delete(switchFilePath);
    #          }
    #      }
    #  }

    pass
