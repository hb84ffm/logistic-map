# app.py
import streamlit as st
from simulation.simulation import LogisticMap
import seaborn as sns
import time
import os

sns.set_theme(style="darkgrid")

# Title
st.title("Chaotic behaviour of logistic map", anchor=False)

# Sidebar inputs
st.sidebar.title("Parameter selection")
st.markdown(r'Simulation of the [logistic map](https://en.wikipedia.org/wiki/Logistic_map) $x_{n+1}=rx_{n}(1-x_{n+1})$ for varying values of $r$.')
st.markdown(r'Chaos starts at $r \approx 3.57$,which is known as [Feigenbaum constant](https://en.wikipedia.org/wiki/Feigenbaum_constants), where dynamics becomes very sensitive to small changes in start values.')
st.markdown("Following observations can be identified:")
st.latex(r"r < 1 \implies x_{n+1} \to 0")
st.latex(r"1 < r < 3 \implies x_{n+1} \to \frac{r - 1}{r}")
st.latex(r"3 < r < 3.57 \implies x_{n+1} \to \text{periodic cycles of } 2^k \text{ with } k \in \mathbb{N}")
st.latex(r"3.57 < r \leq 4 \implies x_{n+1} \to \text{pure chaos}")

r_start = float(st.sidebar.text_input(r"$r_{start}$", "1.0", help=r"Select $r_{start} \leq r_{end}$, usually with $r_{start},r_{end} \in [0,4]$."))
r_final = float(st.sidebar.text_input(r"$r_{end}$", "4.0", help=r"Select $r_{start} \leq r_{end}$, usually with $r_{start},r_{end} \in [0,4]$."))
discretization = int(st.sidebar.text_input("Nr of points", "10", 
                                help=r"Controls how fine $[r_{end},r_{start}]$ is divided, larger values create more simulations with better resolution, but longer compute."))
steps = int(st.sidebar.text_input(r"Iterations per $r$", "100", 
                                help=r"Controls how many iterations are created for a given $r$, larger values create more stable results, but longer compute."))
x_0 = float(st.sidebar.text_input(r"Start value $x_0$", "0.1", help=r"Start value of $x_0$, usually $x_0 \in [0,1]$."))
delay = st.sidebar.slider("Animation speed (seconds)", min_value=0.01, max_value=1.0, value=0.1, step=0.01)

start_simulation = st.sidebar.button("Start")

if start_simulation:
    col1, col2 = st.columns(2)
    placeholder_orbit = col1.empty()
    placeholder_divergence = col2.empty()

    logistic_map = LogisticMap(r_start, 
                               r_final, 
                               discretization,
                               steps, 
                               x_0, 
                               placeholder_orbit,
                               placeholder_divergence, 
                               delay)
    logistic_map.run()

# Exit button
exit_clicked = st.sidebar.button("Exit", type="primary")
if exit_clicked:
    st.toast("Logout!", icon="🌴")
    time.sleep(0.5)
    os._exit(0)
