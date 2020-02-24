def sos(c, n):
  city = 1
  while city < n + 1:
    if not (city in c[1:]):
      return False
    city += 1
  return True
