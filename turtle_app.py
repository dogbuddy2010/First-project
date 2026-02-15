# Import turtle to run the graphics program.
import turtle


def get_user_input(prompt, default):
    """Helper function to get user input with default value"""
    val = input(f"{prompt} [{default}]: ").strip()
    return val if val else default

def is_yes(value):
    """Return True when user enters a yes-like response."""
    return value.strip().lower() in {"y", "yes"}


# Turtle customization allows users to set speed, appearance, color, and shape.
def customize_turtle_speed():
    """Customize the turtle speed (0-10)"""
    try:
        speed = int(get_user_input("Choose turtle speed (0-10, 0 is fastest)", "5"))
        return max(0, min(10, speed))
    except ValueError:
        print("Invalid input. Using default speed 5.")
        return 5


def customize_turtle_appearance():
    """Customize how the turtle looks (shape)"""
    shape = get_user_input("Choose turtle shape (turtle, arrow, circle, square, triangle, classic)", "turtle")
    return shape


def customize_turtle_color():
    """Customize the turtle color"""
    color = get_user_input("Choose turtle color (e.g., red, blue, green, purple, orange)", "blue")
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
    shape = get_user_input("Choose a shape to draw", "square").lower()
    return shape


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
    else:
        print(f"Warning: '{shape_name}' is not a recognized shape. Drawing a square instead.")
        draw_shape(t, 'square', size)


def run_turtle_drawing(t):
    """Run the turtle customization and drawing process"""
    customize = input("Would you like to customize the turtle? (yes/no): ").strip()
    
    # Default settings
    speed = 5
    shape = "turtle"
    color = "blue"
    draw_shape_name = "square"
    size = 100
    
    if is_yes(customize):
        print("\n--- Turtle Customization ---")
        speed = customize_turtle_speed()
        shape = customize_turtle_appearance()
        color = customize_turtle_color()
        draw_shape_name = customize_shape_to_draw()
        
        try:
            size = int(get_user_input("Shape size in pixels", "100"))
            if size <= 0:
                print("Size must be positive. Using default size 100.")
                size = 100
        except ValueError:
            print("Invalid input. Using default size 100.")
            size = 100
    
    start = input("\nStart turtle now? (yes/no): ").strip()
    
    if not is_yes(start):
        print("Launch cancelled.")
        return False
    
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
    except Exception:
        print(f"Warning: '{color}' is not a valid color. Using default color 'blue'.")
        t.color("blue")
    
    # Apply shape
    try:
        t.shape(shape)
    except Exception:
        print(f"Warning: '{shape}' is not a valid shape. Using default shape 'turtle'.")
        t.shape("turtle")
    
    # Draw the requested shape
    draw_shape(t, draw_shape_name, size)
    
    return True


def main():
    """Main function to run the turtle program"""
    launch = input("Would you like to launch the Turtle mode? (yes/no): ").strip()
    
    if not is_yes(launch):
        print("Turtle mode not launched.")
        return
    
    try:
        screen = turtle.Screen()
        screen.title("Turtle Graphics")
        screen.setup(width=800, height=600)
        t = turtle.Turtle()
    except turtle.Terminator:
        print("Turtle window was closed. Please run the program again.")
        return

    # Loop to allow multiple drawings
    while True:
        # Run the turtle drawing
        drawing_completed = run_turtle_drawing(t)
        
        if not drawing_completed:
            print("Turtle Program cancelled. Goodbye!")
            break
        
        # Ask if user wants to draw again
        print("\n" + "="*50)
        draw_again = input("Would you like to draw again? (yes/no): ").strip()
        print("="*50 + "\n")
        
        if not is_yes(draw_again):
            print("Thank you for using Turtle. Goodbye!")
            break

    try:
        screen.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()

print("hello world")