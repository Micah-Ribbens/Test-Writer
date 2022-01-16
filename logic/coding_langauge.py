from abc import ABC, abstractmethod

class CodingLangauge(ABC):
    @abstractmethod
    def is_function(self, line):
        pass

    @abstractmethod
    def get_params(self, function_line):
        pass