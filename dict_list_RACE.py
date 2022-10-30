import random, time

random_stuff = ['dirt', 'mulch', 'pavement cement', 'borderlands 2', 'menace 2 society']
class race():
    def create_dataset(self):
        bang = 500000
        f = open('data.txt', 'w')
        for num in range(bang):
            current=random.choice(random_stuff)
            f.write(current+"\n")
            print('wrote: ', current,"\n")
        f.close()

    def list_race(self):
        list_count = []
        for stuff in random_stuff:
            list_count.append(0)
        with open('data.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line!="":
                    list_count[random_stuff.index(line)]+=1
        print (list_count)

    def dict_race(self):
        dict_count = {}
        for stuff in random_stuff:
            dict_count[stuff]=0
        with open('data.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line!="":
                    dict_count[line]+=1

        print (dict_count)

def main():
    r = race()
    time_00 = time.time()
    print('start_time', time_00)
    r.create_dataset()
    time_01 = time.time()
    print(f'[CREATE DATASET]--> {int(time_01) - int(time_00)}')
    time_03 = time.time()
    r.list_race()
    time_04 = time.time()
    print(f'[LIST RESULTS]--> {int(time_04) - int(time_03)}')
    time_05 = time.time()
    r.dict_race()
    time_06 = time.time()
    print(f'[DICT RESULTS]-->  {int(time_06) - int(time_05)}')


if __name__ == "__main__":
    main()







