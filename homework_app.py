import random
from handlers.algo_comparator import get_results, find_fastest_algorithm
from handlers.binary_search import binary_search
from handlers.deletion import HashTable


class Homework:
    def deletion_task():
        hash = HashTable(5)
        hash.insert("apple", 10)
        hash.insert("orange", 20)
        hash.insert("banana", 30)
        print(hash.delete("apple"))

    def binary_search_task():
        arr = [random.random() for _ in range(1000)]
        arr.sort()
        x = 0.55
        iterations, upper_bound = binary_search(arr, x)
        if upper_bound is not None:
            print(
                f"Upper bound of {x} is {upper_bound}, found in {iterations} iterations"
            )
        else:
            print(f"Element is not present in array, {iterations} iterations was made")

    def algorithm_task():
        results_article_1, results_article_2 = get_results()

        fastest_alg_article_1 = find_fastest_algorithm(results_article_1)
        fastest_alg_article_2 = find_fastest_algorithm(results_article_2)

        t_kmp_1r = results_article_1["Knuth-Morris-Pratt"][0]
        t_kmp_1m = results_article_1["Knuth-Morris-Pratt"][1]
        t_kmp_2r = results_article_2["Knuth-Morris-Pratt"][0]
        t_kmp_2m = results_article_2["Knuth-Morris-Pratt"][1]

        t_boyer_moore_1r = results_article_1["Boyer-Moore"][0]
        t_boyer_moore_1m = results_article_1["Boyer-Moore"][1]
        t_boyer_moore_2r = results_article_2["Boyer-Moore"][0]
        t_boyer_moore_2m = results_article_2["Boyer-Moore"][1]

        t_rabin_karp_1r = results_article_1["Rabin-Karp"][0]
        t_rabin_karp_1m = results_article_1["Rabin-Karp"][1]
        t_rabin_karp_2r = results_article_2["Rabin-Karp"][0]
        t_rabin_karp_2m = results_article_2["Rabin-Karp"][1]

        print(
            f"| {'Algorithm':<25} | {'Real pattern (art. 1)':<25} | {'Missing pattern (art. 1)':<25} | {'Real pattern (art. 2)':<25} | {'Missing pattern (art. 2)':<25} |"
        )
        print(f"| {'-'*25} | {'-'*25} | {'-'*25} | {'-'*25} | {'-'*25} |")
        print(
            f"| {'Knuth-Morris-Pratt':<25} | {t_kmp_1r:25.5f} | {t_kmp_1m:25.5f} | {t_kmp_2r:25.5f} | {t_kmp_2m:25.5f} |"
        )
        print(
            f"| {'Boyer-Moore':<25} | {t_boyer_moore_1r:25.5f} | {t_boyer_moore_1m:25.5f} | {t_boyer_moore_2r:25.5f} | {t_boyer_moore_2m:25.5f} |"
        )
        print(
            f"| {'Rabin-Karp':<25} | {t_rabin_karp_1r:25.5f} | {t_rabin_karp_1m:25.5f} | {t_rabin_karp_2r:25.5f} | {t_rabin_karp_2m:25.5f} |"
        )
        print(
            f"| {'Fastest algorithm':<25} | {fastest_alg_article_1[0]:<25} | {fastest_alg_article_1[1]:<25} | {fastest_alg_article_2[0]:<25} | {fastest_alg_article_2[1]:<25} |"
        )
