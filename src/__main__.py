import json as json_module
import graphviz

_pagestates_file_path = '.\example-data\PageStates.txt'
_pagetransitions_file_path = '.\example-data\PageTransitions.txt'
_state_output_file_path = '.\example-data\state-output.json'
_transition_output_file_path = '.\example-data\\transition-output.json'
_graph_pdf = 'example-graph'

def create_json_arr(file_path):
    # Read the .txt file
    with open(file_path, 'r') as file:
        txt_content = file.read()

    # read each line
    lines = txt_content.split(';')
    result = []
    field_name_arr = []
    for i, line in enumerate(lines):
        data_fields = line.split(',')
        if i == 0:
            # get json property keys
            for field_name in data_fields:
                field_name_arr.append(field_name)
            field_name_arr_len = len(field_name_arr)
        else:
            json = {}
            for h, field_value in enumerate(data_fields):
                # assign values to parsed keys
                json[field_name_arr[h % field_name_arr_len]] = field_value
                if(h % field_name_arr_len == field_name_arr_len - 1):
                    result.append(json)
                    json = {}
    return result


def write_to_json_file(raw_json_arr, file_path):
    # Open a file for writing
    with open(file_path, 'w') as json_file:
        # Serialize and write the list to the file with indentation
        json_module.dump(raw_json_arr, json_file, indent=4)
    return json_module.dumps(raw_json_arr)


def create_graphviz_file(state_arr, transition_arr):
    dot = graphviz.Digraph(graph_attr={'rankdir':'LR'})
    for state in state_arr:
        dot.node(state['Id'], state['Title'])
    for transition in transition_arr:
        dot.edge(transition['StateId'],
                 transition['NextStateId'], transition['EventId'])
    dot.render(_graph_pdf, view=True)


def main():
    raw_state_arr = create_json_arr(_pagestates_file_path)
    raw_transition_arr = create_json_arr(_pagetransitions_file_path)
    write_to_json_file(raw_state_arr, _state_output_file_path)
    write_to_json_file(raw_transition_arr, _transition_output_file_path)
    create_graphviz_file(raw_state_arr, raw_transition_arr)


if __name__ == "__main__":
    main()
