## the input
expression = input("EXPRESSION:" )
## varibles
x, y, z = expression.split(" ")
# x & z became  float
x_ =float(x)
z_ =float(z)
#CALCULATE
match y:
    case "*":
        res= x_ * z_
    case "+":
        res= x_ + z_
    case "/":
        res= x_ / z_
    case "-":
        res = x_ - z_
print(res)
