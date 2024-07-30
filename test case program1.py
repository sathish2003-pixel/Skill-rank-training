# test_file_operations.py

import os
import pytest
from file_operations import store_variable, update_variable, read_variable, delete_file

#for storing the variable the test case
def test_store_variable(tmp_path):
    #define a temp path 
    file_name = tmp_path / "output.txt"
    content = "Hello, World!"
    
    store_variable(file_name, content)
    
    with open(file_name, "r") as file:
        #check the file value is equal to the content value
        assert file.read() == content

#Update test case
def test_update_variable(tmp_path):
    file_name = tmp_path / "output.txt"
    content = "Hello, World!"
    new_data = " Bye bye"
    
    store_variable(file_name, content)
    update_variable(file_name, new_data)
    
    with open(file_name, "r") as file:
        #concatnate the content to new_data
        assert file.read() == content + new_data

#test cases fo the read variable
def test_read_variable(tmp_path):
    file_name = tmp_path / "output.txt"
    content = "Hello, World!"
    
    store_variable(file_name, content)
    #check the value is equal or not
    assert read_variable(file_name) == content

#test case for the delete file
def test_delete_file(tmp_path):
    file_name = tmp_path / "output.txt"
    content = "Hello, World!"
    
    store_variable(file_name, content)
    value = read_variable(file_name)
    if value:
        delete_file(file_name)
        assert not os.path.exists(file_name)
        
#if the file is not exist the test case
        
def test_delete_non_existent_file(tmp_path):
    file_name = tmp_path / "non_existent.txt"
    delete_file(file_name)
    assert not os.path.exists(file_name)
