#Natalie Lunbeck
#This program creates a GPT2 Model and uses it to generate text

import torch
import numpy as np
from transformers import GPT2Model, GPT2Config, GPT2Tokenizer, GPT2TokenizerFast

class Storyteller:

    def __init__(self, source, num_words, prompt="DEFAULT"):
        #where the training data is stored
        self.source = source
        #length of output
        self.num_words = num_words
        #topic (?)
        self.prompt = prompt
        #make the GPT2 model with given configuration
        self.model_config = GPT2Model(self.makeConfig)

    def makeConfig():
        #configuration object with modifiable parameters
        vocab_size = 10000
        config = GPT2Config(vocab_size=vocab_size)
        return config

        
