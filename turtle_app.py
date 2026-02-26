"""Interactive turtle drawing app with customizable and random modes."""

# Import turtle to run the graphics program.
import secrets
import turtle


VALID_TURTLE_SHAPES = {
    "turtle",
    "arrow",
    "circle",
    "square",
    "triangle",
    "classic",
}
VALID_DRAW_SHAPES = {
    "circle",
    "square",
    "triangle",
    "pentagon",
    "hexagon",
    "star",
    "potato",
    "poato",
    "random",
}


class StopProgram(Exception):
    """Raised when the user requests an immediate program stop."""


def ask_input(prompt):
    """Read user input and stop program immediately on Stop! command."""
    value = input(prompt)
    if value.strip().lower() == "stop!":
        raise StopProgram
    return value


def get_user_input(prompt, default):
    """Helper function to get user input with default value"""
    val = ask_input(f"{prompt} [{default}]: ").strip()
    return val if val else default


def get_bounded_int(prompt, default, minimum=None, maximum=None):
    """Get integer input with optional min/max bounds and default fallback."""
    try:
        value = int(get_user_input(prompt, str(default)))
    except ValueError:
        return default, True

    if minimum is not None:
        value = max(minimum, value)
    if maximum is not None:
        value = min(maximum, value)
    return value, False


def get_yes_no_input(prompt):
    """Prompt until user enters a valid yes/no response."""
    while True:
        answer = ask_input(f"{prompt} (yes/no): ").strip().lower()
        if answer in {"y", "yes", "n", "no"}:
            return answer in {"y", "yes"}
        print("Invalid response. Please enter yes or no.")


# Turtle customization allows users to set speed, appearance, color, and shape.
def customize_turtle_speed():
    """Customize the turtle speed (0-10)"""
    speed, used_default = get_bounded_int(
        "Choose turtle speed (0-10, 0 is fastest)", 5, minimum=0, maximum=10
    )
    if used_default:
        print("Invalid input. Using default speed 5.")
    return speed


def customize_turtle_appearance():
    """Customize how the turtle looks (shape)"""
    shape = get_user_input(
        (
            "Choose turtle shape "
            "(turtle, arrow, circle, square, triangle, classic)"
        ),
        "turtle",
    ).lower()
    if shape not in VALID_TURTLE_SHAPES:
        print(
            f"Warning: '{shape}' is not a valid shape. "
            "Using default shape 'turtle'."
        )
        return "turtle"
    return shape


def customize_turtle_color():
    """Customize the turtle color"""
    color = get_user_input(
        "Choose turtle color (e.g., red, blue, green, purple, orange)",
        "blue",
    )
    return color


def customize_shape_to_draw():
    """Customize what shape the turtle will draw"""
    print("\nAvailable shapes to draw:")
    print("  - circle")
    print("  - square")
    print("  - triangle")
    print("  - pentagon")
    print("  - hexagon")
    print("  - star")
    print("  - potato")
    print("  - random")
    shape = get_user_input("Choose a shape to draw", "square").lower()
    if shape not in VALID_DRAW_SHAPES:
        print(
            f"Warning: '{shape}' is not a recognized shape. "
            "Drawing a square instead."
        )
        return "square"
    return shape


def draw_random_art(t):
    """Draw a random composition with varied shapes, colors, and positions."""
    rng = secrets.SystemRandom()
    random_shapes = [
        "circle",
        "square",
        "triangle",
        "pentagon",
        "hexagon",
        "star",
        "potato",
    ]
    random_colors = [
        "red",
        "blue",
        "green",
        "purple",
        "orange",
        "gold",
        "magenta",
        "cyan",
        "black",
    ]

    for _ in range(12):
        shape_name = rng.choice(random_shapes)
        size = rng.randint(30, 120)
        x = rng.randint(-300, 300)
        y = rng.randint(-220, 220)
        heading = rng.randint(0, 359)
        color = rng.choice(random_colors)

        t.penup()
        t.goto(x, y)
        t.setheading(heading)
        t.pendown()

        try:
            t.color(color)
        except (turtle.TurtleGraphicsError, ValueError):
            t.color("blue")

        draw_shape(t, shape_name, size)


