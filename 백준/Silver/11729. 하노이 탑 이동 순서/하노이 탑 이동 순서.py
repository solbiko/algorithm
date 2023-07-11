n=int(input())

    
def hanoi(from_pos, to_pos, aux_pos, n):
    if n == 1: 
        print(from_pos, to_pos)
        return

    hanoi(from_pos, aux_pos, to_pos, n-1)
    print(from_pos, to_pos)
    hanoi(aux_pos, to_pos, from_pos, n-1)

print(2**n-1) 
hanoi(1,3,2,n)
