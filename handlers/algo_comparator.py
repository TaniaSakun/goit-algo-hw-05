import timeit


# Knut-Morris-Pratt Algorithm
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


# Boyer-Moore Algorithm
def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


# Rabin-Karp Algorithm
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i : i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (
                current_slice_hash - ord(main_string[i]) * h_multiplier
            ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])
            ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def get_results():
    with open("articles/article_1.txt", "r") as file:
        text1 = file.read()
        pattern_r1 = "public static int binarySearch(int arr[], int elementToSearch)"
        pattern_m1 = "Editors Ricci F., Rokach L., Shapira B., Kantor P. B. Recommender Systems Handbook"

    t_kmp_1r = timeit.timeit(lambda: kmp_search(text1, pattern_r1), number=30)
    t_kmp_1m = timeit.timeit(lambda: kmp_search(text1, pattern_m1), number=30)
    t_boyer_moore_1r = timeit.timeit(
        lambda: boyer_moore_search(text1, pattern_r1), number=30
    )
    t_boyer_moore_1m = timeit.timeit(
        lambda: boyer_moore_search(text1, pattern_m1), number=30
    )
    t_rabin_karp_1r = timeit.timeit(
        lambda: rabin_karp_search(text1, pattern_r1), number=30
    )
    t_rabin_karp_1m = timeit.timeit(
        lambda: rabin_karp_search(text1, pattern_m1), number=30
    )

    with open("articles/article_2.txt", "r") as file:
        text2 = file.read()
        pattern_r2, pattern_m2 = pattern_m1, pattern_r1

    t_kmp_2r = timeit.timeit(lambda: kmp_search(text2, pattern_r2), number=30)
    t_kmp_2m = timeit.timeit(lambda: kmp_search(text2, pattern_m2), number=30)
    t_boyer_moore_2r = timeit.timeit(
        lambda: boyer_moore_search(text2, pattern_r2), number=30
    )
    t_boyer_moore_2m = timeit.timeit(
        lambda: boyer_moore_search(text2, pattern_m2), number=30
    )
    t_rabin_karp_2r = timeit.timeit(
        lambda: rabin_karp_search(text2, pattern_r2), number=30
    )
    t_rabin_karp_2m = timeit.timeit(
        lambda: rabin_karp_search(text2, pattern_m2), number=30
    )

    results_article_1 = {
        "Knuth-Morris-Pratt": (t_kmp_1r, t_kmp_1m),
        "Boyer-Moore": (t_boyer_moore_1r, t_boyer_moore_1m),
        "Rabin-Karp": (t_rabin_karp_1r, t_rabin_karp_1m),
    }

    results_article_2 = {
        "Knuth-Morris-Pratt": (t_kmp_2r, t_kmp_2m),
        "Boyer-Moore": (t_boyer_moore_2r, t_boyer_moore_2m),
        "Rabin-Karp": (t_rabin_karp_2r, t_rabin_karp_2m),
    }

    return results_article_1, results_article_2


def find_fastest_algorithm(results):
    real_pattern_fastest = min(results, key=lambda k: results[k][0])
    missing_pattern_fastest = min(results, key=lambda k: results[k][1])
    return real_pattern_fastest, missing_pattern_fastest
