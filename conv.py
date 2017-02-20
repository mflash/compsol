bom_file = 'shakespeare.txt'
s = open(bom_file, mode='r', encoding='utf-8-sig').read()
open('shakespeare2.txt', mode='w', encoding='utf-8').write(s)
