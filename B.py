def collision(m, M, v, V):
    d = -1 * (v - V)
    momentum_total = (M * V) + (m * v)

    a = [m, M, momentum_total]
    b = [M, M, M * d]

    elim_1 = a[0] + b[0]
    elim_2 = a[2] + b[2] 

    vm_2 = elim_2 / elim_1
    V_2 = vm_2 - d
    result = [vm_2, V_2]
    return(result)

def main():  
    image = []  
    M = float(input())
    m = float(input())
    V = float(input())
    L = float(input())

    v = 0
    n = 0
    t_col = 0
    n_benda = 0
    n_tembok = 0
    c = collision(m, M, v, V)
    vm_2 = c[0]
    V_2 = c[1]
    d_min = L
    n_benda += 1
    image.append("O >< O")

    if vm_2 > 0:
        t_tembok = L / vm_2
        n_tembok += 1
        image.append("O > |")
        t_col += t_tembok
    vm_3 = -1 * vm_2
    print(f"{L} {V_2} {vm_2}")


    while V_2 > 0:
        s_V2 = V_2 * t_tembok
        d_V2 = L - s_V2
        t_aftertembok = (d_V2 / ((vm_3 * -1) + V_2))
        t_col += t_tembok + t_aftertembok
        L = abs(t_aftertembok * vm_3)

        c = collision(m, M, vm_3, V_2)
        vm_2 = c[0]
        V_2 = c[1]
        n_benda += 1
        image.append("O >< O")
        if L < d_min:
            d_min = L

        if vm_2 > 0:
            t_tembok = L / vm_2
            t_col += t_tembok
            n_tembok += 1
            image.append("O > |")
        vm_3 = -1 * vm_2
        print("-----")
        print(f"{L} {V_2} {vm_2}")
    
    while abs(V_2) < abs(vm_3):
        t_ToCol = (2 * L) / (vm_2 - abs(V_2))
        t_col += t_ToCol - t_tembok
        L += t_ToCol * abs(V_2)

        c = collision(m, M, vm_3, V_2)
        vm_2 = c[0]
        V_2 = c[1]
        n_benda += 1
        image.append("O >< O")

        if L < d_min:
            d_min = L

        if vm_2 > 0:
            t_tembok = L / vm_2
            n_tembok += 1
            image.append("O > |")
            t_col += t_tembok
        vm_3 = -1 * vm_2

        print("****")
        print(f"{L} {V_2} {vm_2}")
    n = n_benda + n_tembok
    print(f"{n} {round(t_col, 2)} {round(d_min, 2)}")
    
    
    for x in range(len(image)):
        print(image[x], end=' then ')
    print('End')
if __name__ == '__main__':
    main()
