import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class DidgedelikAI:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")
        self.conversation_history = []

    def generate_response(self, user_input):
        # Store the conversation history
        self.conversation_history.append(user_input)
        input_text = ' '.join(self.conversation_history)
        inputs = self.tokenizer.encode(input_text, return_tensors="pt")

        if torch.cuda.is_available():
            inputs = inputs.to('cuda')
            self.model.to('cuda')

        response = self.model.generate(inputs, max_length=150)
        bot_response = self.tokenizer.decode(response[0], skip_special_tokens=True)

        # Store the bot response
        self.conversation_history.append(bot_response)
        return bot_response

    def clear_memory(self):
        self.conversation_history = []

    def fine_tune(self, training_data):
        # Fine-tuning logic goes here
        pass

    def rug_integration(self, external_data):
        # RAG integration logic goes here
        pass

if __name__ == '__main__':
    assistant = DidgedelikAI()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = assistant.generate_response(user_input)
        print(f"Didgedelik: {response}")