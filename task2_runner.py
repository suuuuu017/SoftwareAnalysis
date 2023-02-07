import tempfile
import os
import random
import task2

import re


def compile(programString, timeout="10s"):
    with open("task1_tcc_run_string.txt", "r") as tcc_run_string_file:
        run_string = tcc_run_string_file.read()
    with tempfile.NamedTemporaryFile(mode="w") as temp_file:
        temp_file.write(programString)
        temp_file.flush()
        run_string = run_string.replace("@@", temp_file.name)
        ret_val = os.system("timeout %s %s" % (timeout, run_string))
        return ret_val  # 0 indicates success, 31744 indicates timeout, others indicate TCC failure


def export(program_list, program_type):
    for index, program in enumerate(program_list):
        with open("./task2_out/{program_type}-{str(index)}", "w") as f:
            f.write(program)
        print(f,"{program_type} %d" % (index + 1))
        print(program)


def fuzzer(seed_program_string, number_required_mutations=10000):
    valid_mutations = 0
    variants = []
    invalid = []
    crash = []
    hang = []
    program = seed_program_string
    while (
        valid_mutations < number_required_mutations
        and len(crash) + len(hang) < number_required_mutations
    ):
        mutationChoice = random.randrange(0, 4)
        if mutationChoice == 0:
            tentative_program = task2.replace_equal_with_not_equal(program)
        elif mutationChoice == 1:
            tentative_program = task2.add_empty_statement(program)
        elif mutationChoice == 2:
            tentative_program = task2.make_predicate_condition_true(program)
        elif mutationChoice == 3:
            tentative_program = task2.remove_bitwise_operators(program)
        ret_val = compile(tentative_program)
        if ret_val == 0:
            valid_mutations += 1
            program = tentative_program  # retain variations that compile
            variants.append(program)
        elif ret_val == 31744:
            hang.append(tentative_program)
        elif ret_val == 256:
            invalid.append(tentative_program)
        else:
            crash.append(tentative_program)

    print("Programs that passed:")
    export(variants, "passed")

    print("Programs that did not compile:")
    export(invalid, "invalid")

    print("Programs that caused a hang:")
    export(hang, "hang")

    print("Programs that crashed tcc:")
    export(crash, "crash")

    print("Valid count: %d" % len(variants))
    print("Did not compile count: %d" % len(invalid))
    print("Caused TCC to hang count: %d" % len(hang))
    print("Caused TCC to crash count: %d" % len(crash))
    return program


if __name__ == "__main__":
    with open("task2_seed.c", "r") as seed_input:
        seed_program = seed_input.read()
    # num_to_run = 10000
    num_to_run = 1
    # print(seed_program)
    seed_program = task2.make_predicate_condition_true(seed_program)
    print(seed_program)
    # seed_program = task2.make_predicate_condition_true(seed_program)
    # print(seed_program)
    # fuzzer(seed_program, num_to_run)
