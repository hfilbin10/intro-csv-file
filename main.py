import csv

animal_type = input('Please enter the type of animal you are looking for: ')
animal_type = animal_type.lower()

try:
    if animal_type in ('cat', 'cats'):
        csv_file = 'cats'
    elif animal_type in ('dog', 'dogs'):
        csv_file = 'dogs'
    else:
        raise FileNotFoundError

    with open(f"data/{csv_file}.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['name'].title()} is a {row['age']} year old {row['breed'].title()}.")

except FileNotFoundError:
    print(f'Sorry, we do not have any {animal_type} here.')


# with open('./data/cats.csv', mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count ==0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#             continue
#         print(f'\t{row[0]} is a {row[1]} year old {row[2]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')


# with open('./data/cats.csv', mode='w') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')

#     csv_writer.writerow(["name", "age", "breed"])
#     csv_writer.writerow(['Loki', '6', 'shorthair'])
#     csv_writer.writerow(['Shadow', '3', 'siamese'])
#     csv_writer.writerow(['garfield', '2', 'ocelot'])

# def display_animal_info(animal_type):
#     try:
#         data = open(f'./data/{animal_type}.csv', mode='r')
#         reader = csv.DictReader(data)

#         for row in reader:
#            print(f"{row['name'].title()} is {row['age']} years old and is a {row['breed']}.")

#     except FileNotFoundError:
#         print(f"Sorry, we don't have any {animal_type} here.")

# animal_type = input("Enter an animal: ")


# display_animal_info(animal_type)