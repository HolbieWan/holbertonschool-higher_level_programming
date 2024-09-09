def print_sorted_dictionary(a_dictionary):
  new_dict = sorted(a_dictionary)
  for key in new_dict:
    print(key, a_dictionary[key])