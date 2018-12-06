class triangle:

    def checktriangle():
        count = 1
        for i in range(1,28):

            try:

                    x = int(input("Enter the value of x:"))
                    y = int(input("Enter the value of y:"))
                    z = int(input("Enter the value of z:"))
                    if((0 <= x <= 100) and (0 <= y <= 100) and (0 <= z <= 100)):
                        if (x == 0 or y == 0 or z == 0):
                            print(str(count) + ".This is Not a triangle")
                            count = count + 1
                        elif (x == y == z):
                            print( str(count) +".This is Equilateral triangle")
                            count = count + 1
                        elif ((x == y != z) or (x == z != y) or (y == z != x)):
                            print(str(count ) + ".This is Isosceles triangle")
                            count = count + 1
                        elif ((x != y != z) or (x != z != y) or (y != z != x)):
                            print(str(count ) + ".This is Scalene triangle")
                            count = count+1

                    else:
                            print("Enter the values between 1-100")


            except ValueError:
                    print("Not an integer! Try again.")
                    continue

triangle.checktriangle()








