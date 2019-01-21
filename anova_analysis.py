# analysis demo for anova analysis

# input params ################
data_option = {
    'db': 'il',
}

data_filter = {
    'method': 'script', # script
    'include': 'in',    # in or out
    'contetns': """
        ppid == 'rcp1'
    """,
}

path_option = {
    'db': 'path',
}

path_filter = {
    'method': 'layer',  # layer or script
    'layer': ['pc'],
    'contents': """
        step_seq <= 'kz008000'
    """,
}

alias_filter = {
    'method': 'file',   # file or script
    'contents': """
         lot_id == ['az0xx', 'az0h1']
    """,
    'alias_other': '',
}
# input params ################


data = DB(data_option)
filter_data = Filter(data_filter)  # generate filter class
data = data_filter.apply(data)   # adopt filter to data

path = DB(path_option)
filter_path = Filter(path_filter)  # generate filter class
path = filter_path.apply(path)   # adopt filter to data

data = path.append_path(data)  # append path info to data

anova = Anova(correlation_option)
result = anova.run_analysis(data)
