import openai
from tkinter import *
from tkinter import messagebox
import os
import headers
import colorswatch as cs

openai.api_key = None
opsys = ['nt', 'posix', 'mac']
lang = ["English", "日本語"]
isEnglish = True
# currentOS = os.name()

BG = cs.chatGPT["tk"]
APPSIZE = "240x400"

root = Tk()
root.geometry(APPSIZE)
root.title("ChatGPT PDA")
root.resizable(width=False, height=False)
BGPATH = os.path.join("images", "backimage.png")
BGIMAGE = PhotoImage(file=BGPATH)
BACKIMAGE = Label(root, image=BGIMAGE).place(x=0, y=0, anchor=NW)

chatEntry = Entry(root, width = 24)
chatEntry.place(x=20, y=294, anchor=NW)
# chatEntry.config(state="disabled")

englishButton = Radiobutton(root, text="English", bg=cs.chatGPT["tk"])
japaneseButton = Radiobutton(root, text="日本語", bg=cs.chatGPT["tk"])
englishButton.place(x=16, y=350, anchor=NW)
japaneseButton.place(x=116, y=350, anchor=NW)

def ask_gpt_35(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer

def personal_assistant():
    print("Hello. I am your personal assistant powered by GPT-3.5. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Assistant: Goodbye! Have a great day!")
            break

        prompt = f"My user asked: {user_input}\nAnswer:"
        response = ask_gpt_35(prompt)
        print(f"Assistant: {response}")

root.mainloop()

# if __name__ == "__main__":
#     personal_assistant()