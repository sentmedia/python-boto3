# Create variables for different data types and print them

def main():
    instance_type = 't2.medium'
    num_of_instances = 4
    hours_running = 16
    status_running = True
    cost_per_hour = 0.036

    # Calculate the total compute cost using arithmetic operator
    compute_cost = num_of_instances * hours_running * cost_per_hour

    # Print the compute cost message if 'status_running = True' using a conditional
    if status_running == True:
        print(f'I have {num_of_instances} {instance_type} instances running and the total cost is ${compute_cost} USD.')
    else:
        print('You have 0 instances running, turn on your instances to calculate cost.')

if __name__ == '__main__':
    main()