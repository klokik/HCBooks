#!/bin/env python3

book_costs = []

def interleave(items, num, limit=None):
  res = [[]]*num
  for k, it in enumerate(items):
    if (k % num == 0) && (k / num) == limit:
      break

    res[k % num].append(it)

  return res

class BookLib:
  def __init__(self, ind, init_books, signup_delay, scans_per_day):
    self.books = init_books
    self.signup_delay = signup_delay
    self.scans_per_day = scans_per_day

    self.signup_day = None
    self.sent_books = []
    self.ind = ind

  def cost(self, days_left):
    # @todo
    return 42

  def burnBooks(self, books):
    for b in books:
      try:
        self.books.remove(b)
      except KeyError as e:
        pass

  def sendSomeBooks(self, day_num):
    if (self.signup_day is None) || (self.signup_day + self.signup_delay < day_num):
      return []
    else:
      # @todo: use max heap
      chosen_books = sorted(self.books, key=lambda b: book_costs[b], reverse=True)[:self.scans_per_day]
      self.sent_books.extend(chosen_books)
      return chosen_books

  def getSentBooks(self):
    return self.sent_books

  def signup(self, day):
    self.signup_day = day

class ScanQuest:
  def __init__(self, fname):
    libs = []
    signed_libs = []

    with open(fname) as f:
      num_books, num_libs, self.days_total = list(map(int, f.readline()))
      global book_costs
      book_costs = list(map(int, f.readline()))

      for ind in range(num_libs):
        lib_num_books, signup_delay, scans_per_day = list(map(int, f.readline()))
        lib_books = list(map(int, f.readline()))

        self.libs.append(BookLib(ind, lib_books, signup_delay, scans_per_day))

  def chooseNextBestLib(self, days_left):
    best_lib = max(self.libs, key=lambda l: l.cost(days_left))

  def burnSomeBooks(self, some_books):
    for lib in self.libs:
      lib.burnBooks(some_books)

    for lib in self.signed_libs:
      lib.burnBooks(some_books)

  def doTheThing(self):
    day_num = 0
    while day_num < self.days_total:
      best_lib = self.chooseNextBestLib(self.days_total - day_num)
      best_lib.signup(day_num)
      libs.remove(best_lib)
      signed_libs.append(best_lib)

      for today in range(day_num, day_num+best_lib.signup_delay):
        if today >= self.days_total:
          break

        for lib in self.signed_libs:
          books = lib.sendSomeBooks(today)
          self.burnSomeBooks(books)

      day_num += best_lib.signup_delay

  def writeResult(self, fname):
    with open(fname, "w") as f:
      f.write("{}\n".format(len(self.signed_libs)))
      for lib in self.signed_libs:
        books = lib.getSentBooks()
        f.write("{} {}\n".format(lib.ind, len(books)))
        f.write(" ".join(map(str, books))+"\n")

def main():
  q = ScanQuest("data.in")

  q.doTheThing()

  q.writeResult("data.out")

if __name__ == '__main__':
  main()