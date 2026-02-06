from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "hello world"



# from ai import get_ai_response
# print("welcome to AI chat bot")
# print("type 'quit' or 'exit' to end the conversation")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["quit", "exit"]:
#         break
#     response = get_ai_response(user_input)
#     print("AI: ", response)
if __name__ == "__main__":
    app.run(debug=True)
