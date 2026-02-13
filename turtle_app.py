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
            size = int(get_input("Square size in pixels", str(size)))
        except ValueError:
            size = 100

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

        # Draw a square of the requested size
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

