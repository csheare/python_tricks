# Here we are going to look ay building pipelines with generators!
# To start we are going to get an average of all series A rounds in the tech_crunch dataset.

# 1. Read every line of the file
# create a generator expression to yield each line in a file
lines = (line for line in open("techcrunch.csv"))

# 2. Split each line into a list of values
# iterate through the generator within the definition of another generator expression called
# list_line, which turns each line into a list of values
list_line = ( s.rstrip().split(",") for s in lines)

# 3. Extract the column names
# advance the iteration of list_line once to get a list of column names of CSV file
cols = next(list_line)

# 4. Use the column names and lists to create a dictionary

company_dicts = ( dict(zip(cols,data)) for data in list_line)

# 5. Filter out the rounds you aren't interested in

funding = (
    int(company_dict['raisedAmt'])
    for company_dict in company_dicts
    if company_dict['round'] == 'a'
)

# 6. Calculate the total and average values for the rounds you are interested in.
# At this point nothing has been iterated over, need to use a for loop or a
# function that works on iterables like sum()

# iterate over the generators with sum
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
