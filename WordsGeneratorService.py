import markovify
import random

class WordsGenerator:

    def __init__(self):
        self.ReadFile();

    def ReadFile(self):
        self.brain = open("words/text.txt", encoding='utf-8');
        words = self.brain.read();
        self.words_template = markovify.Text(words);

    def GenerateText(self):

        words_length = random.randrange(150, 225, 1);
        return self.words_template.make_short_sentence(words_length);



