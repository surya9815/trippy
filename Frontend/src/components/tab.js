import React from 'react';

const Tab = (props) => {
    // console.log("Inside Tab", props);
    if (props.jsondata !== undefined) {
      {
        // console.log(props.jsondata, "jsondataoutside");
      }
  
      return (
        <>
        {/* <section className="py-5 text-center container"> */}

          <div>
            {props.jsondata.Comparison.length > 0 &&
              props.jsondata.Comparison.slice(0, -1).map((itemlist1) => {
                // console.log("itemlist1", itemlist1);
  
                // if (typeof itemlist1[0].hotelName === "object"){
                let hotelName = itemlist1[0].hotelName;
  
                // hotelName = hotelName &&hotelName.hotelName ? hotelName.hotelName : "";
                // console.log("hotelName: ", hotelName);
  
                return (
                  <>
                          <div className="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                            {/* <!-- Left Section-->
                                              <!-- Picture --> */}
                            <div className="col d-none d-lg-block ">
                              <img
                                src={require("./img/hotel1.jpg")}
                                alt=""
                                width="200"
                                height="250"
                              />
                            </div>
  
                            {/* <!-- Middle Section--> */}
  
                            <a
                              href="..."
                              className="col p-2 d-flex flex-column position-static"
                            >
                              {/* <!-- hotel Name from json--> */}
  
                              {/* uncomment below */}
                              <div className="p-2 mb-2 bg-primary text-white">
                                <h3 className="mb-0">
                                  {" "}
                                  <b>{hotelName}</b>
                                </h3>
                              </div>
  
                              {/* <!-- Star rating--> */}
                              <div className="container d-flex justify-content-center align-items-center">
                                <div className="card p-3">
                                  <div className="mt-1 d-flex justify-content-between align-items-center">
                                    <h6 className="review-stat">Cleanliness</h6>
                                    <div className="small-ratings">
                                      {" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star"></i>{" "}
                                      <i className="fa fa-star"></i>{" "}
                                    </div>
                                  </div>
                                  <div className="mt-1 d-flex justify-content-between align-items-center">
                                    <h6 className="review-stat">Accuracy</h6>
                                    <div className="small-ratings">
                                      {" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star"></i>{" "}
                                    </div>
                                  </div>
                                  <div className="mt-1 d-flex justify-content-between align-items-center">
                                    <h6 className="review-stat">Communication</h6>
                                    <div className="small-ratings">
                                      {" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star"></i>{" "}
                                      <i className="fa fa-star"></i>{" "}
                                      <i className="fa fa-star"></i>{" "}
                                    </div>
                                  </div>
                                  <div className="mt-1 d-flex justify-content-between align-items-center">
                                    <h6 className="review-stat">
                                      Value for Money
                                    </h6>
                                    <div className="small-ratings">
                                      {" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                      <i className="fa fa-star rating-color"></i>{" "}
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </a>
  
                            {/* <!-- Right Section--> */}
                            <div className="col p-4 d-flex flex-column position-static">
                              {/* <!-- Lowest Price from json--> */}
                              <a
                                href="..."
                                className="alert alert-success"
                                role="alert"
                              >
                                <p style={{ color: "green", fontSize: "18px" }}>
                                  <b>Best price </b>
                                </p>
                              </a>
                              {/* <!-- Other prices  from json--> */}
                              <div className="list-group">
                                <a
                                  href="..."
                                  className="list-group-item list-group-item-action"
                                  aria-current="true"
                                >
                                  <div className="d-flex w-100 justify-content-between">
                                    <h6 className="mb-1">
                                      {itemlist1[1][0].vendor1}
                                    </h6>
  
                                    <span className="badge bg-primary rounded-pill">
                                      {itemlist1[1][0].price1} $
                                    </span>
                                  </div>
                                </a>
                                <a
                                  href="..."
                                  className="list-group-item list-group-item-action"
                                  aria-current="true"
                                >
                                  <div className="d-flex w-100 justify-content-between">
                                    <h6 className="mb-1">
                                      {itemlist1[1][1].vendor2}
                                    </h6>
  
                                    <span className="badge bg-primary rounded-pill">
                                      {itemlist1[1][1].price2} $
                                    </span>
                                  </div>
                                </a>
                                <a
                                  href="..."
                                  className="list-group-item list-group-item-action"
                                  aria-current="true"
                                >
                                  <div className="d-flex w-100 justify-content-between">
                                    <h6 className="mb-1">
                                      {itemlist1[1][2].vendor3}
                                    </h6>
  
                                    <span className="badge bg-primary rounded-pill">
                                      {itemlist1[1][2].price3} $
                                    </span>
                                  </div>
                                </a>
                              </div>
                            </div>
                          </div>
                  </>
                );
              })}
          </div>
          {/* </section> */}
        </>
      );
    } else {
      console.log("CAnnot Call TABLE");
    }
  };
  
export default Tab;
