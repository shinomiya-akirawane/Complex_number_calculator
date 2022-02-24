# Complex_number_calculator
A group repository for ENGF0002 

#### Project Strcuture

The structure of the project follows **MVT(Models,Views,templates)** structure
models.py contains the processor of data from database 
views.py contains main logic algorithms 
templates.py contains all html pages

For example:
To realize a log-in page:
 1. Client send log-in information to **View**
 2. **View** send the data to **Model**
 3. **Model** re-mat the data and send it to database to save
 4. Database return the result of saving data to **Model**
 5. **Model** send the result to **View**
 6. **View** request corresponding html page from **Template**
 7. **Template** send page to **View**
 8. **View** send page to Client

#### Variable and functions name Rules
The variable name should follow camel rules. Meaningless name is strictly banned, such as x,y,z
e.g. currentNum

The function name should follow camel rules,too. Aiming to be readable to others.
#### Frames used 
Bootstrap + Django

#### Tasks 

 - **Xinyu, Hou:** Templates genrated by Bootstrap
 - **TianXiang, Xiong:** Model + SQL
 - **Yuhang, Zhou:** urls
 - **Zhaoyan, Dong:** View