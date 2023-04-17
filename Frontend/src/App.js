import React from "react";
import axios from "axios";
import { useState, useEffect, useReducer } from "react";
import "./App.css";
import Tab from "./components/tab";
import Nav from "./components/nav";
import Footer from "./components/footer";

const formReducer = (state, event) => {
  return {
    ...state,
    [event.name]: event.value,
  };
};

function App() {
  const [formData, setFormData] = useReducer(formReducer, {});
  const [features, setFeatures] = useState();
  const [submitting, setSubmitting] = useState(false);

  function handleSubmit(e) {
    e.preventDefault();
    // console.log("You clicked submit.");
    // alert("You have submitted the form.");
    setSubmitting(true);
    setTimeout(() => {
      setSubmitting(false);
    }, 5000);
  }

  const handleChange = (event) => {
    setFormData({
      name: event.target.name,
      value: event.target.value,
    });
  };
//   let inpvalue = formData.name;
//   console.log(inpvalue);
//   console.log(formData);
//   console.log(typeof formData);
  const [dataFlag, setDataFlag] = useState(false);
  useEffect(() => {
    if (submitting === true) {
      axios.get(`http://127.0.0.1:8000/${formData.name}`).then((response) => {
        // console.log(response.data);
        setFeatures(response.data);
        setDataFlag(true);

        // console.log(response.data);
        // console.log("api cal sucesss");
        // localStorage.setItem('data',features)
      });
    }
  }, [submitting]);

  //   const apiCall=  (inpvalue)=>{
  //       console.log("API CALL INITIAL")
  //        axios.get(`http://127.0.0.1:8000/${inpvalue}`)
  //        .then((response) =>{
  //         console.log("API REQ")
  //         console.log(inpvalue,"INPUT VAL of my data")
  //         // let feat = response.data
  //         setFeatures(response.data);
  //         console.log("api call sucesss")
  //         // localStorage.setItem('data',features)

  //       })
  //     }

  return (
    <>
    <Nav/>
      <main>
        <section className="py-5 text-center container">
          <div className="clearfix">
            <img
              src={require("./newtrippylogo.png")}
              className="col-md-4 float-md-center mb-3 ms-md-3"
              alt="..."
            />
          </div>
          <div className="home_search_container">
            <div className="p-3 mb-2 bg-primary bg-gradient text-white">
              <div>
                <h1>
                  <b>Stay more, save more. It's Genius.</b>
                </h1>
                <h6>
                  <b>
                    Enjoy discounts and travel rewards at hundreds of thousands
                    of properties worldwide
                  </b>
                </h6>
              </div>
              {/* line Break Expected */}
              <div className="form-floating">
                <form className="form-floating" onSubmit={handleSubmit}>
                  <div className="d-flex flex-lg-row flex-column align-items-start justify-content-lg-between justify-content-start">
                    {/* <label for="floatingInputDestination">
                        Destination
                        </label> */}
                    <input
                      type="text"
                      onChange={handleChange}
                      value={formData.name || ""}
                      className="form-control"
                      id="floatingInputDestination"
                      placeholder="Destination"
                      required=""
                      name="name"
                    />

                    <input
                      type="date"
                      className="form-control"
                      placeholder="Check In"
                      required=""
                      name="InpCheckin"
                    />

                    <input
                      type="date"
                      className="form-control"
                      placeholder="Check Out"
                      required=""
                      name="InpCheckout"
                    />

                    <input
                      type="number"
                      step="1"
                      max="20"
                      min="1"
                      className="form-control"
                      id="floatingInputAdult"
                      placeholder="Adult"
                      required=""
                      name="InpAdult"
                    />

                    {/* </div> */}
                    {/* <div className="col-2"> */}
                    <input
                      type="number"
                      step="1"
                      max="10"
                      min="0"
                      className="form-control"
                      placeholder="Child"
                      required=""
                      name="InpChild"
                    />
                    {/* </div> */}

                    <button type="submit" className="btn btn-outline-light">
                      search
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>

          {/*Start  */}
          {dataFlag && (
            <div>
              <Tab jsondata={features} />
            </div>
          )}
        </section>
      </main>
      <Footer/>
    </>
  );
}

export default App;
