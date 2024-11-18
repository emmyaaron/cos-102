


# Physics Calculator




def calculate_kinetic_energy():
    """Calculate kinetic energy: KE = 0.5 * m * v^2"""
    mass = float(input("Enter the mass of the object (in kg): "))
    velocity = float(input("Enter the velocity of the object (in m/s): "))
    kinetic_energy = 0.5 * mass * velocity**2
    print(f"Kinetic Energy = {kinetic_energy} Joules\n")

def calculate_gravitational_force():

    """Calculate gravitational force: F = G * (m1 * m2) / r^2"""
    G = 6.67430e-11  # Gravitational constant (m^3 kg^−1 s^−2)
    m1 = float(input("Enter the mass of the first object (in kg): "))
    m2 = float(input("Enter the mass of the second object (in kg): "))
    r = float(input("Enter the distance between the objects (in meters): "))
    gravitational_force = G * (m1 * m2) / r**2
    print(f"Gravitational Force = {gravitational_force} N\n")

def calculate_work_done():
    """Calculate work done: W = F * d * cos(θ)"""
    force = float(input("Enter the force applied (in Newtons): "))
    distance = float(input("Enter the distance traveled (in meters): "))
    angle = float(input("Enter the angle between the force and the direction of motion (in degrees): "))
    import math
    angle_rad = math.radians(angle)  # Convert angle to radians
    work_done = force * distance * math.cos(angle_rad)
    print(f"Work Done = {work_done} Joules\n")

def calculate_Ohm_law():
    """Calculate Ohms law : V = I * R"""
    current = float(input("Enter the current (in Amperes): "))
    resistance = float(input("Enter the resistance (in Ohms): "))
    voltage = current * resistance
    print(f"Voltage = {voltage} Volts\n")

def calculate_velocity():
    """Calculate velocity: v = u + at """
    initial_velocity = float(input("Enter the initial velocity (in m/s): "))
    acceleration = float(input("Enter the acceleration (in m/s^2): "))
    time = float(input("Enter the time (in seconds): "))
    final_velocity = initial_velocity + acceleration * time
    print(f"Final Velocity = {final_velocity} m/s\n")

def main():
    while True:

        print("Physics Equations Calculator")
        print("1. Kinetic Energy (KE = 0.5 * m * v^2)")
        print("2. Gravitational Force (F = G * (m1 * m2) / r^2)")
        print("3. Work Done (W = F * d * cos(θ))")
        print("4. Ohm's Law (V = I * R)")
        print("5. Velocity (v = u + at)")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            calculate_kinetic_energy()
        if choice == '2':
            calculate_gravitational_force()
        if choice == '3':
            calculate_work_done()
        if choice == '4':
            calculate_Ohm_law()
        if choice == '5':
            calculate_velocity()
        if choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "_main_": main()