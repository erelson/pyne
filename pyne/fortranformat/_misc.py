'''
Miscellaneous functions, classes etc
'''
import sys
IS_PYTHON3 = sys.version_info[0] >= 3

class has_next_iterator(object):
  '''
  A wrapper class for iterators so that the .has_next() method is implemented

  See - http://stackoverflow.com/questions/1966591/hasnext-in-python-iterators
  '''
  def __init__(self, it):
    self.it = iter(it)
    self._has_next = None
  def __iter__(self): return self
  def __next__(self):
    if self._has_next:
      result = self._the_next
    else:
      if IS_PYTHON3:
        result = next(self.it)
      else:
        result = self.it.next()
    self._has_next = None
    return result
  def next(self):
    if self._has_next:
      result = self._the_next
    else:
      if IS_PYTHON3:
        result = next(self.it)
      else:
        result = self.it.next()
    self._has_next = None
    return result
  def has_next(self):
    if self._has_next is None:
      try: 
        if IS_PYTHON3:
          self._the_next = next(self.it)
        else:
          self._the_next = self.it.next()
      except StopIteration: self._has_next = False
      else: self._has_next = True
    return self._has_next


def expand_edit_descriptors(eds):
    expanded_eds = []
    for ed in eds:
        if hasattr(ed, 'repeat') and (ed.repeat is not None):
            expanded_eds.extend(ed.repeat * [ed])
        else:
            expanded_eds.append(ed)
    return expanded_eds
