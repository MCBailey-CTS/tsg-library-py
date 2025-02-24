from typing import List

from NXOpen import Part


Step214Ug = "C:\\Program Files\\Siemens\\NX 11.0\\STEP214UG\\step214ug.exe"

_printerCts = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC"

Layers = {1, 94, 100, 111, 200, 230}


def export_design_DeleteOpFolders(part: Part, folder) -> None:
    # if (folder is null)
    #     throw new ArgumentException()
    # // Matches the {part.Leaf} to 000 regex.
    # Match top_match = Regex.Match(part.Leaf, RegexOp000Holder, RegexOptions.IgnoreCase)
    # // If the {match} is not a success, then {part} is not a "000".
    # if (!top_match.Success)
    #     throw new Exception($"Part \"{part.FullPath}\" is not a 000.")
    # // Gets the op of the {part}.
    # string op = top_match.Groups["opNum"].Value
    # // The set that holds the data directories to delete.
    # HashSet<string> directoriesToDelete = new HashSet<string>()
    # switch (op)
    #     // Matches the 900 000's.
    #     case "900":
    #             directoriesToDelete.Add($"{folder.dir_op("900")}\\{folder.CustomerNumber}-900-Step-Assembly")
    #             foreach (Component component in part.ComponentAssembly.RootComponent.GetChildren())
    #                 Match match = Regex.Match(component.DisplayName, RegexLwr)
    #                 if (!match.Success)
    #                     continue
    #                 string assembly_op = match.Groups["opNum"].Value
    #                 if (assembly_op.Length % 2 != 0)
    #                     continue
    #                 for (int i = 0 i < assembly_op.Length - 1 i += 2)
    #                     string temp_op = assembly_op[i] + "" + assembly_op[i + 1] + "0"
    #                     string directory = folder.dir_op(temp_op)
    #                     directoriesToDelete.Add(
    #                         $"{directory}\\{folder.CustomerNumber}-{temp_op}-Parasolids-Castings")
    #                     directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Pdf-4-Views")
    #                     directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-Details")
    #                     directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-Assembly")
    #                     directoriesToDelete.Add($"{directory}\\{folder.CustomerNumber}-{temp_op}-Dwg-Burnouts")
    #                     directoriesToDelete.Add(
    #                         $"{directory}\\{folder.CustomerNumber}-{temp_op}-Step-See-3D-Data")
    #         break
    #     // This matches all the regular op 010, 020, 030 and so 000's.
    #     case var _ when op.Length == 3:
    #             // Gets the assembly folderWithCtsNumber correpsonding to the {assemblyOp000}.
    #             string assemblyFolder = folder.dir_op(op)
    #             // If the directory {assemblyFolder} doesn't exist, then we want to throw.
    #             if (!Directory.Exists(assemblyFolder))
    #                 throw new DirectoryNotFoundException($"Could not find directory \"{assemblyFolder}\".")
    #             foreach (string directory in Directory.GetDirectories(assemblyFolder))
    #                 string dirName = Path.GetFileName(directory)
    #                 if (dirName == null)
    #                     continue
    #                 if (!dirName.StartsWith($"{folder.CustomerNumber}-{op}"))
    #                     continue
    #                 // Adds the {directory} to the {directoriesToDelete}.
    #                 directoriesToDelete.Add(directory)
    #         break
    #     // Matches the assembly holder by ensuring that the op has an even amount of characters.
    #     case var _ when op.Length % 2 == 0:
    #             // A list to hold the ops.
    #             List<string> opList = new List<string>()
    #             // Gets the character array of the {assemblyHolder}.
    #             char[] charArray = op.ToCharArray()
    #             // Grab the op characters two at a time.
    #             for (int i = 0 i < charArray.Length i += 2)
    #                 opList.Add(charArray[i] + "" + charArray[i + 1] + "0")
    #             foreach (string assemblyOp in opList)
    #                 // Gets the assembly folderWithCtsNumber correpsonding to the {assemblyOp000}.
    #                 string assemblyFolder = folder.dir_op(assemblyOp)
    #                 // If the directory {assemblyFolder} doesn't exist, then we want to throw.
    #                 if (!Directory.Exists(assemblyFolder))
    #                     throw new DirectoryNotFoundException($"Could not find directory \"{assemblyFolder}\".")
    #                 foreach (string directory in Directory.GetDirectories(assemblyFolder))
    #                     string dirName = Path.GetFileName(directory)
    #                     if (dirName == null)
    #                         continue
    #                     if (!dirName.StartsWith($"{folder.CustomerNumber}-{assemblyOp}"))
    #                         continue
    #                     // Adds the {directory} to the {directoriesToDelete}.
    #                     directoriesToDelete.Add(directory)
    #         break
    # foreach (string dir in directoriesToDelete)
    #     if (Directory.Exists(dir))
    #         Directory.Delete(dir, true)
    raise NotImplementedError()


