from math import sqrt

V = lambda S1,S2,H: 1/3 * H * (S1 + S2 + (sqrt(S1 * S2)) )


def roe(): 
    S1 = int(input("Введите площадь верхнего основания :"))
    S2 = int(input("Введите площадь нижнего основания :"))
    H = int(input("Введите высоту :"))
    print("Объём усечённой пирамиды :" + str(V(S1,S2,H)))

    
if __name__ == "__main__":
    roe()