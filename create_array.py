import random

def create_array(mx, sz, sort=False, is_set=False):
    if is_set:
        if sort:
            return sorted(list(set([random.randint(1, mx) for x in range(0, sz)])))
        else:
            return list(set([random.randint(1, mx) for x in range(0, sz)]))
    else:
        if sort:
            return sorted([random.randint(1, mx) for x in range(0, sz)])
        else:
            return [random.randint(1, mx) for x in range(0, sz)]