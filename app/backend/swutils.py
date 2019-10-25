import numpy as np
import re
import os
import pickle
from decimal import *
import string
import random
import sys

import swutils as sw

# List of funcs
# - load()
# - find_nearest()
# - find_idx()
# - ls()
# - load_txt()
# - isempty()
# - cat()
# - strip_brackets()
# - rm_linebreak()
# - rm_char()
# - find_substr()
# - get_labels()
# - getdata_col()
# - rm_stopwords()


# ----------------------------------------------------------------------------------------------------------------------
# printtry(): test function to print a string
def printtry(a):
    print("a=",a)

# @vec2dec(): convert to decimal
# deps: from decimal import *
def vec2dec(v):
    # TWOPLACES = Decimal(10) ** -2
    # d = Decimal(str(v).strip('[]')).quantize(TWOPLACES)
    d = Decimal(str(v).strip('[]'))

    return d


def vec2int(v):
    d=int(str(v).strip('[]'))
    return d


# @pwd(): get current dir in linux format, appends a '/' at the end if absent.
# IN - none.
# OUT - this_dir - current directory.
# @ example
# ---------
# this_dir=sw.pwd()
def pwd():
    this_dir=sys.path[0]
    this_dir=this_dir.replace('\\', '/')
    if this_dir[-1]!='/': this_dir=this_dir+"/"

    return this_dir


# load: load all vars from pickle file.
# IN - fn - (string) filename to .pkl
#
# Example
# -------
# vars, var_names = sw.load(fn_save)
# for n in range(0,vars.__len__()):
#     exec(var_names[n] + "=vars[" + str(n) + "]")
# del vars, var_names
#
def load(fn):
    objs = []
    with open(fn, 'rb') as f:
        while 1:
            try:
                o = pickle.load(f)
            except EOFError:
                break
            objs.append(o)

    len=objs[0].__len__()-1
    var_names=objs[0][len]
    vars=objs[0][0:len]
    print("pkl-file loaded:", fn)
    print("var_names:", var_names, "\n")

    return vars, var_names


# @cat(): concantenate matrices
# IN - x1 - matrix 1
# IN - x2 - matrix 2
# IN - parms - '0': horizontal, '1': vertical; default=1, '2': string array
# OUT - y - output
def cat(x1, x2, parms=1):
    if parms==0:     # horizontal
        y=np.concatenate((x1, x2), axis=1)
    elif parms==1:   # vertical
        y=np.concatenate((x1, x2), axis=0)
    elif parms==2:   # string array
        y=np.concatenate((x1,x2), axis=None)
    else: raise ValueError('sw.cat(): value out of bounds: "parms"')

    return y


# @cat_arr2mat(): concatenate array to a matrix
# IN - M - matrix
# IN - v - vector (i.e., row array)
# OUT - out - concatenated matrix
def cat_arr2mat( M, v):
    out=np.hstack((M, np.array([v]).T))

    return out


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx, array[idx]


# @find(): [matlab] idx=find(x==val)
# IN - x - input vector
# IN - str_in - input cmd string (e.g., "==True", '>5')
# OUT - idx - output index array
def find(x, str_in):
    exec("idx=(x" + str_in + ").nonzero()")
    idx=idx[0]

    return idx


# @find_true(): [matlab] idx=find(x)
# IN - x - boolean array of 1's and 0's
# OUT - idx - positions of 1's in x
def find_true(x):
    idx=np.where(x==True)
    idx=idx[0]

    # alt syntax
    # ----------
    # idx=(x==True).nonzero()

    return idx

def find_idx(x):
    idx=np.where(x==True)
    idx=idx[0]

    # alt syntax
    # ----------
    # idx=(x==True).nonzero()

    return idx



def ls(dir_):
    fileList = next(os.walk(dir_))[2]
    fileList.sort()
    sz_list = fileList.__len__()

    return fileList, sz_list


# load_txt(): read in txt-file
def load_txt(fn):
    txt_data = [line.rstrip('\n') for line in open(fn)]
    return txt_data


# isempty: check if numpy array is empty or not
# note: for ~isempty() --> not isempty()
def isempty(x):
    if x.size==0: return True
    else: return False


# @isequal(): check if equal
# IN - A - vector/matrix 1
# IN - B - vector/matrix 2
# OUT - flag - '1': true, '0': false
def isequal(A, B):
    flag=False
    if A.shape==B.shape:
        # if np.all(np.equal(A,B)): flag=True
        flag=np.allclose(A,B,equal_nan=True)

    return flag


# cat: concatenate array
# def cat(idx, x):
#     idx=np.concatenate((idx,x), axis=None)

#     return idx


# strip_brackets: strip a string of brackets
def strip_brackets(s):
    return str(s).strip('[]')


