def find_missing(list1, list2):
    if type(list1) == list and type(list2) == list:
        """
        checks if the lists are empty
        """

        if len(list1) == 0 and len(list2) == 0:
            """
            checks if the lists are empty
            """
            mising_number = 0
            return mising_number
        else:
            """
            casting list to set
            """         
            set1 = set(list1)
            set2 = set(list2)
            """
            check the set difference
            """
            set_length_difference = len(set1) - len(set2)
            
            if abs(set_length_difference) == 1:
                """
                gets the the number that is not present in both list
                """
                mising_number = set1 ^ set2
                return mising_number.pop()

            elif set_length_difference == 0:
                """
                if the sets similarity
                """ 
                if set2.issuperset(set1) or set2.issubset(list1):
                    mising_number = 0

                else:
                    mising_number = "invali input e"

                return mising_number

            else:
                return "invali sets difference is more than one"        

    else:
        return "invali input "              
        
        

        

                

list2 = []
list1 =[]

print(find_missing(list1, list2))           

