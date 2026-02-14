def get_input(prompt, default):
    val = input(f"{prompt} [{default}]: ").strip()
    return val if val else default


launch = input("Would you like to launch the Turtle mode? (yes/no): ").strip()
if launch.lower() == "yes":
    customize = input("Would you like to customize the turtle? (yes/no): ").strip()

    # Defaults
    color = "blue"
    shape = "turtle"
    speed = 3
    pen_size = 2
    size = 100
    draw_shape = "square"

    if customize.lower() == "yes":
        color = get_input("Choose turtle color", color)
        shape = get_input("Choose turtle shape (classic, turtle, circle, square)", shape)
        try:
            speed = int(get_input("Choose speed (0-10)", str(speed)))
            speed = max(0, min(10, speed))
        except ValueError:
            speed = 3
        try:
            pen_size = int(get_input("Pen size (1-10)", str(pen_size)))
            pen_size = max(1, min(10, pen_size))
        except ValueError:
            pen_size = 2
        try:
            size = int(get_input("Shape size in pixels", str(size)))
        except ValueError:
            size = 100
        draw_shape = get_input("Choose shape to draw (square, triangle, circle, pentagon, hexagon, star)", draw_shape)

    start = input("Start turtle now? (yes/no): ").strip()
    if start.lower() == "yes":
        import turtle

        # Create a screen object
        screen = turtle.Screen()
        screen.title("Turtle Graphics")
        screen.setup(width=800, height=600)

        # Create a turtle object with chosen settings
        t = turtle.Turtle()
        try:
            t.color(color)
        except Exception:
            print(f"Warning: '{color}' is not a valid color. Using default color 'blue'.")
            t.color("blue")  # Fallback to default color if invalid
        try:
            t.shape(shape)
        except Exception:
            pass
        t.pensize(pen_size)
        t.speed(speed)

        # Draw the requested shape
        draw_shape = draw_shape.lower()
        if draw_shape == "square":
            for _ in range(4):
                t.forward(size)
                t.right(90)
        elif draw_shape == "triangle":
            for _ in range(3):
                t.forward(size)
                t.left(120)
        elif draw_shape == "circle":
            t.circle(size)
        elif draw_shape == "pentagon":
            for _ in range(5):
                t.forward(size)
                t.right(72)
        elif draw_shape == "hexagon":
            for _ in range(6):
                t.forward(size)
                t.right(60)
        elif draw_shape == "star":
            for _ in range(5):
                t.forward(size)
                t.right(144)
        else:
            print(f"Warning: '{draw_shape}' is not a recognized shape. Drawing a square instead.")
            for _ in range(4):
                t.forward(size)
                t.right(90)

        # Keep the window open
        turtle.done()
        print("Turtle Program completed. Thank you for using Turtle. Goodbye!")
    else:
        print("Launch cancelled.")
else:
    print("Turtle mode not launched.")

