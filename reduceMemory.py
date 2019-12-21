def reduce_memory(df):
    for col in df.columns:
        if df[col].dtypes in ["int64", "int32", "int16"]:
            
            cmin = df[col].min()
            cmax = df[col].max()
            
            if cmin > np.iinfo(np.int8).min and cmax < np.iinfo(np.int8).max:
                df[col] = df[col].astype(np.int8)
            
            elif cmin > np.iinfo(np.int16).min and cmax < np.iinfo(np.int16).max:
                df[col] = df[col].astype(np.int16)
            
            elif cmin > np.iinfo(np.int32).min and cmax < np.iinfo(np.int32).max:
                df[col] = df[col].astype(np.int32)
        
        if df[col].dtypes in ["float64", "float32", "float16"]:
            
            cmin = df[col].min()
            cmax = df[col].max()
            
            if cmin > np.iinfo(np.float8).min and cmax < np.iinfo(np.float8).max:
                df[col] = df[col].astype(np.float8)
            
            elif cmin > np.iinfo(np.float16).min and cmax < np.iinfo(np.float16).max:
                df[col] = df[col].astype(np.float16)
            
            elif cmin > np.iinfo(np.float32).min and cmax < np.iinfo(np.float32).max:
                df[col] = df[col].astype(np.float32)

    
    return df
