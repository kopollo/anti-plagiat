"""
package that contains comparing algorithm and
functions to work with python tokens.

"""
import token
import tokenize
from io import StringIO


def levenstein_distance(first_sequence, second_sequence):
    """
    Find levenshtein distance of two texts.

    :param first_sequence: first text
    :param second_sequence: second text
    :return: levenshtein distance
    """
    n, m = len(first_sequence), len(second_sequence)
    if n > m:
        first_sequence, second_sequence = second_sequence, first_sequence
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = (
                previous_row[j] + 1,
                current_row[j - 1] + 1,
                previous_row[j - 1],
            )
            if first_sequence[j - 1] != second_sequence[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def get_tokens(source_code):
    """
    Generate tokens based on source code.

    :param source_code: code of program
    :return: list of tokens in numeric view
    """
    lines = source_code.strip()
    tokens = []
    rl = StringIO(lines).readline
    try:
        for t_type, t_str, (br, bc), (er, ec), logl in (
                tokenize.generate_tokens(rl)):
            tokens.append(t_type)
    except tokenize.TokenError:
        pass
    return tokens


def print_tokens_info(source_code):
    """
    Print in a formatted way token id, toked name title and
    the object that called this token.

    :param source_code: source where we want to get tokens info
    """
    lines = source_code.strip()
    rl = StringIO(lines).readline
    for t_type, t_str, (br, bc), (er, ec), logl in tokenize.generate_tokens(
            rl):
        print(
            "%3i %10s : %20r" % (t_type, token.tok_name[t_type], t_str)
        )


def tokens_filer(tokens):
    """
    Delete from list COMMENT and NEW LINE tokens.

    :param tokens: list of tokens
    :return: list without COMMENT and NEW LINE tokens
    """
    bad_tokens_id = [60, 61]  # COMMENT and NEW LINE codes
    tokens = [token_i for token_i in tokens if token_i not in bad_tokens_id]
    return tokens


def get_diff_percent(source_code1, source_code2):
    """
    Get two source codes and calculate difference percent
    by this formula (100 - (levenstein_dist * 100) / max_len).

    :param source_code1: first source code
    :param source_code2: second source code
    :return: difference percent%
    """
    source1_tokens = tokens_filer(get_tokens(source_code1))
    source2_tokens = tokens_filer(get_tokens(source_code2))

    max_len = max(len(source1_tokens), len(source2_tokens))
    levenstein_dist = levenstein_distance(source1_tokens, source2_tokens)
    diff_per = 100 - (levenstein_dist * 100) / max_len
    return str(diff_per)[:5]
