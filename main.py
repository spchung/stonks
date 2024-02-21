import numpy as np
np.set_printoptions(threshold=np.inf)
from indicators.super_trend import visual_super_trend

def main():
    visual_super_trend('data/bitcoin.csv', last_n_days=300)

if __name__ == "__main__":
    main()