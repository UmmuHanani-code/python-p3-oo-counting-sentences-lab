#!/usr/bin/env python3

import re
#re stands for regular expressions, and it's a built-in Python module used
#to search, match, and manipulate text based on patterns.
class MyString:
  def __init__(self, value=""):
    self._value = ""
    self.value = value


  @property
  def value(self):
     return self._value

  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value

    else:
       print("The value must be a string.")


  def is_sentence(self):
    return self._value.endswith(".")


  def is_question(self):
    return self._value.endswith("?")


  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    sentences = re.split(r'[.!?]+', self._value)
    sentences = [s.strip() for s in sentences if s.strip() != ""]

    return len(sentences)


string = MyString()
string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
print(string.count_sentences())
print(string.is_question())











