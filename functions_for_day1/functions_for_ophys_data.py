
# create a function that iterates the input ids which is a list of session ids 
# and prints the number of cells in each session
def print_number_of_cells(input_ids):
    for session_id in input_ids:
        data_set = boc.get_ophys_experiment_data(ophys_experiment_id=session_id)
        print('The number of cells in session ' + str(session_id) + ' is ' + str(data_set.get_cell_specimen_ids().shape[0]))