def export_design_WriteStpCyanFiles(expectedFiles: List[str]) -> None:
    # foreach (string expected in expectedFiles)
    #     if (!expected.EndsWith(".stp") || !File.Exists(expected))
    #         continue
    #     string fileText = File.ReadAllText(expected)
    #     if (!fileText.Contains("Cyan"))
    #         continue
    #     File.WriteAllText(expected, fileText.Replace("Cyan", "cyan"))
    raise NotImplementedError()


def export_design_CreateDirectoriesDeleteFiles(expectedFiles: List[str]) -> None:
    # foreach (string file in expectedFiles)
    #     string directory = Path.GetDirectoryName(file)
    #     Directory.CreateDirectory(directory ?? throw new Exception())
    #     File.Delete(file)
    raise NotImplementedError()


def export_design_CheckSizeDescriptions(partsInBom: List[Part]) -> bool:
    # [Obsolete]
    #     //bool allPassed = true
    #     //foreach (Part part in partsInBom)
    #     //    try
    #     //    {
    #     //        if (!SizeDescription1.Validate(part, out string message))
    #     //        {
    #     //            if (message == "Part does not contain a Dynamic Block.")
    #     //                continue
    #     //            allPassed = false
    #     //            print_($"{part.Leaf}:\n{message}\n")
    #     //        }
    #     //    }
    #     //    catch (Exception ex)
    #     //    {
    #     //        ex.__PrintException()
    #     //    }

    #     //return allPassed

    #     throw new NotImplementedException()
    raise NotImplementedError()


def export_design_CreatePath(
    folder, part: Part, directoryTag: str, extension: str
) -> str:
    # string directory =
    #     $"{folder.DirJob}\\{folder.CustomerNumber}-{part.__AskDetailOp()}\\{folder.CustomerNumber}-{part.__AskDetailOp()}{directoryTag}"
    # string stpPath = $"{directory}\\{part.Leaf}{extension}"
    # return stpPath
    raise NotImplementedError()


def export_design_SetLayers() -> None:
    # __display_part_.Layers.SetState(1, NXOpen.Layer.State.WorkLayer)
    # for (int i = 2 i <= 256 i++)
    #     if (Layers.Contains(i))
    #         __display_part_.Layers.SetState(i, NXOpen.Layer.State.Selectable)
    #     else
    #         __display_part_.Layers.SetState(i, NXOpen.Layer.State.Hidden)
    raise NotImplementedError()


def export_design_CreateCasting(part, folder) -> None:
    # using (session_.__UsingDisplayPartReset())
    #     __display_part_ = part
    #     string op = part.__AskDetailOp()
    #     string castingDirectory =
    #         $"{folder.DirJob}\\{folder.CustomerNumber}-{op}\\{folder.CustomerNumber}-{op}-Parasolids-Castings"
    #     if (!Directory.Exists(castingDirectory))
    #         Directory.CreateDirectory(castingDirectory)
    #     print($"Casting Step - {part.FullPath}")
    #     CreateCastingStep(part, castingDirectory)
    #     string castingPath = $"{castingDirectory}\\{part.Leaf}.x_t"
    #     if (File.Exists(castingPath))
    #         File.Delete(castingPath)
    #     List<Tag> tagBodies = part.Bodies
    #         .ToArray()
    #         .OfType<Body>()
    #         .Where(body => body.Layer == 1)
    #         .Select(body => body.Tag)
    #         .ToList()
    #     if (tagBodies.Count == 0)
    #         print($"Did not find any solid bodies on layer 1 in part {part.Leaf}")
    #         return
    #     if (!(part.ComponentAssembly.RootComponent is null))
    #         foreach (Component child in part.ComponentAssembly.RootComponent.GetChildren())
    #             if (child.IsSuppressed)
    #                 continue
    #             if (child.Layer != 96)
    #                 continue
    #             if (child.ReferenceSet == "Empty")
    #                 continue
    #             foreach (Body __body in child.__Members().OfType<Body>().Where(__b => __b.IsSolidBody))
    #                 tagBodies.Add(__body.Tag)
    #     string castingFile =
    #         $"{folder.DirJob}\\{folder.CustomerNumber}-{op}\\{folder.CustomerNumber}-{op}-Parasolids-Castings\\{part.Leaf}.x_t"
    #     ufsession_.Ps.ExportData(tagBodies.ToArray(), castingFile)
    # string FullPath = part.FullPath
    # part.Close(BasePart.CloseWholeTree.False, BasePart.CloseModified.CloseModified, null)
    # session_.__FindOrOpen(FullPath)
    raise NotImplementedError()


