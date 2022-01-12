a = [x for x in range(10)]
# print(a[8:2:2])
# will print an empty list cause we moving  moving forward from 8

# print(a[:2:-2])
# [9, 7, 5, 3]

# print(a[8::-2])
#[8, 6, 4, 2, 0]


# print('beauty'[::-1])
# ytuaeb

def rev(s):
 return s[ : :-1]


def f(s):
    if len(s) < 2:
        return s
    else:
        s2 = s[0:2]

        if s[0] > s[1]:
            s2 = rev(s2)
        return s2[0] + f(s2[1]+s[2:])

def foo(s, n):
    s1 = s
    for i in range(n):
        s1 = f(s1)
    return s1

# print(f(a))

# print(foo('beauty',len('beauty')))
# print(f('beauty'))
# b= list()
# for letter in "beauty":
#     b.append(ord(letter))
# print(b)
# print(f(b))
# c = f(b)
# for letter in c:
#     print(chr(letter),end="")

def fooy(s, i, b):
    if i >= len(s)//2:
        return ' '# empty string
    else:
        s2 = s[i] + s[i+len(s)//2]
        if b:
            s2 = rev(s2)
        print(s2)
    return s2 + fooy(s, i+1, not b)

# print(fooy('beauty', 0, False))


def intersect(segment1, segment2):
    def build_segment(start, end):
        segment = [x for x in range(end+1)][start:]
        return set(segment)


    return (bool(build_segment(segment1[0],segment1[1]) & build_segment(segment2[0],segment2[1])))

def has_intersection(segment_list):
    for segment1 in segment_list:
        for segment2 in segment_list:
            if segment1 != segment2:
                if intersect(segment1,segment2):
                    print(segment1,segment2)
                    return True
    return False

segments = [(0,5),(2,7),(2,7),(1,8),(-3,1),(1,2)]
segments2 = [(0,5),(6,7),(8,9),(-2,-1),(7,9)]
segments2.sort()
# print(segments2)
# print(has_intersection(segments2))

def more_efficient_has_intersection(segment_list):
    for i in range(len(segment_list)-1):
        if intersect(segment_list[i],segment_list[i+1]):
            print(segment_list[i],segment_list[i+1])
            return True
    return False

# print(more_efficient_has_intersection(segments2))

def covers(segment_list, segment):
    segment_list.sort()
    for seg in segment_list:
        print(segment, seg)
        if segment in segment_list or (seg[0]<= segment[0] and seg[1]>=segment[1]) or segment[0] == segment[1]:
            return True
        if seg[0] > segment[0]:
            return False
        if intersect(seg,segment):
            segment = (seg[1],segment[1])
    return False


def test(list):
    for a,b in list:
        print('a:', a, '  b:', b)

test_list = [(1,2),(3,4),(5,6)]

# test(test_list)

def gen(num):
    frac_num = list()

    while num > 0:
        frac_num.append(num%10)
        num //= 10

    frac_num = frac_num[::-1]

    for i in frac_num:
        yield i


a = gen(423)

for i in a:
    print(i)