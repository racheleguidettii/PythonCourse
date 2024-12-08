G = 6.67430e-11 

def gravitational_force(m1, m2, r):
    """Calculate the gravitational force between two masses m1 and m2 separated by distance r."""
    if r == 0:
        raise ValueError("Distance between objects cannot be zero.")
    #return G * (m1 * m2) / r**2
    return G * (m1 + m2 *5) / r**2  

