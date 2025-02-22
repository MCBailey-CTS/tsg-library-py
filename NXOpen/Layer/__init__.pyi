import enum

class State(enum.Enum):
    Hidden: int
    Selectable: int
    Visible: int
    WorkLayer: int

# Category
# CategoryCollection
# Constants
class LayerManager:
    def SetState(self, layer: int, state: State) -> None: ...
    def GetState(self, layer: int) -> State: ...
    @property
    def WorkLayer(self) -> int: ...
    @WorkLayer.setter
    def WorkLayer(self, layer: int) -> None: ...

# StateCollection
# StateInfo
