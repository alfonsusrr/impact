M = float(input())
m = float(input())
VM = float(input())
vm = float(input())

if VM <= vm:
    print("Tidak ada tumbukan")
else:
    d = -1 * (vm - VM)
    momentum_total = (M * VM) + (m * vm)
    
    #Starts SPLDV solving
    #avm' + bVM' = c, dvm' - eVM' = f, d = e = 1

    a = [m, M, momentum_total]
    b = [M, M, M * d]

    elim_1 = a[0] + b[0]
    elim_2 = a[2] + b[2] 

    vm_2 = round(elim_2 / elim_1, 2)
    VM_2 = round(vm_2 - d, 2)

    print(f"{vm_2} {VM_2}")



