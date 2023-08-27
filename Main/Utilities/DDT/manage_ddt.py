import csv


class DDT:
    my_list = []
    @staticmethod
    def write_to_list_from_csv():
        with open('C:\Automation\Hackaton python\Hackathon-Python\Test\db.csv', newline='') as f:
            reader = csv.reader(f)
            my_list = [tuple(row) for row in reader]
            return my_list

        # import csv
        #
        # import pytest
        #
        # def read_test_data_from_csv(csv_path):
        #     test_data = []
        #     with open(csv_path, newline="") as csvfile:
        #         data = csv.reader(csvfile, delimiter=",")
        #         next(data)  # skip header row
        #         for row in data:
        #             test_data.append(row)
        #     return test_data
