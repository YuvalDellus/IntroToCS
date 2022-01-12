from autotest import TestSet

import sys
from importlib import import_module

from ast import literal_eval
from io import StringIO

import testrunners

def dirstr(dir):
    if dir == dirstr.cls.UP: return 'UP'
    if dir == dirstr.cls.DOWN: return 'DOWN'
    if dir == dirstr.cls.LEFT: return 'LEFT'
    if dir == dirstr.cls.RIGHT: return 'RIGHT'
    if dir == dirstr.cls.NOT_MOVING: return 'NOT_MOVING'
    return 'UNKNOWN'

def dirchoose(cls,dir):
    if dir == 'UP': return cls.UP
    if dir == 'DOWN': return cls.DOWN
    if dir == 'LEFT': return cls.LEFT
    if dir == 'RIGHT': return cls.RIGHT

def ident(res):
    return res

def modans(res):
    if type(res)==list:
        cp = res[:]
        res[:1]=[(3,3)]
    return cp

def repr_eval(ship): #or game
    shipstr = repr(ship)
    try:
        return literal_eval(shipstr)
    except ValueError:
        return shipstr

def ship_runner(modulename, fname, args=[], kwargs={}, options={}, tname=''):
    module = import_module(modulename)
    func = getattr(module, fname)
    fseq, argseq, filtseq = options.pop('runseq')
    dirclass = getattr(module, 'Direction')
    dirstr.cls = dirclass
    args = args[:]
    args[2] = dirchoose(dirclass,args[2])
    ship = func(*args, **kwargs)
    resseq = [repr_eval(ship)]
    for i,(f,ar,filt) in enumerate(zip(fseq, argseq, filtseq)):
        resseq.append((filt(getattr(ship, f)(*ar)),repr_eval(ship)))
    return None,resseq

def unorderedlists(exp,ans):
    return type(exp) == type(ans) and sorted(exp) == sorted(ans)


def shipcompare(exp,ans):
    if type(ans)!=type(exp): return False
    return (unorderedlists(exp[0],ans[0]) and
            unorderedlists(exp[1],ans[1]) and
            exp[2]==ans[2] and
            exp[3]==ans[3])

def shipseqcompare(exp,ans):
    if len(exp) != len(ans): return False
    if not shipcompare(exp[0],ans[0]): return False
    for i in range(1,len(exp)):
        if exp[i][0] != ans[i][0]: return False
        if not shipcompare(exp[i][1],ans[i][1]): return False
    return True

defaults = {}

shipdefaults = {'modulename':'ship',
                'runner':ship_runner,
                'fname':'Ship',
                'comparemethod':shipseqcompare,
                }

def buildset(name, args, fseq, argseq, filtseq, ans):
    return {name+'_'+str(i): {'args':args,
                              'options':{'runseq':[fseq[:i], argseq[:i], filtseq[:i]]},
                              'ans':[ans[:i+1]],
                              } for i in range(len(ans))}

cases = {}

cases.update(buildset('contains',
                      [(0,1),2,'RIGHT',3],
                      ['__contains__']*5,
                      [[(0,1)],[(1,1)],[(2,1)],[(0,0)],[(0,2)]],
                      [ident]*5,
                      [([(0, 1), (1, 1)], [], 'RIGHT', 3),
                       (True,([(0, 1), (1, 1)], [], 'RIGHT', 3)),
                       (True,([(0, 1), (1, 1)], [], 'RIGHT', 3)),
                       (False,([(0, 1), (1, 1)], [], 'RIGHT', 3)),
                       (False,([(0, 1), (1, 1)], [], 'RIGHT', 3)),
                       (False,([(0, 1), (1, 1)], [], 'RIGHT', 3)),
                       ]))

cases.update(buildset('movedir',
                      [(1,0),2,'UP',4],
                      ['move','direction']*5,
                      [[]]*10,
                      [dirstr]*10,
                      [([(1, 0), (1, 1)], [], 'UP', 4),
                       ('DOWN',([(1, 2), (1, 1)], [], 'DOWN', 4)),
                       ('DOWN',([(1, 2), (1, 1)], [], 'DOWN', 4)),
                       ('DOWN',([(1, 2), (1, 3)], [], 'DOWN', 4)),
                       ('DOWN',([(1, 2), (1, 3)], [], 'DOWN', 4)),
                       ('UP',([(1, 2), (1, 1)], [], 'UP', 4)),
                       ('UP',([(1, 2), (1, 1)], [], 'UP', 4)),
                       ('UP',([(1, 0), (1, 1)], [], 'UP', 4)),
                       ('UP',([(1, 0), (1, 1)], [], 'UP', 4)),
                       ('DOWN',([(1, 2), (1, 1)], [], 'DOWN', 4)),
                       ('DOWN',([(1, 2), (1, 1)], [], 'DOWN', 4)),
                       ]))

