import NXOpen

class UFSession:
    @staticmethod
    def GetUFSession() -> UFSession:
        pass
    @property
    def Disp(self) -> NXOpen.UF.Disp:
        pass

class Disp:
    def RegenerateDisplay(self) -> None:
        pass
