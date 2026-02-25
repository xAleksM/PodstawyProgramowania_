def hurra():
    print('Hurra!\n' * 50)

#hurra2 - nazwa funkcji
#n - parametr funkcji
#6 - argument funkcji
#hurra2(6) - wywołanie funkcji dla argumentu n = 6

def hurra2(n):
    print('Hurra!\n' * n)

#hurra2(6)

def hurra3(n = 10):
    print('Hurra!\n' * n)

hurra3()

#Jeżeli funkcja po prostu wykonuje jakąś czynność i nie możemy wykorzystać dalej
#efektór jej pracy to jest procedura

#Pole całkowite graniastosłupa prawidłowego trójkątnego

def p_tr_rown(a):
    return a ** 2 * (3 ** 0.5) / 4

#Pp = p_tr_rown(3 ** 0.25)

def p_prst(a, b):
    return a * b

# Psb = p_prst(a: 5, b: 4)

def p_gran_praw_troj(a,b):
    return 2 * p_tr_rown(a) + 3 * p_prst(a, b)

Pg = p_gran_praw_troj(7, 4)
print(Pg)