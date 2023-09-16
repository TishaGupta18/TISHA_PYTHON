row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
print(f"{row1}\n{row2}\n{row3}")
matrix=[row1,row2,row3]
position=input("enter the position where you want to hide your money:")

#you want to access 32
row_no=int(position[0])
col_no=int(position[1])
row_selected=matrix[row_no-1]
row_selected[col_no-1]='x'
print(f"{row1}\n{row2}\n{row3}")
