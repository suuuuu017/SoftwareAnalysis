import random
import re

# TODO generate your own good seed file at ./task2_seed.c


def replace_equal_with_not_equal(programString):
    # TODO implement
    it = list(re.finditer('==', programString))
    repl = random.sample(it, k=1)[0]
    programString = programString[: repl.start()] + '!=' + programString[repl.end():]
    return programString


def add_empty_statement(programString):
    # TODO implement
    # meaning?
    return programString


def make_predicate_condition_true(programString):
    # TODO implement
    # if()?
    return programString


def remove_bitwise_operators(programString):
    # TODO implement
    return programString