#!/bin/env python3

# import numpy as np

book_costs = []

current_task = 'a'

def interleave(items, num, limit=None):
  res = [[]]*num
  for k, it in enumerate(items):
    if (k % num == 0) and (k / num) == limit:
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
    effective_days = days_left - self.signup_delay
    if effective_days < 0:
      return 0

    if current_task != "d":
      effective_books = list(sorted(self.books))[:self.scans_per_day*effective_days] #interleave(self.books, self.scans_per_day, effective_days)
      val = sum(effective_books)
    else:
      return min(effective_days, len(self.books)/self.scans_per_day)*self.scans_per_day*65

    return val

  def burnBooks(self, books):
    for b in books:
      try:
        self.books.remove(b)
      except Exception as e:
        pass

  def sendSomeBooks(self, day_num, used_books):
    if (self.signup_day is None) or (self.signup_day + self.signup_delay < day_num):
      return []
    else:
      # @todo: use max heap
      # chosen_books = self.books[:self.scans_per_day] #sorted(self.books, key=lambda b: book_costs[b], reverse=True)[:self.scans_per_day]
      if current_task != 'd':
        chosen_books = sorted(self.books, key=lambda b: book_costs[b], reverse=True)[:self.scans_per_day]
      else:
        chosen_books = self.books[:self.scans_per_day]
      # chosen_books = []
      # for b in self.books:
      #   if b not in used_books:
      #     self.
      self.sent_books.extend(chosen_books)
      return chosen_books

  def getSentBooks(self):
    return self.sent_books

  def signup(self, day):
    self.signup_day = day

class ScanQuest:
  def __init__(self, fname):
    self.libs = []
    self.signed_libs = []

    with open(fname) as f:
      num_books, num_libs, self.days_total = list(map(int, f.readline().split()))
      global book_costs
      book_costs = list(map(int, f.readline().split()))

      for ind in range(num_libs):
        lib_num_books, signup_delay, scans_per_day = list(map(int, f.readline().split()))
        lib_books = list(map(int, f.readline().split()))

        self.libs.append(BookLib(ind, lib_books, signup_delay, scans_per_day))

  def chooseNextBestLib(self, days_left):
    best_lib = max(self.libs, key=lambda l: l.cost(days_left))
    return best_lib

  def burnSomeBooks(self, some_books):
    for lib in self.libs:
      lib.burnBooks(some_books)

    for lib in self.signed_libs:
      lib.burnBooks(some_books)

  def doTheThing(self):
    day_num = 0
    while day_num < self.days_total:
      if len(self.libs) > 0:
        best_lib = self.chooseNextBestLib(self.days_total - day_num)
        best_lib.signup(day_num)
        self.libs.remove(best_lib)
        self.signed_libs.append(best_lib)
        next_sign_day = day_num+best_lib.signup_delay
      else:
        next_sign_day = self.days_total

      for today in range(day_num, next_sign_day):
        print(current_task, today)
        if today >= self.days_total:
          break

        for lib in self.signed_libs:
          books = lib.sendSomeBooks(today, None)
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
  # fnames = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_choices.txt", "f_libraries_of_the_world.txt"]
  fnames = ["a_example.txt", "b_read_on.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
  for fname in fnames:
    global current_task
    current_task = fname[0]
    # q = ScanQuest("a_example.txt")
    # q = ScanQuest("c_incunabula.txt")
    q = ScanQuest(fname)

    q.doTheThing()

    q.writeResult(fname + ".out")

if __name__ == '__main__':
  main()