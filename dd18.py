#!/usr/bin/python3

class Login(tk.Frame):
    login_tries = 0
    global DEFAULT
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        #create login frame stuff
        self.lbl_username = tk.Label(self, 
                                text = "Username:", 
                                font = DEFAULT)
        self.lbl_username.grid(row = 0, 
                               column = 0)
        
        self.ent_username = tk.Entry(self, 
                                bd = 3, 
                                font = DEFAULT)
        self.background = self.ent_username.cget("bg")
        self.ent_username.grid(row = 0, 
                               column = 1)  
        self.lbl_password = tk.Label(self,
                                text="Password:", 
                                font = DEFAULT)
        self.lbl_password.grid(row = 1, 
                               column = 0)
        self.ent_password = tk.Entry(self,
                                bd = 3, 
                                font = DEFAULT,
                                show = "*")
        self.background = self.ent_password.cget("bg")
        self.ent_password.grid(row = 1, 
                               column = 1)
        self.lbl_instruction_1 = tk.Label(self, 
                                          font = ("Arial", 12),
                                          text = "To login, fill out the")
        self.lbl_instruction_1.grid(row = 2, 
                                    column = 0, 
                                    columnspan = 2)
        
        self.lbl_instruction_2 = tk.Label(self, 
                                          font = ("Arial", 12),
                                          text = "boxes and click Login.")
        self.lbl_instruction_2.grid(row = 3, 
                                    column = 0, 
                                    columnspan = 2)
        
        self.btn_login = tk.Button(self, 
                                   text = "LOGIN", 
                                   bg="green",
                                   command = self.login_button, 
                                   font = DEFAULT)
        self.btn_login.grid(row = 4, 
                            column = 0, 
                            columnspan = 2)
        
        self.btn_login = tk.Button(self, 
                              text = "Login", 
                              font = DEFAULT, 
                              command = self.login_button)
        self.btn_login.grid(row = 4, 
                            column = 0, 
                            columnspan = 2)    
        self.btn_add_user = tk.Button(self,
                                      text = "Add User",
                                      font = DEFAULT)
        self.btn_add_user.grid(row = 5,
                               column = 0)
        self.btn_update_user = tk.Button(self, 
                                         text = "Update User",
                                         font = DEFAULT)
        self.btn_update_user.grid(row = 5,
                                  column = 1,
                                  sticky = "E")
        
    def login_button(self): 
        if Login.login_tries == 2:
            self.btn_login.configure(state = "disabled")
        key = self.ent_username.get()
        if key in users.credentials.keys():
            details = users.credentials[key]
            
            if self.ent_password.get() == details[0]:
                self.ent_username.configure(bg = self.background)
                self.ent_password.configure(bg = self.background) 
                Login.login_tries = 0
                frame_authenticate.answer = details[2]
                frame_authenticate.lbl_question.configure(text = details[1])
                frame_authenticate.update()
                frame_authenticate.tkraise()
            else:
                self.ent_username.configure(bg = "red")
                self.ent_password.configure(bg = "red")
                Login.login_tries += 1        
        else:
            self.ent_username.configure(bg = "red")
            self.ent_password.configure(bg = "red")
            Login.login_tries += 1     