def export_design_CreateCastingStep() -> None:
    #          private static void export_design_CreateCastingStep(Part part, string castingDirectory)
    #          {
    #              try
    #              {
    #                  string step_path = $"{castingDirectory}\\{part.Leaf}.stp"

    #                  if (File.Exists(step_path))
    #                      File.Delete(step_path)

    #                  using (session_.__UsingLockUgUpdates())

    #                  {
    #                      foreach (Component child in __display_part_.ComponentAssembly.RootComponent.GetChildren())
    #                      {
    #                          // sql
    #                          if (child.Layer == 96)
    #                              continue

    #                          if (child.IsSuppressed)
    #                              continue

    #                          child.Suppress()
    #                      }
    #                  }

    #                  Session theSession = Session.GetSession()
    #                  Part workPart = theSession.Parts.Work
    #                  Part displayPart = theSession.Parts.Display
    #                  // ----------------------------------------------
    #                  //   Menu: File->Export->STEP...
    #                  // ----------------------------------------------
    #                  Session.UndoMarkId markId1
    #                  markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

    #                  StepCreator stepCreator1
    #                  stepCreator1 = theSession.DexManager.CreateStepCreator()

    #                  // sql
    #                  stepCreator1.ExportAs = StepCreator.ExportAsOption.Ap214

    #                  stepCreator1.BsplineTol = 0.001

    #                  stepCreator1.SettingsFile = "C:\\Program Files\\Siemens\\NX1899\\step214ug\\ugstep214.def"

    #                  stepCreator1.BsplineTol = 0.001

    #                  stepCreator1.InputFile = part.FullPath

    #                  theSession.SetUndoMarkName(markId1, "Export STEP File Dialog")

    #                  Session.UndoMarkId markId2
    #                  markId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Export STEP File")

    #                  theSession.DeleteUndoMark(markId2, null)

    #                  Session.UndoMarkId markId3
    #                  markId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Export STEP File")

    #                  stepCreator1.OutputFile = step_path

    #                  stepCreator1.FileSaveFlag = false

    #                  stepCreator1.LayerMask = "1,96"

    #                  stepCreator1.ProcessHoldFlag = true

    #                  NXObject nXObject1
    #                  nXObject1 = stepCreator1.Commit()

    #                  theSession.DeleteUndoMark(markId3, null)

    #                  theSession.SetUndoMarkName(markId1, "Export STEP File")

    #                  stepCreator1.Destroy()
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException()
    #              }
    #          }
    raise NotImplementedError()


def export_design_SetLayersInBlanksAndLayoutsAndAddDummies() -> None:
    #          public static void export_design_SetLayersInBlanksAndLayoutsAndAddDummies(Part snapStrip010)
    #          {
    #              if (!Regex.IsMatch(snapStrip010.Leaf, RegexStrip, RegexOptions.IgnoreCase))
    #                  throw new ArgumentException(@"Must be an op 010 strip.", nameof(snapStrip010))

    #              using (session_.__UsingDisplayPartReset())
    #              {
    #                  // sql
    #                  Regex blankNameRegex = new Regex("^BLANK-([0-9]{1,})$")

    #                  Regex layoutNameRegex = new Regex("^LAYOUT-([0-9]{1,})$")

    #                  Part layoutPart = __display_part_.ComponentAssembly.RootComponent.__Descendants()
    #                      .Select(component => component.Prototype)
    #                      .OfType<Part>()
    #                      .FirstOrDefault(component => Regex.IsMatch(component.Leaf, RegexLayout, RegexOptions.IgnoreCase))

    #                  Part blankPart = __display_part_.ComponentAssembly.RootComponent.__Descendants()
    #                      .Select(component => component.Prototype)
    #                      .OfType<Part>()
    #                      .FirstOrDefault(component => Regex.IsMatch(component.Leaf, RegexBlank, RegexOptions.IgnoreCase))

    #                  HashSet<int> layoutLayers = new HashSet<int>()

    #                  HashSet<int> blankLayers = new HashSet<int>()

    #                  foreach (Component child in __display_part_.ComponentAssembly.RootComponent.__Descendants())
    #                  {
    #                      if (!(child.Prototype is Part))
    #                          continue

    #                      if (child.IsSuppressed)
    #                          continue

    #                      Match blankMatch = blankNameRegex.Match(child.Name)
    #                      Match layoutMatch = layoutNameRegex.Match(child.Name)

    #                      if (blankMatch.Success)
    #                      {
    #                          int layer = int.Parse(blankMatch.Groups[1].Value) + 10
    #                          blankLayers.Add(layer)
    #                      }

    #                      if (!layoutMatch.Success) continue
    #                      {
    #                          int layer = int.Parse(layoutMatch.Groups[1].Value) * 10
    #                          layoutLayers.Add(layer)
    #                          layoutLayers.Add(layer + 1)
    #                      }
    #                  }

    #                  if (blankLayers.Count != 0 && blankPart != null)
    #                  {
    #                      __display_part_ = blankPart
    #                      __work_part_ = __display_part_
    #                      AddDummy(blankPart, blankLayers)
    #                      ufsession_.Ui.SetPrompt($"Saving: {blankPart.Leaf}.")
    #                      Session.GetSession().Parts.Display
    #                          .Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False)
    #                  }

    #                  if (layoutLayers.Count != 0 && layoutPart != null)
    #                  {
    #                      __display_part_ = layoutPart
    #                      __work_part_ = __display_part_
    #                      AddDummy(layoutPart, layoutLayers)
    #                      ufsession_.Ui.SetPrompt($"Saving: {layoutPart.Leaf}.")
    #                      session_.Parts.Display.Save(BasePart.SaveComponents.False, BasePart.CloseAfterSave.False)
    #                  }
    #              }

    #              snapStrip010.__Save()
    #          }
    raise NotImplementedError()


