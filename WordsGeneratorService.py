import markovify
import random

class WordsGenerator:



    def ReadFile(self, textConfig):
        self.brain = open(textConfig[0], encoding='utf-8');
        words = self.brain.read();

        self.words_template = markovify.Text(words, state_size=textConfig[1]);

    def GenerateText(self, textConfig):
        self.ReadFile(textConfig);
        words_length = random.randrange(150, 225, 1);

        return self.words_template.make_short_sentence(words_length);



