"""Put this code in the Suspect Agent code in the swarmnode dashboard"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

def main(request):
    """You are a suspect in a gas station robbery, you have a police interrogator infront of you in the interrogation room. Your goal is to come up with a good alibi of why you were seen walking away from the gas station without getting caught for the crime."""

    text = request.payload["text"]

    model = ChatOpenAI(model="gpt-4o-mini")
    messages = [
        SystemMessage(f"You are a suspect in a gas station robbery, you have a police interrogator infront of you in the interrogation room. Your goal is to come up with a good alibi of why you were seen walking away from the gas station without getting caught for the crime. You are Suspect and the interrogator is Interrogator. Respond with what you want to say and nothing else each time, do not include \"Suspect:\""),
        HumanMessage(text),
    ]
    response = model.invoke(messages)
    return response.content

"""Put this code in the Interrogator Agent code in the swarmnode dashboard"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

def main(request):
    """You are a police interrogator, you have a suspect infront of you in the interrogation room. Your job is to try and find out if he committed the crime."""

    text = request.payload["text"]

    model = ChatOpenAI(model="gpt-4o-mini")
    messages = [
        SystemMessage(f"You are a police interrogator, you have a suspect infront of you in the interrogation room. Your job is to try and find out if he committed the crime. You are Interrogator and the suspect is Suspect. Respond with what you want to say and nothing else each time, do not include \"Interrogator:\""),
        HumanMessage(text),
    ]
    response = model.invoke(messages)
    return response.content