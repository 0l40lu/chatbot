import streamlit as st
import difflib


def chat(talk):
    phrase = ['hi', 'hello', 'hey', 'yo', "no", 'how many people died', 'who died', 'who dies', 'who died?',
              'who dies?', "How many people were killed in the September 11 attacks?", 'who died on september 11',
              "How many people were killed in 911?", 'who died on 9 11', 'who died on 911', 'who died on 9/11',
              "How many people were killed in 911", 'who died on 9 11?', 'who died on 911?', 'who died on 9/11?',
              "what is 9/11", "what is 911", "what is 911", "what happened on the 11th of september", "what is 9/11?",
              "what happened on september 11", "what happen", "what happened", "what happened?", "what happened on 9/11"
              , "what is that", "what is that?", "who planned the September 11 attacks?", 'Who attacked America',
              "what did the government do", "how did the government respond", "which building was destroyed",
              "what year did it happen", "which year did it occur", "when did it happen"]

    close = difflib.get_close_matches(talk.lower(), phrase, n=1, cutoff=0.5)

    if close:
        close_match = close[0]
        if close_match in ['hi', 'hello', 'hey', 'yo']:
            return "Hello, do you want to know about 9/11?"
        elif close_match in ["no"]:
            return "Would you like to know?"
        elif close_match in ['yes']:
            return ("9/11 refers to the events that took place in the United States on "
                    "September 11, 2001, when terrorists attacked the World Trade Center in New York and the"
                    " Pentagon. On that morning, 19 terrorists hijacked four commercial airliners, intentionally "
                    "crashing two planes into the Twin Towers of the World Trade Center, causing massive damage and "
                    "loss of life. Another plane was crashed into the Pentagon in Arlington, Virginia, and the fourth"
                    "plane, believed to be heading for the White House or the U.S. Capitol, crashed in a field in "
                    "Pennsylvania after passengers attempted to overcome the hijackers.")

        elif close_match in ['how many people died', 'who died', 'who dies', 'who died?', 'who dies?',
                              "How many people were killed in the September 11 attacks?", 'who died on september 11',
                              "How many people were killed in 911?", 'who died on 9 11', 'who died on 911',
                              'who died on 9/11', "How many people were killed in 911", 'who died on 9 11?',
                              'who died on 911?', 'who died on 9/11?']:
            return "Over 3000 people died during that event"

        elif close_match in ["what is 9/11", "what is 911", "what is 911", "what happened on the 11th of september",
                              "what happened on september 11", "what is 9/11?", "what is that?",
                              "what happened", "what happened?", "what happened on 9/11", "what is that",
                              "what happen"]:
            return ("On September 11, 2001, 19 militants associated with the Islamic extremist group al Qaeda hijacked "
                    "four commercial airplanes and carried out suicide attacks against targets in the United States."
                    " The attacks resulted in the deaths of over 3,000 people.")

        elif close_match in ["who planned the September 11 attacks?", 'Who attacked America']:
            return ("Osama bin Laden was relatively unknown in the United States before 9/11, even as he was amassing"
                    " popularity, followers, and fame in the Middle East during the 1990s. In 1988, he was one of the"
                    " founders of al Qaeda, a militant Islamic terrorist organization that organized and carried out "
                    "the 9/11 attacks.")

        elif close_match in ["how did the government respond", "what did the government do"]:
            return ("After the September 11, 2001 attacks, the United States government responded by commencing  "
                    "immediate rescue operations at the World Trade Center site, grounding civilian aircraft, and "
                    "beginning a long-term response that included official investigations, legislative changes, "
                    "military action, and restoration projects.")

        elif close_match in ["which building was destroyed", "what was destroyed"]:
            return "The twin towers were destroyed during that event"

        elif close_match  in ["what year did it happen", "which year did it occur", "when did it happen"]:
            return "It happened on 2001"

        else:
            return "Can you rephrase the question."


st.title('9/11 Bot')
st.image('9 11.jpeg', width=400)
st.subheader('Ask questions on 9/11')
v = st.text_input('You')
if v:
    response = chat(v)
    st.write(f'Chatbot: {response}')
