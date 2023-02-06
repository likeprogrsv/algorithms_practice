text = 'Apart from, count words, and from! end.'

s1 = (text.replace(',', ' ').
      replace('!', ' ').
      replace('.', ' ').
      split())

print(s1)