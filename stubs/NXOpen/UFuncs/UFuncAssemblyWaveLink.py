import traceback
from NXOpen import Session
from extensions__ import *


class WithDisplayPartReset:
    ...


class WithSuppressDisplay:
    ...


class WithReferenceSetReset:
    ...


def select_many_component1() -> Sequence[Component]:
    # Component[] tools = SelectManyComponents1(c =>
    # {
    #     if (!(c is Component comp))
    #         return false;

    #     return comp.Tag != target.OwningComponent.Tag
    #     && (from refset in comp.__Prototype().GetAllReferenceSets()
    #         let name = refset.Name.ToUpper()
    #         where name == "SUB_TOOL" || Name == "SUB-TOOL" || name == "SUBTOOL"
    #         select refset
    #         ).Any() && !comp.DisplayName.__IsAssemblyHolder();
    # }

    #         );
    raise NotImplementedError()


def select_single_solid_body() -> Body:
    raise NotImplementedError()


def WavelinkSubtool():
    # session().SetUndoMark(Session.MarkVisibility.Visible, f"{ufunc_rev_name} - {nameof(WavelinkSubtool)}");
    target = select_single_solid_body()
    if target is None:
        return
    tools = select_many_component1()
    if len(tools) == 0:
        return
    with WithDisplayPartReset():
        with WithSuppressDisplay():
            try:
                current = display_part().Layers.WorkLayer

                try:
                    __work_component_ = target.OwningComponent
                    display_part().Layers.SetState(96, NXOpen.Layer.State.WorkLayer)
                    for tool in tools:
                        with WithReferenceSetReset():
                            try:
                                # ReferenceSet reference_set = tool.__Prototype()
                                #     .GetAllReferenceSets()
                                #     .SingleOrDefault(refset => refset.Name == "SUB_TOOL" || refset.Name == "SUB-TOOL" || refset.Name == "SUBTOOL");

                                # if reference_set is None:
                                #     print_(f"Didn't find any sub tool reference sets for {tool.DisplayName} - {tool.Name} - {tool.Tag}");
                                #     continue;

                                # tool.__ReferenceSet(reference_set.Name);
                                # ExtractFace linked_body = tool.__CreateLinkedBody();
                                # print_("//////////////////");
                                # print_($"Created {linked_body.GetFeatureName()} in {linked_body.OwningPart.Leaf}");
                                # BooleanFeature boolean_feature = target.__Subtract(linked_body.GetBodies());
                                # print_($"Created {boolean_feature.GetFeatureName()} in {linked_body.OwningPart.Leaf}");
                                pass

                                # }
                                # catch (NXException ex) when (ex.ErrorCode == 670030)
                                # {
                                #     print_($"Error occurred when trying to subtract {tool.DisplayName}, no interference.");
                                # }
                                # catch (InvalidOperationException)
                                # {
                                #     print_($"Found more than one sub tool reference set for {tool.DisplayName} - {tool.Name} - {tool.Tag}");
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


#      public void WaveLinkFasteners(bool blank_tools, string shcs_ref_set, string dwl_ref_set, string jck_ref_set)
#      {
#          session_.SetUndoMark(Session.MarkVisibility.Visible, ufunc_rev_name);

#          using (session_.__UsingDisplayPartReset())
#              try
#              {
#                  Body[] targets = SelectMultipleTaggedObjects1(
#                      "Select Target Body",
#                      "select Target Body",
#                      new[] { BodyMask },
#                      k =>
#                      {

#                          if (!(k is Body b))
#                              return false;

#                          return b.IsOccurrence
#                          && !b.OwningComponent.DisplayName.ToLower().Contains("strip")
#                          && !b.OwningComponent.DisplayName.ToLower().Contains("press")
#                          && !b.OwningComponent.DisplayName.ToLower().Contains("layout")
#                          && !b.OwningComponent.DisplayName.__IsAssemblyHolder();
#                      }).Cast<Body>().ToArray();

#                  if (targets.Length == 0)
#                      return;

