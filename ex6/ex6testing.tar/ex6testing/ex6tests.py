from autotest import TestSet

import testrunners

from copy import deepcopy

defaults = {'modulename':'ex6',}

im1 = [[(20,40,60),(20,40,60),(20,40,60)],
       [(20,40,60),(20,40,60),(20,40,60)]]

im2 = [[(20,40,60),(25,47,69),(10,20,30)],
       [(10,50,60),(30,40,50),(20,30,70)]]

im3 = [[(20,40,60),(25,47,69)],
       [(10,50,60),(30,40,50)],
       [(10,20,30),(20,30,70)]]

im4 = [[(20,40,60),(20,40,60),(20,40,60)],
       [(60,41,20),(60,41,20),(60,41,20)]]

def doubleimage(im):
    return 2*[row+row for row in im]

def modfirst_runner(modulename, fname, args=[], kwargs={}, options={},tname=''):
    options['check_input'] = False
    code,res = testrunners.import_runner(modulename, fname, args, kwargs,options,
                                         tname=tname)
    if code:
        return code,res
    if res is not None:
        return("wrong", 'return value should be None')
    return None,args[0]

cases = {'comparepixel00':{'fname':'compare_pixel',
                 'args':[im1[0][0],im2[0][0]],
                 'ans':[0],
             },
         'comparepixel01':{'fname':'compare_pixel',
                 'args':[im1[0][1],im2[0][1]],
                 'ans':[21],
             },
         'comparepixel10':{'fname':'compare_pixel',
                 'args':[im1[1][0],im2[1][0]],
                 'ans':[20],
             },
         'comparepixel11':{'fname':'compare_pixel',
                 'args':[im1[1][1],im2[1][1]],
                 'ans':[20],
             },
         'comparei1':{'fname':'compare',
                'args':[im1,im2],
                'ans':[141],
             },
         'comparei2':{'fname':'compare',
                'args':[im1,im3],
                'ans':[61],
             },
         'comparei3':{'fname':'compare',
                'args':[im2,im3],
                'ans':[0],
             },
         'getpiece1':{'fname':'get_piece',
                'args':[im2,(0,1),(2,1)],
                'ans':[[[im2[0][1]],[im2[1][1]]]],
             },
         'getpiece2':{'fname':'get_piece',
                'args':[im2,(0,1),(1,2)],
                'ans':[[[im2[0][1],im2[0][2]]]],
             },
         'getpiece3':{'fname':'get_piece',
                'args':[im2,(1,2),(2,2)],
                'ans':[[[im2[1][2]]]],
             },
         'setpiece1':{'fname':'set_piece',
                'args':[deepcopy(im2),(0,1),[[(0,0,0)],[(0,0,0)]]],
                'runner':modfirst_runner,
                'ans':[[[(20,40,60),( 0, 0, 0),(10,20,30)],                      
                        [(10,50,60),( 0, 0, 0),(20,30,70)]]],
             },
         'setpiece2':{'fname':'set_piece',
                'args':[deepcopy(im2),(0,1),[[(0,0,0),(0,0,0)]]],
                'runner':modfirst_runner,
                'ans':[[[(20,40,60),( 0, 0, 0),( 0, 0, 0)],                      
                        [(10,50,60),(30,40,50),(20,30,70)]]],
             },
         'setpiece3':{'fname':'set_piece',
                'args':[deepcopy(im2),(1,2),[[(0,0,0),(0,0,0)],[(0,0,0),(0,0,0)]]],
                'runner':modfirst_runner,
                'ans':[[[(20,40,60),(25,47,69),(10,20,30)],                      
                        [(10,50,60),(30,40,50),( 0, 0, 0)]]],
             },
         'average1':{'fname':'average',
                'args':[im1],
                'ans':[(20.0,40.0,60.0)],
             },
         'average2':{'fname':'average',
                'args':[im4],
                'ans':[(40.0,40.5,40.0)],
             },
         'prepocess':{'fname':'preprocess_tiles',
                'args':[[im1,im4]],
                'ans':[[(20.0,40.0,60.0),(40.0,40.5,40.0)]],
             },
         'getbesttiles':{'fname':'get_best_tiles',
                'args':[im2,
                        [im1,im4,im1,im4],
                        [(20.0,40.0,60.0),(40.0,40.5,40.0),(20.0,40.0,60.0),(40.0,40.5,40.0)],
                        2
],
                'ans':[[im1,im1]],
             },
         'choosetile':{'fname':'choose_tile',
                'args':[im2,[im1,im4]],
                'ans':[im1],
             },
         'makemosaic':{'fname':'make_mosaic',
                'args':[doubleimage(im2),[im1,im4],2],
                'ans':[doubleimage(im1)],
             },
     }


tsets = {'ex6':TestSet({},cases),
}
