import string
import re
from collections import Counter
import streamlit as st

# Custom CSS for black background and red text
st.markdown(
    """
    <style>
    /* Set background color to black */
    .stApp {
        background-color: #000000;  /* Black background */
    }

    /* Change title color to red */
    h1 {
        color: #ff0000;  /* Red color */
    }

    /* Change text input label color to red */
    .stTextInput label {
        color: #ff0000 !important;  /* Red color */
    }

    /* Ensure other text is visible on black background */
    .stMarkdown, .stWrite, .stButton>button {
        color: #ffffff !important;  /* White text */
    }

    /* Add red border to the search bar */
    .stTextInput>div>div>input {
        border: 2px solid #ff0000;  /* Red border */
        border-radius: 5px;         /* Rounded corners */
        background-color: #333333;  /* Dark gray background for input */
        color: #ffffff;             /* White text inside input */
    }

    /* Change button color */
    .stButton>button {
        background-color: #ff0000;  /* Red button background */
        color: #ffffff;             /* White text on button */
        border-radius: 5px;         /* Rounded corners */
        border: none;               /* Remove default border */
    }

    /* Change hover effect for button */
    .stButton>button:hover {
        background-color: #cc0000;  /* Darker red on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def read_corpus(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            words = []
            for line in lines:
                words += re.findall(r'\w+', line.lower())
            return words
    except FileNotFoundError:
        st.error(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return []

corpus = read_corpus('big.txt')
if not corpus:
    st.error("Corpus is empty. Check the input file.")
    st.stop()

vocab = set(corpus)
words_count = Counter(corpus)
N = sum(words_count.values())
words_prob = {word: count / N for word, count in words_count.items()}

def split(word):
    return [(word[:i], word[i:]) for i in range(len(word) + 1)]

def delete(word):
    return [left + right[1:] for left, right in split(word) if right]

def swap(word):
    return [left + right[1] + right[0] + right[2:] for left, right in split(word) if len(right) > 1]

def replace(word):
    return [left + center + right[1:] for left, right in split(word) if right for center in string.ascii_lowercase]

def insert(word):
    return [left + center + right for left, right in split(word) for center in string.ascii_lowercase]

def level_one_edits(word):
    return set(delete(word) + swap(word) + replace(word) + insert(word))

def level_two_edits(word):
    return set(e2 for e1 in level_one_edits(word) for e2 in level_one_edits(e1))

def correct_spelling(word, vocab, words_prob):
    if word in vocab:
        return f"{word} is already correctly spelled."
    
    suggestions = level_one_edits(word)
    best_guess = [w for w in suggestions if w in vocab]
    
    if not best_guess:
        suggestions = level_two_edits(word)
        best_guess = [w for w in suggestions if w in vocab]
    
    if not best_guess:
        return f"No suggestions found for {word}."
    
    suggestions_with_prob = [(w, words_prob.get(w, 0)) for w in best_guess]
    suggestions_with_prob.sort(key=lambda x: x[1], reverse=True)
    top_suggestions = [f"{w} ({prob:.2%})" for w, prob in suggestions_with_prob[:10]]
    return f"Suggestions for {word}: " + ", ".join(top_suggestions)

# App title and input
st.title("Autocorrect Misspelled Word Search Engine System")
word = st.text_input('Search Here')

if st.button('Check'):
    result = correct_spelling(word, vocab, words_prob)
    st.write(result)