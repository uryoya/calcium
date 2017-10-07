from calcium import Calcium

app = Calcium()

@app.command('foo')
def foo():
    return 'foo'

@app.command('bar', args=['argument'])
def bar(argument):
    return 'bar %s' % argument

@app.command('baz', help='show `baz`')
def baz():
    return 'baz'

if __name__ == '__main__':
    app.run()

