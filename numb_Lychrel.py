# -*-coding:UTF-8 -*

print("    Bienevenu! Ce programme a pour but de chercher au mieux possible les nbres de Lychrel.\n\
    Note: Un nombre  de Lychrel est un nombre naturel qui ne peut pas former de nombre palindrome lorsqu'il est soumis au processus\
itératif qui consiste à l'additionner au nombre formé de l'inversion de ses chiffres en base 10.\
Le plus petit nombre suspecté d'être de Lychrel est 196.")
print("    Vue qu'on ne peut itérer un tel processus à l'infini, on se contentera de déterminer les nombres vérifiant cet algorithme\
jusqu'à un rang n : ils seront appelés pseudo-nombres de Lychrel d'ordre n. Mieux encore, on déterminera ces nombres dans [m, M[", end = '\n\n')
    
def is_palindrome(S:str):
    """It tests if S is a palindrome or not"""
    for i in range(int(len(S)/2)):
        if S[i] != S[-i-1]:
            return False
    return True

def is_Lichrel(numb:int, n:int = 100):
    """It tests if numb is a pseudo-number of Lychrel of order n"""
    if is_palindrome(str(numb)) == True:
            return False
    for i in range(n):
        numb = numb+int(str(numb)[-1::-1])
        if is_palindrome(str(numb)) == True:
            return False
    return True

while True:
    try:
        n, m, M = tuple(input("Veuillez entrer n m et M (de la forme n,m,M) : ").split(','))
        assert any([n.isdigit() == False, m.isdigit() == False, M.isdigit() == False]) == False
        n, m, M = int(n), int(m), int(M)
        break
    except:
        print("Données invalides.")
    
print(f"\nLes pseudo-nombres de Lychrel d'ordre {n} emtre {m} et {M} sont : ", end = '')

for i in range(m, M):
    if is_Lichrel(i, n) == True:
        print(i, end = ' ')

input("\n\nRavi de vous avoir servi!")