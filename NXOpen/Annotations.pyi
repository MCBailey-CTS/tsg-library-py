from typing import Iterable

from NXOpen import DisplayableObject

class Annotation(DisplayableObject):
    pass

class DraftingAid(Annotation):
    pass

class SimpleDraftingAid(DraftingAid):
    pass

class NoteBase(SimpleDraftingAid):
    pass

class BaseNote(SimpleDraftingAid):
    pass

class GenericNote(BaseNote):
    pass

class Note(BaseNote):
    pass

class PmiNoter(BaseNote):
    pass

class NoteCollection(Iterable[BaseNote]):
    def __iter__(self):  # type: ignore
        pass
    # def CreatePmiNote(self, note_data, pmi_data, annotation_plane)
    # NewNoteData
