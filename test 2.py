import re
import ipaddress
import matplotlib.pyplot as plt


class GravitationalForce:
    """
    A class to calculate the gravitational force between two bodies and plot it.
    """
    def __init__(self, m1, m2, G):
        self.m1 = m1  # Mass of first body in kg
        self.m2 = m2  # Mass of second body in kg
        self.G = G    # Gravitational constant in N·m²/kg²

    def calculate_force(self, r):
        """
        Calculate the gravitational force for a given distance r.
        """
        return (self.G * self.m1 * self.m2) / (r**2)

    def plot_force_vs_distance(self, start, stop, interval):
        """
        Plot the gravitational force as a function of distance.
        """
        distances = list(range(start, stop + 1, interval))
        forces = [self.calculate_force(r) for r in distances]

        # Plot the graph
        plt.figure(figsize=(8, 6))
        plt.plot(distances, forces, marker='o', color='b')
        plt.title("Gravitational Force vs Distance", fontsize=14)
        plt.xlabel("Distance (m)", fontsize=12)
        plt.ylabel("Gravitational Force (N)", fontsize=12)
        plt.grid(True)
        plt.show()


def validate_ipv6(address):
    """
    Validate whether the given input is a strict IPv6 address.
    """
    try:
        ip = ipaddress.IPv6Address(address)
        return True
    except ipaddress.AddressValueError:
        return False


def validate_email(email):
    """
    Validate whether the given input is a strict email address.
    """
    email_regex = re.compile(
        r"^(?!.*\.\.)(?!.*\.$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    return bool(email_regex.match(email))


def main():
    """
    Main function to accept user input for email and IPv6 validation, and gravitational force calculation.
    """
    print("Welcome to the Validation and Gravitational Force Tool!")

    while True:
        print("\nPlease choose an option:")
        print("1. Validate an IPv6 address")
        print("2. Validate an email address")
        print("3. Calculate and plot gravitational force")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            ipv6 = input("Enter an IPv6 address to validate: ").strip()
            if validate_ipv6(ipv6):
                print(f"The IPv6 address '{ipv6}' is VALID.")
            else:
                print(f"The IPv6 address '{ipv6}' is INVALID.")

        elif choice == "2":
            email = input("Enter an email address to validate: ").strip()
            if validate_email(email):
                print(f"The email address '{email}' is VALID.")
            else:
                print(f"The email address '{email}' is INVALID.")

        elif choice == "3":
            # Gravitational force calculation and plotting
            m1 = 0.5  # Mass of the first body (kg)
            m2 = 1.5  # Mass of the second body (kg)
            G = 6.674 * (10**-11)  # Gravitational constant (N·m²/kg²)

            gravitation = GravitationalForce(m1, m2, G)
            print("Calculating gravitational force between two bodies (m1=0.5kg, m2=1.5kg) from 100m to 1000m...")
            gravitation.plot_force_vs_distance(start=100, stop=1000, interval=50)

        elif choice == "4":
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

print('hello')
