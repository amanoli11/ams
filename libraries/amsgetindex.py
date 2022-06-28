def AMSGetIndex(item_list, value):

    if value == "True":
        value = True
    elif value == "False":
        value = False

    item_list = dict(item_list)
    index_number = None
    for i in item_list.keys():
        if i == value:
            index_number = list(item_list.keys()).index(value)

    # setattr(self.parent_class, self.index, self.ddl_value_index)
    return index_number