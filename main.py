import gnb as gnb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#import pyAgrum as gum
#import pyAgrum.lib.notebook as gnb
from sklearn.metrics import accuracy_score
#import pyAgrum.skbn as skbn
import pandas_profiling as pp
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling as pp

data = pd.read_csv('heart_2020_cleaned.csv')
data.head

import phik
from phik.report import plot_correlation_matrix
from phik import report

phik_overview = data.phik_matrix()
phik_overview.round(1)
plot_correlation_matrix(phik_overview.values,
                        x_labels=phik_overview.columns,
                        y_labels=phik_overview.index,
                        vmin=0, vmax=1,
                        title=r"correlation $\phi_K$",
                        fontsize_factor=0.5,
                        figsize=(10, 8))
plt.tight_layout()
plt.savefig("corr.png")
