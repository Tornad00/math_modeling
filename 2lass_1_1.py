class Alphavit:
  def __init__ (self, lang_0, letters_0):
    self.lang = lang_0
    self.letters  = letters_0

  def pr_all (self, letters_0):
    print(letters_0)

  def cound_all (self, letters_0):
    print(len(letters_0))

lang_1 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "к", "л", "м", "н" ,"о", "п", "р", "с", "т"]
lang_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = Alphavit(1, lang_1)
a.pr_all(lang_1)
a.cound_all(lang_1)
a.pr_all(lang_2)
a.cound_all(lang_2)