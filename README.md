
# Instructions how to run the code

## How to install
#### Using Git
```
git clone https://github.com/amitznaft/Planck-sTechAssignment.git ./myfolder
```
#### Using manual download ZIP
1. Download repository
2. Uncompress to your desired directory

#### Install packages 
pip install . 

## How to run
python api.py

## Server Functionality
#### TEST WITH POSTMAN 

GET /drinks - Returns the id, name, description and price of all drinks
GET /drink/<id> - Returns id, name, description and price of a drink
GET /pizzas - Returns the id, name, description and price of all pizzas
GET /pizza/<id> - Returns id, name, description and price of a pizza
GET /desserts - Returns the id, name, description and price of all desserts
GET /dessert/<id> - Returns id, name, description and price of a dessert
POST /order - receives an order and returns its total price.
body should be:
```
{
    "drinks": [id_5, id_6],  // eg: "drinks": [123, 124] 
    "desserts": [id_1, id_2],
    "pizzas": [id_3, id_4]
}
```
