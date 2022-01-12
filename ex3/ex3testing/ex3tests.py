from autotest import TestSet

import testrunners

def unorderedlists(exp,ans):
    try:
        return exp == sorted(sorted(p) for p in ans)
    except TypeError:
        return False

def unordered(exp,ans):
    try:
        return type(exp)==type(ans) and sorted(exp) == sorted(ans)
    except TypeError:
        return False

defaults = {'modulename':'ex3',}

cases = {'createlist':{'fname':'create_list',
                       'runner':testrunners.input_runner,
                       'options':{'input':'Hello world\nWhat\n \na nice day\n3\n\n'},
                       'args':[],
                       'ans':[['Hello world','What',' ','a nice day','3']],
                   },
         'concatlist':{'fname':'concat_list',
                       'args':[['Hello world','What',' ','a nice day','3']],
                       'ans':['Hello worldWhat a nice day3'],
                   },
         'average':{'fname':'average',
                    'args':[[2.7,5.3,2.5,0,6.5]],
                    'ans':[3.4],
                },
         'cyclic':{'fname':'cyclic',
                   'args':[list('abcd'),list('dabc')],
                   'ans':[True],
               },
         'histogram':{'fname':'histogram',
                   'args':[5,[2,1,4,4,2,4]],
                   'ans':[[0,1,2,0,3]],
             },
         'factors':{'fname':'prime_factors',
                   'args':[24],
                   'ans':[[2,2,2,3]],
              },
         'cartesian':{'fname':'cartesian',
                   'args':[list('abc'),list('mn')],
                   'ans':[[tuple('am'),tuple('an'),tuple('bm'),
                           tuple('bn'),tuple('cm'),tuple('cn'),],
                          [list('am'),list('an'),list('bm'),
                           list('bn'),list('cm'),list('cn'),],
                          ],
                      'comparemethod':unordered,
             },
         'pairs':{'fname':'pairs',
                 'args':[5,[-2,3,7,11,2,6]],
                 'ans':[[[-2,7],[2,3]]],
                 'comparemethod':unorderedlists,
             },
     }

tsets = {'ex3':TestSet({},cases),
}
