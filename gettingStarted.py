### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.
import hashlib

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    email = "mw6140@nyu.edu"
    email_hash = hashlib.sha256(email.encode("utf-8")).hexdigest()
    
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = email_hash
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return answer
    
# Complete all the questions.

if __name__ == "__main__":
#use this space to debug and verify that the program works
#Questions:
    q1 = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    q2 = "Are encoding and encryption the same? - Yes/No"
    q3 = "Is it possible to decrypt a message without a key? - Yes/No"
    q4 = "Is it possible to decode a message without a key? - Yes/No"
    q5 = "Is a hashed message supposed to be un-hashed? - Yes/No"
    q6 = "What is the SHA256 hashing value of your NYU email and use the answer in your code - "
    q7 = "Is MD5 a secured hashing algorithm? - Yes/No"
    q8 = "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
    q9 = "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"

    print(welcome_assignment_answers(q1))
    print(welcome_assignment_answers(q2))
    print(welcome_assignment_answers(q3))
    print(welcome_assignment_answers(q4))
    print(welcome_assignment_answers(q5))
    print(welcome_assignment_answers(q6))
    print(welcome_assignment_answers(q7))
    print(welcome_assignment_answers(q8))
    print(welcome_assignment_answers(q9))

