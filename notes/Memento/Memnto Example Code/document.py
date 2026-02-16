import memento

class Document:
    def __init__(self):
        self._words = ""

        @property
        def words(self):
            return self._words
        
        def add_words(self, w):
            self._words += w

        def backup(self):
            return memento.Memento(self._words)
        
        def restore(self, mem):
            self._words = mem.get_words()
        