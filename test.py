import pandas as pd
import matplotlib.pyplot as plt

test_df = pd.DataFrame({
        "X": [1, 2, 3, 4],
        "Y": [5, 4, 2, 1],
        "C": [1, 2, 3, 4]
    })


test_df.plot(kind="scatter", x="X", y="Y", s=50); 
plt.savefig("scatter-1.png")

test_df.plot(kind="scatter", x="X", y="Y", c="C");
plt.savefig("scatter-2.png")

test_df.plot(kind="scatter", x="X", y="Y", s=50, c="C", cmap="plasma");
plt.savefig("scatter-3.png")
