is_non_negative_num = lambda x: True if x[0] != '-' and x.replace('.', '' ,1).isdigit()  else False