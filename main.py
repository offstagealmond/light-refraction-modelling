import sympy, turtle
x,y,m,c = sympy.symbols("x y m c")

laser = {"origin": [-150,0], "vector": [1,2.5]}
glass_pane = {"origin": [5,-150], "endpoint": [5,150], "vector": None}
object_list = [laser, glass_pane]

for object in object_list:
    # find the gradient using the direction vector
    try:
        if object["vector"] == None:
            glass_pane["vector"] = [(object["origin"][0] - object["endpoint"][0]), (object["origin"][1] - object["endpoint"][1])]
        object["gradient"] = object["vector"][1] / object["vector"][0]
    except ZeroDivisionError:
        object["gradient"] = "infinity"
        object["eq"] = sympy.Eq(x, object["origin"][0])
        continue
    expr = sympy.Eq(y, m*x+c)
    # substitute in values given in the origin and gradient then solve for c
    expr = expr.subs([(y, object["origin"][1]), (x, object["origin"][0]), (m, object["gradient"])])
    y_intercept = sympy.solve(expr)[0]
    object["eq"] = sympy.Eq(y, object["gradient"]*x+y_intercept)

print(sympy.solve([laser["eq"], glass_pane["eq"]], (x,y)))

print(laser)
print(glass_pane)

canvas = turtle.Screen()
# calculate m

# calculate c by setting x to 0 and solving for y in y=mx+c

# find intersection using simultaneous equation
