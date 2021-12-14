##14/12/2021

nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."


l = [1,2,3,4]
l2 = [elem for elem in l]
## primo esercizio

a = [ num for num in nums if num % 8 ==0]
print(a)

## secondo esercizio


b = [num for num in nums if "6" in str(num)]
print(b)


## terzo esercizio

c = [1 for s in string if " " in s]

sum(c)

## quarto esercizio 

words = string.split()

d = [w for w in words if len(w) < 5]
print(d)

## quinto esercizio