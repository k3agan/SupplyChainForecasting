def exp_smooth_opti(d, extra_periods=6):

    params = []  # contains all the different parameter set
    KPIs = []  # contains the reuslts of each model
    dfs = []  # contains all the DataFrames returned by the different models

    for alpha in [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
        df = simple_exp_smooth(d, extra_periods=extra_periods, alpha=alpha)
        params.append(f'Simple Smoothing, alpha: {alpha}')
        dfs.append(df)
        MAE = df['Error'].abs().mean()
        KPIs.append(MAE)

        for beta in [0.05, 0.1, 0.2, 0.3, 0.4]:

            df = double_exp_smooth(
                d, extra_periods=extra_periods, alpha=alpha, beta=beta)
            params.append(f'Double Smoothing, alpha: {alpha}, beta: {beta}')

            dfs.append(df)
            MAE = df['Error'].abs().mean()
            KPIs.append(MAE)

    mini = np.argmin(KPIs)
    print(f'Best solution found for {params[mini]} MAE of ', round(
        KPIs[mini], 2))

    return dfs[mini]
