def multiply_by_2(a_dictionary):
  new_dict = a_dictionary.copy()
  for key in new_dict:
    new_dict[key] = a_dictionary[key] * 2
  
  return new_dict