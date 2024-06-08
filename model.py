from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Define the path to the saved model
save_directory = "./saved_model"

# Load the tokenizer and model from the saved directory
tokenizer = AutoTokenizer.from_pretrained(save_directory)
model = AutoModelForCausalLM.from_pretrained(save_directory)

# Create the text generation pipeline
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def generate_text(input_text):
    if not input_text:
        return {'error': 'No input text provided'}

    # Generate a response
    response = generator(input_text, max_length=50)
    generated_text = response[0]['generated_text']
    
    return {'generated_text': generated_text}