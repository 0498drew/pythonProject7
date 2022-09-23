class Games(object):
    def mul(self, x, y):
        num_type = (int, float, complex)

        if isinstance(x, num_type) and isinstance(y, num_type):
            import pdb; pdb.set_trace()
            return x*y
        else:
            return ValueError
