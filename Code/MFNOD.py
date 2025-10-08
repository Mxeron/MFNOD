import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cdist
import pandas as pd
from sklearn.metrics import roc_auc_score


def MFNOD(data, k):
    n = data.shape[0]
    sim = FSR(data)
    similarity = np.sort(sim, axis=1)[:, ::-1]
    num = np.argsort(-sim, axis=1, kind='stable')
    ksimilarity = similarity[:, k]
    fkNN_temp = np.where(sim >= ksimilarity[:, None], sim, 0)

    fkNN_card = np.sum(fkNN_temp, axis=1)
    count = np.sum(fkNN_temp != 0, axis=1)
    reachsim = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            reachsim[i, j] = min(sim[i, j], ksimilarity[j])

    lrd = np.zeros(n)
    for i in range(n):
        sum_reachdist = 0
        for j in range(count[i]):
            sum_reachdist += reachsim[num[i, j + 1], i]
        lrd[i] = sum_reachdist / fkNN_card[i]

    OS = np.zeros(n)
    for i in range(n):
        sumlrd = 0
        for j in range(count[i]):
            sumlrd += lrd[num[i, j + 1]] / lrd[i]
        OS[i] = sumlrd / fkNN_card[i]
    return OS

def kernel_fs(X_subset, delta):
    squared_dists = cdist(X_subset, X_subset, 'sqeuclidean')
    kernel_matrix = np.exp(-squared_dists / delta)
    return kernel_matrix

def compute_silverman_delta(data):
    n, m = data.shape
    sigma = np.std(data, axis=0)
    iqr = np.percentile(data, 75, axis=0) - np.percentile(data, 25, axis=0)
    factor = np.minimum(sigma, iqr / 1.34)
    delta = 0.9 * factor * (n ** (-1/5))
    return np.mean(delta)


def FSR(data):
    base_delta = compute_silverman_delta(data)
    deltas = [base_delta * 0.5, base_delta, base_delta * 2]
    fs = []
    for delta in deltas:
        cur_fs = kernel_fs(data, delta)
        fs.append(cur_fs)
    sum_fs_1 = np.sum(fs[0])
    sum_fs_2 = np.sum(fs[1])
    sum_fs_3 = np.sum(fs[2])
    cur_sum = sum_fs_1 + sum_fs_2 + sum_fs_3
    final_fs = (sum_fs_1 / cur_sum) * fs[0] + (sum_fs_2 / cur_sum) * fs[1] + (sum_fs_3 / cur_sum) * fs[2]
    return final_fs

if __name__ == "__main__":
    data = pd.read_csv("./Example.csv")
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)
    k = 3
    OS = MFNOD(data, k)
    print(OS)