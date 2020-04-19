# Accept input for the number of questions and save it to a variable "n"

n = int (input ("Number of questions and answers you want to display: "))

#Open the files which contains the Questions and answers
# Store the values into variables "q" for questions and "a" for answers
# c represents the combined Questions and answers

q = open ('c:/Users/User/Desktop/Hackathon/GeographyTestQuestions.txt','r')
a = open ('c:/Users/User/Desktop/Hackathon/GeographyTestAnswers.txt','r')
c = open ('c:/Users/User/Desktop/Hackathon/GeographyCombinedAnswers.txt','w')

# Loop through the questions and answers and 
# Write answers to the Combined Folder
for x in range (n):
    question = q.readline()
    c.write(question)
    answer = a.readline()
    c.write (answer)
#    Print Question and Answer to verify progress
    print (question, answer)
    
print ("Thank You")   