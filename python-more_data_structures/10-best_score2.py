def best_score(a_dictionary):
  valeur_max = 0
  best_key = None
  for key in a_dictionary:
    if a_dictionary[key] > valeur_max:
      valeur_max = a_dictionary[key]
      best_key = key

  return best_key