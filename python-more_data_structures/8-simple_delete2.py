def simple_delete(a_dictionary, key=""):
  if key not in a_dictionary:
    return a_dictionary
  else:
    a_dictionary.pop(key)

  return a_dictionary
