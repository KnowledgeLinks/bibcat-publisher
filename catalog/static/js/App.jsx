import React from "react";

function Search(props) {
    return (
        <form className="form-inline mx-lg-3" method="POST" action="{props.action}">
            <div className="form-group">
                <input className="form-control" id="query" placeholder="Query"></input>
            </div>
            <button type="submit" className="btn btn-primary">Search</button>
        </form>
    );
}

export default class App extends React.Component {
    render () {
        return (
            <div className="container">
                <h1>BIBCAT Publisher</h1>
                <Search action="/search"></Search>
            </div>
        );
    }
}
