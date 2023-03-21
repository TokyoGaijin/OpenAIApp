import openai
from tkinter import *
from tkinter import messagebox
import os
import colorswatch as cs



BG = cs.chatGPT["tk"]
APPSIZE = "240x400"

root = Tk()
root.geometry(APPSIZE)
root.title("ChatGPT PDA")
root.resizable(width=False, height=False)
BGPATH = os.path.join("images", "backimage.png")
BGIMAGE = PhotoImage(file=BGPATH)
BACKIMAGE = Label(root, image=BGIMAGE).place(x=0, y=0, anchor=NW)

chatEntry = Entry(root, width = 23)
chatEntry.place(x=20, y=294, anchor=NW)


apiEntry = Entry(root, width = 33, show="*")
apiEntry.place(x=20, y=350, anchor=NW)
keyLabel = Label(root, text="API Key / キー", bg=BG).place(x=20, y=328, anchor=NW)

chatBox = Text(root, width=33, height=17, wrap=WORD, font=("Helvetica", 8))
chatBox.place(x=21, y=38, anchor=NW)



def kill_me():
    root.destroy()

exitButton = Button(root, text="Exit / 終了", command=kill_me)
exitButton.place(x=164, y=373, anchor=NW)

def ask_gpt_35(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"User Prompt: {prompt}\n Answer:",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer


def enter_text(sendText):
    global chatBox
    chatBox.config(state="normal")
    sendText = sendText.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
    chatBox.insert(END, f"{sendText}\n")
    chatBox.config(state="disabled")



def send_button():
    global chatEntry, apiEntry
    openai.api_key = apiEntry.get()
    inquiry = chatEntry.get()
    chatEntry.delete(0, END)
    if inquiry == "help".lower():
        messagebox.showinfo("Info", "Enter your API Key\nEnter your inquiry\nPress 'Send' to chat.")
    elif inquiry == "quit".lower() or inquiry == "exit".lower():
        enter_text("Have a great day! Goodbye!")
        root.destroy()
    elif inquiry == "さよなら":
        enter_text("ご利用いただきありがとうございました。")
        root.destroy()
    else:
        try:
            enter_text(f"Assistant: {ask_gpt_35(inquiry)}")
        except openai.error.AuthenticationError:
            messagebox.showerror("No API Key", "You did not specify a valid API Key.")



sendButton = Button(root, command=send_button, text="Send/送信")
sendButton.place(x=165, y=292, anchor=NW)



def run():
    enter_text("Welcome.")
    enter_text("Enter your API Key,")
    enter_text("Enter your inquiry,")
    enter_text("Click SEND to chat.")
    enter_text("How can I help you?")


    root.mainloop()


if __name__ == "__main__":
    run()