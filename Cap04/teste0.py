
import pandas as pd
import numpy as np
particulas = []
for x in range(0, 3):
    globals()[f"particula{x}"] = pd.read_csv("particula"  + f"{x}" ".dat" , header = 0)
    particulas.append(f"particula{x}")
