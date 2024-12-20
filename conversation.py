import swarmnode

# Initialize the API key and agents
swarmnode.api_key = "API_KEY"
interrogatorAgent = swarmnode.Agent.retrieve(id="AGENT_ID")
suspectAgent = swarmnode.Agent.retrieve(id="AGENT_ID")

# Initialize the payload
payload = {"text": "Interrogator: What is your name?\n"}

# Number of exchanges between the agents
num_exchanges = 10

# Loop between the agents
for i in range(num_exchanges):
    if i % 2 == 0:  # Even iterations: suspectAgent responds
        execution = suspectAgent.execute(wait=True, payload=payload)
        print(f"SuspectAgent: {execution.return_value}")
        payload["text"] += f"SuspectAgent: {execution.return_value}\n"
    else:  # Odd iterations: interrogatorAgent responds
        execution = interrogatorAgent.execute(wait=True, payload=payload)
        print(f"InterrogatorAgent: {execution.return_value}")
        payload["text"] += f"InterrogatorAgent: {execution.return_value}\n"

# Final conversation output
print("Final Conversation:")
print(payload["text"])
