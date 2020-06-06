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
        setupModel()


    def setupModel(size="124M"):
        #create a gpt2 model based on dataset
        #first time runthrough, do not run twice
        gpt2.download_gpt2(model_name=size)

    def runGenerator(num_words=self.num_words, variance=0.9):
        session = gpt2.start_tf_sess()
        gpt2.load_gpt2(session)
        
