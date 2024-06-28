## Ticket Torque Backend API
* Live Link: Todo
* [Client App Github](https://github.com/AlFahimBinFaruk/TicketTorque_Client)
* [Admin App Github](https://github.com/AlFahimBinFaruk/Adminpanel_TicketTorque/)


### Client Requirements

As a guest user, I can
* View homepage, Schedules
* Signup to buy tickets
* Search for ticket from one destination to another
* Select ticket of what category(Bus,Train,Plane) I want.

As an Admin user, I can
* Login
* View & edit profile(first_name,last_name,email,password)
* CRUD Users
* CRUD roles(only 2 roles: admin,customer)
* CRUD Tickets
* Logout

As a Customer, I can
* Login
* View & edit profile(first,last name,email,password)
* Purchase a Ticket if available.
* Cancel purchase.
* See my purchase history
* Checkout - 

### Technology

* Language: Python3
* Framework: Django
* Database: PostgreSQL

### Database Models
![Database Model Image](https://drive.google.com/uc?export=view&id=1dAJKpOz3uefWzbuPdgm63obFaGpkaBK3)

### Screenshots

* Home
![Image](https://drive.google.com/uc?export=view&id=1IIirQc-Kh-lshGVmeCXR1eW0ds5FXtWv)
* Ticket List
![Image](https://drive.google.com/uc?export=view&id=1eyO5RCiibwwYYCaTLk0EBgP1vktJPB98)
* Checkout
![Image](https://drive.google.com/uc?export=view&id=1JGYd2u_3aqtFNsGkrk5Es5RkpUV4Akyq)
* History
![Image](https://drive.google.com/uc?export=view&id=1e5CF0FUNbZNPsx4c-g4N0mwXfskD4Dga)
* Profile
![Image](https://drive.google.com/uc?export=view&id=1Sar4l3-AOIvoW42FToooKh7PY1Ow5n0P)
* Login
![Image](https://drive.google.com/uc?export=view&id=1XmpgvCdYP8mndJ7ZOgmWcUszN_yN9aHz)
* Register
![Image](https://drive.google.com/uc?export=view&id=1HBbWgdmuRefimzI7TIVt6d7VoQHe8fHJ)


### API Routes
* To register - POST
```text
/api/user/register
```
* To login : will get and jwt token. - POST
```text
/api/user/login
```
* To Logout - will logout user/admin - GET
```text
/api/user/logout
```
* Get all user list : secured, authorized to admin only - GET
```text
/api/user/all
```
* Get individual user details : secured, only authorized admin and user himself and access it - GET
```text
/api/user/{id}
```
* Update user information : secured, only authorized admin and user himself and access it - PUT
```text
/api/user/update/{id}
```
* Update user role : only authorized admin can do it - PUT
```text
/api/user/update/role/{id}
```
* Delete a user : secured, only authorized admin and user himself and access it - DELETE
```text
/api/user/delete/{id}
```
* Get all vehicle list : everyone can access it - GET
```text
/api/vehicle/all
```
* Get individual vehicle details : everyone can access it - GET
```text
/api/vehicle/{id}
```
* Add new vehicle : Only authorized admin can do it - POST
```text
/api/vehicle/add-new
```
* Update vehicle : Only authorized admin can do it - PUT
```text
/api/vehicle/update/{id}
```
* Delete vehicle : Only authorized admin can do it - DELETE
```text
/apu/vehicle/delete/{id}
```
* Get all category list : everyone can access it - GET
```text
/api/category/all
```
* Get individual category details : everyone can access it - GET
```text
/api/category/{id}
```
* Add new category : Only authorized admin can do it - POST
```text
/api/category/add-new
```
* Update category : Only authorized admin can do it - PUT
```text
/api/category/update/{id}
```
* Delete category : Only authorized admin can do it - DELETE
```text
/apu/category/delete/{id}
```
* Get all location list : everyone can access it - GET
```text
/api/location/all
```
* Get individual location details : everyone can access it - GET
```text
/api/location/{id}
```
* Add new location : Only authorized admin can do it - POST
```text
/api/location/add-new
```
* Update location : Only authorized admin can do it - PUT
```text
/api/location/update/{id}
```
* Delete location : Only authorized admin can do it - DELETE
```text
/apu/location/delete/{id}
```
* Get all ticket list : everyone can access it, will have pagination - GET
```text
/api/ticket/{vehicle_id}/{category_id}/all
```
* Get individual ticket details : everyone can access it- GET
```text
/api/ticket/{id}
```
* Add new Ticket : only authorized admin can do it - POST     
```text
/api/ticket/add-new
```
* Update Ticket : only authorized admin can do it - PUT
```text
/api/ticket/update/{id}
```
* Delete Ticket : only authorized admin can do it - DELETE
```text
/api/ticket/delete/{id}
```
* Buy a ticket : only logged-in user can do it,we will only send the transaction id,user id : POST
```text
/api/ticket/buy/{ticket_id}
```
* Cancel purchase : only user himself and admin can do it : PUT
```text
/api/ticket/cancel/{ticket_id}
```
* Show purchase history : only admin and user himself can do it : POST
```text
/api/user/{id}/purchase-history
```
* Download ticket pdf : only tickets whose payment status is SUCCESS can be downloaded by authorized user - GET
```text
/api/download/ticket/{ticket_id}/user/{user_id}
```

### How to Build and Run