#                  Component[] tools = SelectMultipleTaggedObjects1(
#                      "Select Tool Components",
#                      "Select Tool Components",
#                      new[] { Masks.ComponentMask },
#                      tool1 =>
#                      {

#                          if (!(tool1 is Component tool))
#                              return false;

#                          return !tool.DisplayName._IsLayout_()
#                          && !tool.DisplayName.ToLower().Contains("strip")
#                          && !tool.DisplayName._IsFastenerExtended_()
#                          && !tool.DisplayName.__IsAssemblyHolder()
#                          && targets.All(t => t.OwningComponent.Tag != tool.Tag);
#                      }).Cast<Component>().ToArray();

#                  if (tools.Length == 0)
#                      return;

#                  using (session_.__UsingSuppressDisplay())
#                      foreach (var target in targets)
#                          foreach (Component tool in tools)
#                              using (session_.__UsingDisplayPartReset())
#                              using (session_.__UsingResetWorkLayer())
#                                  try
#                                  {
#                                      __work_component_ = target.OwningComponent;
#                                      display_part().Layers.SetState(96, NXOpen.Layer.State.WorkLayer);

#                                      foreach (Component child in tool.GetChildren())
#                                          try
#                                          {
#                                              if (!child.__IsLoaded())
#                                              {
#                                                  print_($"Child fastener {child.DisplayName} was not loaded.");
#                                                  continue;
#                                              }

#                                              if (child.IsSuppressed)
#                                                  continue;

#                                              //if (child._IsJckScrewTsg_() || child._IsJckScrew_())
#                                              //    continue;

#                                              using (child.__UsingReferenceSetReset())
#                                              {
#                                                  string original_ref_set = child.ReferenceSet;
#                                                  Component proto_child_fastener = child.__ProtoChildComp();

#                                                  if (proto_child_fastener.Layer != LayerFastener)
#                                                      continue;

#                                                  try
#                                                  {
#                                                      string[] ref_sets = new[] { shcs_ref_set, dwl_ref_set, jck_ref_set }
#                                                          .Where(__r => !string.IsNullOrEmpty(__r))
#                                                          .ToArray();

#                                                      string[] fastener_ref_set_names = proto_child_fastener.__Prototype()
#                                                          .GetAllReferenceSets()
#                                                          .Select(__r => __r.Name)
#                                                          .Intersect(ref_sets)
#                                                          .ToArray();

#                                                      switch (fastener_ref_set_names.Length)
#                                                      {
#                                                          case 0:
#                                                              if ((!(shcs_ref_set is null)&& child._IsShcs_())
#                                                                  || (!(dwl_ref_set is null) && child._IsDwl_())
#                                                                  || (!(jck_ref_set is null) && child._IsJckScrewTsg_() || child._IsJckScrew_()))
#                                                                  print_(
#                                                                      $"Coulnd't find any valid ref sets for {child.DisplayName}");
#                                                              continue;
#                                                          case 1:
#                                                              child.__ReferenceSet(fastener_ref_set_names[0]);
#                                                              break;
#                                                          default:
#                                                              print_(
#                                                                  $"Found more than one valid ref set for {child.DisplayName}");
#                                                              continue;
#                                                      }

#                                                      if (!target.__InterferesWith(child))
#                                                      {
#                                                          print_(
#                                                              $"Could not subtract fastener {child.DisplayName}, no interference.");
#                                                          continue;
#                                                      }

#                                                      ExtractFace ext = child.__CreateLinkedBody();
#                                                      //ext.__Layer(96);
#                                                      print_("//////////////////");
#                                                      print_($"Created {ext.GetFeatureName()} in {ext.OwningPart.Leaf}");
#                                                      BooleanFeature boolean_feature = target.__Subtract(ext.GetBodies());
#                                                      print_($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}");
#                                                  }
#                                                  catch (Exception ex)
#                                                  {
#                                                      ex.__print_Exception(child.DisplayName);
#                                                  }
#                                              }
#                                          }
#                                          catch (Exception ex)
#                                          {
#                                              ex.__print_Exception();
#                                          }

