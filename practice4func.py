
def max_num(a,b,c):
    #just use the max func to find max
    return max(a,b,c)

def mult_list(lst):
    #return 0 if the list is empty
    if len(lst) == 0:
        return 0

    answer = lst[0]

    if len(lst) > 1:
        for element in lst [1:]:
            answer *= element
    return answer

def rev_string(rev):
    return rev[::-1]

def num_within(num, top, bottom):
    return num in range(top,bottom+1)

triangle = [[1],[1,1]]
def pascal(n):

  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)


print(max_num(1,2,3))
print(mult_list([]))
print(mult_list([1,5,5]))
print(rev_string("apple"))
print(num_within(2,1,2))
print(num_within(8,3,7))
pascal(2)