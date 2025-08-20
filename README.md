# logistic_map
A Python package that highlights the chaotic behavoiur for the logistic map under different values for $r$

### FEATURES
- Simulates trajectories of the recursion $x_n+1=x_nr(1-x_n)$ for different values of $r$
- Provides a sidebar where user can state values for r_start,r_end, stepsize and startvalue $x_0$
- Visualizes trajectories of the orbits and the variation chart

### REQUIREMENTS
- Python 3.11+ (tested with 3.11.9)
- Required dependencies (see requirements.txt for details):
    streamlit==1.24.1
    numpy==1.24.3
    matplotlib==3.7.1
    seaborn==0.12.2

### INSTALLATION
1. Clone the repository:
       git clone https://github.com/hb84ffm/logistic_map.git
       cd logistic_map

2. Create & activate your virtual environment:
       python3 -m venv venv
       source venv/bin/activate      # On Mac/Linux
       venv\Scripts\activate         # On Windows

3. Install dependencies:
       pip install -r requirements.txt

### USAGE
1. Import the package (to desktop!)

2. Use terminal to run the app by providing full path to the app with command "streamlit run /path/app.py" (Mac users!)

### PACKAGE STRUCTURE

<pre>logistic_map/
├─── __init__.py
├─── app.py                    # main app that rns in browser
├─── simulate/
     ├─── __init__.py
     ├─── simulate             # Module that calculates all trajectories of the dynamical system</pre>

### EXAMPLE WORKFLOW
Gif soon to come!

### AUTHOR
For questions or feedback reach out via: [GitHub](https://github.com/hb84ffm).
