import matplotlib.pyplot as plt
import numpy as np

def draw_caesar_cipher_disk():
    outer_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    inner_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Create a figure and a single subplot
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.set_aspect('equal')

    # Define radius for outer and inner circles
    radius_outer = 1
    radius_inner = 0.8

    # Calculate angles for each letter
    theta = np.linspace(0, 2 * np.pi, len(outer_letters), endpoint=False)

    # Draw the outer circle letters
    for i, letter in enumerate(outer_letters):
        x = radius_outer * np.cos(theta[i])
        y = radius_outer * np.sin(theta[i])
        ax.text(x, y, letter, ha='center', va='center', fontsize=14, fontweight='bold')

    # Draw the inner circle letters
    for i, letter in enumerate(inner_letters):
        x = radius_inner * np.cos(theta[i])
        y = radius_inner * np.sin(theta[i])
        ax.text(x, y, letter, ha='center', va='center', fontsize=12)

    plt.subplots_adjust(left=0.4, bottom=0.5, right=1.0, top=0.9, wspace=0.2, hspace=0.2)

    # Remove axes
    ax.axis('off')
    # Display the plot
    plt.show()

# Run the function
draw_caesar_cipher_disk()
