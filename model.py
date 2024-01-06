from textblob import TextBlob
from language_tool_python import LanguageTool

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageTool('en-US')  # Specify the language (e.g., 'en-US')

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)

        corrected_text = " ".join(corrected_words)
        matches = self.grammar_check.check(corrected_text)

        if matches:
            # Extract corrected text from matches
            corrected_text = self.grammar_check.correct(text)

        return corrected_text
    
    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)

        found_mistakes = []
        for error in matches:
            found_mistakes.append(error.ruleIssueType)

        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count

        

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello worlds you am did working mashine larnuing"
    print(obj.correct_spell(message))
    corrected_text = obj.correct_spell(message)
    x=[corrected_text]
    print(obj.correct_grammar(x))
    mistakes, mistakes_count = obj.correct_grammar(x)
    print(f"Found Mistakes: {mistakes}")
    print(f"Number of Mistakes: {mistakes_count}")

