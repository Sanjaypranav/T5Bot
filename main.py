import re
import pandas as pd
import numpy as np
from readtextfile import read_even_lines, read_odd_lines 
from simplet5 import SimpleT5
from sklearn.model_selection import train_test_split


conversation = pd.DataFrame(
    {
        "source_text": read_odd_lines("conversation.txt"),
        "target_text": read_even_lines("conversation.txt"),
    }
)



print(len(read_even_lines("conversation.txt")),len(read_odd_lines("conversation.txt")))

def remove_new_line(text):
    #regex function to remove \n
    return text.strip().replace('\n', '')

conversation['source_text'] = conversation["source_text"].apply(remove_new_line)
conversation['target_text'] = conversation["target_text"].apply(remove_new_line)

train_data , val_data = conversation.sample(int(conversation.shape[0]*0.80)) , conversation.sample(int(conversation.shape[0]* 0.20))
print(train_data.shape)

model = SimpleT5()
model.from_pretrained(model_type="t5", model_name="t5-base")
model.train(train_df = train_data,
            eval_df = val_data, 
            source_max_token_len=128, 
            target_max_token_len=50, 
            batch_size=8, max_epochs=3, use_gpu=True)