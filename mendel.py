#Mendelian Inheritance

def mendel(homoD, hetero, homoR):
    x= (homoD + hetero + homoR)
    return (1-   (  ((hetero**2-hetero)*0.25) + (hetero*homoR) + ((homoR**2-homoR)))/(x**2 - x)         )

print mendel(28,17,26)

#take in homodominant, hetero, and homo recessive, get probability of dominant in children
