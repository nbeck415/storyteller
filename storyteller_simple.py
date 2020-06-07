#Natalie Lunbeck
#This program creates a simple GPT2 Model and uses it to generate text

import torch
#import numpy as np
import gpt_2_simple as gpt2

class StorytellerSimple:

    def __init__(self, source, num_words, prompt="DEFAULT"):
        #where the training data is stored
        self.source = source
        #length of output
        self.num_words = num_words
        #topic (?)
        self.prompt = prompt
        #first-time runthrough
        self.setupModel()
        #print('setup complete')
        self.session = gpt2.start_tf_sess()
        #story generator, give parameters if necessary
        self.runGenerator()
        print('training complete')
        self.loadRun()
        print('done')


    def setupModel(self, size="124M"):
        #create a gpt2 model based on dataset
        #first time runthrough, do not run twice
        gpt2.download_gpt2(model_name=size)

    def runGenerator(self, num_words=200, variance=0.9):
        session = self.session #gpt2.start_tf_sess()
        print('here')
        #gpt2.load_gpt2(session)
        print('there')
        gpt2.finetune(session, dataset=self.source, model_name='124M', steps=50, restore_from='fresh',run_name='run1',sample_every=200,save_every=500, print_every=10)
        sentence = self.prompt
        default_sentence = "The quick brown fox jumped over the lazy dog"
        if sentence == "DEFAULT":
            sentence = default_sentence
        result = gpt2.generate(session, length=num_words, temperature=variance, top_k=1, top_p=0.9,
              run_name='run1', prefix=sentence, return_as_list=True)

    def loadRun(self):
        session = gpt2.start_tf_sess()
        gpt2.load_gpt2(session)#, run_name='run1')
        gpt2.generate_to_file(session, destination_path='generated5.txt', length=self.num_words, temperature=0.9, prefix=self.prompt)


def main():
    story = StorytellerSimple('reddit_comments.txt', 200, "beautiful rain sad saturday")

if __name__ == "__main__":
    main()
