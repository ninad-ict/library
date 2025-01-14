import React, { useEffect,useState } from "react";



export default function Books() {


    const [books, setBooks] = useState([])

    useEffect(()=>{


        fetch("http://127.0.0.1:8000/library/apis/inventory/")
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
            setBooks(data)
        })
        .catch((err) => {
            console.log(err)
        })



    },[])

    /*
    {
    "id": 1,
    "book_name": "Alice in wonderland",
    "isbn": "1234",
    "author": "Ralh",
    "book_cost": "123.00",
    "available_qty": 4,
    "publication_date": "2025-01-01",
    "rental_days": 7,
    "is_deleted": false,
    "created_at": "2025-01-14T07:44:55.349559Z",
    "updated_at": "2025-01-14T10:04:28.044758Z"
}
    */

    return (
        <>{books?.map((v,k)=>{

            return (
                <div key={k}>
                    <h1>{v.book_name}</h1>
                    <p>{v.autauthorhor}</p>
                    <p>{v.isbn}</p>
                    <p>{v.book_cost}</p>
                    <p>{v.publication_date}</p>
                    <p>{v.rental_days}</p>
                </div>
            )

        })}</>
    )


}