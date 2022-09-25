from tkinter import*
root= Tk()
root.geometry("600x600")
root.configure(background= "lime")
root.title("Detecting Cardiovascular Symptoms")

question1_RadioButton=StringVar(value= "0")

Question1= Label(root, text= "Do you experience any shortness of breath while doing routine activities?")
Question1.pack()
Question_radio1= Radiobutton(root, text="yes", variable= question1_RadioButton, value= "yes")
Question_radio1.pack()
Question_radio2= Radiobutton(root, text="no", variable= question1_RadioButton, value= "no")
Question_radio2.pack()

question2_radioButton=StringVar(value= "0")

Question2= Label(root, text= "Do you have swelling in the feet/ankles/legs (shoes feel tighter) or abdomen?")
Question2.pack()
Question2_radio1= Radiobutton(root, text="yes", variable= question2_radioButton, value= "yes")
Question2_radio1.pack()
Question2_radio2= Radiobutton(root, text="no", variable= question2_radioButton, value= "no")
Question2_radio2.pack()

question3_radioButton=StringVar(value= "0")

Question3= Label(root, text= "Do you feel any of these symptoms- confusion, disorientation, or loss of memory?")
Question3.pack()
Question3_radio1= Radiobutton(root, text="yes", variable= question3_radioButton, value= "yes")
Question3_radio1.pack()
Question3_radio2= Radiobutton(root, text="no", variable= question3_radioButton, value= "no")
Question3_radio2.pack()

question4_radioButton=StringVar(value= "0")

Question4= Label(root, text= "Do you experience any shortness of breath while resting/lying down?")
Question4.pack()
Question4_radio1= Radiobutton(root, text="yes", variable= question4_radioButton, value= "yes")
Question4_radio1.pack()
Question4_radio2= Radiobutton(root, text="no", variable= question4_radioButton, value= "no")
Question4_radio2.pack()

question5_radioButton=StringVar(value= "0")

Question5= Label(root, text= "Do you experience persistsnt wheezing / coughing that produces white or pink blood tinged mucus?")
Question5.pack()
Question5_radio1= Radiobutton(root, text="yes", variable= question5_radioButton, value= "yes")
Question5_radio1.pack()
Question5_radio2= Radiobutton(root, text="no", variable= question5_radioButton, value= "no")
Question5_radio2.pack()

def fever_score():
    score=0
    
    if question1_RadioButton.get()=="yes":
        score= score+20
        print(score)
        
    if question2_radioButton.get()=="yes":
            score= score+20
            print(score)
            
    if question3_radioButton.get()=="yes":
                score= score+20
                print(score)
                
    if question4_radioButton.get()=="yes":
                score= score+20
                print(score)
                
    if question5_radioButton.get()=="yes":
                score= score+20
                print(score)
                
    if score <= 20:
        messagebox.showinfo("Report","You dont need to call a doctor.")
        
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report","You might perhaps need to call a doctor.")   
      
    else:
        messagebox.showinfo("Report","I strongly advice you to go to the doctor.")
        
btn= Button(root, text="Click Me", command= fever_score)
btn.pack()
root.mainloop()
    




