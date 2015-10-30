import pandas as pd
import numpy as np
df = pd.DataFrame({'rainy': [.4, .7], 
                   'sunny': [.6, .3]
                  }, 
                  index=["rainy", "sunny"])
print df
np.linalg.matrix_power(df,5) #probability after 5 transitions