from typing import List, Sequence, Tuple
import NXOpen

class Assem:
    def AskOccsOfPart(
        self, parent_part: int, descedant_part: int
    ) -> Tuple[Sequence[int], int]: ...

class Csys:
    def MapPoint(
        self, input_csys: int, input_point: List[float], output_csys: int
    ) -> List[float]:
        """
        Maps a point from one coordinate system to a point in another
        coordinate system. The coordinate system can be one of the following
        constants.

        UF_CSYS_ROOT_COORDS is the ABS of the displayed part.
        UF_CSYS_WORK_COORDS is the ABS of the work part.
        UF_CSYS_ROOT_WCS_COORDS is the WCS of the displayed part.
        For example:
        To convert a point from absolute coordinates of the displayed part to
        the WCS:
        input_csys = UF_CSYS_ROOT_COORDS;
        output_csys = UF_CSYS_ROOT_WCS_COORDS;
        To convert a point from the work part absolute coordinates to the
        displayed part absolute coordinates:
        input_csys = UF_CSYS_WORK_COORDS;
        output_csys = UF_CSYS_ROOT_COORDS;
        """
    pass

class Disp:
    def RegenerateDisplay(self) -> None: ...

class Eval: ...
class Modl: ...

class Obj:
    def CycleByName(self, name: str, tag: int) -> int: ...

class Vec3:
    def Scale(self, scale: float, vec: Sequence[float]) -> Sequence[float]: ...
    # def DistancetoPlane(self, pnt1, pnt_on_plane, plane_normal, tolerance)->float:
    #     pass
    def Unitize(
        self, vec: Sequence[float], tolerance: float
    ) -> Tuple[float, Sequence[float]]: ...

class UFConstants:
    UF_CSYS_ROOT_WCS_COORDS: int
    UF_CSYS_ROOT_COORDS: int
    UF_CSYS_WORK_COORDS: int

class UFSession:
    @property
    def Assem(self) -> Assem: ...
    @staticmethod
    def GetUFSession() -> UFSession: ...
    @property
    def Disp(self) -> Disp: ...
    @property
    def Eval(self) -> Eval: ...
    @property
    def Modl(self) -> Modl: ...
    @property
    def Obj(self) -> Obj: ...
    @property
    def Vec3(self) -> Vec3: ...
    @property
    def Csys(self) -> Csys: ...
