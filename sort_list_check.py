"""Check if list is sorted or not """
def is_sorted(lst):
  new=sorted(lst)

  if new == lst:
      return True
  else:
      return False
lst=[2,3,4]
print(is_sorted(lst))

