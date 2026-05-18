#!/usr/bin/env python3
"""
生成练习题（不含答案），用于 UK 本科数学和编程课程的自主练习。

用法:
  # 列出所有可用话题
  python generate_practice.py --list-topics

  # 生成 3 道一元二次方程练习题
  python generate_practice.py --topic "quadratic" --count 3

  # 生成 2 道编程练习题
  python generate_practice.py --topic "binary-search" --count 2 --category programming

  # 从数学题库随机抽取 5 道
  python generate_practice.py --count 5 --category math

UK 适配:
  - 题干使用英式英语拼写 (analyse, behaviour, centre 等)
  - 统计题使用 UK 习惯符号
"""

import argparse
import random
import sys
from typing import Callable

# ============================================================
# 数学题目生成器
# ============================================================

def _quadratic_equation() -> str:
    """解一元二次方程"""
    a = random.randint(1, 4)
    b = random.choice([r for r in range(-8, 9) if r != 0])
    c = random.choice([r for r in range(-12, 13) if r != 0])

    def sign(x, with_one=False):
        if x >= 0:
            return "+" if not (with_one and abs(x) == 1) else ""
        return "-"

    b_term = f"{sign(b, True)} {abs(b)}x" if abs(b) != 1 else f"{sign(b)} x"
    c_str = f"{sign(c)} {abs(c)}"
    eq = f"{a}x^2 {b_term} {c_str} = 0"

    return (
        f"Solve the quadratic equation: {eq}\n"
        f"  (a) Calculate the discriminant D.\n"
        f"  (b) Determine the number of real roots.\n"
        f"  (c) Find all roots (if any)."
    )


def _simultaneous_equations() -> str:
    """二元一次方程组"""
    x, y = random.randint(1, 9), random.randint(1, 9)
    a1, b1 = random.randint(1, 5), random.randint(1, 5)
    c1 = a1 * x + b1 * y
    a2, b2 = random.randint(1, 5), random.randint(1, 5)
    # 确保不是同一条直线的倍数
    while a1 * b2 == a2 * b1:
        a2 = random.randint(1, 5)
        b2 = random.randint(1, 5)
    c2 = a2 * x + b2 * y

    return (
        f"Solve the simultaneous equations:\n"
        f"  {a1}x + {b1}y = {c1}\n"
        f"  {a2}x + {b2}y = {c2}\n"
        f"  Use either substitution or elimination method."
    )


def _differentiation() -> str:
    """求导"""
    pool = [
        ("3x^4 - 2x^3 + 5x^2 - 7x + 1", "polynomial"),
        ("sin(2x) + cos(x^2)", "trigonometric + chain rule"),
        ("e^x * ln(x)", "product rule"),
        ("ln(x^2 + 1)", "chain rule with log"),
        ("(x^2 + 1) / (x - 1)", "quotient rule"),
    ]
    expr, hint = random.choice(pool)
    return f"Differentiate f(x) = {expr} with respect to x.\n  Hint: think about which rule(s) apply ({hint})."


def _integration() -> str:
    """积分"""
    pool = [
        ("integral of (3x^2 - 4x + 2) dx", "basic power rule"),
        ("integral of sin(3x) dx", "u-substitution"),
        ("integral of x*e^(x^2) dx", "u-substitution"),
        ("integral of ln(x) dx", "integration by parts"),
        ("integral of x*cos(x) dx", "integration by parts (LIATE)"),
    ]
    expr, hint = random.choice(pool)
    return f"Evaluate the indefinite integral: {expr}\n  Hint: {hint}."


def _limits() -> str:
    """极限"""
    pool = [
        "lim(x -> 0) sin(3x) / x",
        "lim(x -> inf) (1 + 2/x)^x",
        "lim(x -> 2) (x^2 - 4) / (x - 2)",
        "lim(x -> 0) (e^x - 1) / x",
    ]
    return f"Evaluate the limit: {random.choice(pool)}\n  Show your working step by step."


