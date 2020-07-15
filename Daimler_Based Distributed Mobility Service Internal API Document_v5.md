# Smart Contract-Based Distributed Mobility Service Internal API Document

***
We define the API specifications for interacting with match making algorithm (MMA) in this document including availibility check and transaction confirmation.
***

**Flow Chart**

![](https://i.imgur.com/1IX2Hxi.png)

***

## Query For Available Cars (MMA1)

**URL** : `http://127.0.0.1:5000/api/query/car?params=<Base64_Encoded_Params>`


**Method** : `GET`

**Query Conditions**
```json
{
    "query_id": "1001",
    "query_time": 1583868012,
    "vehicle_type": "car", 
    "subtype": "unspecified",
    "location": "(25.016695, 121.543692)",
    "start_time": 1585134000, 3600 unix time == 1 hour
    "end_time": 1585137600
}
```

**subtype: Unspecified, Sedan, SUV.**

## Success Responses

**Condition** : Successfully query but no available car.

**Code** : `200 OK`

**Content**
```json
{} //blank response
```

### OR

**Condition** : Successfully query and one or more cartypes are available.

**Code** : `200 OK`

**Content** : Array of available cartypes in JSON format

```json
[
    {
        "query_id": "1003",
        "location": "(25.016695, 121.543692",
        "deal_id": "1587232599",
        "brand_id": "Pontiac",
        "bmid": "1000022",
        "vehicle_type": "car", 
        "subtype": "Hatchback",
        "model_id": "SC",
        "price": "3"
    }
    ,
    {
            "query_id": "1003",
            "location": "(25.016695, 121.543692",
            "deal_id": "1587232600",
            "brand_id": "Nissan",
            "bmid": "1000023",
            "vehicle_type": "car", 
            "subtype": "Coupe, Convertible, Wagon, Sedan",
            "model_id": "458 Italia",
            "price": "4"
    }
]
```

***

## Transaction Confirmation (MMA4)

***
Booked and Activate and Return the car using three url but same database
 
**1. MMA4 :** OrderConfirmed
   (item_id = null)

**2. MMA5 :** OrderCanceled

**3. MMA6 :** CarActivated
   (Ready to drive, assign item_id)
   
**4. MMA7 :** OrderFinished
   (Returned the car) 
***

**URL** : `http://127.0.0.1:5000/api/order/confirm/car`

**Method** : `POST`
// 正常用deal id 找price
**Message Body**
```json
{
    "query_id": "1003",
    "deal_id": "1587221268", 
    "order_id":"101231126",
    "order_time": 1583868012,
    "user_id":"10001",
    "bmid": "1000022",
    "location": "(25.016695, 121.543692",,
    "start_time": 1585134900, 
    "end_time": 1585138500
}	
```

## Success Responses

**Condition** : Successfully order car and update its status.

**Code** : `200 OK`

**Content**
```json
{
    "bmid": "1000022",
    "message": true,
    "order_id": "101231126",
    "price": 3,
    "user_id": "10001"
}
```

## Failed Responses

**Condition** : Fail to order car due to resource unavailable.

**Code** : `409 Conflict`

**Content**
```json
{
    "bmid": "1000022",
    "message": false,
    "order_id": "101231126",
    "price": 3,
    "user_id": "10001"
}
```


***

## Transaction Cancelation (MMA5)

**URL** : `http://127.0.0.1:5000/api/order/cancel/car`

**Method** : `POST`

**Message Body**
```json
{
    "order_id":"101231125"
}
```

## Success Responses

**Condition** : Successfully cancel the order. 

**Code** : `200 OK`

**Content**
```json
{
    "message": true,
    "order_id":"101231125",
}
```

## Failed Responses

**Condition** : Fail to cancel order 

**Code** : `409 Conflict`

**Content**
```json
{
    "message": false,
    "order_id":"101231125",
}
```


***

## Car Activation (MMA6)


**URL** : `http://127.0.0.1:5000/api/activate/car`

**Method** : `POST`

**Message Body**
```json
{
    "order_id": "101231125",
    "activate_time": 1583868012,
    "user_id": "10001"
}
```

## Success Responses

**Condition** : Successfully activate the car.

**Code** : `200 OK`

**Content**
```json
{
{
    "item_id": "1000006",
    "message": true,
    "order_id": "101231125"
}
}
```

## Failed Responses

**Condition** : Fail to activate the car. 

**Code** : `409 Conflict`

**Content**
```json
{
    "message": false,
    "item_id": "1000006",
    "order_id": "101231125"
}
```




***

## Return Car (MMA7)


**URL** : `http://127.0.0.1:5000/api/return/car`

**Method** : `POST`

**Message Body**
```json
{
    "order_id": "101231125",
    "return_time": 1583868012,
    "user_id": "10001"
}
```

## Success Responses

**Condition** : Successfully activate the car.

**Code** : `200 OK`

**Content**
```json
{
{
    "message": true,
    "order_id": "101231125"
}
}
```

## Failed Responses

**Condition** : Fail to activate the car. 

**Code** : `409 Conflict`

**Content**
```json
{
    "message": false,
    "order_id": "101231125"
}
```

# Database Schema

* FON location spot convert to absolute location
![Imgur](https://i.imgur.com/0KgVESi.png)
* Car All info
![Imgur](https://i.imgur.com/khxplOF.png)
* Available cars time table
![](https://i.imgur.com/fz6FEyf.png)

* Query Record
![Imgur](https://i.imgur.com/1Ad5jcu.png)
* Order Record
![Imgur](https://i.imgur.com/xfDxUvc.png)



