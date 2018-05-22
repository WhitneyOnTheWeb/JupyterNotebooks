# Count XML Tags in Text
def tag_count(tokens):
    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1
    return count

# Create an HTML List
def html_list(list_items):
    HTML_string = "<ul>\\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\\n".format(item)
    HTML_string += "</ul>"
    return HTML_string

# Create Nearest Square Function
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2

print(nearest_square(100))


def top_two(input_list):
    
    #Write your code in the white space here
    top1 = max(input_list)
    input_list.remove(max(input_list))
    top2 = max(input_list)
    top_two = [top1, top2]
    return top_two