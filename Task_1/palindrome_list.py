'''Lab 12.1'''

class Palindrome():

    '''
    class Palindrome
    '''

    def find_palindromes(self, path_from, save_path):
        '''
        Finds a palindrome and connects other functions
        '''
        return_list = []

        for element in self.read_file(path_from):
            for i in range(int(len(element) / 2)):
                if element[i] != element[-(i + 1)]:
                    break
            else:
                return_list.append(element)
        self.write_to_file(save_path, return_list)

        return return_list

    def read_file(self, main_path):
        '''
        Read a file
        '''
        return_list = []

        with open(main_path, 'r', encoding = 'utf-8') as file:
            for element in file:
                return_list.append(element.strip().split()[0])

        return return_list

    def write_to_file(self, save_path, list_words):
        '''
        Write to a file
        '''
        with open(save_path, 'w', encoding = 'utf-8') as file:
            file.write(list_words[0])
            for element in list_words[1:]:
                file.write("\n" + element)
