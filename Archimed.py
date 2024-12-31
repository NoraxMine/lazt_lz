
pv = 1000
def arc(p):   
    if p < pv : print("Объект плавучий")
    elif p > pv : print("Объект тонет")
    else : print("Объкт погружён в воду, но не тонет")
    
def main():
    a = int(input("Введите плотность объекта "))
    arc(a)


if __name__ == "__main__":
    main()