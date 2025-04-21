import argparse

from num2words import num2words
from typing import Union
from decimal import Decimal

class NumberToWords:
    """
    Class to convert numbers to their word representation, supporting multiple languages.
    """
    SUPPORTED_LANGUAGES = {
        'pt_BR': 'pt_BR',  # Brazilian
        'en': 'en'      # English
    }

    def __init__(self, number: Union[int, float, Decimal], language: str = 'pt_BR'):
        """
        Initialize the converter with a number and language.

        Args:
            number: Number to be converted
            language: Language code ('pt_BR' for Brazilian or 'en' for English)
        
        Raises:
            ValueError: If language is not supported
            TypeError: If number is not a numeric type
        """
        self._validate_number(number)
        self._validate_language(language)
        
        self.number = number
        self.language = language

    def _validate_number(self, number: Union[int, float, Decimal]) -> None:
        """Validate if the input is a numeric value."""
        if not isinstance(number, (int, float, Decimal)):
            raise TypeError("Number must be a numeric value")

    def _validate_language(self, language: str) -> None:
        """Validate if the language is supported."""
        if language not in self.SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language. Use {list(self.SUPPORTED_LANGUAGES.keys())}")

    def convert(self) -> str:
        """
        Convert the stored number to words.
        
        Returns:
            str: Number in words in the specified language
            
        Examples:
            >>> converter = NumberToWords(42)
            >>> converter.convert()
            'quarenta e dois'
            
            >>> converter = NumberToWords(42, 'en')
            >>> converter.convert()
            'forty-two'
        """
        try:
            return num2words(
                self.number,
                lang=self.SUPPORTED_LANGUAGES[self.language],
                to='cardinal'
            )
        except Exception as e:
            raise ValueError(f"Error converting number: {str(e)}")

    @classmethod
    def get_supported_languages(cls) -> list:
        """Get list of supported language codes."""
        return list(cls.SUPPORTED_LANGUAGES.keys())

def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for CLI."""
    parser = argparse.ArgumentParser(
        description="Convert numbers to words in different languages (OO version)"
    )
    parser.add_argument(
        "--number",
        type=float,
        required=True,
        help="Number to be converted (e.g., 1234.56)"
    )
    parser.add_argument(
        "--language",
        type=str,
        default="pt",
        choices=NumberToWords.get_supported_languages(),
        help="Language for conversion (default: pt)"
    )
    return parser

def main():
    """CLI entry point for the number converter."""
    parser = create_parser()
    args = parser.parse_args()

    try:
        converter = NumberToWords(args.number, args.language)
        result = converter.convert()
        print(f"Result: {result}")
    except (ValueError, TypeError) as e:
        print(f"Error: {str(e)}")
        return 1
    return 0

if __name__ == '__main__':
    exit(main())
