def direction_repr_str(cls, dir):
    if dir == cls.UP: return 'UP'
    if dir == cls.DOWN: return 'DOWN'
    if dir == cls.LEFT: return 'LEFT'
    if dir == cls.RIGHT: return 'RIGHT'
    if dir == cls.NOT_MOVING: return 'NOT_MOVING'
    return 'UNKNOWN'
