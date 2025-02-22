class UFuncAddPierceComponents:
    #     public partial class AddPierceComponents : _UFuncForm
    #     {
    #         private static List<Tuple<Component, Face>> _addedComponents;

    #         public AddPierceComponents()
    #         {
    #             InitializeComponent();
    #         }

    #         internal static string PunchDetail { get; set; }

    #         internal static string ButtonDetail { get; set; }

    #         internal static string RetainerDetail { get; set; }

    #         private void btnSelect_Click(object sender, EventArgs e)
    #         {
    #             try
    #             {
    #                 Hide();

    #                 #region Revision • 1.1 – 2017 / 11 / 28

    #                 string[] controls = session_.Parts.ToArray().Select(part => part.FullPath)
    #                     .Where(s => s.Contains("strip-control")).ToArray();
    #                 switch (controls.Length)
    #                 {
    #                     case 0:
    #                         print("There is no strip control loaded. Please load one before continuing.");
    #                         return;
    #                     case 1:
    #                         break;
    #                     default:
    #                         print("More than one strip control is loaded:");
    #                         controls.ToList().ForEach(print);
    #                         return;
    #                 }

    #                 #endregion

    #                 ButtonDetail = txtButton.Text;
    #                 PunchDetail = txtPunch.Text;
    #                 RetainerDetail = txtRetainer.Text;
    #                 using (session_.__UsingDisplayPartReset())
    #                 {
    #                     if (chkAssembly.Checked)
    #                         SameAssembly(rdoMetric.Checked, chkButton.Checked, chkPunch.Checked, chkRetainer.Checked);
    #                     else
    # #pragma warning disable CS0612 // Type or member is obsolete
    #                         DifferentAssemblies(rdoMetric.Checked, chkButton.Checked, chkPunch.Checked,
    #                             chkRetainer.Checked);
    # #pragma warning restore CS0612 // Type or member is obsolete
    #                 }
    #             }
    #             catch (Exception ex)
    #             {
    #                 ex.__PrintException();
    #             }
    #             finally
    #             {
    #                 Show();
    #             }
    #         }

    #         public static string GetNextDetailNumber(Part snapUspLsp)
    #         {
    #             string detailDirectory = Path.GetDirectoryName(snapUspLsp.FullPath);
    #             string partLeaf = snapUspLsp.Leaf.ToLower();
    #             Regex shortRegex = new Regex("^([0-9]+)-([0-9]{3,})-(lsp|usp)([0-9]{1})$");
    #             Match match = shortRegex.Match(partLeaf);
    #             if (match.Success)
    #             {
    #                 string customerJobNumber = match.Groups[1].Value;
    #                 string partOp = match.Groups[2].Value;
    #                 string uspLsp = match.Groups[3].Value;
    #                 int uspLspOp = int.Parse(match.Groups[4].Value);
    #                 bool isLower = uspLsp == "lsp";
    #                 int detailNumber = isLower
    #                     ? GetLspDetailNumberShort(uspLspOp)
    #                     : GetUspDetailNumberShort(uspLspOp);
    #                 string newDisplayName;
    #                 do
    #                 {
    #                     newDisplayName = $"{customerJobNumber}-{partOp}-{detailNumber++}";

    #                     if (snapUspLsp.ComponentAssembly.RootComponent.GetChildren()
    #                         .Any(component => component.DisplayName == newDisplayName))
    #                         continue;

    #                     string newFullPath = $"{detailDirectory}\\{newDisplayName}.prt";

    #                     if (File.Exists(newFullPath))
    #                         continue;

    #                     if (isLower && detailNumber > 499)
    #                         throw new Exception("Exceeded the detail numbers for the Lower");

    #                     if (detailNumber > 990)
    #                         throw new Exception("Exceeded the detail numbers for the Upper");

    #                     return newFullPath;
    #                 }
    #                 while (true);
    #             }

    #             Regex longRegex = new Regex("^([0-9]{4,5})-([0-9]{3,})-(lsp|usp)([0-9]{3})$");
    #             match = longRegex.Match(partLeaf);
    #             if (!match.Success) throw new ArgumentException("Part is not a valid Usp or Lsp.", nameof(snapUspLsp));
    #             {
    #                 string customerJobNumber = match.Groups[1].Value;
    #                 string partOp = match.Groups[2].Value;
    #                 string uspLsp = match.Groups[3].Value;
    #                 int uspLspOp = int.Parse(match.Groups[4].Value);
    #                 bool isLower = uspLsp == "lsp";
    #                 int detailNumber = isLower
    #                     ? GetLspDetailNumberLong(uspLspOp)
    #                     : GetUspDetailNumberLong(uspLspOp);
    #                 string newDisplayName;
    #                 do
    #                 {
    #                     newDisplayName = $"{customerJobNumber}-{partOp}-{detailNumber++}";

    #                     if (snapUspLsp.ComponentAssembly.RootComponent.GetChildren()
    #                         .Any(component => component.DisplayName == newDisplayName))
    #                         continue;

    #                     string newFullPath = $"{detailDirectory}\\{newDisplayName}.prt";

    #                     if (File.Exists(newFullPath))
    #                         continue;

    #                     if (isLower && detailNumber > 499)
    #                         throw new Exception("Exceeded the detail numbers for the Lower");

    #                     if (detailNumber > 990)
    #                         throw new Exception("Exceeded the detail numbers for the Upper");

    #                     return newFullPath;
    #                 }
    #                 while (true);
    #             }
    #         }

    #         /// <summary>
    #         ///     The path to the "Smart Button Metric.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartButtonMetric => "G:\\0Library\\Button\\Smart Button Metric.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Button English.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartButtonEnglish => "G:\\0Library\\Button\\Smart Button English.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Punch Metric.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartPunchMetric => "G:\\0Library\\PunchPilot\\Metric\\Smart Punch Metric.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Punch English.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartPunchEnglish => "G:\\0Library\\PunchPilot\\English\\Smart Punch English.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Ball Lock Retainer Metric.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartBallLockRetainerMetric =>
    #             "G:\\0Library\\Retainers\\Metric\\Smart Ball Lock Retainer Metric.prt";

    #         /// <summary>
    #         ///     The path to the "Smart Ball Lock Retainer English.prt" file in G:\\0Library.
    #         /// </summary>
    #         public static string SmartBallLockRetainerEnglish =>
    #             "G:\\0Library\\Retainers\\English\\Smart Ball Lock Retainer English.prt";

    #         /// <summary>
    #         ///     Returns the name of the reference set to be used for AddPierceComponents.
    #         /// </summary>
    #         public static string SlugRefsetName => "SLUG BUTTON ALIGN";

    #         // ReSharper disable once StringLiteralTypo
    #         public static string RetainerAlignPunchFaceName => "ALIGNPUNCH";

    #         // ReSharper disable once StringLiteralTypo
    #         public static string PunchTopFaceName => "PUNCHTOPFACE";

    #         public static string PiercedP => "PIERCED_P";

    #         public static string PiercedW => "PIERCED_W";

    #         public static string PiercedType => "PIERCED_TYPE";

    #         public static Regex PiercedFaceRegex => new Regex("^PIERCED_([0-9]{1,})$");

    #         public static int GetUspDetailNumberShort(int number)
    #         {
    #             switch (number)
    #             {
    #                 case 1:
    #                     return 600;
    #                 case 2:
    #                     return 700;
    #                 case 3:
    #                     return 800;
    #                 case 4:
    #                     return 900;
    #                 case 5:
    #                     return 650;
    #                 case 6:
    #                     return 750;
    #                 case 7:
    #                     return 850;
    #                 case 8:
    #                     return 950;
    #                 case 9:
    #                     return 675;
    #                 case 10:
    #                     return 775;
    #                 case 11:
    #                     return 875;
    #                 case 12:
    #                     return 975;
    #                 case 13:
    #                     return 680;
    #                 case 14:
    #                     return 780;
    #                 case 15:
    #                     return 880;
    #                 default:
    #                     return 881;
    #             }
    #         }

    #         public static int GetLspDetailNumberShort(int number)
    #         {
    #             switch (number)
    #             {
    #                 case 1:
    #                     return 100;
    #                 case 2:
    #                     return 200;
    #                 case 3:
    #                     return 300;
    #                 case 4:
    #                     return 400;
    #                 case 5:
    #                     return 150;
    #                 case 6:
    #                     return 250;
    #                 case 7:
    #                     return 350;
    #                 case 8:
    #                     return 450;
    #                 case 9:
    #                     return 175;
    #                 case 10:
    #                     return 275;
    #                 case 11:
    #                     return 375;
    #                 case 12:
    #                     return 475;
    #                 case 13:
    #                     return 180;
    #                 case 14:
    #                     return 280;
    #                 case 15:
    #                     return 380;
    #                 default:
    #                     return 381;
    #             }
    #         }

    #         public static int GetUspDetailNumberLong(int number)
    #         {
    #             switch (number)
    #             {
    #                 case 10:
    #                     return 600;
    #                 case 20:
    #                     return 700;
    #                 case 30:
    #                     return 800;
    #                 case 40:
    #                     return 900;
    #                 case 50:
    #                     return 650;
    #                 case 60:
    #                     return 750;
    #                 case 70:
    #                     return 850;
    #                 case 80:
    #                     return 950;
    #                 case 90:
    #                     return 675;
    #                 case 100:
    #                     return 775;
    #                 case 110:
    #                     return 875;
    #                 case 120:
    #                     return 975;
    #                 case 130:
    #                     return 680;
    #                 case 140:
    #                     return 780;
    #                 case 150:
    #                     return 880;
    #                 default:
    #                     return 881;
    #             }
    #         }

    #         public static int GetLspDetailNumberLong(int number)
    #         {
    #             switch (number)
    #             {
    #                 case 10:
    #                     return 100;
    #                 case 20:
    #                     return 200;
    #                 case 30:
    #                     return 300;
    #                 case 40:
    #                     return 400;
    #                 case 50:
    #                     return 150;
    #                 case 60:
    #                     return 250;
    #                 case 70:
    #                     return 350;
    #                 case 80:
    #                     return 450;
    #                 case 90:
    #                     return 175;
    #                 case 100:
    #                     return 275;
    #                 case 110:
    #                     return 375;
    #                 case 120:
    #                     return 475;
    #                 case 130:
    #                     return 180;
    #                 case 140:
    #                     return 280;
    #                 case 150:
    #                     return 380;
    #                 default:
    #                     return 381;
    #             }
    #         }

    #         /// <summary>
    #         ///     Gets the current detail number of all the children of <paramref name="snapComponent" /> who passes the Regex
    #         ///     <see cref="Constants.Regex_Detail" />, or returns -1 if no valid children are found.
    #         /// </summary>
    #         /// <param name="snapComponent">The component.</param>
    #         /// <returns>The highest/current detail or -1 if <paramref name="snapComponent" /> doesn't have any child who are valid.</returns>
    #         public static int GetCurrentDetailNumberOfChildren(Component snapComponent)
    #         {
    #             int[] validDetailNumbers = snapComponent.GetChildren()
    #                 .Select(component => component.DisplayName)
    #                 .Select(s => Regex.Match(s, RegexDetail))
    #                 .Where(match => match.Success)
    #                 .Select(match => int.Parse(match.Groups[3].Value))
    #                 .ToArray();

    #             return validDetailNumbers.Length >= 0
    #                 ? -1
    #                 : validDetailNumbers.Max();
    #         }

    #         /// <summary>
    #         ///     Checks to see if a face is named properly for AddPierceComponents.
    #         /// </summary>
    #         /// <param name="snapFace">The face whose name is to be checked.</param>
    #         /// <remarks>
    #         ///     The integer that is tagged at the end of the face name will be used to find the
    #         ///     <see cref="NXOpen.Features. DatumCsys" /> that
    #         ///     is associated with the face.
    #         /// </remarks>
    #         /// <exception cref="ArgumentNullException">When <paramref name="snapFace" /> is null.</exception>
    #         /// <returns>True if the name of the face starts with "PIERCED_FACE_" followed immediately by a non-negative integer.</returns>
    #         public static bool IsFaceNameValid(Face snapFace)
    #         {
    #             if (snapFace == null) throw new ArgumentNullException(nameof(snapFace));
    #             return PiercedFaceRegex.IsMatch(snapFace.Name);
    #         }

    #         /// <summary>
    #         ///     Gets the integer used to find a <see cref="NXOpen.Features. DatumCsys" />.
    #         /// </summary>
    #         /// <param name="snapFace">The face to parse an integer from it's name.</param>
    #         /// <exception cref="ArgumentNullException">When <paramref name="snapFace" /> is null.</exception>
    #         /// <exception cref="FormatException">If <paramref name="snapFace" />.Name isn't valid.</exception>
    #         /// <returns>Returns integer that corresponds to a <see cref="NXOpen.Features. DatumCsys" />. </returns>
    #         public static int GetFaceNameInteger(Face snapFace)
    #         {
    #             if (snapFace == null) throw new ArgumentNullException(nameof(snapFace));
    #             Match match = PiercedFaceRegex.Match(snapFace.Name);
    #             if (!match.Success) throw new FormatException("\"" + snapFace.Name + "\" is invalid.");
    #             return int.Parse(match.Groups[1].Value);
    #         }

    #         /// <summary>
    #         ///     Creates a new a snapButton and adds it to the current __work_part_.
    #         /// </summary>
    #         /// <remarks>
    #         ///     Adds the snapButton using the <paramref name="csys" /> layer, Origin, and Orientation as parameters for the
    #         ///     added snapButton.
    #         /// </remarks>
    #         /// <param name="buttonUnit">The unit type of the added component.</param>
    #         /// <param name="csys">The csys whose parameters will be used for the added component.</param>
    #         /// <exception cref="ArgumentNullException"><paramref name="csys" /> is null.</exception>
    #         /// <returns>The added snapButton.</returns>
    #         public static Component AddButton(BasePart.Units buttonUnit, CoordinateSystem csys)
    #         {
    #             if (csys == null) throw new ArgumentNullException(nameof(csys));
    #             double multiplier;

    #             string buttonPath;
    #             switch (buttonUnit)
    #             {
    #                 case BasePart.Units.Inches:
    #                     buttonPath = SmartButtonEnglish;
    #                     multiplier = 1.0;
    #                     break;
    #                 case BasePart.Units.Millimeters:
    #                     buttonPath = SmartButtonMetric;
    #                     multiplier = 25.4;
    #                     break;
    #                 default:
    #                     throw new ArgumentOutOfRangeException(nameof(buttonUnit));
    #             }

    #             CartesianCoordinateSystem absCys = __display_part_.__CreateCsys();
    #             CartesianCoordinateSystem tempCsys = __display_part_.__CreateCsys(csys.Origin, csys.Orientation.Element);
    #             Point3d mappedOrigin = csys.Origin.__MapCsysToCsys(absCys, tempCsys);
    #             mappedOrigin = new Point3d(mappedOrigin.X, mappedOrigin.Y, mappedOrigin.Z + 6 / multiplier);
    #             Point3d newOrigin = mappedOrigin.__MapCsysToCsys(tempCsys, absCys);
    #             return __work_part_.ComponentAssembly.AddComponent(buttonPath, "ALIGN",
    #                 Path.GetFileNameWithoutExtension(buttonPath), newOrigin, csys.Orientation.Element, csys.Layer, out _);
    #         }

    #         public static Component AddPunch(BasePart.Units buttonUnit, CoordinateSystem csys)
    #         {
    #             if (csys == null) throw new ArgumentNullException(nameof(csys));
    #             string punchPath;
    #             switch (buttonUnit)
    #             {
    #                 case BasePart.Units.Inches:
    #                     punchPath = SmartPunchEnglish;
    #                     break;
    #                 case BasePart.Units.Millimeters:
    #                     punchPath = SmartPunchMetric;
    #                     break;
    #                 default:
    #                     throw new ArgumentOutOfRangeException(nameof(buttonUnit));
    #             }

    #             return AddComponent(punchPath, csys, "ALIGN");
    #         }

    #         public static Component AddRetainer(BasePart.Units buttonUnit, CoordinateSystem csys)
    #         {
    #             if (csys == null) throw new ArgumentNullException(nameof(csys));
    #             string retainerPath;
    #             switch (buttonUnit)
    #             {
    #                 case BasePart.Units.Inches:
    #                     retainerPath = SmartBallLockRetainerEnglish;
    #                     break;
    #                 case BasePart.Units.Millimeters:
    #                     retainerPath = SmartBallLockRetainerMetric;
    #                     break;
    #                 default:
    #                     throw new ArgumentOutOfRangeException(nameof(buttonUnit));
    #             }

    #             return AddComponent(retainerPath, csys, "MATE");
    #         }

    #         private static Component AddComponent(string path, CoordinateSystem csys, string referenceSet)
    #         {
    #             CartesianCoordinateSystem absCys = __display_part_.__CreateCsys();
    #             CartesianCoordinateSystem tempCsys = __display_part_.__CreateCsys(csys.Origin, csys.Orientation.Element);
    #             Point3d mappedOrigin = csys.Origin.__MapCsysToCsys(absCys, tempCsys);
    #             Point3d newOrigin = mappedOrigin.__MapCsysToCsys(tempCsys, absCys);

    #             return __work_part_.ComponentAssembly.AddComponent(
    #                 path,
    #                 referenceSet,
    #                 Path.GetFileNameWithoutExtension(path),
    #                 newOrigin,
    #                 csys.Orientation.Element,
    #                 csys.Layer,
    #                 out _);
    #         }

    #         private static bool IsUsp(Part snapPart)
    #         {
    #             return snapPart.Leaf.Contains("usp");
    #         }

    #         private static void GetPartPaths(bool isMetric, out string buttonPath, out string retainerPath,
    #             out string punchPath)
    #         {
    #             string directory = Path.GetDirectoryName(__display_part_.FullPath);

    #             var details = (from file in Directory.GetFiles(directory, "*.prt", SearchOption.TopDirectoryOnly)
    #                            where file.__IsDetail()
    #                            let detailNumber = file.__AskDetailNumber()
    #                            select new { file, detailNumber }).ToArray();

    #             if (string.IsNullOrEmpty(ButtonDetail))
    #             {
    #                 buttonPath = isMetric ? SmartButtonMetric : SmartButtonEnglish;
    #             }
    #             else
    #             {
    #                 var argDetail = details.SingleOrDefault(arg => arg.file == ButtonDetail)
    #                                 ??
    #                                 throw new InvalidOperationException("Could not find a detail with # \'" + ButtonDetail +
    #                                                                     "\' in folderWithCtsNumber \'" + directory + "\'.");

    #                 Part tempPart = session_.__FindOrOpen(argDetail.file);

    #                 if (!tempPart.HasUserAttribute("LIBRARY", NXObject.AttributeType.String, -1))
    #                     throw new InvalidOperationException("The selected part does not have a \'LIBRARY\' attribute.");

    #                 string expectedLibraryAttributeValue = Path.GetFileNameWithoutExtension(isMetric
    #                     ? SmartButtonMetric
    #                     : SmartButtonEnglish);
    #                 string libraryAttributeValue =
    #                     tempPart.GetUserAttributeAsString("LIBRARY", NXObject.AttributeType.String, -1);

    #                 if (expectedLibraryAttributeValue != libraryAttributeValue)
    #                     throw new InvalidOperationException(
    #                         $"The library attribute value {tempPart.Leaf} does not equal {expectedLibraryAttributeValue}.");

    #                 buttonPath = tempPart.FullPath;
    #             }

    #             if (string.IsNullOrEmpty(PunchDetail))
    #             {
    #                 punchPath = isMetric ? SmartPunchMetric : SmartPunchEnglish;
    #             }
    #             else
    #             {
    #                 var argDetail = details.SingleOrDefault(arg => arg.file == PunchDetail)
    #                                 ??
    #                                 throw new InvalidOperationException("Could not find a detail with # \'" + PunchDetail +
    #                                                                     "\' in folderWithCtsNumber \'" + directory + "\'.");

    #                 Part tempPart = session_.__FindOrOpen(argDetail.file);

    #                 if (!tempPart.HasUserAttribute("LIBRARY", NXObject.AttributeType.String, -1))
    #                     throw new InvalidOperationException("The selected part does not have a \'LIBRARY\' attribute.");

    #                 string expectedLibraryAttributeValue =
    #                     Path.GetFileNameWithoutExtension(isMetric
    #                         ? SmartPunchMetric
    #                         : SmartPunchEnglish);
    #                 string libraryAttributeValue =
    #                     tempPart.GetUserAttributeAsString("LIBRARY", NXObject.AttributeType.String, -1);

    #                 if (expectedLibraryAttributeValue != libraryAttributeValue)
    #                     throw new InvalidOperationException(
    #                         $"The library attribute value {tempPart.Leaf} does not equal {expectedLibraryAttributeValue}.");

    #                 punchPath = tempPart.FullPath;
    #             }

    #             if (string.IsNullOrEmpty(RetainerDetail))
    #             {
    #                 retainerPath = isMetric
    #                     ? SmartBallLockRetainerMetric
    #                     : SmartBallLockRetainerEnglish;
    #             }
    #             else
    #             {
    #                 var argDetail = details.SingleOrDefault(arg => arg.file == RetainerDetail)
    #                                 ??
    #                                 throw new InvalidOperationException("Could not find a detail with # \'" +
    #                                                                     RetainerDetail + "\' in folderWithCtsNumber \'" +
    #                                                                     directory + "\'.");

    #                 Part tempPart = session_.__FindOrOpen(argDetail.file);

    #                 if (!tempPart.HasUserAttribute("LIBRARY", NXObject.AttributeType.String, -1))
    #                     throw new InvalidOperationException("The selected part does not have a \'LIBRARY\' attribute.");

    #                 string expectedLibraryAttributeValue =
    #                     Path.GetFileNameWithoutExtension(isMetric
    #                         ? SmartBallLockRetainerMetric
    #                         : SmartBallLockRetainerEnglish);
    #                 string libraryAttributeValue =
    #                     tempPart.GetUserAttributeAsString("LIBRARY", NXObject.AttributeType.String, -1);

    #                 if (expectedLibraryAttributeValue != libraryAttributeValue)
    #                     throw new InvalidOperationException(
    #                         $"The library attribute value {tempPart.Leaf} does not equal {expectedLibraryAttributeValue}.");

    #                 retainerPath = tempPart.FullPath;
    #             }
    #         }

    #         private static void ConfirmStripControlAndEExpression()
    #         {
    #             string[] stripControls = session_.Parts
    #                 .OfType<Part>()
    #                 .Select(part => part.Leaf.ToLower())
    #                 .Where(s => s.Contains("strip-control"))
    #                 .ToArray();

    #             if (stripControls.Length < 1)
    #                 throw new InvalidOperationException("You need to have a strip control loaded.");

    #             string[] expressions = __display_part_.Expressions
    #                 .ToArray()
    #                 .Select(expression => expression.Name.ToLower())
    #                 .Where(s => s == "e")
    #                 .ToArray();

    #             if (expressions.Length < 1)
    #                 throw new InvalidOperationException("Unable to find an expression with the name of \'e\'.");
    #         }

    #         public static void SameAssembly(bool isMetric, bool addButton, bool addPunch, bool addRetainer)
    #         {
    #             ConfirmStripControlAndEExpression();
    #             _addedComponents = new List<Tuple<Component, Face>>();
    #             GetPartPaths(isMetric, out string buttonPath, out string retainerPath, out string punchPath);
    #             Regex uspLspRegex = new Regex("^[0-9]{4,5}-([0-9]{3})-[l|u]sp([0-9]{1,})$");
    #             string _display_part_DisplayName = Path.GetFileNameWithoutExtension(__display_part_.FullPath);
    #             if (_display_part_DisplayName == null) throw new NullReferenceException("_display_part_DisplayName");
    #             Match nameMatch = uspLspRegex.Match(_display_part_DisplayName);
    #             if (!nameMatch.Success)
    #                 throw new FormatException(_display_part_DisplayName + " is not a valid usp or lsp.");
    #             GFolder folder = GFolder.create_or_null(__work_part_);
    #             if (folder is null)
    #                 throw new InvalidOperationException("The current displayed part does not reside within a GFolder.");
    #             string op = nameMatch.Groups[1].Value;
    #             int uspLspNumberAsInteger = int.Parse(nameMatch.Groups[2].Value);
    #             Part uspLspPart = session_.__FindOrOpen(_display_part_DisplayName);

    #             /////////////////////////////////////////////
    #             /////////////////////////////////////////////

    #             __SetUndoMark(MarkVisibility.Visible, "FastClass");

    #             try
    #             {
    #                 Face[] faces = Ui.Selection.SelectManyFaces();

    #                 IDictionary<string, List<Face>> dictionaryShape =
    #                     faces.__ToILookIDict(face => face.GetStringUserAttribute("PIERCED_TYPE", -1));

    #                 foreach (string keyShape in dictionaryShape.Keys)
    #                 {
    #                     List<Face> shapeFaces = dictionaryShape[keyShape];
    #                     // Revision • 1.2 – 2017 / 12 / 07
    #                     IDictionary<double, List<Face>> dictionaryP = shapeFaces.__ToILookIDict(face =>
    #                         System.Math.Round(face.GetRealUserAttribute("PIERCED_P", -1), 4));
    #                     foreach (double keyP in dictionaryP.Keys)
    #                     {
    #                         List<Face> pFaces = dictionaryP[keyP];
    #                         // Revision • 1.2 – 2017 / 12 / 07
    #                         IDictionary<double, List<Face>> dictionaryW = pFaces.__ToILookIDict(face =>
    #                             System.Math.Round(face.GetRealUserAttribute("PIERCED_W", -1), 4));
    #                         foreach (double keyW in dictionaryW.Keys)
    #                         {
    #                             string partOfThePath = $"{folder.dir_op(op)}\\{folder.CustomerNumber}-{op}-";
    #                             int currentLowerDetailNumber =
    #                                 GetCurrentDetailNumberOfChildren(uspLspPart.__RootComponent());
    #                             if (currentLowerDetailNumber == -1)
    #                                 // Revision • 1.2 – 2017 / 12 / 07
    #                                 currentLowerDetailNumber = IsUsp(uspLspPart)
    #                                     ? !folder.is_cts_job()
    #                                         ? GetUspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetUspDetailNumberShort(uspLspNumberAsInteger)
    #                                     : !folder.is_cts_job()
    #                                         ? GetLspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetLspDetailNumberShort(uspLspNumberAsInteger);
    #                             string newButtonPath = buttonPath.StartsWith("G:\\0Library")
    #                                 ? GetNewPartPath(partOfThePath, buttonPath, currentLowerDetailNumber)
    #                                 : buttonPath;
    #                             string newRetainerPath = retainerPath.StartsWith("G:\\0Library")
    #                                 ? GetNewPartPath(partOfThePath, retainerPath, currentLowerDetailNumber)
    #                                 : retainerPath;
    #                             string newPunchPath = punchPath.StartsWith("G:\\0Library")
    #                                 ? GetNewPartPath(partOfThePath, punchPath, currentLowerDetailNumber)
    #                                 : punchPath;
    #                             foreach (Face faceW in dictionaryW[keyW])
    #                             {
    #                                 Component button = null, punch = null, retainer = null;
    #                                 Component layoutComponent = faceW.OwningComponent;
    #                                 string originalRefset = layoutComponent.ReferenceSet;
    #                                 layoutComponent.__ReferenceSet(SlugRefsetName);
    #                                 Expression expression = __display_part_.Expressions
    #                                     .ToArray()
    #                                     .SingleOrDefault(tempExpression => tempExpression.Name == "e");
    #                                 int layer = uspLspPart.Leaf.Contains("lsp") ? 1 : 101;

    #                                 if (addPunch)
    #                                     punch = AddComponentAndConstrain(faceW, newPunchPath, uspLspPart, "ALIGN", layer,
    #                                         expression);

    #                                 if (addRetainer)
    #                                     retainer = AddComponentAndConstrain(faceW, newRetainerPath, uspLspPart, "MATE",
    #                                         layer);

    #                                 if (addButton)
    #                                     button = AddComponentAndConstrain(faceW, newButtonPath, uspLspPart, "ALIGN", layer,
    #                                         expression);

    #                                 if (retainer != null && punch != null)
    #                                     ConstrainPunchAndRetainer(punch, retainer);

    #                                 List<Component> listComps = new List<Component>();

    #                                 if (button != null)
    #                                     listComps.Add(button);

    #                                 if (retainer != null)
    #                                     listComps.Add(retainer);

    #                                 if (punch != null)
    #                                     listComps.Add(punch);

    #                                 ChangeRefsets("BODY", listComps.ToArray());
    #                                 layoutComponent.__ReferenceSet(originalRefset);
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #             finally
    #             {
    # #pragma warning disable CS0612 // Type or member is obsolete
    #                 PrintResults(isMetric);
    # #pragma warning restore CS0612 // Type or member is obsolete
    #             }
    #         }

    #         [Obsolete]
    #         public static void DifferentAssemblies(bool isMetric, bool addButton, bool addPunch, bool addRetainer)
    #         {
    #             GFolder folder = GFolder.create_or_null(__work_part_)
    #                              ??
    #                              throw new InvalidOperationException(
    #                                  "The current work part does not reside within a job folder.");

    #             ConfirmStripControlAndEExpression();
    #             _addedComponents = new List<Tuple<Component, Face>>();
    #             GetPartPaths(isMetric, out string buttonPath, out string retainerPath, out string punchPath);

    #             string _display_part_DisplayName = Path.GetFileNameWithoutExtension(__display_part_.FullPath)
    #                                                ??
    #                                                throw new NullReferenceException("_display_part_DisplayName");

    #             Match nameMatch = Regex.Match(_display_part_DisplayName, RegexLspUsp);

    #             if (!nameMatch.Success)
    #                 throw new FormatException($"{_display_part_DisplayName} is not a valid usp or lsp.");

    #             string op = nameMatch.Groups["opNum"].Value;
    #             string uspLspNumberAsString = nameMatch.Groups["extraOpNum"].Value;
    #             int uspLspNumberAsInteger = int.Parse(uspLspNumberAsString);
    #             string lspName = $"{folder.CustomerNumber}-{op}-lsp{uspLspNumberAsString}";
    #             string uspName = $"{folder.CustomerNumber}-{op}-usp{uspLspNumberAsString}";
    #             BasePart lspPart = session_.Parts.ToArray().SingleOrDefault(part => part.FullPath.Contains(lspName));
    #             BasePart uspPart = session_.Parts.ToArray().SingleOrDefault(part => part.FullPath.Contains(uspName));

    #             if (addButton && lspPart == null)
    #                 throw new InvalidOperationException($"Could not find part \"{lspName}\" loaded in your session.");

    #             if ((addPunch || addRetainer) && uspPart == null)
    #                 throw new InvalidOperationException("Could not find part " + "\"" + uspName +
    #                                                     "\" loaded in your session.");

    #             /////////////////////////////////////////////
    #             /////////////////////////////////////////////

    #             __SetUndoMark(MarkVisibility.Visible, "FastClass");
    #             try
    #             {
    #                 Face[] faces = Ui.Selection.SelectManyFaces();

    #                 IDictionary<string, List<Face>> dictionaryShape =
    #                     faces.__ToILookIDict(face => face.GetStringUserAttribute("PIERCED_TYPE", -1));

    #                 foreach (string keyShape in dictionaryShape.Keys)
    #                 {
    #                     List<Face> shapeFaces = dictionaryShape[keyShape];
    #                     // Revision • 1.2 – 2017 / 12 / 01
    #                     IDictionary<double, List<Face>> dictionaryP = shapeFaces.__ToILookIDict(face =>
    #                         System.Math.Round(face.GetRealUserAttribute("PIERCED_P", -1), 4));
    #                     foreach (double keyP in dictionaryP.Keys)
    #                     {
    #                         List<Face> pFaces = dictionaryP[keyP];
    #                         // Revision • 1.2 – 2017 / 12 / 01
    #                         IDictionary<double, List<Face>> dictionaryW = pFaces.__ToILookIDict(face =>
    #                             System.Math.Round(face.GetRealUserAttribute("PIERCED_W", -1), 4));
    #                         foreach (double keyW in dictionaryW.Keys)
    #                         {
    #                             string partOfThePath = $"{folder.dir_op(op)}\\{folder.CustomerNumber}-{op}-";
    #                             string newPunchPath = null, newRetainerPath = null, newButtonPath = null;
    #                             if (lspPart != null)
    #                             {
    #                                 int currentLowerDetailNumber =
    #                                     GetCurrentDetailNumberOfChildren(lspPart.ComponentAssembly.RootComponent);
    #                                 if (currentLowerDetailNumber == -1)
    #                                     // Revision • 1.2 – 2017 / 12 / 07
    #                                     currentLowerDetailNumber = !folder.is_cts_job()
    #                                         ? GetLspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetLspDetailNumberShort(uspLspNumberAsInteger);
    #                                 newButtonPath = buttonPath.StartsWith("G:\\0Library")
    #                                     ? GetNewPartPath(partOfThePath, buttonPath, currentLowerDetailNumber)
    #                                     : buttonPath;
    #                             }

    #                             if (uspPart != null)
    #                             {
    #                                 int currentUpperDetailNumber =
    #                                     GetCurrentDetailNumberOfChildren(uspPart.ComponentAssembly.RootComponent);
    #                                 if (currentUpperDetailNumber == -1)
    #                                     // Revision • 1.2 – 2017 / 12 / 07
    #                                     currentUpperDetailNumber = !folder.is_cts_job()
    #                                         ? GetUspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetUspDetailNumberShort(uspLspNumberAsInteger);

    #                                 newRetainerPath = retainerPath.StartsWith("G:\\0Library")
    #                                     ? GetNewPartPath(partOfThePath, retainerPath, currentUpperDetailNumber)
    #                                     : retainerPath;
    #                                 currentUpperDetailNumber =
    #                                     GetCurrentDetailNumberOfChildren(uspPart.ComponentAssembly.RootComponent);
    #                                 if (currentUpperDetailNumber == -1)
    #                                     // Revision • 1.2 – 2017 / 12 / 07
    #                                     currentUpperDetailNumber = !folder.is_cts_job()
    #                                         ? GetUspDetailNumberLong(uspLspNumberAsInteger)
    #                                         : GetUspDetailNumberShort(uspLspNumberAsInteger);
    #                                 newPunchPath = punchPath.StartsWith("G:\\0Library")
    #                                     ? GetNewPartPath(partOfThePath, punchPath, currentUpperDetailNumber)
    #                                     : punchPath;
    #                             }

    #                             foreach (Face faceW in dictionaryW[keyW])
    #                             {
    #                                 Component button = null, punch = null, retainer = null;
    #                                 Component layoutComponent = faceW.OwningComponent;
    #                                 string originalRefset = layoutComponent.ReferenceSet;
    #                                 layoutComponent.__ReferenceSet(SlugRefsetName);
    #                                 Expression expression = __display_part_.Expressions
    #                                     .ToArray()
    #                                     .SingleOrDefault(tempExpression => tempExpression.Name == "e");

    #                                 if (addPunch)
    #                                     punch = AddComponentAndConstrain(faceW, newPunchPath, (Part)uspPart, "ALIGN", 101,
    #                                         expression);

    #                                 // Revision • 1.3 – 2017 / 12 / 28
    #                                 if (addRetainer)
    #                                     retainer = AddComponentAndConstrain(faceW, newRetainerPath, (Part)uspPart, "MATE",
    #                                         101);

    #                                 // Revision • 1.3 – 2017 / 12 / 28
    #                                 if (addButton)
    #                                     button = AddComponentAndConstrain(faceW, newButtonPath, (Part)lspPart, "ALIGN", 1,
    #                                         expression);

    #                                 if (retainer != null && punch != null)
    #                                     ConstrainPunchAndRetainer(punch, retainer);

    #                                 List<Component> listComps = new List<Component>();

    #                                 if (button != null)
    #                                     listComps.Add(button);

    #                                 if (retainer != null)
    #                                     listComps.Add(retainer);

    #                                 if (punch != null)
    #                                     listComps.Add(punch);

    #                                 ChangeRefsets("BODY", listComps.ToArray());
    #                                 layoutComponent.__ReferenceSet(originalRefset);
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #             finally
    #             {
    #                 PrintResults(isMetric);
    #             }
    #         }

    #         [Obsolete]
    #         private static void PrintResults(bool isMetric)
    #         {
    #             throw new NotImplementedException();
    #             //try
    #             //{
    #             //    print_("Results:");
    #             //    BasePart stripControl = session_.Parts.ToArray().Single(part => part.Leaf.Contains("strip-control"));
    #             //    Expression materialThicknessExp = stripControl.Expressions.ToArray()
    #             //        .SingleOrDefault(expression => expression.Name == "M");
    #             //    if (materialThicknessExp == null)
    #             //        print_("Unable to find Material Thickness.");
    #             //    else
    #             //        print_("Material Thickness (M): " + materialThicknessExp.RightHandSide);

    #             //    if (_addedComponents == null)
    #             //    {
    #             //        print_("  addedComponents was null");
    #             //        return;
    #             //    }

    #             //    if (_addedComponents.Count <= 0)
    #             //    {
    #             //        print_("  addedComponents was empty");
    #             //        return;
    #             //    }

    #             //    IOrderedEnumerable<Tuple<Component, Face>> trimmedTuples = _addedComponents
    #             //        .DistinctBy(tup => tup.Item1.DisplayName)
    #             //        .OrderBy(tuple => tuple, new Comparer());

    #             //    double divider = isMetric ? 1.0 : 25.4;

    #             //    foreach (Tuple<NXOpen.Assemblies.Component, NXOpen.Face> tuple in trimmedTuples)
    #             //    {
    #             //        const string circle = "Circle";
    #             //        const string roundedRectangle = "RoundedRectangle";
    #             //        double p = Math.Round(tuple.Item1.GetRealUserAttribute(PiercedP, -1) / divider, 4);
    #             //        double w = Math.Round(tuple.Item1.GetRealUserAttribute(PiercedW, -1) / divider, 4);
    #             //        string type = tuple.Item1.GetStringUserAttribute(PiercedType, -1);
    #             //        switch (type)
    #             //        {
    #             //            case circle:
    #             //                print_($"{tuple.Item1.DisplayName}, P = {p}");
    #             //                break;
    #             //            case roundedRectangle:
    #             //                double radius = tuple.Item2.GetEdges().Select(edge => Snap.NX.Edge.Wrap(edge.Tag)).OfType<Snap.NX.Edge.Arc>().First().Geometry.Radius;
    #             //                print_($"{tuple.Item1.DisplayName}, P = {p}, W = {w}, R = {radius}");
    #             //                break;
    #             //            default:
    #             //                print_($"{tuple.Item1.DisplayName}, P = {p}, W = {w}");
    #             //                break;
    #             //        }
    #             //    }
    #             //    throw new NotImplementedException();
    #             //}
    #             //catch (Exception ex)
    #             //{
    #             //    ex.__PrintException();
    #             //}
    #         }

    #         private static void ConstrainPunchAndRetainer(Component punch, Component retainer)
    #         {
    #             __display_part_ = (Part)punch.OwningComponent.Prototype;
    #             __work_part_ = __display_part_;
    #             Constraints.ConstrainFixPunch(punch);
    #             Constraints.ConstrainZAxes(__work_part_, punch, retainer);
    #             Constraints.ConstrainFaces(__work_part_, punch, retainer);
    #             Constraints.ConstrainAlignBallSetAndPlane(punch, retainer);
    #         }

    #         private static void ChangeRefsets(string refsetName, params Component[] components)
    #         {
    #             components?.Where(component => component != null).ToList()
    #                 .ForEach(component => component.__ReferenceSet(refsetName));
    #         }

    #         private static string GetNewPartPath(string partOfThePath, string originalPartPath,
    #             int currentUpperDetailNumber)
    #         {
    #             string newPath = "";
    #             for (int i = 0; i < 1000; i++)
    #             {
    #                 newPath = partOfThePath + (currentUpperDetailNumber + i) + ".prt";
    #                 if (File.Exists(newPath)) continue;
    #                 File.Copy(originalPartPath, newPath);
    #                 break;
    #             }

    #             return newPath;
    #         }

    #         public static Component AddComponentAndConstrain(
    #             Face snapFace,
    #             string path,
    #             Part part,
    #             string referenceSet,
    #             int layer,
    #             Expression zOffsetExpression = null)
    #         {
    #             __display_part_ = part;
    #             __work_part_ = __display_part_;
    #             snapFace.Unhighlight();
    #             int integer = GetFaceNameInteger(snapFace);

    #             // Revision • 1.2 – 2017 / 12 / 07
    #             Component layout = snapFace.OwningComponent;
    #             DatumAxis xAxis = layout.__Members().OfType<DatumAxis>()
    #                 .Single(axis => axis.Name == "PIERCED_AXIS_X_" + integer);
    #             DatumAxis yAxis = layout.__Members().OfType<DatumAxis>()
    #                 .Single(axis => axis.Name == "PIERCED_AXIS_Y_" + integer);
    #             DatumAxis zAxis = layout.__Members().OfType<DatumAxis>()
    #                 .Single(axis => axis.Name == "PIERCED_AXIS_Z_" + integer);
    #             Matrix3x3 orientation = xAxis.Direction.__ToMatrix3x3(yAxis.Direction);
    #             Point3d newOrigin = xAxis.Origin;
    #             if (zOffsetExpression != null)
    #                 newOrigin = new Point3d(xAxis.Origin.X, xAxis.Origin.Y, xAxis.Origin.Z + zOffsetExpression.Value);

    #             Component addedComponent = part.ComponentAssembly.AddComponent(
    #                 path,
    #                 referenceSet,
    #                 Path.GetFileNameWithoutExtension(path),
    #                 newOrigin,
    #                 orientation,
    #                 layer,
    #                 out _);

    #             addedComponent.SetUserAttribute(PiercedP, -1,
    #                 snapFace.GetStringUserAttribute(PiercedP, -1), NXOpen.Update.Option.Now);

    #             addedComponent.SetUserAttribute(PiercedW, -1,
    #                 snapFace.GetStringUserAttribute(PiercedW, -1), NXOpen.Update.Option.Now);

    #             addedComponent.SetUserAttribute(PiercedType, -1,
    #                 snapFace.GetStringUserAttribute(PiercedType, -1), NXOpen.Update.Option.Now);

    #             addedComponent.__ReferenceSet(referenceSet);

    #             using (new ReferenceSetReset(addedComponent))
    #             {
    #                 addedComponent.__ReferenceSet("BODY");
    #                 Part owningPart = addedComponent.OwningComponent.__Prototype();
    #                 ReferenceSet bodyReferenceSet = owningPart.__FindReferenceSetOrNull("BODY");
    #                 bodyReferenceSet?.AddObjectsToReferenceSet(new NXObject[] { addedComponent });
    #             }

    #             DatumAxis zAxisComponent = addedComponent.__Members()
    #                 .OfType<DatumAxis>()
    #                 .Single(axis => axis.Direction.__IsEqual(__Vector3dZ()));

    #             DisplayedConstraint constraint = Constraints.CreateAlign(__work_part_, zAxisComponent, zAxis);
    #             session_.__DeleteObjects(constraint);

    #             if (!addedComponent.GetStringUserAttribute("LIBRARY", -1).ToLower().Contains("retainer"))
    #                 _addedComponents.Add(new Tuple<Component, Face>(addedComponent, snapFace));

    #             return addedComponent;
    #         }

    #         [Obsolete]
    #         public static class Selection
    #         {
    #             // ReSharper disable once ReturnTypeCanBeEnumerable.Global
    #             [Obsolete]
    #             public static Face[] SelectFaces()
    #             {
    #                 //const string message = "Select Faces";
    #                 //const int scope = UFConstants.UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY;
    #                 //UFUi.SelInitFnT initialProcess = InitialProcess;
    #                 //IntPtr userData = IntPtr.Zero;
    #                 //Tag[] objects = null;
    #                 //try
    #                 //{
    #                 //    TheUFSession.Ui.LockUgAccess(UFConstants.UF_UI_FROM_CUSTOM);
    #                 //    TheUFSession.Ui.SelectWithClassDialog(message, message, scope, initialProcess, userData, out _,
    #                 //        out _, out objects);
    #                 //}
    #                 //catch (Exception ex)
    #                 //{
    #                 //    ex.__PrintException();
    #                 //}
    #                 //finally
    #                 //{
    #                 //    TheUFSession.Ui.UnlockUgAccess(UFConstants.UF_UI_FROM_CUSTOM);
    #                 //}

    #                 //return objects == null || objects.Length == 0 ? new NXOpen.Face[0] : objects.Select(tag => Snap.NX.Face.Wrap(tag).NXOpenFace).ToArray();

    #                 throw new NotImplementedException();
    #             }

    #             private static int InitialProcess(IntPtr select, IntPtr userData)
    #             {
    #                 UFUi.Mask mask = new UFUi.Mask
    #                 {
    #                     object_type = UFConstants.UF_face_type,
    #                     object_subtype = 0,
    #                     solid_type = 0
    #                 };
    #                 ufsession_.Ui.SetSelMask(select, UFUi.SelMaskAction.SelMaskClearAndEnableSpecific, 1, new[] { mask });
    #                 ufsession_.Ui.SetSelProcs(select, FilterProcess, null /* SelectionCallback*/, userData);
    #                 return UFConstants.UF_UI_SEL_SUCCESS;
    #             }

    #             private static int FilterProcess(Tag _object, int[] type, IntPtr userData, IntPtr select)
    #             {
    #                 var snapFace = _object.__To<Face>();

    #                 if (!snapFace.Name.StartsWith("PIERCED_"))
    #                     return NXOpen.UF.UFConstants.UF_UI_SEL_REJECT;

    #                 if (!snapFace.IsOccurrence)
    #                     return NXOpen.UF.UFConstants.UF_UI_SEL_REJECT;

    #                 if (!snapFace.__IsPlanar())
    #                     return NXOpen.UF.UFConstants.UF_UI_SEL_REJECT;

    #                 return snapFace.__NormalVector().__IsEqual(__Vector3dZ().__Negate())
    #                     ? NXOpen.UF.UFConstants.UF_UI_SEL_REJECT
    #                     : NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT;
    #             }
    #         }

    #         private class Comparer : IComparer<Tuple<Component, Face>>
    #         {
    #             #region Implementation of IComparer<in Tuple<Component,Face>>

    #             public int Compare(Tuple<Component, Face> x, Tuple<Component, Face> y)
    #             {
    #                 if (x == null) throw new ArgumentNullException(nameof(x));
    #                 if (y == null) throw new ArgumentNullException(nameof(y));
    #                 return string.Compare(x.Item1.DisplayName, y.Item1.DisplayName, StringComparison.Ordinal);
    #             }

    #             #endregion
    #         }

    #         public static class Constraints
    #         {
    #             /// <summary>
    #             ///     The path to the "Smart Button Metric.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartButtonMetric => "G:\\0Library\\Button\\Smart Button Metric.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Button English.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartButtonEnglish => "G:\\0Library\\Button\\Smart Button English.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Punch Metric.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartPunchMetric => "G:\\0Library\\PunchPilot\\Metric\\Smart Punch Metric.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Punch English.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartPunchEnglish => "G:\\0Library\\PunchPilot\\English\\Smart Punch English.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Ball Lock Retainer Metric.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartBallLockRetainerMetric =>
    #                 "G:\\0Library\\Retainers\\Metric\\Smart Ball Lock Retainer Metric.prt";

    #             /// <summary>
    #             ///     The path to the "Smart Ball Lock Retainer English.prt" file in G:\\0Library.
    #             /// </summary>
    #             public static string SmartBallLockRetainerEnglish =>
    #                 "G:\\0Library\\Retainers\\English\\Smart Ball Lock Retainer English.prt";

    #             /// <summary>
    #             ///     Returns the name of the reference set to be used for AddPierceComponents.
    #             /// </summary>
    #             public static string SlugRefsetName => "SLUG BUTTON ALIGN";

    #             // ReSharper disable once StringLiteralTypo
    #             public static string RetainerAlignPunchFaceName => "ALIGNPUNCH";

    #             // ReSharper disable once StringLiteralTypo
    #             public static string PunchTopFaceName => "PUNCHTOPFACE";

    #             // ReSharper disable once InconsistentNaming
    #             public static string Pierced_P => "PIERCED_P";

    #             // ReSharper disable once InconsistentNaming
    #             public static string Pierced_W => "PIERCED_W";

    #             // ReSharper disable once InconsistentNaming
    #             public static string Pierced_Type => "PIERCED_TYPE";

    #             public static Regex PiercedFaceRegex => new Regex("^PIERCED_([0-9]{1,})$");

    #             public static DisplayedConstraint CreateAlign(
    #                 Part part,
    #                 NXObject movableObject,
    #                 NXObject nonMovableObject)
    #             {
    #                 return CreateTouchAlignImpl(part, Constraint.Alignment.CoAlign, movableObject, nonMovableObject);
    #             }

    #             public static void ConstrainZAxes(Part part, Component punch, Component retainer)
    #             {
    #                 punch.__ReferenceSet("ALIGN");
    #                 retainer.__ReferenceSet("MATE");
    #                 DatumAxis retainerZAxis = (DatumAxis)retainer.__Members().Single(o => o.Name == "ZAXIS");
    #                 CartesianCoordinateSystem punchCartesian = punch.__Members().OfType<CartesianCoordinateSystem>().Single();
    #                 var punchOrientation = punchCartesian.Orientation.Element;

    #                 DatumAxis punchZAxis = punch.__Members()
    #                     .OfType<DatumAxis>()
    #                     .Single(axis => new Vector3d(axis.Direction.X, axis.Direction.Y, axis.Direction.Z)
    #                         .__IsEqual(punchOrientation.__AxisZ()));

    #                 DisplayedConstraint constraint = CreateAlign(part, retainerZAxis, punchZAxis);
    #                 constraint.__Layer(254);
    #             }

    #             public static DisplayedConstraint CreateTouchAlignImpl(
    #                 Part part,
    #                 Constraint.Alignment alignmentType,
    #                 NXObject movableObject, NXObject nonMovableObject)
    #             {
    #                 ComponentAssembly componentAssembly = part.ComponentAssembly;
    #                 ComponentPositioner positioner = componentAssembly.Positioner;
    #                 positioner.ClearNetwork();
    #                 positioner.PrimaryArrangement = componentAssembly.Arrangements.FindObject("Arrangement 1");
    #                 positioner.BeginAssemblyConstraints();
    #                 ComponentNetwork componentNetwork = (ComponentNetwork)positioner.EstablishNetwork();
    #                 componentNetwork.MoveObjectsState = true;
    #                 componentNetwork.NetworkArrangementsMode = ComponentNetwork.ArrangementsMode.Existing;
    #                 ComponentConstraint constraint = (ComponentConstraint)positioner.CreateConstraint(true);
    #                 constraint.ConstraintAlignment = alignmentType;
    #                 constraint.ConstraintType = Constraint.Type.Touch;
    #                 constraint.CreateConstraintReference(movableObject.OwningComponent, movableObject, false, false, false);
    #                 constraint.CreateConstraintReference(nonMovableObject.OwningComponent, nonMovableObject, false, false,
    #                     false);
    #                 componentNetwork.Solve();
    #                 positioner.ClearNetwork();
    #                 session_.__DeleteObjects(componentNetwork);
    #                 positioner.EndAssemblyConstraints();
    #                 return constraint.GetDisplayedConstraint();
    #             }

    #             public static DisplayedConstraint CreateTouch(Part part, NXObject movableObject, NXObject nonMovableObject)
    #             {
    #                 return CreateTouchAlignImpl(part, Constraint.Alignment.ContraAlign, movableObject, nonMovableObject);
    #             }

    #             public static void ConstrainFaces(Part part, Component punch, Component retainer)
    #             {
    #                 punch.__ReferenceSet("ALIGN");
    #                 retainer.__ReferenceSet("MATE");

    #                 Face punchFace = punch.__Members()
    #                     .OfType<Face>()
    #                     .Single(face => face.Name == PunchTopFaceName);

    #                 Face retainerFace = retainer.__Members()
    #                     .OfType<Face>()
    #                     .Single(face => face.Name == RetainerAlignPunchFaceName);

    #                 DisplayedConstraint constraint = CreateTouch(part, retainerFace, punchFace);
    #                 constraint.__Layer(254);
    #             }

    #             public static DisplayedConstraint CreateParallelConstraint(NXObject movableObject, NXObject geometry)
    #             {
    #                 ComponentPositioner positioner = _WorkPart.ComponentAssembly.Positioner;
    #                 positioner.ClearNetwork();
    #                 positioner.PrimaryArrangement = _WorkPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1");
    #                 positioner.BeginAssemblyConstraints();
    #                 ComponentNetwork componentNetwork = (ComponentNetwork)positioner.EstablishNetwork();
    #                 componentNetwork.MoveObjectsState = true;
    #                 componentNetwork.NetworkArrangementsMode = 0;
    #                 Constraint constraint = positioner.CreateConstraint(true);
    #                 ComponentConstraint componentConstraint = (ComponentConstraint)constraint;
    #                 componentConstraint.ConstraintType = (Constraint.Type)5;
    #                 componentConstraint.CreateConstraintReference(movableObject.OwningComponent, movableObject, false, false, false);
    #                 componentConstraint.CreateConstraintReference(geometry.OwningComponent, geometry, false, false, false);
    #                 componentNetwork.Solve();
    #                 positioner.ClearNetwork();
    #                 componentNetwork.__Delete();
    #                 positioner.DeleteNonPersistentConstraints();
    #                 positioner.EndAssemblyConstraints();
    #                 return constraint.GetDisplayedConstraint();
    #                 throw new NotImplementedException();
    #             }

    #             public static void ConstrainAlignBallSetAndPlane(Component punch, Component retainer)
    #             {
    #                 punch.__ReferenceSet("MATE");
    #                 retainer.__ReferenceSet("MATE");
    #                 DatumPlane retainerXZPlane = (DatumPlane)retainer.__Members().Single(o => o.Name == "XZPLANE");
    #                 DatumPlane punchBallSeatPlane = (DatumPlane)punch.__Members().Single(o => o.Name == "BALL_SEAT_ANGLE");
    #                 DisplayedConstraint constraint = CreateParallelConstraint(retainerXZPlane, punchBallSeatPlane);
    #                 constraint.__Layer(254);
    #             }

    #             public static void ConstrainFixPunch(Component punch)
    #             {
    #                 DisplayedConstraint constraint = CreateFixedConstraint(punch);
    #                 constraint.__Layer(254);
    #             }

    #             public static DisplayedConstraint CreateFixedConstraint(Component component)
    #             {
    #                 ComponentPositioner positioner = __work_part_.ComponentAssembly.Positioner;
    #                 positioner.ClearNetwork();
    #                 positioner.PrimaryArrangement = __work_part_.ComponentAssembly.Arrangements.FindObject("Arrangement 1");
    #                 positioner.BeginAssemblyConstraints();
    #                 ComponentConstraint constraint = (ComponentConstraint)positioner.CreateConstraint(true);
    #                 constraint.ConstraintType = (Constraint.Type)3;
    #                 constraint.CreateConstraintReference(component, component, false, false, false);
    #                 positioner.EndAssemblyConstraints();
    #                 return constraint.GetDisplayedConstraint();
    #             }
    #         }

    #         #region Obsolete Methods, look before you delete.

    #         public static DatumAxis GetZAxisOccurenceOfSlug(Face face)
    #         {
    #             int integer = GetFaceNameInteger(face);
    #             return face.OwningComponent.__Members()
    #                 .OfType<DatumAxis>()
    #                 .Single(plane => plane.Name == "PIERCED_AXIS_Z_" + integer);
    #         }

    #         public static DatumPlane GetYZPlaneOccurenceOfSlug(Face face)
    #         {
    #             int integer = GetFaceNameInteger(face);
    #             return face.OwningComponent.__Members()
    #                 .OfType<DatumPlane>()
    #                 .Single(plane => plane.Name == "PIERCED_PLANE_YZ_" + integer);
    #         }

    #         [Obsolete(nameof(NotImplementedException))]
    #         public static DatumAxis GetZAxisOccurence(Component snapButton)
    #         {
    #             //NXOpen.CoordinateSystem tempCsys = snapButton.__Members().OfType<NXOpen.CoordinateSystem>().Single();
    #             //IEnumerable<NXOpen.DatumAxis> DatumAxis = snapButton.__Members()
    #             //    .OfType<NXOpen.DatumAxis>();
    #             //foreach (NXOpen.DatumAxis axis in DatumAxis)
    #             //    if (((NXOpen.Assemblies.Component)(tempCsys.Tag)).orientation.z_vec._IsEqualTo(axis.Direction))
    #             //        return axis;
    #             //throw new ArgumentException("End Exception");
    #             throw new NotImplementedException();
    #         }

    #         [Obsolete(nameof(NotImplementedException))]
    #         public static DatumPlane GetYZPlaneOccurence(Component snapButton)
    #         {
    #             //NXOpen.CoordinateSystem tempCsys = snapButton.__Members().OfType<NXOpen.CoordinateSystem>().Single();
    #             //IEnumerable<NXOpen.DatumPlane> planes = snapButton.__Members()
    #             //    .OfType<NXOpen.DatumPlane>();
    #             //foreach (NXOpen.DatumPlane plane in planes)
    #             //    if (((NXOpen.Assemblies.Component)(tempCsys.Tag)).orientation.z_vec._IsEqualTo(plane.Normal))
    #             //        return plane;

    #             //throw new ArgumentException("End Exception");
    #             throw new NotImplementedException();
    #         }

    #         public static Face GetTopFaceOfPunch(Component snapPunch)
    #         {
    #             // ReSharper disable once StringLiteralTypo
    #             return snapPunch.__Members().OfType<Face>().Single(face => face.Name == "PUNCHTOPFACE");
    #         }

    #         public static Face GetAlignFaceOfRetainer(Component snapPunch)
    #         {
    #             // ReSharper disable once StringLiteralTypo
    #             return snapPunch.__Members().OfType<Face>().Single(face => face.Name == "ALIGNPUNCH");
    #         }

    #         internal static string EditInteger(int integer)
    #         {
    #             if (integer < 0)
    #                 throw new ArgumentOutOfRangeException(nameof(integer));
    #             if (integer < 10)
    #                 return "00" + integer;
    #             if (integer < 100)
    #                 return "0" + integer;
    #             return integer.ToString();
    #         }

    #         public static Part _Prototype(Component component) => component.Prototype as Part ?? throw new Exception();

    #         [Obsolete]
    #         internal static DatumAxis GetZAxisOccurenceOfRetainer(Component retainer)
    #         {
    #             //string retainerRefset = retainer.ReferenceSet;

    #             //print_(retainer.__Prototype().GetAllReferenceSets().Single(set => set.Name == retainerRefset).AskMembersInReferenceSet()
    #             //    .OfType<NXOpen.CoordinateSystem>().Count());

    #             //Snap.NX.CoordinateSystem tempCsys = retainer.__Members().Select(obj => (Snap.NX.NXObject)obj).OfType<Snap.NX.CoordinateSystem>().Single();
    #             //IEnumerable<NXOpen.DatumAxis> k = retainer.__Members()
    #             //    .OfType<NXOpen.DatumAxis>();
    #             //foreach (NXOpen.DatumAxis axis in k)
    #             //    if (new NXOpen.Vector3d(axis.Direction.X, axis.Direction.Y, axis.Direction.Z).__IsEqualTo(tempCsys.AxisZ))
    #             //        return axis;

    #             //throw new ArgumentException("End Exception");

    #             throw new NotImplementedException();
    #         }

    #         #endregion

    #         private void AddPierceComponents_Load(object sender, EventArgs e)
    #         {
    #             Text = AssemblyFileVersion;
    #             Location = Properties.Settings.Default.add_pierce_components_form_window_location;
    #         }

    #         private void AddPierceComponents_FormClosed(object sender, System.Windows.Forms.FormClosedEventArgs e)
    #         {
    #             Properties.Settings.Default.add_pierce_components_form_window_location = Location;
    #             Properties.Settings.Default.Save();
    #         }
    #     }
    pass
