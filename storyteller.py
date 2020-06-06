#Natalie Lunbeck
#This program creates a GPT2 Model and uses it to generate text

import torch
import numpy as np
from transformers import GPT2Model, GPT2Config, GPT2Tokenizer, GPT2TokenizerFast

class Storyteller:

    def __init__(self, source, num_words, prompt):
        
