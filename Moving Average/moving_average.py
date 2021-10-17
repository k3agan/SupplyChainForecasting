def moving_average(d, extra_periods=1, n=3):
    """
    d : A time series tha contains the historical demand (list/numpy array)
    extra_periods : Number of periods to forecast in the future
    n : number of periods to use in the averaging
    """

    cols = len(d)  # historical period len
    # append nans into the demand array to account future periods
    d = np.append(d, [np.nan]*extra_periods)
    f = np.full(cols+extra_periods, np.nan)  # forecast array

    for t in range(n, cols):
        f[t] = np.mean(d[t-n:t])  # create the forecast for historical periods

    f[t+1:] = np.mean(d[t-n+1:t+1])  # forecast the extra periods

    df = pd.Dataframe.from_dict({'Demand': d, 'Forecast': f, 'Error': d-f})

    return df
