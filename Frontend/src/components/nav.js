import React from "react";

function Nav(){
    return(
        <header>
        <div className="collapse bg-primary" id="navbarHeader">
          <div className="container">
            <div className="row">
              <div className="col-sm-8 col-md-7 py-4"></div>
            </div>
          </div>
        </div>
        <div className="navbar navbar-primary bg-primary shadow-sm">
          <div className="container">
            <a href="#" className="navbar-brand d-flex align-items-center"></a>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarHeader"
              aria-controls="navbarHeader"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
          </div>
        </div>
      </header>
    )
}
export default Nav;
