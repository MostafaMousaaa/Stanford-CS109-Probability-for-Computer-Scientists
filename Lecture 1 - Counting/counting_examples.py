"""
Stanford CS109 - Lecture 1: Counting
Code Examples and Demonstrations
"""

import math
from itertools import permutations, combinations

def factorial(n):
    """Calculate n!"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def permutation(n, r):
    """Calculate P(n,r) = n!/(n-r)!"""
    if r > n:
        return 0
    return factorial(n) // factorial(n-r)

def combination(n, r):
    """Calculate C(n,r) = n!/(r!(n-r)!)"""
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n-r))

def permutation_with_repetition(n, r):
    """Calculate n^r"""
    return n ** r

def combination_with_repetition(n, r):
    """Calculate C(n+r-1, r)"""
    return combination(n + r - 1, r)

def inclusion_exclusion_three_sets(a, b, c, ab, ac, bc, abc):
    """Calculate |A ∪ B ∪ C| using inclusion-exclusion principle"""
    return a + b + c - ab - ac - bc + abc

def main():
    print("STANFORD CS109 - LECTURE 1: COUNTING EXAMPLES")
    print("=" * 50)
    
    # Example 1: Basic Counting
    print("\n1. BASIC COUNTING EXAMPLES")
    print("-" * 30)
    print(f"5! = {factorial(5)}")
    print(f"P(5,3) = {permutation(5,3)}")
    print(f"C(5,3) = {combination(5,3)}")
    print(f"3-digit numbers: {permutation_with_repetition(10,3)}")
    
    # Example 2: Password Combinations
    print("\n2. PASSWORD EXAMPLE")
    print("-" * 30)
    # How many 4-character passwords using letters a-z?
    letters = 26
    password_length = 4
    total_passwords = permutation_with_repetition(letters, password_length)
    print(f"4-character passwords using a-z: {total_passwords:,}")
    
    # Example 3: Committee Selection
    print("\n3. COMMITTEE SELECTION")
    print("-" * 30)
    # How many ways to select a committee of 3 from 10 people?
    people = 10
    committee_size = 3
    ways_to_select = combination(people, committee_size)
    print(f"Ways to select committee of 3 from 10 people: {ways_to_select}")
    
    # Example 4: Candy Distribution
    print("\n4. CANDY DISTRIBUTION")
    print("-" * 30)
    # How many ways to distribute 8 identical candies to 4 children?
    candies = 8
    children = 4
    distribution_ways = combination_with_repetition(children, candies)
    print(f"Ways to distribute {candies} candies to {children} children: {distribution_ways}")
    
    # Example 5: Using itertools for verification
    print("\n5. VERIFICATION WITH ITERTOOLS")
    print("-" * 30)
    items = ['A', 'B', 'C', 'D']
    r = 2
    
    # Permutations
    perm_list = list(permutations(items, r))
    print(f"Permutations of {items} taken {r} at a time:")
    print(f"Count: {len(perm_list)} (should be {permutation(len(items), r)})")
    print(f"Permutations: {perm_list}")
    
    # Combinations
    comb_list = list(combinations(items, r))
    print(f"\nCombinations of {items} taken {r} at a time:")
    print(f"Count: {len(comb_list)} (should be {combination(len(items), r)})")
    print(f"Combinations: {comb_list}")
    
    # Example 6: Inclusion-Exclusion Principle
    print("\n6. INCLUSION-EXCLUSION PRINCIPLE")
    print("-" * 30)
    # Example: In a class of 100 students:
    # 60 take Math, 40 take Physics, 30 take Chemistry
    # 20 take Math and Physics, 15 take Math and Chemistry, 10 take Physics and Chemistry
    # 5 take all three
    math_students = 60
    physics_students = 40
    chemistry_students = 30
    math_physics = 20
    math_chemistry = 15
    physics_chemistry = 10
    all_three = 5
    
    total_taking_at_least_one = inclusion_exclusion_three_sets(
        math_students, physics_students, chemistry_students,
        math_physics, math_chemistry, physics_chemistry, all_three
    )
    print(f"Students taking at least one subject: {total_taking_at_least_one}")
    
    # Example 7: Poker Hands
    print("\n7. POKER HANDS")
    print("-" * 30)
    # How many 5-card poker hands from a 52-card deck?
    deck_size = 52
    hand_size = 5
    poker_hands = combination(deck_size, hand_size)
    print(f"Number of 5-card poker hands: {poker_hands:,}")
    
    # Example 8: Letter Arrangements
    print("\n8. LETTER ARRANGEMENTS")
    print("-" * 30)
    word = "MISSISSIPPI"
    # Count letters
    letter_counts = {}
    for letter in word:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    # Calculate arrangements accounting for repeated letters
    numerator = factorial(len(word))
    denominator = 1
    for count in letter_counts.values():
        denominator *= factorial(count)
    
    arrangements = numerator // denominator
    print(f"Word: {word}")
    print(f"Letter counts: {letter_counts}")
    print(f"Number of distinct arrangements: {arrangements:,}")
    
    # Example 9: Binary Strings
    print("\n9. BINARY STRINGS")
    print("-" * 30)
    # How many 8-bit binary strings have exactly 3 ones?
    string_length = 8
    ones_count = 3
    binary_strings = combination(string_length, ones_count)
    print(f"8-bit binary strings with exactly 3 ones: {binary_strings}")
    
    # Example 10: Lattice Paths
    print("\n10. LATTICE PATHS")
    print("-" * 30)
    # How many ways to go from (0,0) to (5,3) moving only right or up?
    # This is equivalent to choosing 5 right moves out of 8 total moves
    right_moves = 5
    up_moves = 3
    total_moves = right_moves + up_moves
    lattice_paths = combination(total_moves, right_moves)
    print(f"Lattice paths from (0,0) to (5,3): {lattice_paths}")

if __name__ == "__main__":
    main() 