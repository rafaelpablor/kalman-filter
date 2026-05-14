import numpy as np

def kalman_filter(z, F, H, Q, R, x0=None, P0=None):
    if x0 is None:
        x = np.array([z[0], 0])
    else:
        x = x0

    if P0 is None:
        P = np.eye(2)
    else:
        P = P0
    I=np.eye(len(x))
    filtered = []
    for z_k in z:
        x=F@x
        P=F@P@F.T + Q

        K=P@H.T@np.linalg.inv((H@P@H.T+R))
        x=x+K@(z_k-H@x)
        P=(I-K@H)@P

        filtered.append(x[0])

    filtered_data = np.array(filtered)
    return filtered_data