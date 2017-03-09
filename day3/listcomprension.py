class ListCompresnsion(object):

    def __init__(self, a, b):
        """
        this function takes in list length and step(difference between consecutive values and process a list)
        """

        self.a = a
        self.b = b

        self.my_list =[]
        """
        processing a list
        """
        list_length = range(a, (a * b))

        for value in list_length:
            my_list.append(value)

class  BinarySearch(ListCompresnsion):


    BinarySearch.__init__(self)
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



