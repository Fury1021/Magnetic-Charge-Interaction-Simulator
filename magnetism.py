class FORCE:
    def F(self):
        import os
        os.system('cls')
        print("What is the status of the Charge")
        print("1. Moving charge is INTO and has Positive Charge")
        print("2. Moving charge is INTO and has Negative Charge")
        print("3. Moving charge is OUTOF and has Positive Charge")
        print("4. Moving charge is OUTOF and has Negative Charge")
        option = int(input("Type your option: "))
        if option == 1:
            FM.Pinto()
        elif option == 2:
            FM.Poutof()
        elif option == 3:
            FM.Ninto()
        elif option == 4:
            FM.Noutof()
            


class LENGTH:
    def L(self):
        import os
        os.system('cls')
        F = float(input("What is the Force (N): "))
        I = float(input("What is the Current (amp): "))
        T= float(input("What is the Magnetic Field (T): "))

        ib = I * T
        L = F / ib
        print("The Length is: ", L)
            
class Menu:
    def MN(self):
        import os
        os.system('cls')
        print("1. Force is determined")
        print("2. Lenght is determined")
        option = int(input("What is determined?: "))
        if option == 1:
            f.F()
        elif option == 2:
            l.L()


class FMOVING:
    def Pinto(self):
        import os
        os.system('cls')
        I = float(input("What is the Current (amp): "))
        L = float(input("What is the Length (cm): "))
        T= float(input("What is the Magnetic Field (T): "))
        A= float(input("What is the theta or angle: "))
        option = input("What is the Trigonometric Function? cos, sin, tan: ")
        S = I * L * T * A
        import math
        if option == 'sin':
            F = math.sin((math.radians(S)))
        elif option == 'con':
            F = math.con((math.radians(S)))
        elif option == 'tan':
            F = math.tan((math.radians(S)))
        
        direction = input("What is the direction of the magnetic field: ")
        if direction == 'LEFT' or 'Left' or 'left':
            print("The FORCE is: ",F, "N Upward")
        elif direction == 'DOWN' or 'Down' or 'down':
            print("The FORCE is: ",F, "N Left")
        elif direction == 'RIGHT' or 'Right' or 'Right':
            print("The FORCE is: ",F, "N Downward")
        elif direction == 'UP' or 'Up' or 'up':
            print("The FORCE is: ",F, "N Right")

    def Poutof(self):
        import os
        os.system('cls')
        I = float(input("What Current (amp): "))
        L = float(input("What is the Length (cm): "))
        T= float(input("What is the Magnetic Field (T): "))
        A= float(input("What is the theta or angle: "))
        F = I * L * T * A
        option = input("What is the Trigonometric Function? cos, sin, tan: ")
        S = I * L * T * A
        import math
        if option == 'sin':
                F = math.sin((math.radians(S)))
        elif option == 'con':
            F = math.con((math.radians(S)))
        elif option == 'tan':
            F = math.tan((math.radians(S)))
        
        direction = int(print("What is the direction of the magnetic field: "))
        if direction == 'RIGHT'or'Right'or'Right':
            print("The FORCE is: ",F, "N Upward")
        elif direction == 'DOWN'or'Down'or'down':
            print("The FORCE is: ",F, "N Right")
        elif direction == 'LEFT'or'Left'or'left':
            print("The FORCE is: ",F, "N Downward")
        elif direction == 'UP'or'Up'or'up':
            print("The FORCE is: ",F, "N Left")

    def Ninto(self):
        import os
        os.system('cls')
        I = float(input("What Current (amp): "))
        L = float(input("What is the Length (cm): "))
        T= float(input("What is the Magnetic Field (T): "))
        A= float(input("What is the theta or angle: "))
        F = I * L * T * A
        option = input("What is the Trigonometric Function? cos, sin, tan: ")
        S = I * L * T * A
        import math
        if option == 'sin':
            F = math.sin((math.radians(S)))
        elif option == 'con':
            F = math.con((math.radians(S)))
        elif option == 'tan':
            F = math.tan((math.radians(S)))        
        direction = int(print("What is the direction of the magnetic field: "))
        if direction == 'RIGHT'or'Right'or'Right':
            print("The FORCE is: ",F, "N Upward")
        elif direction == 'DOWN'or'Down'or'down':
            print("The FORCE is: ",F, "N Right")
        elif direction == 'LEFT'or'Left'or'left':
           print("The FORCE is: ",F, "N Downward")
        elif direction == 'UP'or'Up'or'up':
            print("The FORCE is: ",F, "N Left")

    def Noutof(self):
        import os
        os.system('cls')
        I = float(input("What Current (amp): "))
        L = float(input("What is the Length (cm): "))
        T= float(input("What is the Magnetic Field (T): "))
        A= float(input("What is the theta or angle: "))
        F = I * L * T * A
        option = input("What is the Trigonometric Function? cos, sin, tan: ")
        S = I * L * T * A
        import math
        if option == 'sin':
            F = math.sin((math.radians(S)))
        elif option == 'con':
            F = math.con((math.radians(S)))
        elif option == 'tan':
            F = math.tan((math.radians(S)))        
        
        direction = input("What is the direction of the magnetic field: ")
        if direction == 'LEFT'or'Left'or'left':
            print("The FORCE is: ",F, "N Upward")
        elif direction == 'DOWN'or'Down'or'down':
            print("The FORCE is: ",F, "N Left")
        elif direction == 'RIGHT'or'Right'or'Right':
            print("The FORCE is: ",F, "N Downward")
        elif direction == 'UP'or'Up'or'up':
            print("The FORCE is: ",F, "N Right")
        


FM = FMOVING()
f = FORCE()
l = LENGTH()
m = Menu()
m.MN()
