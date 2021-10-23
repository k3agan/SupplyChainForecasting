def simple_exp_smooth(d, extra_periods=1, alpha=0.4):

    # Historical period length
    cols = len(d)

    # Append np.nan into the demand array to cover future periods
    d = np. append(d, [np.nan]*extra_periods)

    # Forecast array
    f = np.full(cols+extra_periods, np.nan)
    # Initialization of first forecast
    f[1] = d[0]

    # Create all the t+1 forecast until end of historical period
    for t in range(2, cols+1):
        f[t] = alpha*d[t-1]+(1-alpha)*f[t-1]

    # Forecast for all extra periods
    for t in range(cols+1, cols+extra_periods):
        # Update the forecast as the previous forecast
        f[t] = f[t-1]

    df = pd.DataFrame.from_dict({'Demand': d, 'Forecast': f, 'Error': d-f})

    return df
