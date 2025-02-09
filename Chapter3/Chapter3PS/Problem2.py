#write a program to fill in a letter template given below with name and date...

letter = """ 
        Dear <|name|>,
        You are Selected !
        <|Date|>
        """

print(letter.replace("<|name|>", "ROHIT").replace("<|Date|>", "10 Jully 2024"))