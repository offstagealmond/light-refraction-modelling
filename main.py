import sympy, turtle, math
x,y,m,c = sympy.symbols("x y m c")

laser = {"origin": [-150,0], "vector": [1,0.2]}
glass_pane = {"origin": [5,-150], "endpoint": [5,150], "vector": None, "refractive index": 1.52}
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
    object["y intercept"] = y_intercept
    object["eq"] = sympy.Eq(y, object["gradient"]*x+y_intercept)

intersection_coordinates = sympy.solve([laser["eq"], glass_pane["eq"]], (x,y))
intersection_coordinates = [intersection_coordinates[x], intersection_coordinates[y]]
if glass_pane["gradient"] == "infinity":
    normal = sympy.Eq(y, intersection_coordinates[1])
    angle_of_intersection = sympy.atan(laser["gradient"])
    angle_of_refraction = sympy.asin(sympy.sin(angle_of_intersection) / glass_pane["refractive index"])
    gradient_of_refracted_laser = sympy.atan(angle_of_refraction)
    refracted_laser_equation = sympy.Eq(y, gradient_of_refracted_laser*x+intersection_coordinates[1])
    print(refracted_laser_equation)

print(laser)
print(glass_pane)

canvas = turtle.Screen()
turtle_laser = turtle.Turtle()
turtle_laser.hideturtle()
turtle_laser.color("red")
glass_pane_laser = turtle.Turtle()
glass_pane_laser.penup()
glass_pane_laser.color("gray")
glass_pane_laser.setpos(glass_pane["origin"])
glass_pane_laser.pendown()
glass_pane_laser.setpos(glass_pane["endpoint"])
turtle_laser.penup()
turtle_laser.setpos(laser["origin"])
turtle_laser.pendown()
turtle_laser.pensize(3)
turtle_laser.setpos(intersection_coordinates)
turtle_laser.setpos(1000, 1000*gradient_of_refracted_laser)
# calculate m

# calculate c by setting x to 0 and solving for y in y=mx+c

# find intersection using simultaneous equation
