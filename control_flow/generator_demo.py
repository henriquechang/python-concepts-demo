class GeneratorDemo:

    def __init__(self, sentence):
        self.sentence = sentence

    def __iter__(self):
        for word in self.sentence:
            yield word
        return