def export_design_AddDummy() -> None:
    #          private static void export_design_AddDummy(Part part, IEnumerable<int> layers)
    #          {
    #              ufsession_.Ui.SetPrompt($"Setting layers in {__display_part_.Leaf}.")
    #              int[] layerArray = layers.ToArray()
    #              __display_part_.Layers.SetState(1, NXOpen.Layer.State.WorkLayer)

    #              for (int i = 2 i < +256 i++)
    #                  __display_part_.Layers.SetState(i, layerArray.Contains(i)
    #                      ? NXOpen.Layer.State.Selectable
    #                      : NXOpen.Layer.State.Hidden)

    #              __display_part_.Layers.SetState(layerArray.Min(), NXOpen.Layer.State.WorkLayer)
    #              __display_part_.Layers.SetState(1, NXOpen.Layer.State.Hidden)

    #              if (!(part.ComponentAssembly.RootComponent is null))
    #              {
    #                  Component validChild = part.ComponentAssembly.RootComponent
    #                      .GetChildren()
    #                      .Where(component => component.__IsLoaded())
    #                      .FirstOrDefault(component => !component.IsSuppressed)

    #                  if (validChild != null)
    #                      return
    #              }

    #              Part dummyPart = session_.__FindOrOpen(DummyPath)
    #              ufsession_.Ui.SetPrompt($"Adding dummy file to {part.Leaf}.")
    #              __work_part_.ComponentAssembly.AddComponent(dummyPart, "Entire Part", "DUMMY", _Point3dOrigin,
    #                  _Matrix3x3Identity, 1, out _)
    #          }
    raise NotImplementedError()


def export_design_CheckAssemblyDummyFiles() -> None:
    #          public static void export_design_CheckAssemblyDummyFiles()
    #          {
    #              ufsession_.Ui.SetPrompt("Checking Dummy files exist.")

    #              if (__display_part_.ComponentAssembly.RootComponent == null)
    #                  return

    #              foreach (Component childOfStrip in __display_part_.ComponentAssembly.RootComponent.GetChildren())
    #              {
    #                  if (childOfStrip.IsSuppressed)
    #                      continue

    #                  if (!childOfStrip.__IsLoaded())
    #                      continue

    #                  if (!Regex.IsMatch(childOfStrip.DisplayName, RegexPressAssembly, RegexOptions.IgnoreCase))
    #                      continue

    #                  if (childOfStrip.GetChildren().Length == 0)
    #                      throw new InvalidOperationException(
    #                          $"A press exists in your assembly without any children. {childOfStrip.__AssemblyPathString()}")

    #                  switch (childOfStrip.GetChildren().Length)
    #                  {
    #                      case 1:
    #                          throw new InvalidOperationException(
    #                              $"A press exists in your assembly with only one child. Expecting a ram and a bolster. {childOfStrip.__AssemblyPathString()}")
    #                      case 2:
    #                          foreach (Component childOfPress in childOfStrip.GetChildren())
    #                          {
    #                              if (!childOfPress.__IsLoaded())
    #                                  throw new InvalidOperationException(
    #                                      $"The child of a press must be loaded. {childOfPress.__AssemblyPathString()}")

    #                              if (childOfPress.IsSuppressed)
    #                                  throw new InvalidOperationException(
    #                                      $"The child of a press cannot be suppressed. {childOfPress.__AssemblyPathString()}")

    #                              if (childOfPress.GetChildren().Length != 0 && childOfPress.GetChildren()
    #                                      .Select(component => component)
    #                                      .Any(component => !component.IsSuppressed && component.Prototype is Part))
    #                                  continue

    #                              throw new InvalidOperationException(
    #                                  $"The child of a bolster or ram under a press must be the Dummy file: {DummyPath}. {childOfPress.__AssemblyPathString()}")
    #                          }

    #                          break
    #                  }
    #              }
    #          }
    raise NotImplementedError()


def export_design_GetReports(ctsJobNumber: str) -> object:
    # return (from directory in Directory.GetDirectories("X:\\")
    #         let directoryName = Path.GetFileName(directory)
    #         where directoryName != null
    #         // sql
    #         let match = new Regex("^Reports-([0-9]{4})-([0-9]{4})$").Match(directoryName)
    #         where match.Success
    #         let startRange = int.Parse(match.Groups[1].Value)
    #         let endRange = int.Parse(match.Groups[2].Value)
    #         let jobNumber = int.Parse(ctsJobNumber)
    #         where startRange <= jobNumber && jobNumber <= endRange
    #         from report in Directory.GetFiles(directory, "*.7z")
    #         let fileName = Path.GetFileNameWithoutExtension(report)
    #         where fileName.StartsWith(ctsJobNumber)
    #         select report).ToArray()
    raise NotImplementedError()


