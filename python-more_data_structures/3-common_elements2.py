def common_elements(set_1, set_2):
  new_list = []
  for i in set_1:
    if i in set_2:
      new_list.append(i)
  return set(new_list)
