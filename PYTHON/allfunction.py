class more():
    def subfield():
        LIST=["Machine Learning","neural networks","vision","robotics","speech processing","natural language processing"]
        print("Sub-fields in AI are:")
        for i in LIST:
            print(i)
    def oddeven():
        a=int(input("Enter the number:"))  
        if(a%2==0):
             print(a,"is even number")      
        else:
            print(a,"is odd number")              
    def elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="male" and age==30):
            print("ELIGIBLE")
            marrige="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            marrige="NOT ELIGIBLE"
            return marrige
    def percentage():
        a=int(input("Subject1="))
        b=int(input("Subject2="))
        c=int(input("Subject3="))
        d=int(input("Subject4="))
        e=int(input("Subject5="))
        add=a+b+c+d+e
        print("total:",add)
        pr=(a+b+c+d+e)/5
        print("percantage:",pr) 
    def triangle():
        a=int(input("height:"))
        b=int(input("breadth:"))
        print("areaformula:(height*breadth)/2")
        print("area formula:",(a*b)/2)
        x=int(input("height1:"))
        y=int(input("height2:"))
        z=int(input("breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",x+y+z)
        