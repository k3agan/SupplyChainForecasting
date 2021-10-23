def seasonal_factors_add(s,d,slen,cols):
    for i in range(slen):
        # Calculate season average
        s[i] = np.mean(d[i:ccols:slen])

    # Scale all season factors (sum of factors = 0)
    s -= np.mean(s[:slen])
    return s

def triple_exp_smooth_add(d,slen=12, extra_periods = 1, alpha = 0.4, beta=0.4, phi=0.9, gamma=0.3):

    cols = len(d) # Hisorical period length

    # Append np.nan into the demand array to cover future periods
    d = np.append(d,[np.nan]*extra_periods)

    # components initialization
    f,a,b,s = np.full((4, cols+extra_periods),np.nan)
    s = seasonal_factors_add(s,d,slen,cols)

    # Level & Trend initialization
    a[0] = d[0]-s[0]
    b[0]  (d[1]-s[1]) - (d[0]-s[0])

    # Create the forecast for the first season
    for t in range(1, slen):
        f[t] = a[t-1] + phi*b[t-1] + s[t]
        a[t] = alpha*(d[t]-s[t]) + (1-alpha)*(a[t-1)
        b[t] = beta*(a[t]-a[t-1]) + (1-beta)*phi*b[t-1]
    
    # Create all the t+1 forecasts
    for t in range(slen,cols):
        f[t] = a[t-1] + phi*b[t-1] + s[t-slen]
        a[t] = alpha*(d[t]-s[t-slen]) + (1-alpha)*(a[t-1]+phi*b[t-1])
        b[t] = beta*(a[t]-a[t-1]) + (1-beta)*phi*b[t-1]
        s[t] = gamma*(d[t]-a[t]) + (1-gamma)*s[t-slen]
    
    # Forecast for all extra periods
    for t in range(cols,cols+extra_periods):
        f[t] = a[t-1] + phi*b[t-1] + s[t-slen]
        a[t] = f[t]-s[t-slen]
        b[t] = phi*b[t-1]
        s[t] = s[t-slen]

    df = pd.DataFrame.from_dict({'Demand':d, 'Forecast':f,'Level':a,'Trend':b,'Season':s,'Error':d-f})

    return df