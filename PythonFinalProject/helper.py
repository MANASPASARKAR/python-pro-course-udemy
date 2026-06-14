class Helper:

    def get_binary(self, prompt):

        while True:
            val = int(input(prompt))

            if val in [0, 1]:
                return val

            print("Enter 0 or 1 Only")


    def get_three_categorical(self, prompt):

        while True:

            val = int(input(prompt))

            if val in [1, 2, 3]:
                return val

            print("Enter value 1, 2 or 3 only")

    def get_btwn_range(self, prompt, min_val, max_val, keyword):

        while True:

            val = int(input(prompt))

            if min_val < val < max_val:
                return val

            print("Enter realistic ", keyword)

    def get_gender(self, prompt):

        while True:
            val = int(input(prompt))

            if val in [1, 2]:
                return val

            print("Enter 1 or 2 Only")