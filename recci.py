def compoundinterest(principal0,principal,rate,n,time,itera):
    if(itera==n*time):
        return (principal-principal0)
    interest=principal*(rate/(n * 100))
    return compoundinterest(principal0,principal + interest,rate,n,time,itera + 1)
def main():
    principal=float(input("principal:"))
    rate=float(input("interest rate:"))
    n=int(input("compound year:"))
    time=int(input("year:"))
    comp_interest= compoundinterest(principal,principal,rate,n,time, 0)
    print("Compound interest is:",round(comp_interest, 3))
main()


