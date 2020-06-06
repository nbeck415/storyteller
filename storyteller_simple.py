#Natalie Lunbeck
#This program creates a simple GPT2 Model and uses it to generate text

import torch
import numpy as np
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
        setupModel()
        self.session = gpt2.start_tf_sess()
        #story generator, give parameters if necessary
        runGenerator()
        loadRun()


    def setupModel(size="124M"):
        #create a gpt2 model based on dataset
        #first time runthrough, do not run twice
        gpt2.download_gpt2(model_name=size)

    def runGenerator(num_words=self.num_words, variance=0.9):
        session = self.session
        gpt2.load_gpt2(session)
        gpt2.finetune(session, dataset=self.source, model_name='124M')
        sentence = self.prompt
        default_sentence = "The quick brown fox jumped over the lazy dog"
        if sentence == "DEFAULT":
            sentence = default_sentence
        gpt2.generate(session, length=num_words, temperature=variance, top_k=1, top_p=0.9,
              run_name='run1', prefix=sentence, return_as_list=True)

    def loadRun():
        gpt2.load_gpt2(self.session, run_name='run1')
        gpt2.generate_to_file(self.session, filepath='generated.txt', length=self.num_words, temperature=0.9, prefix=self.prompt)
