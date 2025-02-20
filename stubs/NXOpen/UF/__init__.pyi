import NXOpen

class Disp:
    def RegenerateDisplay(self) -> None: ...
    

class Obj:
    def CycleByName(self, name:str, tag:int)->int: ...

class UFSession:
    @staticmethod
    def GetUFSession() -> UFSession: ...
    @property
    def Disp(self) -> Disp: ...
    @property
    def Obj(self) -> Obj: ...

