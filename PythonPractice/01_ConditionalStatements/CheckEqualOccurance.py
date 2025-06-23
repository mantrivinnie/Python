#You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
#Note: str contains only lowercase English alphabets.

def cat_hat(str):
  cat_count=str.count("cat")
  hat_count=str.count("hat")
  if cat_count == hat_count:
    return True
  else:
    return False