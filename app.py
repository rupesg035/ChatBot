from flask import Flask, request
from twilio.rest import Client
# import os
# import openai
from markets import stockPrice
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

ACCOUNT_ID = 'AC92054e49229c48b8792a8235048ce26c'
TWILIO_TOKEN = 'f993d7ebaa811836d419391203e525ca'
TWILIO_NUMBER = 'whatsapp:+14155238886'




client = Client(ACCOUNT_ID, TWILIO_TOKEN)

# openai.api_key = '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'

# def generate_answer(question):
#     model_engine = "text-davinci-002"
#     prompt = f"Q: {question}\nA:"

#     response = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )

#     answer = response.choices[0].text.strip()
#     return answer

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

def process_msg(msg):
    incoming_que = msg.upper()
    
    if incoming_que == "HI":
        response = "Welcome to our Stock platform!!!\n *Use capital words for best experience.*\nType *LIST* for list of stock symbols."
        response+="\nType <stock_symbol> to know the last stock price. \n *eg-R:AAPL*"
        
    elif msg=="LIST" or msg=="list" or msg=="List":
        response =" Type below stock codes to get their stock price\n 1)R:AAPL \n 2)R:FB \n 3)R:GOOGL"
        response+="\nFor more details visit - \n https://marketstack.com/ "
    
        
    elif "R" in msg:
        data=msg.split(":")
        stock_symbol=data[1]
        stock_price = stockPrice(stock_symbol)
        last_price=str(stock_price["last_price"])
        response = f"The stock price of {stock_symbol} is ${last_price} ."
    else:
        response = "Welcome to our Stock platform!!!\nSend *'Hi'* to get started !!! :) "
    
    return response

@app.route("/webhook", methods=["POST"])
def webhook():
    msg = request.form['Body']
    sender = request.form['From']
    response = process_msg(msg)

    send_msg(response, sender)

    return "OK", 200

if __name__ == "__main__":
    app.run()
