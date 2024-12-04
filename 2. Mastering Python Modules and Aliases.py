
 # text_utils.py

def reverse_string(s):
        """function to reverse a string."""
        return s[::-1]

def capitalize_string(s):
        """function to capitalize a string."""
        return s.capitalize()

# main.py
        print("Script started")
        import text_utils as tu 
# Import text_utils using an alias and utilize its functions

        #if __name__ == "__main__":
        original_text = "Hello world"
        reversed_text = tu.reverse_string(original_text)
        capitalized_text = tu.capitalize_string(original_text)

        print("Original:", original_text)
        print("Reversed:", reversed_text)
        prin("Capitalized:", capitalize_text)