from typing import Tuple

text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

vowels = 'aeiou'


def strip_vowels(text: str) -> Tuple[str, int]:
   count_text = list(text.lower())
   replaced_text = []

   # Counter, I wanted to separate the two tasks
   count = len([letter for letter in count_text if letter in vowels] )

   # Text Changer
   for letter in text:
      if letter.lower() in vowels: #Using lower() means the vowels variable only needs half the iterable elements
         letter = '*'
      replaced_text.append(letter) #Add each letter to the replaced text list
   replaced_text = ''.join(replaced_text) # Join the list of letters together

   return replaced_text, count

print(strip_vowels(text))
# strip_vowels(text)
