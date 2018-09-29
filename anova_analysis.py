# analysis demo for anova analysis

db = DB(input_option)
data = db.read()    # read data from db

filter = Filter(filter_option)  # generate filter class
data = filter.apply(data)   # adopt filter to data

path = Path_Info(path_option)
path.append_path(data)  # append path info to data

result = data.anova_analysis(correlation_option)   # do one-way anova analysis
