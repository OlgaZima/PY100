# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list_b_d_h_o = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]

pprint(list_b_d_h_o)


#deff = ['bin', 'dec', 'hex', 'oct']
#list_ = []
#for i in range(16):
#    for j in range(len(deff)):
#        b_d_h_o = {deff[j]: bin(i), deff[j + 1]: i, deff[j + 2]: hex(i), deff[j + 3]: oct(i)}
#        break
#    list_.append(b_d_h_o)