#                                      if (blank_tools)
#                                          tool.Blank();
#                                  }
#                                  catch (Exception ex)
#                                  {
#                                      ex.__print_Exception();
#                                  }

#              }
#              catch (NothingSelectedException)
#              {
#                  //Control jump
#              }
#              catch (Exception ex)
#              {
#                  ex.__print_Exception();
#              }
#      }

#      public static void WaveLinkBoolean(bool blank_tools, Feature.BooleanType booleanType)
#      {
#          session_.SetUndoMark(Session.MarkVisibility.Visible, "Assembly Wavelink");

#          using (session_.__UsingDisplayPartReset())
#          {
#              try
#              {
#                  Body[] targets = SelectManySolidBodies1();

#                  if (targets.Length == 0)
#                      return;

#                  Component[] tools = SelectManyComponents1(c =>
#                  {
#                      if (!(c is Component comp))
#                          return false;

#                      return targets.All(b => b.OwningComponent.Tag != c.Tag)
#                      && !comp.DisplayName.__IsAssemblyHolder();
#                  });

#                  if (tools.Length == 0)
#                      return;

#                  var referenceSets = tools.Select(snapComponent => new { snapComponent, snapComponent.ReferenceSet }).ToList();
#                  RefSetForm formCts = new RefSetForm(tools);

#                  if (booleanType != Feature.BooleanType.Create)
#                      formCts.RemoveReferenceSet("BODY");

#                  formCts.ShowDialog();

#                  if (!formCts.IsSelected)
#                      return;

#                  foreach (var target in targets)
#                      foreach (var child in tools)
#                          using (session_.__UsingDisplayPartReset())
#                          using (child.__UsingReferenceSetReset())
#                          using (session_.__UsingResetWorkLayer())
#                          {
#                              var current = display_part().Layers.WorkLayer;

#                              try
#                              {
#                                  __work_component_ = target.OwningComponent;

#                                  display_part().Layers.SetState(96, NXOpen.Layer.State.WorkLayer);

#                                  child.__ReferenceSet(formCts.SelectedReferenceSetName);

#                                  foreach (var ext in child.__CreateLinkedBodies())
#                                      try
#                                      {
#                                          print_("//////////////////");

#                                          print_($"Created {ext.GetFeatureName()} in {ext.OwningPart.Leaf}");

#                                          switch (booleanType)
#                                          {
#                                              case Feature.BooleanType.Subtract:
#                                                  {
#                                                      BooleanFeature boolean_feature = target.__Subtract(ext.GetBodies());
#                                                      print_($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}");
#                                                  }
#                                                  break;

#                                              case Feature.BooleanType.Unite:
#                                                  {
#                                                      BooleanFeature boolean_feature = target.__Unite(ext.GetBodies());
#                                                      print_($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}");
#                                                  }
#                                                  break;

#                                              case Feature.BooleanType.Intersect:
#                                                  {
#                                                      BooleanFeature boolean_feature = target.__Intersect(ext.GetBodies());
#                                                      print_($"Created {boolean_feature.GetFeatureName()} in {ext.OwningPart.Leaf}");
#                                                  }
#                                                  break;
#                                          }
#                                      }
#                                      catch (NXException ex) when (ex.ErrorCode == 670030)
#                                      {
#                                          print_($"Error occurred when trying to subtract {child.DisplayName}, no interference.");
#                                      }
#                                      catch (Exception ex)
#                                      {
#                                          ex.__print_Exception();
#                                      }
#                              }
#                              finally
#                              {
#                                  display_part().Layers.SetState(current, NXOpen.Layer.State.WorkLayer);
#                              }
#                          }

#                  if (blank_tools)
#                      foreach (var tool in tools)
#                          tool.Blank();
#              }
#              catch (NothingSelectedException)
#              {
#              }
#              catch (Exception ex)
#              {
#                  ex.__print_Exception();
#              }
#          }
#      }

#  }
