def find_max_min(my_list):

    """
    function to get the minimum nd maximum values in a list and return the result in alist
    """

    min_max_result = []

    if type(my_list) == list:

        """
        checks if the input is alist in order to perform the intended task
        use max() and min() methods to find the maximum and minimum values from the list respectively and return the output in a list
        """
        max_value=max(my_list)
        min_value=min(my_list)

        if max_value == min_value:

            """
            checks if the maximum and minimum are equal
            if they are equal
            if they are not equal it returns a list that contains the minimum and maximum values
            """
            pass
 

        else:
            min_max_result.append(min_value)
            min_max_result.append(max_value)
            return min_max_result

    else:
        return "invalid input"

my_list = [67, 67]
print(find_max_min(my_list)) 
