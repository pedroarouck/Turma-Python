def power_of_two(num):

    if num == 0:
        return False

    while num > 1:
        if num % 2 == 0:
            num = num // 2
            return True
        else:
            return False

def dash_insert(a):
    nova_string = ''
    ultimo_digito = a[len(a)-1]
    for i in range(0,len(a)-1):
        digito = int(a[i])
        proximo_digito = int(a[i+1])

        if digito % 2 != 0 and proximo_digito % 2 != 0:
            nova_string = nova_string + str(digito) + '-'
        else:
            nova_string = nova_string + str(digito)
    return nova_string + ultimo_digito


print(dash_insert('12345679'))