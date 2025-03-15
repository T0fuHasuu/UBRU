# Put in :

    import pandas as pd
    print(pd.Series([1, 2, 3], index=['a', 'b', 'c']))

# Display info with row and column :

    import pandas as pd
    data = [
        [0,2,3],
        [0, 4,1],
        [10, 20, 30]
    ]
    col = ['A', 'B', 'C']
    name = [4,5,6]
    print(pd.DataFrame(data, index=name, columns=col))

# Put in II :

    import pandas as pd
    print(pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], name=0))

# Sort as dataframe :

    import pandas as pd
    data = [
        [1,2,3,4],
        [100,200,300,400],
        [1000,2000,3000,400]
    ]
    col = ['a', 'b', 'c', 'd']
    name = [0,1,2]
    df = pd.DataFrame(data, index=name, columns=col)
    print(df)

    # Extract b and d of index 0 and 2 :

        print(df.loc[[0,2], ['b','d']]) 

    # Extract a, b and c of index 1 2 :

        print(df.loc[[1,2], ['a', 'b','c']])

# Sort as dataframe :

    import pandas as pd
    data = [
        [1,2],
        [4,5],
        [7,8]
    ]
    col = ['max_speed', 'shield']
    name = ['cobra', 'viper', 'sidewinder']
    df = pd.DataFrame(data, index=name, columns=col)
    print(df)

# Extract only Viper :

    print(df.loc['viper'])

# Extract viper and sidewinder :

    print(df.loc[['viper', 'sidewinder']])

# Get one column for viper and sidewinder :

    print(df.loc[['cobra', 'viper'], 'max_speed'])

# Extract only sidewinder :

    print(df.loc[['sidewinder']])

