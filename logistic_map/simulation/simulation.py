# simulation.py
import numpy as np
import matplotlib.pyplot as plt

class LogisticMap:
    """ Class for the chaotic behaviour of the logistic map"""
    def __init__(self, 
                 r_start, 
                 r_final, 
                 discretization, 
                 steps, 
                 x_0,
                 placeholder_orbit, 
                 placeholder_divergence, 
                 delay):
        
        self.r_start = r_start
        self.r_final = r_final
        self.discretization = discretization
        self.steps = steps
        self.x_0 = x_0
        self.placeholder_orbit = placeholder_orbit
        self.placeholder_divergence = placeholder_divergence
        self.delay = delay
        self.r_values = np.arange(r_start, r_final + discretization, discretization)
        self.r_values = self.r_values[self.r_values <= r_final]

    def compute_orbit(self, r):
        """ implements the recursion"""
        x = [self.x_0]
        for _ in range(self.steps - 1):  # x_{n+1} = r * x_n * (1 - x_n)
            x_next = r * x[-1] * (1 - x[-1])
            x.append(x_next)
        return x

    def compute_variation(self, x):
        """ calcualtes the variation of xn and xn+1"""
        return np.abs(np.diff(x))

    def plot_orbit(self, r, x):
        """plots trajectories of orbits"""
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.plot(range(self.steps), x, marker='.', linewidth=0.5, color="#130153")
        ax1.set_xlim(-0.5, self.steps + 0.5)
        ax1.set_ylim(-0.05, 1.05)
        ax1.set_xlabel("Iterations")
        ax1.set_ylabel(r'$x_n$')
        ax1.set_title(f"Orbit for $r = {r:.3f}$")
        ax1.grid(False)
        self.placeholder_orbit.pyplot(fig1)
        plt.close(fig1)

    def plot_variation(self, r, differences):
        """plots trajectory of variation"""
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.plot(range(self.steps - 1), differences, linewidth=0.8, color="#BA9803")
        ax2.set_xlim(-0.5, self.steps - 1 + 0.5)

        if max(differences) > 0:
            ymax = max(differences) * 1.1
        else:
            ymax = 0.1

        ax2.set_ylim(-0.05, ymax)
        ax2.set_xlabel("Iterations")
        ax2.set_ylabel(r"$|x_{n+1} - x_n|$")
        ax2.set_title(f"Variation for $r = {r:.3f}$")
        ax2.grid(False)
        ax2.ticklabel_format(axis='y', style='plain')
        self.placeholder_divergence.pyplot(fig2)
        plt.close(fig2)

    def run(self):
        """orchestartes the methods to run the simulation"""
        import time
        for r in self.r_values:
            x = self.compute_orbit(r)
            differences = self.compute_variation(x)
            self.plot_orbit(r, x)
            self.plot_variation(r, differences)
            time.sleep(self.delay)
