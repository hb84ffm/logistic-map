# logistic_map
A Python package that highlights the chaotic behavoiur for the logistic map under different values for $r$

<p align="center">
  <img src="[https://github.com/](https://github.com/user-attachments/assets/c0d6632f-e67b-45b9-afd4-d9ec78efa9c2)" alt="App Screenshot" 
       style="border: 3px solid black; border-radius: 4px;" width="600" />
</p>


### FEATURES
- Simulates trajectories of the recursion $x_{n+1}=rx_n(1-x_n)$ for different values of $r$
- Provides a sidebar where user can state values for r_start,r_end, stepsize and startvalue $x_0$
- Visualizes trajectories of the orbits and the variation chart

### REQUIREMENTS
- Python 3.11+ (tested with 3.11.9)
- Required dependencies (see requirements.txt for details):
  - streamlit==1.24.1
  - numpy==1.24.3
  - matplotlib==3.7.1
  - seaborn==0.12.2

### INSTALLATION
1. Clone the repository:<br>
   git clone https://github.com/hb84ffm/logistic_map.git<br>
   cd logistic_map

3. Create & activate your virtual environment:<br>
       python3 -m venv venv<br>
       source venv/bin/activate      # On Mac/Linux<br>
       venv\Scripts\activate         # On Windows

4. Install dependencies:<br>
       pip install -r requirements.txt

### USAGE
1. Import the package (to desktop!)

2. Use terminal to run the app by providing full path to the app with command "streamlit run /path/app.py" (Mac users!)

### PACKAGE STRUCTURE

<pre>logistic_map/
├─── __init__.py
├─── app.py                    # main app that runs the simulation in the browser
├─── simulate/
     ├─── __init__.py
     ├─── simulate             # Module that calculates all orbit-trajectories of the dynamical system</pre>

### EXAMPLE WORKFLOW
Gif soon to come!

### AUTHOR
For questions or feedback reach out via: [GitHub](https://github.com/hb84ffm).
