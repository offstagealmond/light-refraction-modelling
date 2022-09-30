import sympy, turtle, math
x,y,m,c = sympy.symbols("x y m c")

laser = {"origin": [-100,0], "vector": [5,1], "current medium ri": 1}
glass_pane = {"origin": [0,-150], "endpoint": [0,150], "vector": None, "refractive index": 1.52}
object_list = [laser, glass_pane]

intersection_coordinates = []
gradient_of_refracted_laser = None

for object in object_list:
    # find the gradient using the direction vector
    try:
        if object["vector"] == None:
            object["vector"] = [(object["origin"][0] - object["endpoint"][0]), (object["origin"][1] - object["endpoint"][1])]
        object["gradient"] = object["vector"][1] / object["vector"][0]
    except ZeroDivisionError: # if the gradient is infinity
        object["gradient"] = "infinity"
        object["eq"] = sympy.Eq(x, object["origin"][0])
    else:
        expr = sympy.Eq(y, m*x+c)
        # substitute in values given in the origin and gradient then solve for c
        expr = expr.subs([(y, object["origin"][1]), (x, object["origin"][0]), (m, object["gradient"])])
        y_intercept = sympy.solve(expr)[0]
        object["y intercept"] = y_intercept
        object["eq"] = sympy.Eq(y, object["gradient"]*x+y_intercept) # form the line equation
    finally:
        if object == laser:
            continue
        solve_for_coordinates = sympy.solve([laser["eq"], object["eq"]], (x,y))
        solve_for_coordinates = [solve_for_coordinates[x], solve_for_coordinates[y]]
        intersection_coordinates.append(solve_for_coordinates)

for count, object in enumerate(object_list):
    count-=1
    if object == laser:
        continue
    if object["gradient"] == "infinity":
        normal = sympy.Eq(y, intersection_coordinates[count][1])
        angle_of_intersection = sympy.atan(laser["gradient"])
        angle_of_refraction = sympy.asin((laser["current medium ri"]*sympy.sin(angle_of_intersection)) / object["refractive index"])
        gradient_of_refracted_laser = sympy.tan(angle_of_refraction)
        refracted_laser_equation = sympy.Eq(y, gradient_of_refracted_laser*x+intersection_coordinates[0][1])
    else:
        normal_gradient = (-1/object["gradient"])
        normal = sympy.Eq(y, normal_gradient*x+intersection_coordinates[count][1])
        difference_of_gradients = laser["gradient"] - normal_gradient
        angle_of_intersection = sympy.atan(difference_of_gradients)
        angle_of_refraction = sympy.asin((laser["current medium ri"]*sympy.sin(angle_of_intersection)) / object["refractive index"])
        gradient_of_refracted_laser = sympy.tan(angle_of_refraction)
        refracted_laser_equation = sympy.Eq(y, gradient_of_refracted_laser*x+intersection_coordinates[0][1])
    print(refracted_laser_equation)
    print(angle_of_intersection, angle_of_refraction)
    print(laser["gradient"], gradient_of_refracted_laser)
    print(refracted_laser_equation)


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
turtle_laser.setpos(intersection_coordinates[0])
turtle_laser.setpos(1000, 1000*gradient_of_refracted_laser)
# calculate m

# calculate c by setting x to 0 and solving for y in y=mx+c

# find intersection using simultaneous equation