cases.update(buildset('hitsmult',
                      [(1,0),2,'DOWN',4],
                      ['hit']*5,
                      [[(0,1)],[(1,1)],[(2,1)],[(1,0)],[(1,1)]],
                      [ident]*5,
                      [([(1, 0), (1, 1)], [], 'DOWN', 4),
                       (False,([(1, 0), (1, 1)], [], 'DOWN', 4)),
                       (True,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       (False,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       (True,([(1, 0), (1, 1)], [(1, 0), (1, 1)], 'NOT_MOVING', 4)),
                       (False,([(1, 0), (1, 1)], [(1, 0), (1, 1)], 'NOT_MOVING', 4)),
                       ]))

cases.update(buildset('hitdirmove',
                      [(1,0),2,'DOWN',4],
                      ['direction','hit','direction','move','hit'],
                      [[],[(1,1)],[],[],[(1,1)]],
                      [dirstr,ident,dirstr,dirstr,ident],
                      [([(1, 0), (1, 1)], [], 'DOWN', 4),
                       ('DOWN',([(1, 0), (1, 1)], [], 'DOWN', 4)),
                       (True,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       ('NOT_MOVING',([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       ('NOT_MOVING',([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       (False,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       ]))

cases.update(buildset('hitterminated',
                      [(1,0),2,'DOWN',4],
                      ['terminated','hit','terminated','hit','terminated'],
                      [[],[(1,1)],[],[(1,0)],[]],
                      [ident]*5,
                      [([(1, 0), (1, 1)], [], 'DOWN', 4),
                       (False,([(1, 0), (1, 1)], [], 'DOWN', 4)),
                       (True,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       (False,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       (True,([(1, 0), (1, 1)], [(1, 1),(1,0)], 'NOT_MOVING', 4)),
                       (True,([(1, 0), (1, 1)], [(1, 1),(1,0)], 'NOT_MOVING', 4)),
                       ]))

cases.update(buildset('hitcontains',
                      [(1,0),2,'DOWN',4],
                      ['hit','__contains__','__contains__','__contains__','__contains__'],
                      [[(1,1)],[(1,1)],[(1,0)],[(0,0)],[(2,2)]],
                      [ident]*5,
                      [([(1, 0), (1, 1)], [], 'DOWN', 4),
                       (True,([(1, 0), (1, 1)], [(1,1)], 'NOT_MOVING', 4)),
                       (True,([(1, 0), (1, 1)], [(1,1)], 'NOT_MOVING', 4)),
                       (True,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       (False,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       (False,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       ]))

cases.update(buildset('hitstatus',
                      [(1,0),2,'DOWN',4],
                      ['cell_status','hit','cell_status','cell_status','cell_status'],
                      [[(1,1)],[(1,1)],[(1,1)],[(1,0)],[(0,0)]],
                      [ident]*5,
                      [([(1, 0), (1, 1)], [], 'DOWN', 4),
                       (False,([(1, 0), (1, 1)], [], 'DOWN', 4)),
                       (True,([(1, 0), (1, 1)], [(1,1)], 'NOT_MOVING', 4)),
                       (True,([(1, 0), (1, 1)], [(1,1)], 'NOT_MOVING', 4)),
                       (False,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       (None,([(1, 0), (1, 1)], [(1, 1)], 'NOT_MOVING', 4)),
                       ]))

cases.update(buildset('coordinates',
                      [(1,1),1,'LEFT',4],
                      ['coordinates']*2,
                      [[]]*2,
                      [modans,ident],
                      [([(1, 1)], [], 'LEFT', 4),
                       ([(1,1)],([(1, 1)], [], 'LEFT', 4)),
                       ([(1,1)],([(1, 1)], [], 'LEFT', 4)),
                       ]))


cases.update(buildset('damaged',
                      [(1,1),1,'LEFT',4],
                      ['damaged_cells','damaged_cells','hit']*2,
                      [[],[],[(1,1)]]*2,
                      [modans,ident,ident]*2,
                      [([(1, 1)], [], 'LEFT', 4),
                       ([],([(1, 1)], [], 'LEFT', 4)),
                       ([],([(1, 1)], [], 'LEFT', 4)),
                       (True,([(1, 1)], [(1,1)], 'NOT_MOVING', 4)),
                       ([(1,1)],([(1, 1)], [(1,1)], 'NOT_MOVING', 4)),
                       ([(1,1)],([(1, 1)], [(1,1)], 'NOT_MOVING', 4)),
                       (False,([(1, 1)], [(1,1)], 'NOT_MOVING', 4)),
                       ]))


startstate = (5, {}, [([(1,1)],[],'LEFT',5),([(1,3),(2,3),(3,3)],[],'RIGHT',5)])
endstate = (5, {(0,0):1,(0,1):2}, [])

gametext = '''legend
_____,_X___,_____,_XXX_,_____
target:(0, 0)
3____,X____,_____,__XXX,_____
0 hits, 0 terminations
target:(3, 1)
2____,_X_3_,_____,_XXX_,_____
0 hits, 0 terminations
target:(1, 3)
1____,__X2_,_____,X*X__,_____
1 hits, 0 terminations
target:(4, 4)
_____,___*_,_____,XOX__,____3
1 hits, 1 terminations
target:(4, 4)
_____,_____,_____,XOX__,____3
0 hits, 0 terminations
target:(0, 3)
_____,_____,_____,*OX__,____2
1 hits, 0 terminations
target:(0, 0)
3____,_____,_____,OOX__,____1
0 hits, 0 terminations
target:(0, 1)
2____,3____,_____,OOX__,_____
0 hits, 0 terminations
target:(2, 3)
1____,2____,_____,OO*__,_____
1 hits, 1 terminations
gameover
'''

def makeship(shipmodule,args):
    shipclass = getattr(shipmodule, 'Ship')
    dirclass = getattr(shipmodule, 'Direction')
    args = args[:]
    args[2] = dirchoose(dirclass,args[2])
    return shipclass(*args)


def getgame(args):
    module = import_module('game')
    func = getattr(module, 'Game')
    shipmodule = import_module('ship')
    args = args[:]
    args[1] = [makeship(shipmodule,a) for a in args[1]]
    return func(*args)

def run_start_state(modulename=None, fname=None, args=[], kwargs={}, options={}, tname=''):
    game = getgame(args)
    res = repr_eval(game)
    return None,res

def run_end_state(modulename=None, fname=None, args=[], kwargs={}, options={}, tname=''):
    game = getgame(args)
    try:
        _stdout = sys.stdout
        tmpout = StringIO()
        sys.stdout = tmpout                        
        game.play()
    finally:
        sys.stdout = _stdout
    res = repr_eval(game)
    return None,res

def run_game_prints(modulename=None, fname=None, args=[], kwargs={}, options={}, tname=''):
    game = getgame(args)
    try:
        _stdout = sys.stdout
        tmpout = StringIO()
        sys.stdout = tmpout                        
        game.play()
        res = tmpout.getvalue()
    finally:
        sys.stdout = _stdout
    return None,res


def gamestatecompare(exp,ans):
    if type(ans)==str: return False
    if type(exp) != type(ans): return False
    if len(exp) != len(ans): return False
    if exp[:2] != ans[:2]: return False
    if type(exp[2]) != type(ans[2]): return False
    exp2 = exp[2][:]
    ans2 = ans[2][:]
    while exp2:
        expship = exp2.pop()
        for i,ansship in enumerate(ans2):
            if shipcompare(expship,ansship):
                ans2.pop(i)
                break
        else:
            return False
    return True

gamedefaults = {'modulename':'game',
                'fname':'Game',
                'args':[5,[[(1,1),1,'LEFT',5],[(1,3),3,'RIGHT',5]]]}

gamecases = {'start':{'ans':[startstate],
                      'runner':run_start_state,
                      'comparemethod':gamestatecompare,
                      },
             'over':{'ans':[endstate],
                     'runner':run_end_state,
                      'comparemethod':gamestatecompare,
                     },
             'report':{'ans':[gametext],
                       'runner':run_game_prints},
             }

tsets = {'ship':TestSet(shipdefaults,cases),
         'game':TestSet(gamedefaults,gamecases),
         }