def _matrix_ops() -> str:
    """矩阵运算"""
    a11, a12 = random.randint(1, 4), random.randint(-2, 3)
    a21, a22 = random.randint(-2, 4), random.randint(1, 5)
    b11, b12 = random.randint(-3, 3), random.randint(1, 4)
    b21, b22 = random.randint(1, 4), random.randint(-3, 3)

    return (
        f"Given matrices:\n"
        f"  A = [[{a11}, {a12}], [{a21}, {a22}]]\n"
        f"  B = [[{b11}, {b12}], [{b21}, {b22}]]\n"
        f"  (a) Calculate A + B\n"
        f"  (b) Calculate AB (matrix multiplication)\n"
        f"  (c) Find det(A) and determine if A is invertible."
    )


def _probability_distribution() -> str:
    """概率分布"""
    n = random.randint(8, 15)
    p = random.choice([0.2, 0.25, 0.3, 0.4, 0.5])
    return (
        f"A fair coin is tossed {n} times. Let X be the number of heads.\n"
        f"  (a) State the distribution of X and its parameters.\n"
        f"  (b) Find P(X = {random.randint(2, n//2)})\n"
        f"  (c) Find E[X] and Var(X)."
    )


def _hypothesis_testing() -> str:
    """假设检验"""
    population_mean = random.randint(80, 120)
    sample_mean = population_mean + random.choice([-8, -5, -3, 3, 5, 8])
    sample_sd = random.randint(10, 20)
    n = random.choice([25, 30, 36, 49])

    return (
        f"A researcher wants to test whether the population mean differs from {population_mean}.\n"
        f"A random sample of n = {n} gives a sample mean of x-bar = {sample_mean} and sample standard deviation s = {sample_sd}.\n"
        f"  (a) State H0 and H1.\n"
        f"  (b) Calculate the test statistic (use alpha = 0.05).\n"
        f"  (c) State your conclusion in context. What assumption(s) are you making?"
    )


MATH_GENERATORS: dict[str, tuple[str, Callable[[], str]]] = {
    "quadratic": ("Quadratic Equations", _quadratic_equation),
    "simultaneous": ("Simultaneous Equations", _simultaneous_equations),
    "differentiation": ("Differentiation", _differentiation),
    "integration": ("Integration", _integration),
    "limits": ("Limits", _limits),
    "matrices": ("Matrix Operations", _matrix_ops),
    "probability": ("Probability Distributions", _probability_distribution),
    "hypothesis": ("Hypothesis Testing", _hypothesis_testing),
}


# ============================================================
# 编程题目生成器
# ============================================================

def _fizzbuzz_variant() -> str:
    """FizzBuzz 变体"""
    n = random.randint(20, 40)
    a, b = random.sample([3, 4, 5, 7], 2)
    wa = random.choice(["Fizz", "Foo", "Tick"])
    wb = random.choice(["Buzz", "Bar", "Tock"])
    return (
        f"Write a function that prints numbers from 1 to {n}. For multiples of {a}, print '{wa}'.\n"
        f"For multiples of {b}, print '{wb}'. For multiples of both {a} and {b}, print '{wa}{wb}'.\n"
        f"Pay attention to the order of your conditional statements."
    )


def _binary_search_problem() -> str:
    """二分查找"""
    arr_size = random.randint(8, 15)
    arr = sorted(random.sample(range(-20, 30), arr_size))
    target = random.choice(arr + [999])

    return (
        f"Implement binary search to find target = {target} in the sorted array:\n"
        f"  arr = {arr}\n"
        f"  (a) Return the index if found, otherwise return -1.\n"
        f"  (b) State the loop invariant.\n"
        f"  (c) What is the worst-case time complexity? Justify your answer."
    )


def _two_sum() -> str:
    """Two Sum"""
    arr = [random.randint(-10, 15) for _ in range(random.randint(6, 10))]
    i, j = random.sample(range(len(arr)), 2)
    target = arr[i] + arr[j]

    return (
        f"Given arr = {arr} and target = {target}, find all pairs of indices (i, j) with i < j\n"
        f"such that arr[i] + arr[j] == target.\n"
        f"  (a) Implement a brute-force O(n²) solution.\n"
        f"  (b) Optimise to O(n) using a hash map. Explain the trade-off."
    )