def rm_linebreak(str_in):
    idx=[]
    for a in list(re.finditer("\n", str_in)):
        idx = a.start()

    if not not idx:
        str_in = str_in[:idx] + " " + str_in[idx + 1:]

    return str_in


# rm_char: remove a character from a string sentence
def rm_char(str_in, idx):
    str_in = str_in[:idx] + str_in[idx + 1:]
    return str_in


# @find_str: find substring in string and return the index
# IN - s - string
# IN - s2 - substring
# OUT - index - position of s2 in set

# example
# -------
# idx=find_str(s, "min")

# def find_str(s, s2):
#     index = 0

#     if s2 in s:
#         c = s2[0]
#         for ch in s:
#             if ch == c:
#                 if s[index:index+len(s2)] == s2:
#                     return index

#             index += 1

#     return -1
def find_str(s, s2):
    if s2 in s:
        mem_idx=np.empty(0)
        idx=0
        len_s2=len(s2)
        for ch in s:
            if ch==s2[0]:
                if s[idx:idx+len_s2]==s2:
                    mem_idx=sw.cat(mem_idx, idx, 2)
            idx+=1

    return mem_idx.astype(int)


# @find_substr: find substring in string and return the index
# IN - s - string
# IN - s2 - substring
# OUT - index - position of s2 in set

# example
# -------
# idx=find_substr(s, "min")
#
# OR ALTERNATIVELY: idx=[m.start() for m in re.finditer('/', m)]
def find_substr(s, s2):
    index = 0

    if s2 in s:
        c = s2[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(s2)] == s2:
                    return index

            index += 1

    return -1


# @rand_int(): generate random integers (useful for indices selection)
# IN - lb - lower bound
# IN - ub - upper bound
# IN - N - number of random integers to generate
# OUT - idx - output numpy array of random integers
#
# example
# -------
# idx2=sw.rand_int(0, idx.shape[0]-1, num_pts)   # idx.shape[0]-1: 0th-indexing therefore minus 1
def rand_int(lb, ub, N):
    idx=np.zeros(shape=(N,), dtype=int)
    for n in range(N):
        idx[n]=random.randint(lb, ub)

    return idx


# @getdate_datetime64(): get date from datetime64 struct
# IN - dt - date; format: np.datetime64()
# OUT - out - date format; format: str
def getdate_datetime64(t):
    out=str(t)[0:10]

    return out

# @gettime_datetime64(): get hours from datetime64 struct
# IN - t - time; format: np.datetime64()
# OUT - out - hours format; format: str
def gettime_datetime64(t):
    s=str(t)[11:16]
    idx=find_str(s, ":")
    idx=idx[0]

    out=s[0:idx]+s[idx+1:]+"h"

    return out

# TODO: @compare_time(t1, t2)
# IN - t1 - 1st time instance; format: np.datetime64()
# IN - t2 - 2nd time instance; format: np.datetime64()
# IN - t_interval - time interval in comparison; format: minutes
# OUT - out - is greater, or not; format: bool.
def compare_time(t1, t2, t_interval):
    out=(t2-t1)>np.timedelta64(t_interval*60,'s')

    return out


# @clean_nan(): remove all nans from a vector
# IN/OUT - x - input vector / output with no nan.
def clean_nan(x):
    x=x[~np.isnan(x)]

    return x


# pandas excel tools ---------------------------------------------------------------------------------------------------
# @get_labels: get all labels for alarms and trips
# IN - x - alarm/trip data from df
# IN - src_str - search string
# OUT - y - cleaned up labels
#
# example
# -------
# y=get_labels(df["CH-1 SYS ALARM"])
def get_labels(x, src_str):
    # '12:50AM 0min', '1:50AM 0min'  --> so need to search for the position of src_str="min"
    N=x.size
    y=np.zeros(shape=(N), dtype=int)
    for n in range(0,N):
        s=x[n]
        idx=find_str(s, src_str)
        y[n]=s[idx-1]

    return y


# @getdata_col - extract data from a column in df
# IN  - df - excel data struct
# IN  - col_name - column name
# OUT - out - the data from the column
#
# example
# -------
def getdata_col(df, col_name):
    out=df[col_name]
    out=out.values

    return out

# NLP Tools ------------------------------------------------------------------------------------------------------------

# describe: remove stopwords from a string
# in - str_in - input string
# in - stopwords - list of unwanted words.
# out - str_out - the result
# example start ---
#     str_in = 'What is hello'
#     stopwords = ['what','who','is','a','at','is','he']
#     str_clean = csw.rm_stopwords(str_in, stopwords)
# example end ---
def rm_stopwords(str_in, stopwords):
    querywords = str_in.split()
    resultwords = [word for word in querywords if word.lower() not in stopwords]
    str_out = ' '.join(resultwords)

    return str_out

