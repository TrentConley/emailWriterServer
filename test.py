import openai
import json

openai.api_key = ""

# prompt = """Generate email that follows these properties: To Ken from Trent subject money for real estate property 
#             Tone: trying to convince to give money. Body: found house outside of Atlanta for 200k, PE ratio is 3, 
#             very good value property. Need Ken to cover downpayment for 8% interest."""

def generate_response(prompt):
    # Set the model and prompt
    model = "text-davinci-002"
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    
    # Get the generated response
    response_text = response["choices"][0]["text"]
    return response_text

def lambda_handler(event, context):
    # TODO implement
    prompt = event['key1']
    response = generate_response(prompt)
    return {
        'statusCode': 200,
        'body': json.dumps('hello')
    }
