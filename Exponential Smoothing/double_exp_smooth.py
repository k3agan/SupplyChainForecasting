
def double_exp_smooth(d, extra_periods=1, alpha=0.4, beta=0.4):

    # Historical period length
    cols = len(d)

    # Append np.nan into the demand array to cover future periods
    d = np.append(d, [np.nan]*extra_periods)

    # Creation of the leve, trend and forecast arrays
    f, a, b = np.full((3, cols+extra_periods), np.nan)

    # Level & Trend initialization
    a[0] = d[0]
    b[0] = d[1] - d[0]

    # Create all the t+1 forecast
    for t in range(1, cols):
        f[t] = a[t-1] + b[t-1]
        a[t] = alpha*d[t] + (1-alpha)*(a[t-1]+b[t-1])
        b[t] = beta*(a[t]-a[t-1]) + (1-beta)*b[t-1]

    # forecast for all extra periods
    for t in range(cols, cols+extra_periods):
        f[t] = a[t-1] + b[t-1]
        a[t] = f[t]
        b[t] = b[t-1]

    df = pd.DataFrame.from_dict(
        {'Demand': d, 'Forecast': f, 'Level': a, 'Trend': b, 'Error': d-f})

    return df
