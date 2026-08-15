import anthropic

client = anthropic.Anthropic()

message = client.messages.create(

    model = "claude-opus-5",
    max_tokens=1000,
    messages=[{
        "role" : "user",
        "content" : "Hey Claude! How are you today man??",
    }],
)
    
for block in message.content:
        if block.type=="text":
            print(block.text)
    
