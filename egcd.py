def egcd(a, b):
    # Find the Extended Eculidian Distance
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    
if __name__ == "__main__":
    x = 35
    y = 15
    gcd = egcd(x,y)
    print("GCD(", x, ",", y, "):", gcd[0])
    print(gcd)