def export_design_SortPartsForExport() -> None:
    #          public static IDictionary<string, ISet<Part>> export_design_SortPartsForExport(IEnumerable<Part> validParts)
    #          {
    #              Regex detailRegex = new Regex(RegexDetail, RegexOptions.IgnoreCase)

    #              IDictionary<string, ISet<Part>> exportDict = new Dictionary<string, ISet<Part>>
    #          {
    #              { "PDF_4-VIEW", new HashSet<Part>() },
    #              { "STP_DETAIL", new HashSet<Part>() },
    #              { "DWG_BURNOUT", new HashSet<Part>() },
    #              { "STP_999", new HashSet<Part>() },
    #              { "STP_SEE3D", new HashSet<Part>() },
    #              { "X_T_CASTING", new HashSet<Part>() },
    #              { "X_T", new HashSet<Part>() }
    #          }

    #              foreach (Part part in validParts)
    #              {
    #                  Match match = detailRegex.Match(part.Leaf)

    #                  if (!match.Success)
    #                      continue

    #                  if (part.Leaf.__IsAssemblyHolder())
    #                      continue

    #                  if (part.Leaf.EndsWith("000"))
    #                      continue

    #                  if (part.__HasDrawingSheet("4-VIEW"))
    #                      exportDict["PDF_4-VIEW"].Add(part)

    #                  if (part.__HasDrawingSheet("BURNOUT"))
    #                      exportDict["DWG_BURNOUT"].Add(part)

    #                  if (part.__IsSee3DData())
    #                      exportDict["STP_SEE3D"].Add(part)

    #                  if (part.__Is999())
    #                      exportDict["STP_999"].Add(part)

    #                  if (part.__IsCasting())
    #                      exportDict["X_T_CASTING"].Add(part)

    #                  if (part.__HasReferenceSet("BODY"))
    #                      exportDict["X_T"].Add(part)
    #              }

    #              return exportDict
    #          }
    raise NotImplementedError()


def export_design_UpdateParts() -> None:
    #          public static void export_design_UpdateParts(
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
    #                      new HashSet<Part>(selected_components.Select(__c => __c.Prototype).OfType<Part>())

    #                  ISet<Part> partsToUpdate = new HashSet<Part>()

    #                  if (isRto || pdf4Views || stpDetails)
    #                      foreach (Part part in partsWith4ViewsNoAssemblyHolders)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part)

    #                  if (isRto || dwgBurnout)
    #                      foreach (Part part in burnoutParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part)

    #                  if (isRto || print4Views)
    #                      foreach (Part part in partsWith4Views)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part)

    #                  if (isRto || paraCasting)
    #                      foreach (Part part in castingParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part)

    #                  if (isRto || stp999)
    #                      foreach (Part part in nine99Parts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part)

    #                  if (isRto || stpSee3DData)
    #                      foreach (Part part in see3DDataParts)
    #                          if (selected_parts.Contains(part))
    #                              partsToUpdate.Add(part)

    #                  if (partsToUpdate.Count > 0)
    #                      UpdateParts(partsToUpdate.ToArray())
    #              }
    #          }
    raise NotImplementedError()


def export_design_ZipupDirectories() -> None:
    #          public static void export_design_ZipupDirectories(string sevenZip, IEnumerable<string> directoriesToExport, string zipPath)
    #          {
    #              try
    #              {
    #                  // Constructs the arguments that deletes the sub data folders in the newly created assembly zip folderWithCtsNumber.
    #                  string arguments = $"d \"{zipPath}\" -r {directoriesToExport.Select(Path.GetFileName).Where(dir => dir != null).Aggregate("", (s1, s2) => $"{s1} \"{s2}\"")}"

    #                  // Starts the actual delete process.
    #                  Process deleteProcess = Process.Start(sevenZip, arguments)

    #                  // Waits for the {deleteProcess} to finish.
    #                  deleteProcess?.WaitForExit()
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException()
    #              }
    #          }
    raise NotImplementedError()


def export_design_MoveSimReport(folder, exportDirectory: str) -> None:
    # if (!folder.is_cts_job())
    #     return
    # if (GetReports(folder.CtsNumber).Length != 0)
    #     foreach (string report in GetReports(folder.CtsNumber))
    #         string reportName = Path.GetFileName(report)
    #         if (reportName == null)
    #             continue
    #         string exportedReportPath = $"{exportDirectory}\\{reportName}"
    #         if (File.Exists(exportedReportPath))
    #             print($"Sim report \"{exportedReportPath}\" already exists.")
    #             continue
    #         File.Copy(report, exportedReportPath)
    # else
    #     print("Unable to find a sim report to transfer.")
    raise NotImplementedError()


