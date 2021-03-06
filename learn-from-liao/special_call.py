class Chain(object):
    def __init__(self, path='GET '):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def users(self, name):
        return Chain('%s/users/:%s' % (self._path, name))
    def __str__(self):
        return self._path
    __repr__=__str__
    def __call__(self):
        print(self._path)

s = Chain().status.user.timeline.list
s()
p = Chain().users('michael').repos
p()
