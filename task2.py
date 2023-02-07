import random
import re

# TODO generate your own good seed file at ./task2_seed.c


def replace_equal_with_not_equal(programString):
    # TODO implement
    it = list(re.finditer('==', programString))
    if len(it) >0:
        repl = random.sample(it, k=1)[0]
        programString = programString[: repl.start()] + '!=' + programString[repl.end():]
    return programString


def add_empty_statement(programString):
    # TODO implement
    it = list(re.finditer(r';\n|{\n', programString))
    if len(it) > 0:
        repl = random.sample(it, k=1)[0]
        programString = programString[: repl.end()] + ';\n' + programString[repl.end():]
    return programString


def make_predicate_condition_true(programString):
    # TODO implement
    # if() while() for()
    # it = list(re.finditer(r'if(\s*?\([^True]|.*? $(\s? \)))', programString))
    itif = list(re.finditer('if(\s*?)\((?!True)(.*?)(?=\))', programString))
    itwhile = list(re.finditer('while(\s*?)\((?!True)(.*?)(?=\))', programString))
    itfor = list(re.finditer('for(\s*?)\((?!True)(.*?)(?=\))', programString))
    it = itif + itwhile + itfor
    if len(it) > 0:
        repl = random.sample(it, k=1)[0]
        idx = it.index(repl)
        # offset=[3,6,4]
        o = 0
        if idx < len(itif):
            o = 3
        elif idx >= len(itif) and idx < len(itif) + len(itwhile):
            o = 6
        else:
            o = 5
        programString = programString[: repl.start()+o] + 'True' + programString[repl.end():]
    return programString


def remove_bitwise_operators(programString):
    # TODO implement
    return programString