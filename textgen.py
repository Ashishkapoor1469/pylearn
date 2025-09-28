from transformers import GPT2LMHeadModel, GPT2Tokenizer
import re
# 1. Load pre-trained model & tokenizer
model_name = "gpt2"   # you can use "gpt2-medium", "gpt2-large", or others
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# 2. Encode input text
input_text = "Once upon a time"
inputs = tokenizer.encode(input_text, return_tensors="pt")

# 3. Generate text
outputs = model.generate(
    inputs,
    max_length=15,        # total tokens (input + generated)
    num_return_sequences=1, # number of outputs
    temperature=0.7,        # creativity (higher = more random)
    top_p=0.9,              # nucleus sampling
    do_sample=True          # enable sampling
)

# 4. Decode & print
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