def _palindrome_check() -> str:
    """回文判断"""
    cases = [
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("Was it a car or a cat I saw?", True),
        ("No lemon, no melon", True),
    ]
    s, _ = random.choice(cases)
    return (
        f'Write a function that checks whether the string "{s}" is a palindrome.\n'
        f"  Requirements:\n"
        f"  (a) Ignore case, spaces, and non-alphanumeric characters.\n"
        f"  (b) Implement using two pointers — do NOT use [::-1] slicing.\n"
        f"  (c) Analyse the space complexity of your solution."
    )


def _fibonacci_comparison() -> str:
    """斐波那契三种写法对比"""
    n = random.randint(7, 15)
    return (
        f"Implement a function to compute the {n}-th Fibonacci number (0-indexed, F(0)=0, F(1)=1).\n"
        f"  (a) Recursive implementation (without memoisation).\n"
        f"  (b) Iterative implementation.\n"
        f"  (c) Compare the time complexity of (a) and (b). Which is more efficient and why?\n"
        f"  (d) Can you improve (a) with memoisation? What is the new time complexity?"
    )


def _anagram_check() -> str:
    """变位词"""
    pairs = [("listen", "silent"), ("debit card", "bad credit"), ("hello", "world"), ("astronomer", "moon starer")]
    s1, s2 = random.choice(pairs)
    return (
        f'Write a function to determine whether "{s1}" and "{s2}" are anagrams.\n'
        f"  Requirements:\n"
        f"  (a) Ignore spaces and case.\n"
        f"  (b) Implement TWO approaches: (i) sorting, (ii) frequency counting.\n"
        f"  (c) Compare the time and space complexity of both."
    )


def _recursive_sum() -> str:
    """递归求和/列表处理"""
    arr = [random.randint(1, 10) for _ in range(random.randint(4, 7))]
    return (
        f"Write a recursive function to compute the sum of all elements in a list, e.g. arr = {arr}.\n"
        f"  (a) Identify the base case.\n"
        f"  (b) Implement the function.\n"
        f"  (c) Trace the recursion for arr = [1, 2, 3] — show the call stack."
    )


PROG_GENERATORS: dict[str, tuple[str, Callable[[], str]]] = {
    "fizzbuzz": ("FizzBuzz Variant", _fizzbuzz_variant),
    "binary-search": ("Binary Search", _binary_search_problem),
    "two-sum": ("Two Sum", _two_sum),
    "palindrome": ("Palindrome Check", _palindrome_check),
    "fibonacci": ("Fibonacci Sequence", _fibonacci_comparison),
    "anagram": ("Anagram Check", _anagram_check),
    "recursion": ("Recursive Sum", _recursive_sum),
}


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generate practice problems for UK undergraduate maths and programming courses.",
    )
    parser.add_argument("--topic", type=str, help="Topic key (e.g. quadratic, binary-search)")
    parser.add_argument("--count", type=int, default=1, help="Number of problems to generate")
    parser.add_argument(
        "--category",
        type=str,
        choices=["math", "programming"],
        default="math",
        help="Which pool to draw from",
    )
    parser.add_argument("--list-topics", action="store_true", help="List available topics")
    args = parser.parse_args()

    if args.list_topics:
        print("=== Mathematics ===")
        for key, (name, _) in MATH_GENERATORS.items():
            print(f"  {key:<18} {name}")
        print("=== Programming ===")
        for key, (name, _) in PROG_GENERATORS.items():
            print(f"  {key:<18} {name}")
        print("\nUsage: python generate_practice.py --topic <key> --count N [--category math|programming]")
        return

    pool = MATH_GENERATORS if args.category == "math" else PROG_GENERATORS

    if args.topic:
        args.topic = args.topic.strip().lower()
        matched = {k: v for k, v in pool.items() if args.topic in k.lower()}
        if not matched:
            print(f"[!] No topic matching '{args.topic}' found in {args.category}", file=sys.stderr)
            print(f"[!] Use --list-topics to see available topics.", file=sys.stderr)
            sys.exit(1)
        pool = matched

    entries = list(pool.items())
    for i in range(args.count):
        key, (name, gen_func) = entries[i % len(entries)]
        print(f"--- Problem {i+1}: {name} ---")
        print(gen_func())
        print()


if __name__ == "__main__":
    main()
