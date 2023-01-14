# quantcast.py

# Takes in a log file as input and finds the most active cookie on a 
# specified day
class ActiveCookie :

    # date : date to look for
    # log_file_path : file path
    # valid : tracks each valid cookie to a count of appearances
    def __init__(self, log_file_path, date, valid=None):
        self.date = date 
        self.log_file_path= log_file_path 
        self.valid = valid 

    # parses through file to track all logged cookies on the given day, as 
    # well as increments their count accordingly
    def parse(self) :
        with open(self.log_file_path) as r:
            for line in r:
                cols = line.split(",")
                cookie = cols[0]
                date = cols[1].split('T')[0] # current log date 
                if date == self.date :
                    if cookie not in self.valid :
                        self.valid.update({cookie : 0})
                    self.valid[cookie] += 1
    
    # iterates through all valid cookies and outputs the most active cookie
    # on the given day
    def output(self) :
        max = 0
        cookies = []
        for c in self.valid :
            if self.valid.get(c) > max :
                max = self.valid.get(c)
                cookies = [c]
            elif self.valid.get(c) == max :
                cookies.append(c)
        for value in cookies :
            print(value)
	return cookies

    def main(self):
        self.parse()
        ret = self.output()
        return ret

if __name__ == "__main__":
    import sys
    file_name = sys.argv[1]
    option_arg = sys.argv[2]
    date = sys.argv[3]
    if option_arg != '-d':
        print("Wrong option!")
    else:
        cur = ActiveCookie(file_name, date, {})
        ret = cur.main()


