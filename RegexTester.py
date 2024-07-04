import time
import re

def evaluate_regex_performance(symbol, text, pattern_template):
    """
    Evaluates the performance of a regex pattern with a given symbol in various positions.
    
    :param symbol: The symbol to be evaluated.
    :param text: The input text on which regex will be evaluated.
    :param pattern_template: The regex pattern template with a placeholder for the symbol.
    :return: A list of tuples containing position and performance rating.
    """
    performance_ratings = []
    
    # Iterate through each position in the text
    for position in range(len(text) + 1):
        # Insert the symbol at the current position
        pattern = pattern_template.format(symbol * position)
        
        # Measure the time taken to perform the regex match
        start_time = time.perf_counter()
        re.match(pattern, text)
        end_time = time.perf_counter()
        
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        
        # Assign a performance rating based on the elapsed time
        performance_rating = elapsed_time
        
        performance_ratings.append((position, performance_rating))
    
    return performance_ratings

def main():
    symbol = r"([\s\S]*?)"  # Symbol to be evaluated
    text = "your long input text goes here"  # The text on which regex will be tested
    pattern_template = r"{}your_regex_pattern_here"
    
    performance_ratings = evaluate_regex_performance(symbol, text, pattern_template)
    
    # Print performance ratings
    print(f"Position\tPerformance Rating (in seconds)")
    for position, rating in performance_ratings:
        print(f"{position}\t{rating:.6f}")

if __name__ == "__main__":
    main()
