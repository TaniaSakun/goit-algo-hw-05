# goit-algo-hw-05

**To run the project please complete the following steps:**
1. pip install -r requirements.txt or pip3 install -r requirements.txt
2. python main.py or python3 main.py


**Algorithms comparison**
| Algorithm                 | Real pattern (art. 1)     | Missing pattern (art. 1)  | Real pattern (art. 2)     | Missing pattern (art. 2)  |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| Knuth-Morris-Pratt        |                   0.00853 |                   0.02451 |                   0.03079 |                   0.03607 |
| Boyer-Moore               |                   0.00076 |                   0.00150 |                   0.00162 |                   0.00230 |
| Rabin-Karp                |                   0.02488 |                   0.07320 |                   0.09444 |                   0.10802 |
| Fastest algorithm         | Boyer-Moore               | Boyer-Moore               | Boyer-Moore               | Boyer-Moore               |

**Based on the results of the algorithm comparison we have the next conclusions:**

1. Knuth-Morris-Pratt (KMP):

Performs relatively well for both real and missing patterns in both articles.
Shows consistent performance across different scenarios.

2. Boyer-Moore:

Demonstrates the fastest performance among all algorithms for both real and missing patterns in both articles.
Offers significantly faster execution times compared to KMP and Rabin-Karp.

3. Rabin-Karp:

Shows the slowest performance among the tested algorithms for both real and missing patterns in both articles.
Despite its simplicity, it exhibits slower execution times compared to KMP and Boyer-Moore.

4. Overall Observation:

Boyer-Moore consistently outperforms other algorithms in terms of execution time, making it the preferred choice when efficiency is a priority.
Knuth-Morris-Pratt offers reasonable performance and can be considered a reliable alternative.
Rabin-Karp, while simple to implement, may not be suitable for scenarios requiring high performance due to its slower execution times compared to the other algorithms.
Therefore, based on the given results, the Boyer-Moore algorithm emerges as the fastest and most efficient choice for string pattern matching in the given context.
