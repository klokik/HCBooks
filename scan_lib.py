#!/bin/env python3

book_costs = []

class BookLib:
  def __init__(self, init_books, signup_delay, scans_per_day):
    self.books = init_books
    self.signup_delay = signup_delay
    self.scans_per_day = scans_per_day

    self.signup_day = None
    self.sent_books = []

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
      raise "todo"

  def getSentBooks(self):
    pass

  def signup(self, day):
    self.signup_day = day

# def lib_cost(library_books, signup_delay, scans_per_day, days_left):
#   pass

class ScanQuest:
  def __init__(self, fname):
    libs = []
    submitted_books = []
    signed_libs = []
    # @todo: load data: create libs, init days, book_costs
    pass

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

      for today in range(day_num, day_num+best_lib.signup_delay)
        for lib in self.signed_libs:
          books = lib.sendSomeBooks(today)
          self.burnSomeBooks(books)

      day_num += best_lib.signup_delay

  def writeResult(self, fname):
    # @todo

def main():
  q = ScanQuest("data.in")

  q.doTheThing()

  q.writeResult("data.out")

if __name__ == '__main__':
  main()