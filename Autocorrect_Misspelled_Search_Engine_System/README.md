```
# 🦊 ShadowFox Projects

This repository is a collection of **AI/ML projects** designed to operate at the edge of innovation, blending cutting-edge algorithms with stealth-oriented applications. 🚀

---

# 🔍 Autocorrect Misspelled Word Search Engine System
An **Autocorrect Misspelled Word Search Engine System** built using **Python** and **Streamlit**. This project uses a probabilistic approach to suggest corrections for misspelled words based on a pre-trained corpus. The system provides a user-friendly web interface where users can input a word and get suggestions for the correct spelling along with their probabilities. ✨

---

## 🌟 Features

- **🔤 Spelling Correction**: Automatically suggests corrections for misspelled words.
- **📊 Probability-Based Suggestions**: Ranks suggestions based on their occurrence probability in the corpus.
- **🛠️ Two-Level Edit Distance**: Uses both **level-one** (single edit) and **level-two** (double edit) operations to generate candidate corrections.
- **🖥️ Interactive Web Interface**: Built with **Streamlit**, providing a sleek and responsive UI.
- **🎨 Customizable Theme**: Dark theme with black background, red accents, and white text for better readability.

---

## 🛠️ How It Works

1. **📂 Corpus Loading**:
   - The system loads a text corpus (`big.txt`) and processes it to build a vocabulary and calculate word probabilities.

2. **✂️ Edit Operations**:
   - Generates candidate corrections using:
     - **Delete**: Removes one character.
     - **Swap**: Swaps two adjacent characters.
     - **Replace**: Replaces one character with another.
     - **Insert**: Inserts a new character.

3. **📈 Probability Calculation**:
   - Ranks suggestions based on their frequency in the corpus.

4. **🖱️ User Interface**:
   - Users input a word, and the system displays the top suggestions along with their probabilities.

---

## 🚀 Installation

1. **📥 Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/autocorrect-search-engine.git
   cd autocorrect-search-engine
   ```

2. **📦 Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **📂 Download the Corpus**:
   - Place the `big.txt` file in the project directory. You can use any text corpus for training.

4. **▶️ Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **🌐 Access the App**:
   - Open your browser and navigate to [http://localhost:8501](http://localhost:8501).

---

## 🕹️ Usage

1. **⌨️ Input a Word**:
   - Enter a word in the search bar and click the **Check** button.

2. **📋 View Suggestions**:
   - The system will display the top suggestions along with their probabilities.

---

## 🎨 Customization

- **Change Theme**:  
  Modify the custom CSS in the `st.markdown` section of `app.py` to change the background color, text color, or button styles.

- **Use a Different Corpus**:  
  Replace `big.txt` with your own text file to train the system on a different vocabulary.

---

---

## 🛠️ Technologies Used

- 🐍 **Python**: Core programming language.
- 🎈 **Streamlit**: For building the web interface.
- 📚 **NLTK**: For text processing (optional, if needed).
- 📊 **Collections**: For counting word frequencies.
- 🔍 **Regex**: For tokenizing the corpus.

```

