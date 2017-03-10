import cmd

class Skills(cmd.Cmd):
    """
    Simple program that allows user to add skills, view a list of all the skills added, 
    indicate the skills studied, indicate the skills studied, view a list of skills studied
    and see my learning progress.
    """
    def do_input_skill(self,line):
        """
        Prompt user to add new skill
        """
        print("\n HELLO, WELCOME!!!\n1. Add skill \n 2. view a list of all the skills added \n 3. indicate the skills studied \n 4. indicate the skills studied  \n 4. View a list of skills studied \n")
        skill_addded = str(input("Please enter a skill to add"))
        self.skills ={}
        self.skills [skill_addded] = "NOT_STUDIED"
        return self.skills

    def do_indicate_skills_studied(self, args):
    	"""Set skill to studied
        """
    	check_skill = args
    	# check if the skill existsnot
    	# Check that the has not been studied
    	if self.skills[check_skill] == "STUDIED":
    		print("{} has already been studied".format(self.skills[check_skill]))
    	else:
    		self.skills[check_skill] = "STUDIED"
    		print("{} set to studied".format(self.skills[check_skill]))

    def do_view_skills_studied(self, args):
    	""" list all skills studied
        """
    	studied_skills = []
    	for k, v in self.skills.items():
    		if v == "STUDIED":
    			studied_skills.append(k)
    	print(studied_skills)

    def do_view_skills_not_studied(self, args):
    	"""list all skills not studied
        """
    	not_studied_skills = []
    	for k, v in self.skills.items():
    		if v == "NOT_STUDIED":
    			not_studied_skills.append(k)
    	print(not_studied_skills)




if __name__ == '__main__':
    Skills().cmdloop()
