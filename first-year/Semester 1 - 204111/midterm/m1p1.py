def generate_p_triple(m: int,n :int) -> None:
    m,n = max(m,n),min(m,n)
    a = (m**2) - (n**2)
    b = 2*m*n 
    c = (m**2) + (n**2)
    print(f'{a} {b} {c}')