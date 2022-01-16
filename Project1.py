#All Modules
import math
import statistics
import json


#All Variables



#User-defined Functions for creating structures

def create_list():
    List_init = []
    number_ele_List = int(input("please enter number of elements to be available in list"))  
    for element in range(number_ele_List):
        element_n = int(input("please enter the element: "))
        List_init.append(element_n)
    return List_init

def create_tuple():
    Tuple_init = []
    number_ele_Tuple = int(input("please enter number of elements to be available in tuple"))  
    for element in range(number_ele_Tuple):
        element_n = int(input("please enter the element: "))
        Tuple_init.append(element_n)
    return Tuple_init

def create_set():
    Set_init = []
    number_ele_Set = int(input("please enter number of elements to be available in set"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_init.append(element_n)
    return Set_init

def create_dict():
    Dict_init = {}
    number_ele_Dict = int(input("please enter number of key-value pairs to be added in dictionary"))  
    for element in range(number_ele_Dict):
        key = int(input("please enter the key: "))
        value = int(input("please enter the value: "))
        Dict_init[key]=value
    return Dict_init


#Initial code

print("Welcome to Data structure calculator")

print("Please select any operation to proceed \n1.List \n2.Tuple \n3.Set \n4.Dictionary ")

data_input = int(input("please enter a number between 1 and 4 "))



#LIST OPERATION CODE




#User-defined Functions for List 


def append_list(List):
    element_to_be_inserted = int(input("Please enter the element to be inserted: "))
    List.append(element_to_be_inserted)
    return List

def pop_list(List):
    List.pop(int(input("Please enter the index of the element to be popped")))
    return List
    
def len_list(List):
    return len(List)

def copy_list(List):
    new_list=List.copy()
    return (new_list)

def count_list(List):
    a=List.count(int(input("Please enter the element which you want to search the frequency of")))
    return (a)

def reverse_list(List):    
    List.reverse()
    return List

def sort_list(List):   
    List.sort()
    return List

def remove_list(List):          
    List.remove(int(input("Please enter the element that you want to remove")))
    return List

def insert_list(List):
    List.insert((int(input("What position do you want to put your new value?"))), int(input("What element do you want to insert")))
    return List

def extend_list(List):
    a=int(input("Please enter new elements to add to your list"))
    List.extend(a)
    return List

def index_list(List):
    return List.index(int(input("please enter the value which you want to find the index of")))

def min_list(List):   
    return min(List)

def max_list(List):
    return max(List)

def conc_list(List): 
    a = []
    number = int(input("please enter number of elements to be available in list"))  
    for element in range(number):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
    return [List+a]



#TUPLE OPERATION CODE


def count_tuple(Tuple):
    a=Tuple.count(int(input("Please enter the element which you want to check the frequency of")))
    return a

def index_tuple(Tuple):
    a=Tuple.index((int(input("Please enter the element of which you want to find the first occurrence of"))))
    return a

def conc_tuple(Tuple):  
    a = []
    number_ele_Tuple = int(input("please enter number of elements to be available in tuple"))  
    for element in range(number_ele_Tuple):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
        b=tuple(a)
    return (Tuple+b)

def repeat_tuple(Tuple):
    a=int(input("How many times do you want to repeat the tuple"))
    return Tuple*a

def len_tuple(Tuple):
    return len(Tuple)
    
    
    
    



#SET OPERATION CODE


def add_set(Set):        
    Set.add(int(input("Please enter the element you want to add")))
    return Set

def copy_set(Set):
    a=Set.copy()
    return a

def discard_set(Set):    
    a=int(input("Please enter the element you want to discard"))
    Set.discard(a)
    return Set


def pop_set(Set):   
    Set.pop()
    return Set

def difference_set(Set):
    a= []
    number_ele_Set = int(input("please enter number of elements to be available in set"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
    return Set.difference(a)

def intersection_set(Set):
    a= []
    number_ele_Set = int(input("please enter number of elements to be available in set"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
    return Set.intersection(a)

def union_set(Set):
    a= []
    number_ele_Set = int(input("please enter number of elements to be available in set"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
    return Set.union(a)

def update_set(Set):   
    a=set(create_set())
    Set.update(a)
    return Set



def sym_diff_set(Set):
    a= []
    number_ele_Set = int(input("please enter number of elements to be available in set"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
    return Set.symmetric_difference(a)

def int_update_set(Set): 
    a= set(create_set())
    Set.intersection_update(a)
    return Set


def diff_update_set(Set): 
    a=set(create_set())
    Set.difference_update(a)
    return Set

def isdisjoint_set(Set):
    a= []
    number_ele_Set = int(input("please enter number of elements to be available in set"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
    return Set.isdisjoint(a)

def issubset_set(Set):
    a= []
    number_ele_Set = int(input("please enter number of elements to be available in set"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
    return Set.issubset(a)

def issuperset_set(Set):
    a= []
    number_ele_Set = int(input("please enter number of elements to be available in set"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        a.append(element_n)
    return Set.issuperset(a)



#DICTIONARY OPERATION CODE

def copy_dict(Dict):
    a= Dict.copy()
    return a

def get_dict(Dict):
    a=Dict.get(int(input("Please enter a valid key")))
    return a

def update_dict(Dict):
    a=dict(create_dict())
    Dict.update(a)
    return Dict

def values_dict(Dict):
    a=Dict.values()
    return a

def pop_dict(Dict):    
    Dict.pop(int(input("Please enter a key to be removed")))
    return Dict

def items_dict(Dict):
    a=Dict.items()
    return a

def keys_dict(Dict):
    a=Dict.keys()
    return a

def popitem_dict(Dict):
    Dict.popitem()
    return Dict

def len_dict(Dict):
    return len(Dict)
    
    
    
#IF_ELSE PROGRAMMING

if data_input==1:
                 print("Welcome to List operations ")
                 print("Create a List for proceeding List Operations")
                 List_main = create_list()
                 print("The created list is ", List_main)
                 print("Please select any one List operation to proceed (Any number between 1-15)")
                 print("1.append\n2.pop\n3.len\n4.clear\n5.copy\n6.count\n7.reverse\n8.sort\n9.remove\n10.insert\n11.extend\n12.index\n13.min\n14.max\n15.concatenate")

                 List_operation_input = int(input("please enter any one number from 1 to 15"))

                 if List_operation_input==1:
                                        output_append=append_list(List_main)
                                        print("The output after append operation is ", output_append)
                                        
                 elif List_operation_input==2:
                                        output_pop=pop_list(List_main)
                                        print("The output after pop operation is ", output_pop)
                                        
                 elif List_operation_input==3:
                                        output_len=len_list(List_main)
                                        print("The number of elements in the list are: ", output_len)

                 elif List_operation_input==4:                   
                                        print("The output after clear operation is []")

                 elif List_operation_input==5:
                                        output_copy=copy_list(List_main)
                                        print('The new list is ', output_copy)

                 elif List_operation_input==6:
                                        output_count=count_list(List_main)
                                        print("The number of times the element appears is: ", output_count)

                 elif List_operation_input==7:
                                        output_reverse=reverse_list(List_main)
                                        print("The new list is ", output_reverse)

                 elif List_operation_input==8:
                                        output_sort=sort_list(List_main)
                                        print("The new list is ", output_sort)

                 elif List_operation_input==9:
                                        output_remove=remove_list(List_main)
                                        print("The new list is", output_remove)

                 elif List_operation_input==10:
                                        output_insert=insert_list(List_main)
                                        print("The new list is", output_insert)

                 elif List_operation_input==11:
                                        output_extend=extend_list(List_main)
                                        print("The new list is", output_extend)


                 elif List_operation_input==12:
                                        output_index=index_list(List_main)
                                        print("The index value is", output_index)

                 elif List_operation_input==13:
                                        output_min=min_list(List_main)
                                        print("The minimum element is", output_min)  

                 elif List_operation_input==14:
                                        output_max=max_list(List_main)
                                        print("The maximum element is", output_max)

                 elif List_operation_input==15:
                                        output_conc=conc_list(List_main)
                                        print("The new list is", output_conc)
                 
  

elif data_input==2:
                print("Welcome to Tuple Operations")
                print("Create a Tuple for proceeding Tuple Operations")
                Tuple_main = tuple(create_tuple())
                print("The created tuple is ", Tuple_main)
                print("Please select any one Tuple operation to proceed (Any number between 1-5)")
                print("1.count\n2.index\n3.concatenate\n4.repeat\n5.len")                

                Tuple_operation_input = int(input("please enter any one number from 1 to 5"))

                if Tuple_operation_input==1:
                    output_count=count_tuple(Tuple_main)
                    print("The number of times the element occurs is", output_count)

                elif Tuple_operation_input==2:
                    output_index=index_tuple(Tuple_main)
                    print("The element is found at", output_index)

                elif Tuple_operation_input==3:
                    output_conc=conc_tuple(Tuple_main)
                    print("The new tuple is", output_conc)

                elif Tuple_operation_input==4:
                    output_repeat=repeat_tuple(Tuple_main)
                    print("The new tuple is", output_repeat)

                elif Tuple_operation_input==5:
                    output_len=len_tuple(Tuple_main)
                    print("The number of elements in the tuple is", output_len)
                    


                
elif data_input==3:
                print("Welcome to Set Operations")
                print("Create a Set for proceeding Set Operations")
                Set_main = set(create_set())
                print("The created set is ", Set_main)
                print("Please select any one Set operation to proceed (Any number between 1-15)")
                print("1.add\n2.clear\n3.copy\n4.discard\n5.pop\n6.difference\n7.intersection\n8.union\n9.update\n10.symmetric_difference\n11.intersection_update\n12.difference_update\n13.isdisjoint\n14.issubset\n15.issuperset")

                Set_operation_input = int(input("please enter any one number from 1 to 15"))

                if Set_operation_input==1:
                    output_add=add_set(Set_main)
                    print("The new set is", output_add)

                elif Set_operation_input==2:
                    print("The new set is {}")

                elif Set_operation_input==3:
                    output_copy=copy_set(Set_main)
                    print("The new set is", output_copy)

                elif Set_operation_input==4:
                    output_discard=discard_set(Set_main)
                    print("The new set is", output_discard)

                elif Set_operation_input==5:
                    output_pop=pop_set(Set_main)
                    print("The new set is", output_pop)

                elif Set_operation_input==6:
                    output_difference=difference_set(Set_main)
                    print("The difference is", output_difference)

                elif Set_operation_input==7:
                    output_intersection=intersection_set(Set_main)
                    print("The intersection is", output_intersection)

                elif Set_operation_input==8:
                    output_union=union_set(Set_main)
                    print("The union of the sets is", output_union)

                elif Set_operation_input==9:
                    output_update=update_set(Set_main)
                    print("The updated set is", output_update)

                elif Set_operation_input==10:
                    output_sym_diff=sym_diff_set(Set_main)
                    print("The set of symmetrical difference is", output_sym_diff)

                elif Set_operation_input==11:
                    output_int_update=int_update_set(Set_main)
                    print("The new set is", output_int_update)

                elif Set_operation_input==12:
                    output_diff_update=diff_update_set(Set_main)
                    print("The set is", output_diff_update)

                elif Set_operation_input==13:
                    output_isdisjoint=isdisjoint_set(Set_main)
                    print(output_isdisjoint)
                    
                elif Set_operation_input==14:
                    output_issubset=issubset_set(Set_main)
                    print(output_issubset)

                elif Set_operation_input==15:
                    output_issuperset=issuperset_set(Set_main)
                    print(output_issuperset)
                    
                




#DICTIONARY OPERATION CODE



elif data_input==4:
                print("Welcome to Dictionary Operations")
                print("Create a Dictionary for proceeding Dictionary Operations")
                Dict_main = dict(create_dict())
                print("The created dictionary is ", Dict_main)
                print("Please select any one Dictionary operation to proceed (Any number between 1-10)")
                print("1.clear\n2.copy\n3.get\n4.update\n5.values\n6.pop\n7.items\n8.keys\n9.popitem\n10.len")

                Dict_operation_input = int(input("please enter any one number from 1 to 10"))

                if Dict_operation_input==1:
                    print("The dictionary is now {}")

                elif Dict_operation_input==2:
                    output_copy=copy_dict(Dict_main)
                    print("The new dictionary is", output_copy)

                elif Dict_operation_input==3:
                    output_get=get_dict(Dict_main)
                    print("The value is", output_get)
                    
                elif Dict_operation_input==4:
                    output_update=update_dict(Dict_main)
                    print("The new dictionary is", output_update)

                elif Dict_operation_input==5:
                    output_values=values_dict(Dict_main)
                    print("The values in the dictionary are", output_values)

                elif Dict_operation_input==6:
                    output_pop=pop_dict(Dict_main)
                    print("The new dictionary is", output_pop)
                
                elif Dict_operation_input==7:
                    output_items=items_dict(Dict_main)
                    print("The list is", output_items)

                elif Dict_operation_input==8:
                    output_keys=keys_dict(Dict_main)
                    print("The keys are", output_keys)

                elif Dict_operation_input==9:
                    output_popitem=popitem_dict(Dict_main)
                    print("The new dictionary is", output_popitem)

                elif Dict_operation_input==10:
                    output_len=len_dict(Dict_main)
                    print("The number of elements in the dictionary is", output_len)
                             
