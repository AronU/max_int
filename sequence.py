#for loopa sem stjórnar því hversu oft það keyrist(notar n inputtið)
#þrjár breytur, tala 1, 2 og 3. Tala 1 er tala 2 + 3 og síðan færist tala 1
#í tölu 2 og tala 2 færist í 3 og 3 hverfur. 
#1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

int_1 = 0
int_2 = 0
int_3 = 0
newest_int = 0

n = int(input("Enter the length of the sequence: ")) # Do not change this line
    
for x in range(0, n):
    if x == 0:
        int_1 = 1
        print(int_1)
    elif x == 1:
        int_2 = 2
        print(int_2)
    elif x == 2:
        int_3 = 3
        print(int_3)
    else:
        newest_int = int_1 + int_2 + int_3

        print(newest_int)
        int_1 = int_2
        int_2 = int_3
        int_3 = newest_int

