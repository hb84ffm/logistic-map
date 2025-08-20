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
r_start = float(st.sidebar.text_input(r"$r_{start}$", "1.0", help=r"Select $r_{start} \leq r_{end}$ and $r_{start},r_{end} \in [0,4]$"))
r_final = float(st.sidebar.text_input(r"$r_{end}$", "4.0", help=r"Select $r_{start} \leq r_{end}$ and $r_{start},r_{end} \in [0,4]$"))
discretization = float(st.sidebar.text_input("Stepsize", "0.1", help=r"Select stepsize from $(0,4]$"))
steps = int(st.sidebar.text_input(r"Iterations per $r$", "100", help=r"Number of iterations per $r$, must be positive integer"))
x_0 = float(st.sidebar.text_input(r"Start value $x_0$", "0.1", help=r"Initial value $x_0 \in [0,1]$"))
delay = st.sidebar.slider("Animation speed (seconds)", min_value=0.01, max_value=1.0, value=0.1, step=0.01)

start_simulation = st.sidebar.button("Start")

if start_simulation:
    col1, col2 = st.columns(2)
    placeholder_orbit = col1.empty()
    placeholder_divergence = col2.empty()

    logistic_map = LogisticMap(r_start, r_final, discretization,
        steps, x_0, placeholder_orbit,
        placeholder_divergence, delay)
    logistic_map.run()

# Exit button
exit_clicked = st.sidebar.button("Exit", type="primary")
if exit_clicked:
    st.toast("Logout!", icon="🌴")
    time.sleep(0.5)
    os._exit(0)
