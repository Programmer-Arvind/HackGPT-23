import re
import openai

# Using api key saved in the text file
openai.api_key_path = "./hackGPT_api_key.txt"

def gpt_get(destination, start):
    # Getting output from gpt-3.5-turbo model
    message = [{"role" : "user", "content" : f"""I want to travel to {destination} from {start}.
                Give me 6 common phrases used there in day to day life, which is the best travel medium ,
                the tourist places, famous food items in eighty words. Give it in bullets for everything. 
                Give me a python list named food with the food items (enclosed by single quote) mentioned above (dont do anything with it)"""} ]
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message
    )
    
    reply =  completion.choices[0].message.content
    print(reply) # Printing reply just to know what is received
    # Using re module to use the python list generated by gpt api
    pattern = "food = \[(.+)\]"
    foods_as_str = re.findall(pattern, reply)[0]
    # Foods as str is like 'Vada pav', 'Pav Bhaji' so, split at ", " and strip the "'"
    food = [i.strip("'") for i in foods_as_str.split(", ")]
    return food