def export_design_UpdateParts(parts: List[Part]) -> None:
    # Part[] validParts = parts.Where(part => !part.Leaf.__IsAssemblyHolder()).Distinct(new EqualityLeaf())
    #     .ToArray()

    # for (int i = 0 i < validParts.Length i++)
    #         string report = $"Updating: {i + 1} of {validParts.Length}. "
    #         Part part = validParts[i]
    #         ufsession_.Ui.SetPrompt($"{report}Setting Display Part to {part.Leaf}. ")
    #         __display_part_ = part
    #         __work_part_ = __display_part_
    #         if (part.__IsCasting() && !(part.ComponentAssembly.RootComponent is null))
    #             # If it is a casting then it cannot contain a child that is a lift lug and set to entire part.
    #             if ((from child in part.ComponentAssembly.RootComponent.GetChildren()
    #                 where child.Prototype is Part
    #                 where child.__Prototype().FullPath.Contains("LiftLugs")
    #                 where child.ReferenceSet != RefsetEmpty
    #                 select child)
    #                 .Any(child => child.ReferenceSet == RefsetEntirePart))
    #                 print(
    #                     $"Casting part {__display_part_.Leaf} contains a Lift Lug that is set to Entire Part. Casting Part cannot be made.")
    #         ufsession_.Ui.SetPrompt($"{report}Setting layers in {part.Leaf}.")
    #         SetLayers()
    #         ufsession_.Ui.SetPrompt($"{report}Finding DisplayableObjects in {part.Leaf}.")
    #         List<DisplayableObject> objects = new List<DisplayableObject>()
    #         foreach (int layer in Layers)
    #             objects.AddRange(__display_part_.Layers.GetAllObjectsOnLayer(layer)
    #                 .OfType<DisplayableObject>())
    #         ufsession_.Ui.SetPrompt($"{report}Unblanking objects in {part.Leaf}.")
    #         session_.DisplayManager.UnblankObjects(objects.ToArray())
    #         foreach (DraftingView view in __display_part_.DraftingViews)
    #             view.Update()
    #         ufsession_.Ui.SetPrompt($"{report}Switching back to modeling in {part.Leaf}.")
    #         session_.ApplicationSwitchImmediate("UG_APP_MODELING")
    #         __work_part_.Drafting.ExitDraftingApplication()
    #         ufsession_.Ui.SetPrompt($"{report}Saving {part.Leaf}.")
    #         part.__Save()
    raise NotImplementedError()


def export_design_SetUpStrip(folder) -> None:
    #          {
    #              try
    #              {
    #                  string strip_010 = folder.file_strip("010")

    #                  if (!File.Exists(strip_010))
    #                      return

    #                  Part op010Strip = session_.__FindOrOpen(strip_010)

    #                  SetLayersInBlanksAndLayoutsAndAddDummies(op010Strip)

    #                  CheckAssemblyDummyFiles()

    #                  op010Strip.__Save()
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException()
    #              }
    #          }
    raise NotImplementedError()


def export_design_ErrorCheck() -> None:
    #          public static void export_design_ErrorCheck(bool isRto, bool zipAssembly, IEnumerable<string> expectedFiles)
    #          {
    #              string[] enumerable = expectedFiles as string[] ?? expectedFiles.ToArray()

    #              int fileCreatedCount = enumerable.Where(File.Exists).Count()

    #              print($"Created {fileCreatedCount} file(s).")

    #              if (!isRto && !zipAssembly)
    #                  print(
    #                      "Created files will have to be manually moved to outgoingData folderWithCtsNumber if that is desired. (Example: RTO)")

    #              List<string> filesThatWereNotCreated = enumerable.Where(s => !File.Exists(s)).ToList()

    #              List<Tuple<string, string>> errorList = new List<Tuple<string, string>>()

    #              foreach (string file in filesThatWereNotCreated)
    #              {
    #                  string extension = Path.GetExtension(file)

    #                  if (extension == null)
    #                      continue

    #                  string errorFilePath = file.Replace(extension, ".err")

    #                  if (File.Exists(errorFilePath))
    #                  {
    #                      string[] fileContents = File.ReadAllLines(errorFilePath)

    #                      errorList.Add(new Tuple<string, string>(file, fileContents[0]))

    #                      File.Delete(errorFilePath)
    #                  }
    #                  else
    #                  {
    #                      errorList.Add(new Tuple<string, string>(file, "Unknown error."))
    #                  }
    #              }

    #              if (errorList.Count <= 0)
    #                  return

    #              print("Files that were not created.")

    #              errorList.ForEach(print)
    #          }
    raise NotImplementedError()