def draw_potato(t, size):
    """Draw a potato-like organic shape."""
    segments = [
        (35, 0.40),
        (28, 0.48),
        (42, 0.36),
        (25, 0.50),
        (50, 0.34),
        (30, 0.46),
        (45, 0.38),
        (25, 0.47),
        (40, 0.41),
        (40, 0.39),
    ]

    previous_pen_color = t.pencolor()
    previous_fill_color = t.fillcolor()
    t.pencolor("peru")
    t.fillcolor("saddlebrown")

    t.begin_fill()
    for turn_angle, segment_multiplier in segments:
        t.forward(size * segment_multiplier)
        t.right(turn_angle)
    t.end_fill()

    t.pencolor(previous_pen_color)
    t.fillcolor(previous_fill_color)


def draw_shape(t, shape_name, size):
    """Draw the specified shape with the turtle"""
    if shape_name == "circle":
        t.circle(size / 2)
    elif shape_name == "square":
        for _ in range(4):
            t.forward(size)
            t.right(90)
    elif shape_name == "triangle":
        for _ in range(3):
            t.forward(size)
            t.left(120)
    elif shape_name == "pentagon":
        for _ in range(5):
            t.forward(size)
            t.right(72)
    elif shape_name == "hexagon":
        for _ in range(6):
            t.forward(size)
            t.right(60)
    elif shape_name == "star":
        for _ in range(5):
            t.forward(size)
            t.right(144)
    elif shape_name in {"potato", "poato"}:
        draw_potato(t, size)
    else:
        print(
            f"Warning: '{shape_name}' is not a recognized shape. "
            "Drawing a square instead."
        )
        draw_shape(t, "square", size)


def run_turtle_drawing(t):
    """Run the turtle customization and drawing process"""
    customize = get_yes_no_input("Would you like to customize the turtle?")

    # Default settings
    speed = 5
    shape = "turtle"
    color = "blue"
    draw_shape_name = "square"
    size = 100

    if customize:
        print("\n--- Turtle Customization ---")
        speed = customize_turtle_speed()
        shape = customize_turtle_appearance()
        color = customize_turtle_color()
        draw_shape_name = customize_shape_to_draw()

        size, used_default = get_bounded_int(
            "Shape size in pixels", 100, minimum=1
        )
        if used_default:
            print("Invalid input. Using default size 100.")

    if draw_shape_name in {"potato", "poato"} and color == "blue":
        color = "saddlebrown"

    try:
        t.clear()
        t.penup()
        t.home()
        t.setheading(0)
        t.pendown()
    except turtle.Terminator:
        print("Turtle window was closed. Please run the program again.")
        return False

    # Apply speed
    t.speed(speed)

    # Apply color
    try:
        t.color(color)
    except (turtle.TurtleGraphicsError, ValueError):
        print(
            f"Warning: '{color}' is not a valid color. "
            "Using default color 'blue'."
        )
        t.color("blue")

    t.shape(shape)

    # Draw the requested shape
    if draw_shape_name == "random":
        draw_random_art(t)
    else:
        draw_shape(t, draw_shape_name, size)

    return True


def main():
    """Main function to run the turtle program"""
    screen = None
    print("Tip: type Stop! at any prompt to exit immediately.")

    try:
        launch = get_yes_no_input("Would you like to launch the Turtle mode?")

        if not launch:
            print("Turtle mode not launched.")
            return

        screen = turtle.Screen()
        screen.title("Turtle Graphics")
        screen.setup(width=800, height=600)
        t = turtle.Turtle()
    except turtle.Terminator:
        print("Turtle window was closed. Please run the program again.")
        return

    try:
        # Loop to allow multiple drawings
        while True:
            # Run the turtle drawing
            drawing_completed = run_turtle_drawing(t)

            if not drawing_completed:
                print("Turtle session ended.")
                break

            # Ask if user wants to draw again
            print("\n" + "="*50)
            draw_again = get_yes_no_input("Would you like to draw again?")
            print("="*50 + "\n")

            if not draw_again:
                print("Thank you for using Turtle. Goodbye!")
                break

        try:
            turtle.done()
        except turtle.Terminator:
            pass
    except StopProgram:
        print("Stop! detected. Exiting program. Please start again if you want to use Turtle.")
        if screen is not None:
            try:
                screen.bye()
            except turtle.Terminator:
                pass


if __name__ == "__main__":
    main()
