class UFuncDeleteUnusedCurves:
    #     public class DeleteUnusedCurves : _UFunc
    # {
    #     public override void execute()
    #     {
    #         Curve[] curves = Selection.SelectCurves(
    #             ufunc_rev_name,
    #             ufunc_rev_name,
    #             NXOpen.Selection.SelectionScope.WorkPart
    #         );

    #         if (curves is null || curves.Length == 0)
    #             return;

    #         foreach (Curve delete in curves)
    #         {

    #             ufsession_.Modl.AskObjectFeat(delete.Tag, out Tag featTag);

    #             if (featTag == Tag.Null)
    #                 delete.__Delete();
    #         }
    #     }
    # }
    pass
