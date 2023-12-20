import openai 
import os


API_KEY=open("API_KEY", "r").read()

openai.api_key=API_KEY

respond = openai.ChatCompletion.create(

    model="gpt-3.5-turbo",

    messages=[

        {"role": "user", "content": "What is the different between Celsius and Fahrenheit?"}


    ]
)
print(respond)
