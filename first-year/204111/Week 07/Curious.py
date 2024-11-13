# List of tuples
my_list = [["1", "2.5"], ["3","4.7"], ["5", "6.1"]]
# Apply a lambda function to each tuple using map
processed_list = list(map(lambda t: ("-".join(t)), my_list))
print(processed_list)

# %g turn int to str but only .four digit
a = '%g' % 10.4567899877
print(a,type(a))
a = '%G' % 10
print(a,type(a))

a = [1,2,3,4,5,6]
print(a[2:][-1])