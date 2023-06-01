import openai
openai.api_key  = input('Enter OpenAI key here: ')

#The function to generate a response by VhatGPT
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=.7, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

#Taking the review from user
def get_review():
  review = input ('Enter desired review: ')
  return review


#Telling the model what we expect as output
def extract_opinion(review):
    length = len(review)
    prompt = f"""
    You are working for a hotel and you've just received a customer review.\
   The review mentions the cleanliness of the hotel and the behavior of the \
   staff. Identify whether the review is concerning \
   about the cleanliness and staff behavior. If it is, \
   please provide the customer's opinion on the cleanliness and staff behavior.\
   Start the response with: "The review has {length} word."
   Format the response as follows:\
   Cleanliness: (summarized opinion of the customer about cleanliness; each item in a separated line)\
   Staff: (summarized opinion of the customer about staff behaviour; each item in a separated line)\
   Food & Restaurant: (summarized opinion of the customer about Food & Restaurant; each item in a separated line)\


   At last, wirte a 5 sentence reply (each sentence in a single line) to be sent to customer as email, \
   containing admiring him and making sure that his review will be considered well. \
   Putting each sentence in a single line is ery important to make the email being readable easily.

   Review text: '''{review}'''
   """
    response = get_completion(prompt)
    print(response)