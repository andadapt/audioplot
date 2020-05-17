import plotting


def bar_test():
    print('bar chart with default settings')
    data_items = ['car','bicycle','bus']
    data_values=[20,10,5]
    out = plotting.plot('bar')
    out.data(data_values,data_items)
    out.play()

def rate_test():
    print('a bar chart with increased speaking rate')
    data_items = ['car','bicycle','bus']
    data_values=[20,10,5]
    out = plotting.plot('bar')
    out.data(data_values,data_items)
    out.rate('400' )
    out.play()
def verbose_test():
    print('a bar chart with verbose output')
    data_items = ['car','bicycle','bus']
    data_values=[20,10,5]
    out = plotting.plot('bar')
    out.data(data_values,data_items)
    out.verbosity(True)
    out.title('A bar chart of the number of people that take different modes of transport')
    out.play()
def run():
    bar_test()
    rate_test()
    verbose_test()

run()
