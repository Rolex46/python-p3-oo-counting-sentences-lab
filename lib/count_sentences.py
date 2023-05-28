#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value = None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,value):
        if (type(value) == str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self._value is not None and self._value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        if self._value is not None and self._value.endswith("?"):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value is not None and self._value.endswith("!"):
            return True
        else:
            return False
        
    def count_sentences(self):
        '''Returns  the number of sentences in the value.'''
        if self.value is None:
            return 0
        else:
            sentences = re.split(r'[.!?]+', self.value)
            non_empty_sentences = [sentence for sentence in sentences if len(sentence.strip()) > 0]
            return len(non_empty_sentences)