"""
Stanford CS109 - Lecture 1: Counting
Practice Problems with Solutions
"""

from counting_examples import factorial, permutation, combination, permutation_with_repetition, combination_with_repetition

def problem_1():
    """How many ways can you arrange the letters in "PROBABILITY"?"""
    print("Problem 1: Letter arrangements in 'PROBABILITY'")
    print("-" * 50)
    
    word = "PROBABILITY"
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
    print(f"Answer: {arrangements:,} ways")
    return arrangements

def problem_2():
    """In a group of 20 people, how many ways can you form a committee of 5?"""
    print("\nProblem 2: Committee selection")
    print("-" * 50)
    
    people = 20
    committee_size = 5
    ways = combination(people, committee_size)
    print(f"People: {people}")
    print(f"Committee size: {committee_size}")
    print(f"Answer: {ways:,} ways")
    return ways

def problem_3():
    """How many 5-card poker hands are possible from a 52-card deck?"""
    print("\nProblem 3: Poker hands")
    print("-" * 50)
    
    deck_size = 52
    hand_size = 5
    hands = combination(deck_size, hand_size)
    print(f"Deck size: {deck_size}")
    print(f"Hand size: {hand_size}")
    print(f"Answer: {hands:,} possible hands")
    return hands

def problem_4():
    """How many ways can you distribute 15 identical balls into 6 boxes?"""
    print("\nProblem 4: Ball distribution")
    print("-" * 50)
    
    balls = 15
    boxes = 6
    ways = combination_with_repetition(boxes, balls)
    print(f"Balls: {balls}")
    print(f"Boxes: {boxes}")
    print(f"Answer: {ways:,} ways")
    return ways

def problem_5():
    """How many 4-digit numbers can be formed using digits 1-9 with no repetition?"""
    print("\nProblem 5: 4-digit numbers without repetition")
    print("-" * 50)
    
    digits = 9  # 1-9
    length = 4
    numbers = permutation(digits, length)
    print(f"Available digits: 1-9 ({digits} digits)")
    print(f"Number length: {length}")
    print(f"Answer: {numbers:,} numbers")
    return numbers

def problem_6():
    """How many ways can you arrange 3 red balls, 2 blue balls, and 1 green ball in a row?"""
    print("\nProblem 6: Colored ball arrangements")
    print("-" * 50)
    
    total_balls = 3 + 2 + 1  # 6 total balls
    red_balls = 3
    blue_balls = 2
    green_balls = 1
    
    # Calculate arrangements accounting for repeated colors
    arrangements = factorial(total_balls) // (factorial(red_balls) * factorial(blue_balls) * factorial(green_balls))
    
    print(f"Red balls: {red_balls}")
    print(f"Blue balls: {blue_balls}")
    print(f"Green balls: {green_balls}")
    print(f"Total balls: {total_balls}")
    print(f"Answer: {arrangements} arrangements")
    return arrangements

def problem_7():
    """How many ways can you choose 3 books from 10 books if 2 specific books must be included?"""
    print("\nProblem 7: Book selection with constraints")
    print("-" * 50)
    
    total_books = 10
    required_books = 2
    committee_size = 3
    
    # If 2 specific books must be included, we only need to choose 1 more from the remaining 8
    remaining_books = total_books - required_books
    additional_books_needed = committee_size - required_books
    
    ways = combination(remaining_books, additional_books_needed)
    
    print(f"Total books: {total_books}")
    print(f"Required books: {required_books}")
    print(f"Committee size: {committee_size}")
    print(f"Remaining books to choose from: {remaining_books}")
    print(f"Additional books needed: {additional_books_needed}")
    print(f"Answer: {ways} ways")
    return ways

def problem_8():
    """How many 6-character passwords can be made using letters a-z and digits 0-9?"""
    print("\nProblem 8: Password combinations")
    print("-" * 50)
    
    letters = 26  # a-z
    digits = 10   # 0-9
    total_chars = letters + digits
    password_length = 6
    
    passwords = permutation_with_repetition(total_chars, password_length)
    
    print(f"Letters: {letters} (a-z)")
    print(f"Digits: {digits} (0-9)")
    print(f"Total characters: {total_chars}")
    print(f"Password length: {password_length}")
    print(f"Answer: {passwords:,} passwords")
    return passwords

def problem_9():
    """How many ways can you distribute 12 identical candies to 5 children if each child must get at least 1 candy?"""
    print("\nProblem 9: Candy distribution with minimum constraint")
    print("-" * 50)
    
    total_candies = 12
    children = 5
    minimum_per_child = 1
    
    # Give each child 1 candy first, then distribute remaining candies
    remaining_candies = total_candies - (children * minimum_per_child)
    
    if remaining_candies < 0:
        ways = 0
    else:
        ways = combination_with_repetition(children, remaining_candies)
    
    print(f"Total candies: {total_candies}")
    print(f"Children: {children}")
    print(f"Minimum per child: {minimum_per_child}")
    print(f"Remaining candies to distribute: {remaining_candies}")
    print(f"Answer: {ways} ways")
    return ways

def problem_10():
    """How many ways can you arrange 4 men and 4 women in a row if no two men can sit next to each other?"""
    print("\nProblem 10: Gender arrangement with constraint")
    print("-" * 50)
    
    men = 4
    women = 4
    
    # First, arrange the women: 4! ways
    women_arrangements = factorial(women)
    
    # Then, place men in the 5 possible positions (before first woman, between women, after last woman)
    # This is equivalent to choosing 4 positions from 5 available positions
    available_positions = women + 1  # 5 positions
    men_positions = combination(available_positions, men)
    
    # Finally, arrange the men in their chosen positions: 4! ways
    men_arrangements = factorial(men)
    
    total_ways = women_arrangements * men_positions * men_arrangements
    
    print(f"Men: {men}")
    print(f"Women: {women}")
    print(f"Women arrangements: {women_arrangements}")
    print(f"Men position choices: {men_positions}")
    print(f"Men arrangements: {men_arrangements}")
    print(f"Answer: {total_ways} ways")
    return total_ways

def run_all_problems():
    """Run all practice problems"""
    print("STANFORD CS109 - LECTURE 1: COUNTING PRACTICE PROBLEMS")
    print("=" * 60)
    
    problems = [
        problem_1,
        problem_2,
        problem_3,
        problem_4,
        problem_5,
        problem_6,
        problem_7,
        problem_8,
        problem_9,
        problem_10
    ]
    
    results = []
    for i, problem in enumerate(problems, 1):
        print(f"\n{'='*60}")
        print(f"PROBLEM {i}")
        print(f"{'='*60}")
        result = problem()
        results.append(result)
    
    print(f"\n{'='*60}")
    print("SUMMARY OF ANSWERS")
    print(f"{'='*60}")
    for i, result in enumerate(results, 1):
        print(f"Problem {i}: {result:,}")

if __name__ == "__main__":
    run_all_problems() 