def export_design_Print4Views(allParts) -> None:
    # bool IsNotAssembly(Part part)
    # {
    #     string name = Path.GetFileNameWithoutExtension(part.FullPath)

    #     if (name == null)
    #         return false

    #     name = name.ToLower()

    #     if (name.EndsWith("000") || name.EndsWith("lsh") || name.EndsWith("ush") || name.EndsWith("lwr") ||
    #         name.EndsWith("upr"))
    #         return false

    #     return !name.Contains("lsp") && !name.Contains("usp")
    # # }
    # List<Part> parts = allParts
    #     .Where(part => Regex.IsMatch(part.Leaf, RegexDetail, RegexOptions.IgnoreCase))
    #     .Where(IsNotAssembly)
    #     .Where(part => part.DraftingDrawingSheets.ToArray().Any(__d => __d.Name.ToUpper() == "4-VIEW"))
    #     .ToList()
    # parts.Sort((part1, part2) => string.Compare(part1.Leaf, part2.Leaf, StringComparison.Ordinal))
    # for (int i = 0 i < parts.Count i++)
    #     Part part = parts[i]
    #     ufsession_.Ui.SetPrompt($"{i + 1} of {parts.Count}. Printing 4-VIEW of {part.Leaf}.")
    #     __display_part_ = part
    #     __work_part_ = __display_part_
    #     printBuilder = __work_part_.PlotManager.CreatePrintBuilder()
    #     using (new Destroyer(printBuilder))
    #         printBuilder.Copies = 1
    #         printBuilder.ThinWidth = 1.0
    #         printBuilder.NormalWidth = 2.0
    #         printBuilder.ThickWidth = 3.0
    #         printBuilder.Output = PrintBuilder.OutputOption.WireframeBlackWhite
    #         printBuilder.ShadedGeometry = true
    #         DrawingSheet drawingSheet = __work_part_.DraftingDrawingSheets.FindObject("4-VIEW")
    #         drawingSheet.Open()
    #         printBuilder.SourceBuilder.SetSheets(new NXObject[] { drawingSheet })
    #         printBuilder.PrinterText = "\\\\ctsfps1.cts.toolingsystemsgroup.com\\CTS Office MFC"
    #         printBuilder.Orientation = PrintBuilder.OrientationOption.Landscape
    #         printBuilder.Paper = PrintBuilder.PaperSize.Letter
    #         printBuilder.Commit()
    raise NotImplementedError()


def export_design_MoveStocklist() -> None:
    #          public static void export_design_MoveStocklist(GFolder folder, string topDisplayName, string exportDirectory)
    #          {
    #              try
    #              {
    #                  string stocklist = (from file in Directory.GetFiles(folder.DirStocklist)
    #                                      let name = Path.GetFileNameWithoutExtension(file)
    #                                      where name != null
    #                                      where name.EndsWith($"{topDisplayName}-stocklist")
    #                                      select file).SingleOrDefault()

    #                  if (stocklist is null)
    #                  {
    #                      print($"Could not find a stocklist named: {topDisplayName}-stocklist")
    #                      return
    #                  }

    #                  File.Copy(stocklist, $"{exportDirectory}\\{Path.GetFileName(stocklist)}")
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException()
    #              }
    #          }
    raise NotImplementedError()


def export_design_AssemblyExportDesignDataPdf() -> None:
    #          public static void export_design_AssemblyExportDesignDataPdf(Part part, string drawingSheetName, string filePath)
    #          {
    #              string directory = Path.GetDirectoryName(filePath)

    #              if (!filePath.EndsWith(".pdf"))
    #                  throw new InvalidOperationException("File path for PDF must end with \".pdf\".")

    #              if (File.Exists(filePath))
    #                  throw new ArgumentOutOfRangeException("output_path", "PDF \"" + filePath + "\" already exists.")

    #              //We can use SingleOrDefault here because NX will prevent the naming of two drawing sheets the exact same string.
    #              DrawingSheet sheet = part.DrawingSheets
    #                                       .ToArray()
    #                                       .SingleOrDefault(drawingSheet => drawingSheet.Name == drawingSheetName)
    #                                   ??
    #                                   throw new ArgumentException(
    #                                       $@"Part ""{part.Leaf}"" does not have a sheet named ""{drawingSheetName}"".",
    #                                       "drawingSheetName")

    #              __display_part_ = part
    #              session_.__SetDisplayToWork()
    #              SetLayers()

    #              PrintPDFBuilder pdfBuilder = part.PlotManager.CreatePrintPdfbuilder()

    #              using (session_.__UsingBuilderDestroyer(pdfBuilder))
    #              {
    #                  // sql
    #                  pdfBuilder.Scale = 1.0
    #                  pdfBuilder.Size = PrintPDFBuilder.SizeOption.ScaleFactor
    #                  pdfBuilder.OutputText = PrintPDFBuilder.OutputTextOption.Polylines
    #                  pdfBuilder.Units = PrintPDFBuilder.UnitsOption.English
    #                  pdfBuilder.XDimension = 8.5
    #                  pdfBuilder.YDimension = 11.0
    #                  pdfBuilder.RasterImages = true
    #                  pdfBuilder.Colors = PrintPDFBuilder.Color.BlackOnWhite
    #                  pdfBuilder.Watermark = ""
    #                  UFSession.GetUFSession().Draw.IsObjectOutOfDate(sheet.Tag, out bool flag)

    #                  if (flag)
    #                  {
    #                      UFSession.GetUFSession().Draw.UpdOutOfDateViews(sheet.Tag)
    #                      part.__Save()
    #                  }

    #                  sheet.Open()
    #                  pdfBuilder.SourceBuilder.SetSheets(new NXObject[] { sheet })
    #                  pdfBuilder.Filename = filePath
    #                  pdfBuilder.Commit()
    #              }
    #          }
    raise NotImplementedError()


