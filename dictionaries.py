
# Packing within a function into a dictionary
def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_teacher(name='Ashey', job='Instructor', topic='python')

# Unpacking a dictionary within a function

teacher2 = {
  'name': 'Ashley',
  'job': 'Instructor',
  'topic': 'Python'}


def print_teacher2(name, job, topic):
    print(name)
    print(job)
    print(topic)


print_teacher2(**teacher2)
