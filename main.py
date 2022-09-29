import sympy
x,y,m,c = sympy.symbols("x y m c")

laser = {"origin": [-150,0], "vector": [1,0.2]}
glass_pane = {"origin": [0,-150], "vector": [0,1], "gradient": 0}
object_list = [laser, glass_pane]

for object in object_list:
    # find the gradient using the direction vector
    try:
        object["gradient"] = object["vector"][1] / object["vector"][0]
    except ZeroDivisionError:
        object["gradient"] = "infinity"
        object["line equation"] = sympy.Eq(x, object["origin"][0])
        continue
    expr = sympy.Eq(y, m*x+c)
    # substitute in values given in the origin and gradient then solve for c
    expr = expr.subs([(y, object["origin"][1]), (x, object["origin"][0]), (m, object["gradient"])])
    y_intercept = sympy.solve(expr)[0]
    object["line equation"] = sympy.Eq(y, object["gradient"]*x+y_intercept)

print(laser)
print(glass_pane)
# calculate m

# calculate c by setting x to 0 and solving for y in y=mx+c

# find intersection using simultaneous equation
