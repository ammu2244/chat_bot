import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "gpt-4o-mini"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def chat():
    """Interactive chatbot that maintains conversation history."""
    print("\n" + "="*50)
    print("🤖 Interactive Chatbot")
    print("="*50)
    print("Type your message and press Enter to chat.")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("="*50 + "\n")
    
    # Initialize conversation history with system message
    messages = [SystemMessage("You are a helpful assistant.")]
    
    while True:
        # Get user input
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye! 👋")
            break
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
            print("\nGoodbye! 👋")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        # Add user message to history
        messages.append(UserMessage(user_input))
        
        try:
            # Get response from the model
            response = client.complete(
                messages=messages,
                temperature=1.0,
                top_p=1.0,
                max_tokens=1000,
                model=model
            )
            
            # Extract assistant's reply
            assistant_reply = response.choices[0].message.content
            
            # Add assistant's reply to history for context
            from azure.ai.inference.models import AssistantMessage
            messages.append(AssistantMessage(assistant_reply))
            
            # Display the response
            print(f"\nBot: {assistant_reply}\n")
            
        except Exception as e:
            print(f"\n❌ Error: {e}\n")
            # Remove the failed user message from history
            messages.pop()

if __name__ == "__main__":
    chat()

