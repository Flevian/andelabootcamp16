class ListCompresnsion(object):

    """Binary Search to traverse an ordered list, effectively
       Populate the arrays with valid content
    """    

    def __init__(self, a, b):
        """
        this function takes in list length and step(difference between consecutive values and process a list)
        """

        self.one_to_twenty =[]
        self.two_to_forty =[]
        """
        processing a list
        """
        """
        create an array from 1 to 20, with intervals of 1
        """
        self.one_to_twenty_length = range(a, (a * b)) 

        for value in self.one_to_twenty_length:
            self.one_to_twenty.append(value)

        """
        create an array from 2 to 40, with intervals of 2
        """    

        self.two_to_forty_length = range(a, (a * b + 1))

        self.two_to_forty = [value * 2 for value in self.two_to_forty_length]

        """
        create an array from 10 to 1000, with intervals of 10
        """

        self.ten_to_thousand_length = range(b, (a * b * 50 + 1))

        self.ten_to_thousand = [value * 10 for value in self.ten_to_thousand_length]                    

class  BinarySearch(ListCompresnsion):
    def __init__(self, a, b):
        self.a = a
        self.b = b 


    ListCompresnsion.__init__(self, a, b)
    """
    this class takes the list processed from the parent class to search for the desired value
    """
    def search(self, desired_value):
      
        """
        this function takes in a list and the desired, searches the desired value and return the number of interation to get the desired value and the index of the value 
        """

        start = 0
        last = len(self.my_list) - 1
        count = 0
        out_dict = {}

        while start <= last:
            mid_point = start + last // 2
            count += 1

            if self.my_list[mid_point] == desire_value:
                """
                compares the mid point value and the desired value
                  """
                index = [mid_point]
                break


            else:
                if desire_value < self.my_list[mid_point]:
                    last = mid_point - 1

        out_dict[count] = index
        return out_dict 



