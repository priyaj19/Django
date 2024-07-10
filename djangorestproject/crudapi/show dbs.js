show dbs
use ('myntra')

use ('myntra')
show collections

use ('myntra')
db.product.find()

use ('myntra')
db.product.updateOne(
    {name:'Moto AC'},
    {$set:{price:50000}}
)

use ('myntra')
db.product.find()

use ('myntra')
db.product.updateOne(
    {category:'laptop'},
    {$set:{price:80000}}
)

use ('myntra')
db.product.find()

use ('myntra')
db.product.insertMany([
    {
        name:"xolo mobile",
        category:"mobile",
        price:50000,
        features:
        {
            memory:
            {
                ram:'4gb',
                rom:'64gb'
            },
            cameras:
            {
                front:'18px',
                back:'48px'
            }
        }
    },
    {
        name:"oppo",
        category:"mobile",
        price:35000,
        features:
        {
            memory:
            {
                ram:'3gb',
                rom:'16gb'
            },
            cameras:
            {
                front:'10px',
                back:'20px'
            }
        }
    }
])

use ('myntra')
db.product.find()

use ('myntra')
db.product.updateMany(
    {category:'mobile'},
    {$set:{price:40000}}
)


use ('myntra')
db.product.find()

# find product whose category is laptop
use ('myntra')
db.product.find({category:'laptop'})

# find product whose category is smartwatch but price is 4000
use ('myntra')
db.product.find({category:'smartwatch',price:4000})

# find product whose  price is 3000
use ('myntra')
db.product.find({price:3000})

use ('myntra')
db.product.find({price:{$eq:3000}})

# find product whose  price is greater than 60000
use ('myntra')
db.product.find({price:{$gt:60000}})

# show products data as per names
































