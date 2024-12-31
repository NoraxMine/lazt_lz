import Archimed as arc
import pyramid as pyr

def main():
    user_choes = input("Введите 1 для определения плавучести предмета\nВведите 2 для вычисления объёма пирамиды")
    #user_temp = input("")
    if user_choes.lower() == "1" :
        print("", arc.main())
    elif user_choes.lower() == "2" :
        print("", pyr.roe())   
        main()
    


if __name__ == "__main__":
    main()