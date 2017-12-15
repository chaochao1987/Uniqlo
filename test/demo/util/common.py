import yaml
import os

class GetTestData(object):
    def __init__(self):
        self.data = {}

    # def get_file_path(self):
    #     file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'runcase/testdata/add_same_items_to_cart.yaml')
    #     return file_path

    def get_datas_in_file(self, file_name):
        target_file_dir = self.get_file_path(file_name)
        with open(target_file_dir, 'r') as f:
            self.data = yaml.load(f)

    def get_file_path(self, file_name):
        current_file_dir =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        root_dir = os.path.join(current_file_dir, 'runcase/testdata')
        target_file_dir = os.path.join(root_dir, file_name)
        return target_file_dir

    # def save_datas_in_dic(self, lines):
    #     file_data = {}
    #     for line in lines:
    #         if line == '' or line.startswith('#'):
    #             continue
    #         else:
    #             line = line.split('=', 1) if '=' in line else []
    #             if not (all(line) and line):
    #                 print line
    #                 raise Exception("the format is wrong")
    #             line_v = line[0]
    #             line_k = line[1].replace('\n', '')
    #             # print self.type, '\n', self.value
    #             # if self.type == key:
    #             #     return self.value
    #             file_data[line_k] = line_v
    #             return file_data

    # def element_path_wz_format(self, element_path, txt):
    #     self.element_path = element_path.format(txt)
    #
    # def get_value_from_page_locator(self, locator_path):
    #     if '=' in locator_path:
    #         locator_element = locator_path.split('=', 1)
    #     else:
    #         raise Exception("locator_path is not correct format")
    #     return locator_element[0], locator_element[1]







# c = GetTestData()
# print c.get_datas_in_file('../runcase/testdata/add_same_items_to_cart.yaml')
# print c.data




















