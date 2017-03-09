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


    pass