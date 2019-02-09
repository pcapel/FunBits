"""
Process a name to determine if it can be spelled using the elemental symbols
from the periodic table of elements.  If so, generate all such spellings.

Starts by getting arrays of the available matches to all single characters and
double characters in the name.
Then it creates arrays of truth values that can be compared using the logic that
a match

name = 'cinu' # purely for example's sake
singles = [c i n u]
doubles = [ci in nu]
[T T T T]

[F T F]

(s1 /\ s2) \/ d1
forms the logical basis for describing a potential solution, with the trival
case of all s or d being just all(singles) \/ every_other(doubles)

Every other is required due to the inherent duplication of getting doubled letters.

d0 /\ d2 /\ d4 ... dn
Is the only sequence that actually forms the name.  The other possibilities are
described by
(sn /\ sn+1) \/ dn

if dn then n+2 and continue the checks.

I aim to have only the main function know about the other functions.  It's a
good design practice in my experience.
"""
import json
from os.path import join


def split_up(name):
    singles = [char for char in name]
    # you'll always end up with an extra 1 character on the end
    # slicing doesn't throw index errors, you just get the rest of the string
    # convenient!
    doubles = [name[i:(i + 2)] for i in range(len(name))][:-1]
    return singles, doubles


def table_set():
    with open(join('json', 'periodic-table.json'), 'r') as f:
        data = json.load(f)
    table_set = set([el['symbol'].lower() for el in data['elements']])
    return table_set


def availability(check_list, check_set):
    return [value in check_set for value in check_list]


def main():
    table = table_set()
    name = input('What\'s your name?\n>').lower()
    solutions = dict()
    singles, doubles = split_up(name)
    s_avail = availability(singles, table)
    d_avail = availability(doubles, table)
    for char, i in enumerate(s_avail):
        single_works = all(s_avail[i:i+2])
        double_works = d_avail[i]
        print(single_works or double_works)



if __name__ == '__main__':
    main()
