from typing import Sequence, Tuple
import NXOpen





class Disp:
    def RegenerateDisplay(self) -> None: ...

class Obj:
    def CycleByName(self, name: str, tag: int) -> int: ...

class Vec3:
    def Scale(self, scale: float, vec: Sequence[float]) -> Sequence[float]:...
    # def DistancetoPlane(self, pnt1, pnt_on_plane, plane_normal, tolerance)->float:
    #     pass
    def Unitize(vec:Sequence[float], tolerance:float)->Tuple[float,Sequence[float]]:...

class UFSession:
    @staticmethod
    def GetUFSession() -> UFSession: ...
    @property
    def Disp(self) -> Disp: ...
    @property
    def Obj(self) -> Obj: ...
    @property
    def Vec3(self) -> Vec3: ...
