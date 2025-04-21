
import argparse

from num2words import num2words
from typing import Union
from decimal import Decimal

def number_to_words(number: Union[int, float, Decimal], language: str = 'pt_BR') -> str:
    """
    Converts a number to its word representation.
    
    Args:
        number: Number to be converted
        language: Language code ('pt_BR' for Portuguese or 'en' for English)
    
    Returns:
        str: Number in words in the specified language
    
    Raises:
        ValueError: If language is not supported
        TypeError: If number is not a numeric type
        
    Examples:
        >>> number_to_words(42)
        'quarenta e dois'
        >>> number_to_words(42, 'en')
        'forty-two'
    """
    if not isinstance(number, (int, float, Decimal)):
        raise TypeError("Parameter 'number' must be a numeric value.")
        
    supported_languages = ['pt_BR', 'en']
    if language not in supported_languages:
        raise ValueError(f"Unsupported language. Use {supported_languages}.")
    try:
        return num2words(number, lang=language, to='cardinal')
    except Exception as e:
        raise ValueError(f"Error converting number: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert number to words (imperative mode).")
    parser.add_argument("--number", type=float, help="Number to be converted (ex: 9999999.99)")
    parser.add_argument("--language", type=str, default="pt_BR",
                        choices=["pt_BR", "en"], 
                        help="Conversion language (pt_BR or en).")

    args = parser.parse_args()
    result = number_to_words(args.number, args.language)
    print(result)