def export_design_AssemblyExportDesignDataStp() -> None:
    #          public static void export_design_AssemblyExportDesignDataStp(string partPath, string output_path, string settings_file)
    #          {
    #              try
    #              {
    #                  if (!output_path.EndsWith(".stp"))
    #                      throw new InvalidOperationException("File path for STP must end with \".stp\".")

    #                  if (File.Exists(output_path))
    #                      throw new ArgumentOutOfRangeException("output_path", "STP \"" + output_path + "\" already exists.")

    #                  if (!File.Exists(partPath))
    #                      throw new FileNotFoundException("Could not find file location \"" + partPath + "\".")

    #                  session_.__FindOrOpen(partPath)

    #                  StepCreator stepCreator = Session.GetSession().DexManager.CreateStepCreator()

    #                  using (session_.__UsingBuilderDestroyer(stepCreator))
    #                  {
    #                      // sql
    #                      stepCreator.ExportAs = StepCreator.ExportAsOption.Ap214
    #                      stepCreator.SettingsFile = settings_file
    #                      stepCreator.ObjectTypes.Solids = true
    #                      stepCreator.OutputFile = output_path
    #                      stepCreator.BsplineTol = 0.0254
    #                      stepCreator.ObjectTypes.Annotations = true
    #                      stepCreator.ExportFrom = StepCreator.ExportFromOption.ExistingPart
    #                      stepCreator.InputFile = partPath
    #                      stepCreator.FileSaveFlag = false
    #                      stepCreator.LayerMask = "1, 96"
    #                      stepCreator.ProcessHoldFlag = true
    #                      stepCreator.Commit()
    #                  }

    #                  string switchFilePath = output_path.Replace(".stp", ".log")

    #                  if (File.Exists(switchFilePath))
    #                      File.Delete(switchFilePath)
    #              }
    #              catch (Exception ex)
    #              {
    #                  ex.__PrintException()
    #              }
    #          }
    raise NotImplementedError()


def export_design_AssemblyExportDesignDataDwg() -> None:
    #          public static void export_design_AssemblyExportDesignDataDwg(string partPath, string drawingSheetName, string filePath)
    #          {
    #              string directory = Path.GetDirectoryName(filePath)

    #              if (File.Exists(filePath))
    #                  throw new ArgumentOutOfRangeException("output_path", "DWG \"" + filePath + "\" already exists.")

    #              Part part = session_.__FindOrOpen(partPath)

    #              DrawingSheet sheet = part.DrawingSheets
    #                                       .ToArray()
    #                                       .SingleOrDefault(drawingSheet => drawingSheet.Name == drawingSheetName)
    #                                   ??
    #                                   throw new ArgumentException(
    #                                       $"Part \"{part.Leaf}\" does not have a sheet named \"{drawingSheetName}\".",
    #                                       "drawingSheetName")

    #              UFSession.GetUFSession().Draw.IsObjectOutOfDate(sheet.Tag, out bool flag)

    #              if (flag)
    #              {
    #                  SetLayers()
    #                  UFSession.GetUFSession().Draw.UpdOutOfDateViews(sheet.Tag)
    #                  part.__Save()
    #              }

    #              DxfdwgCreator dxfdwgCreator1 = session_.DexManager.CreateDxfdwgCreator()
    #              using (session_.__UsingBuilderDestroyer(dxfdwgCreator1))
    #              {
    #                  // sql
    #                  dxfdwgCreator1.ExportData = DxfdwgCreator.ExportDataOption.Drawing
    #                  dxfdwgCreator1.AutoCADRevision = DxfdwgCreator.AutoCADRevisionOptions.R2004
    #                  dxfdwgCreator1.ViewEditMode = true
    #                  dxfdwgCreator1.FlattenAssembly = true
    #                  dxfdwgCreator1.SettingsFile = "C:\\Program Files\\Siemens\\NX 11.0\\dxfdwg\\dxfdwg.def"
    #                  dxfdwgCreator1.ExportFrom = DxfdwgCreator.ExportFromOption.ExistingPart
    #                  dxfdwgCreator1.OutputFileType = DxfdwgCreator.OutputFileTypeOption.Dwg
    #                  dxfdwgCreator1.ObjectTypes.Curves = true
    #                  dxfdwgCreator1.ObjectTypes.Annotations = true
    #                  dxfdwgCreator1.ObjectTypes.Structures = true
    #                  dxfdwgCreator1.FlattenAssembly = false
    #                  dxfdwgCreator1.ExportData = DxfdwgCreator.ExportDataOption.Drawing
    #                  dxfdwgCreator1.InputFile = part.FullPath
    #                  dxfdwgCreator1.ProcessHoldFlag = true
    #                  dxfdwgCreator1.OutputFile = filePath
    #                  dxfdwgCreator1.WidthFactorMode = DxfdwgCreator.WidthfactorMethodOptions.AutomaticCalculation
    #                  dxfdwgCreator1.LayerMask = "1-256"
    #                  dxfdwgCreator1.DrawingList = drawingSheetName
    #                  dxfdwgCreator1.Commit()
    #              }

    #              string switchFilePath = filePath.Replace(".dwg", ".log")

    #              if (File.Exists(switchFilePath))
    #                  File.Delete(switchFilePath)
    #          }
    #      }
    #  }
    raise NotImplementedError()
