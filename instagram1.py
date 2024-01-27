from instagrapi import Client
cl = Client()
cl.login('mypythonexperiments', 'BBking0123') #Logging in.
while True:
    thread_data = cl.direct_threads(1, 'unread', '', None)
    if thread_data:
        break

def Send(text):
    thread_ID = thread_data[0].id #Getting the thread ID of the last thread at the inbox.
    try:
        cl.direct_answer(thread_ID, text) #Sanding the massege.
    except:
        pass

def WaitAndGet():
    while True:
        thread_data = cl.direct_threads(1, 'unread', '', None)
        try:
            thread_ID = thread_data[0].id #Getting the thread id of the last thread at the inbox.
            last_message = thread_data[0].messages[0].text #Getting the last message from the thread.
            return last_message
            break
        except:
            thread_ID = None
            last_message = None

Send("Let's get started!")
GameArchive = []
x = True
def UserLost():
    global x
    x = False
    Send('Your score is: ' + str(len(GameArchive) - 1))
while x:
    UserAns = WaitAndGet()
    if ((len(GameArchive) + 1) % 7 == 0) or ('7' in str((len(GameArchive) + 1))):
        if UserAns == 'BOOM':
            GameArchive.append(UserAns)
        else:
            UserLost()
    else:
        if UserAns == str((len(GameArchive) + 1)):
            GameArchive.append(UserAns)
        else:
            UserLost()

    if ((len(GameArchive) + 1) % 7 == 0) or ('7' in str((len(GameArchive) + 1))):
        Send('BOOM')
        GameArchive.append('BOOM')
    else:
        Send(str(len(GameArchive) + 1))
        GameArchive.append(len(GameArchive) + 1)
    cl.login('mypythonexperiments', 'BBking0123')  # Logging in stay in the conacting.