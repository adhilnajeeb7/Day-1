from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, sentences_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    summary_text = " ".join(str(sentence) for sentence in summary)
    return summary_text

def get_user_input():
    print("Enter the text you want to summarize:")
    user_input = input()
    return user_input

# Example usage
user_text = get_user_input()
summary = summarize_text(user_text)
print("Summary:")
print(summary)

