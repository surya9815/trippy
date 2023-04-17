import React from "react";
import axios from "axios";

const HotelImage = () => {
  console.log("IMAGE API CALL INITIAL");
  
  axios.get('https://api.unsplash.com/photos/random?query=hotels&client_id=aigYJM8z-Aq46bCU37h1NHhX-u7Ho6QkjFksh_OXPPs'
  ).then((response) => {
    console.log(response.data);
    

    console.log("IMAGE API REQ");
    return(
            <>           
            Sucess                   
            {/* <img
            src={require("./img/hotel1.jpg")}
            alt=""
            width="200"
            height="250"
        /> */}
        </>
    )

  }).catch("ERROR")

};

export default HotelImage;
